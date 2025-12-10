from ApiTestVisitor import ApiTestVisitor
from ApiTestParser import ApiTestParser
from model import ApiSpec, Scenario, Case

class ApiTestCustomVisitor(ApiTestVisitor):
    def visitSpec(self, ctx: ApiTestParser.SpecContext):
        base_url = None
        scenarios = []

        if ctx.baseDecl():
            base_url = self.visit(ctx.baseDecl())

        for scen_ctx in ctx.scenarioDecl():
            scenarios.append(self.visit(scen_ctx))

        return ApiSpec(base_url=base_url, scenarios=scenarios)

    def visitBaseDecl(self, ctx: ApiTestParser.BaseDeclContext):
        # base_url STRING NEWLINE+
        text = ctx.STRING().getText()
        return text[1:-1]  # remove aspas

    def visitScenarioDecl(self, ctx: ApiTestParser.ScenarioDeclContext):
        name = ctx.STRING().getText()[1:-1]
        cases = []

        for case_ctx in ctx.caseDecl():
            cases.append(self.visit(case_ctx))

        return Scenario(name=name, cases=cases)

    def visitCaseDecl(self, ctx: ApiTestParser.CaseDeclContext):
        name = ctx.STRING().getText()[1:-1]

        request = self.visit(ctx.requestBlock())
        expect = self.visit(ctx.expectBlock())

        return Case(name=name, request=request, expect=expect)

    def visitRequestBlock(self, ctx: ApiTestParser.RequestBlockContext):
        data = {
            "method": None,
            "path": None,
            "query": {}
        }

        for item_ctx in ctx.requestItem():
            # Cada item pode ser methodDecl, pathDecl ou queryDecl
            val = self.visit(item_ctx)
            # visit(item_ctx) vai retornar um dicionário parcial
            for k, v in val.items():
                data[k] = v

        return data

    def visitRequestItem(self, ctx: ApiTestParser.RequestItemContext):
        if ctx.methodDecl():
            return self.visit(ctx.methodDecl())
        if ctx.pathDecl():
            return self.visit(ctx.pathDecl())
        if ctx.queryDecl():
            return self.visit(ctx.queryDecl())
        return {}

    def visitMethodDecl(self, ctx: ApiTestParser.MethodDeclContext):
        # METHOD HTTP_METHOD NEWLINE+
        method = ctx.HTTP_METHOD().getText()
        return {"method": method}

    def visitPathDecl(self, ctx: ApiTestParser.PathDeclContext):
        path = ctx.STRING().getText()[1:-1]
        return {"path": path}

    def visitQueryDecl(self, ctx: ApiTestParser.QueryDeclContext):
        query = {}
        for pair_ctx in ctx.queryPair():
            k, v = self.visit(pair_ctx)
            query[k] = v
        return {"query": query}

    def visitQueryPair(self, ctx: ApiTestParser.QueryPairContext):
        key = ctx.ID().getText()
        val = self.visit(ctx.value())
        return key, val

    def visitValue(self, ctx: ApiTestParser.ValueContext):
        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        if ctx.INT():
            return int(ctx.INT().getText())
        return None

    def visitExpectBlock(self, ctx: ApiTestParser.ExpectBlockContext):
        data = {
            "status": None,
            "json_has": [],
            "json_eq": {}
        }

        for item_ctx in ctx.expectItem():
            val = self.visit(item_ctx)
            # val pode ser {"status": 200}, {"json_has": "token"} ou ("campo","valor")
            if "status" in val:
                data["status"] = val["status"]
            if "json_has" in val:
                data["json_has"].append(val["json_has"])
            if "json_eq_pair" in val:
                k, v = val["json_eq_pair"]
                data["json_eq"][k] = v

        return data

    def visitExpectItem(self, ctx: ApiTestParser.ExpectItemContext):
        if ctx.statusDecl():
            return self.visit(ctx.statusDecl())
        if ctx.jsonHasDecl():
            return self.visit(ctx.jsonHasDecl())
        if ctx.jsonEqDecl():
            return self.visit(ctx.jsonEqDecl())
        return {}

    def visitStatusDecl(self, ctx: ApiTestParser.StatusDeclContext):
        status_code = int(ctx.INT().getText())
        return {"status": status_code}

    def visitJsonHasDecl(self, ctx: ApiTestParser.JsonHasDeclContext):
        field = ctx.STRING().getText()[1:-1]
        return {"json_has": field}

    def visitJsonEqDecl(self, ctx: ApiTestParser.JsonEqDeclContext):
        strings = ctx.STRING()
        field = strings[0].getText()[1:-1]
        value = strings[1].getText()[1:-1]
        return {"json_eq_pair": (field, value)}


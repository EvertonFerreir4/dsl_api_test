# Generated from ApiTest.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ApiTestParser import ApiTestParser
else:
    from ApiTestParser import ApiTestParser

# This class defines a complete generic visitor for a parse tree produced by ApiTestParser.

class ApiTestVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ApiTestParser#spec.
    def visitSpec(self, ctx:ApiTestParser.SpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#baseDecl.
    def visitBaseDecl(self, ctx:ApiTestParser.BaseDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#scenarioDecl.
    def visitScenarioDecl(self, ctx:ApiTestParser.ScenarioDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#caseDecl.
    def visitCaseDecl(self, ctx:ApiTestParser.CaseDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#requestBlock.
    def visitRequestBlock(self, ctx:ApiTestParser.RequestBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#requestItem.
    def visitRequestItem(self, ctx:ApiTestParser.RequestItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#methodDecl.
    def visitMethodDecl(self, ctx:ApiTestParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#pathDecl.
    def visitPathDecl(self, ctx:ApiTestParser.PathDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#queryDecl.
    def visitQueryDecl(self, ctx:ApiTestParser.QueryDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#queryPair.
    def visitQueryPair(self, ctx:ApiTestParser.QueryPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#expectBlock.
    def visitExpectBlock(self, ctx:ApiTestParser.ExpectBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#expectItem.
    def visitExpectItem(self, ctx:ApiTestParser.ExpectItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#statusDecl.
    def visitStatusDecl(self, ctx:ApiTestParser.StatusDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#jsonHasDecl.
    def visitJsonHasDecl(self, ctx:ApiTestParser.JsonHasDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#jsonEqDecl.
    def visitJsonEqDecl(self, ctx:ApiTestParser.JsonEqDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ApiTestParser#value.
    def visitValue(self, ctx:ApiTestParser.ValueContext):
        return self.visitChildren(ctx)



del ApiTestParser
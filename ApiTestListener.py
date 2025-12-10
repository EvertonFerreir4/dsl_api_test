# Generated from ApiTest.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ApiTestParser import ApiTestParser
else:
    from ApiTestParser import ApiTestParser

# This class defines a complete listener for a parse tree produced by ApiTestParser.
class ApiTestListener(ParseTreeListener):

    # Enter a parse tree produced by ApiTestParser#spec.
    def enterSpec(self, ctx:ApiTestParser.SpecContext):
        pass

    # Exit a parse tree produced by ApiTestParser#spec.
    def exitSpec(self, ctx:ApiTestParser.SpecContext):
        pass


    # Enter a parse tree produced by ApiTestParser#baseDecl.
    def enterBaseDecl(self, ctx:ApiTestParser.BaseDeclContext):
        pass

    # Exit a parse tree produced by ApiTestParser#baseDecl.
    def exitBaseDecl(self, ctx:ApiTestParser.BaseDeclContext):
        pass


    # Enter a parse tree produced by ApiTestParser#scenarioDecl.
    def enterScenarioDecl(self, ctx:ApiTestParser.ScenarioDeclContext):
        pass

    # Exit a parse tree produced by ApiTestParser#scenarioDecl.
    def exitScenarioDecl(self, ctx:ApiTestParser.ScenarioDeclContext):
        pass


    # Enter a parse tree produced by ApiTestParser#caseDecl.
    def enterCaseDecl(self, ctx:ApiTestParser.CaseDeclContext):
        pass

    # Exit a parse tree produced by ApiTestParser#caseDecl.
    def exitCaseDecl(self, ctx:ApiTestParser.CaseDeclContext):
        pass


    # Enter a parse tree produced by ApiTestParser#requestBlock.
    def enterRequestBlock(self, ctx:ApiTestParser.RequestBlockContext):
        pass

    # Exit a parse tree produced by ApiTestParser#requestBlock.
    def exitRequestBlock(self, ctx:ApiTestParser.RequestBlockContext):
        pass


    # Enter a parse tree produced by ApiTestParser#requestItem.
    def enterRequestItem(self, ctx:ApiTestParser.RequestItemContext):
        pass

    # Exit a parse tree produced by ApiTestParser#requestItem.
    def exitRequestItem(self, ctx:ApiTestParser.RequestItemContext):
        pass


    # Enter a parse tree produced by ApiTestParser#methodDecl.
    def enterMethodDecl(self, ctx:ApiTestParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by ApiTestParser#methodDecl.
    def exitMethodDecl(self, ctx:ApiTestParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by ApiTestParser#pathDecl.
    def enterPathDecl(self, ctx:ApiTestParser.PathDeclContext):
        pass

    # Exit a parse tree produced by ApiTestParser#pathDecl.
    def exitPathDecl(self, ctx:ApiTestParser.PathDeclContext):
        pass


    # Enter a parse tree produced by ApiTestParser#queryDecl.
    def enterQueryDecl(self, ctx:ApiTestParser.QueryDeclContext):
        pass

    # Exit a parse tree produced by ApiTestParser#queryDecl.
    def exitQueryDecl(self, ctx:ApiTestParser.QueryDeclContext):
        pass


    # Enter a parse tree produced by ApiTestParser#queryPair.
    def enterQueryPair(self, ctx:ApiTestParser.QueryPairContext):
        pass

    # Exit a parse tree produced by ApiTestParser#queryPair.
    def exitQueryPair(self, ctx:ApiTestParser.QueryPairContext):
        pass


    # Enter a parse tree produced by ApiTestParser#expectBlock.
    def enterExpectBlock(self, ctx:ApiTestParser.ExpectBlockContext):
        pass

    # Exit a parse tree produced by ApiTestParser#expectBlock.
    def exitExpectBlock(self, ctx:ApiTestParser.ExpectBlockContext):
        pass


    # Enter a parse tree produced by ApiTestParser#expectItem.
    def enterExpectItem(self, ctx:ApiTestParser.ExpectItemContext):
        pass

    # Exit a parse tree produced by ApiTestParser#expectItem.
    def exitExpectItem(self, ctx:ApiTestParser.ExpectItemContext):
        pass


    # Enter a parse tree produced by ApiTestParser#statusDecl.
    def enterStatusDecl(self, ctx:ApiTestParser.StatusDeclContext):
        pass

    # Exit a parse tree produced by ApiTestParser#statusDecl.
    def exitStatusDecl(self, ctx:ApiTestParser.StatusDeclContext):
        pass


    # Enter a parse tree produced by ApiTestParser#jsonHasDecl.
    def enterJsonHasDecl(self, ctx:ApiTestParser.JsonHasDeclContext):
        pass

    # Exit a parse tree produced by ApiTestParser#jsonHasDecl.
    def exitJsonHasDecl(self, ctx:ApiTestParser.JsonHasDeclContext):
        pass


    # Enter a parse tree produced by ApiTestParser#jsonEqDecl.
    def enterJsonEqDecl(self, ctx:ApiTestParser.JsonEqDeclContext):
        pass

    # Exit a parse tree produced by ApiTestParser#jsonEqDecl.
    def exitJsonEqDecl(self, ctx:ApiTestParser.JsonEqDeclContext):
        pass


    # Enter a parse tree produced by ApiTestParser#value.
    def enterValue(self, ctx:ApiTestParser.ValueContext):
        pass

    # Exit a parse tree produced by ApiTestParser#value.
    def exitValue(self, ctx:ApiTestParser.ValueContext):
        pass



del ApiTestParser
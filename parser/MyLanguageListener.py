# Generated from MyLanguage.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLanguageParser import MyLanguageParser
else:
    from MyLanguageParser import MyLanguageParser

# This class defines a complete listener for a parse tree produced by MyLanguageParser.
class MyLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by MyLanguageParser#program.
    def enterProgram(self, ctx:MyLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#program.
    def exitProgram(self, ctx:MyLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#statement.
    def enterStatement(self, ctx:MyLanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#statement.
    def exitStatement(self, ctx:MyLanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:MyLanguageParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:MyLanguageParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#assignment.
    def enterAssignment(self, ctx:MyLanguageParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#assignment.
    def exitAssignment(self, ctx:MyLanguageParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#printStatement.
    def enterPrintStatement(self, ctx:MyLanguageParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#printStatement.
    def exitPrintStatement(self, ctx:MyLanguageParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#ifStatement.
    def enterIfStatement(self, ctx:MyLanguageParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#ifStatement.
    def exitIfStatement(self, ctx:MyLanguageParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#whileStatement.
    def enterWhileStatement(self, ctx:MyLanguageParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#whileStatement.
    def exitWhileStatement(self, ctx:MyLanguageParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#block.
    def enterBlock(self, ctx:MyLanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#block.
    def exitBlock(self, ctx:MyLanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#expression.
    def enterExpression(self, ctx:MyLanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#expression.
    def exitExpression(self, ctx:MyLanguageParser.ExpressionContext):
        pass



del MyLanguageParser
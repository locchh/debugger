# Generated from MyLanguage.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLanguageParser import MyLanguageParser
else:
    from MyLanguageParser import MyLanguageParser

# This class defines a complete generic visitor for a parse tree produced by MyLanguageParser.

class MyLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLanguageParser#program.
    def visitProgram(self, ctx:MyLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#statement.
    def visitStatement(self, ctx:MyLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MyLanguageParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#assignment.
    def visitAssignment(self, ctx:MyLanguageParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#printStatement.
    def visitPrintStatement(self, ctx:MyLanguageParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#ifStatement.
    def visitIfStatement(self, ctx:MyLanguageParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#whileStatement.
    def visitWhileStatement(self, ctx:MyLanguageParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#block.
    def visitBlock(self, ctx:MyLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#expression.
    def visitExpression(self, ctx:MyLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)



del MyLanguageParser
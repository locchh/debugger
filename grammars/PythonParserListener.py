# Generated from grammars/PythonParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonParserListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#file_input.
    def enterFile_input(self, ctx:PythonParser.File_inputContext):
        pass

    # Exit a parse tree produced by PythonParser#file_input.
    def exitFile_input(self, ctx:PythonParser.File_inputContext):
        pass


    # Enter a parse tree produced by PythonParser#interactive.
    def enterInteractive(self, ctx:PythonParser.InteractiveContext):
        pass

    # Exit a parse tree produced by PythonParser#interactive.
    def exitInteractive(self, ctx:PythonParser.InteractiveContext):
        pass


    # Enter a parse tree produced by PythonParser#eval.
    def enterEval(self, ctx:PythonParser.EvalContext):
        pass

    # Exit a parse tree produced by PythonParser#eval.
    def exitEval(self, ctx:PythonParser.EvalContext):
        pass


    # Enter a parse tree produced by PythonParser#func_type.
    def enterFunc_type(self, ctx:PythonParser.Func_typeContext):
        pass

    # Exit a parse tree produced by PythonParser#func_type.
    def exitFunc_type(self, ctx:PythonParser.Func_typeContext):
        pass


    # Enter a parse tree produced by PythonParser#fstring_input.
    def enterFstring_input(self, ctx:PythonParser.Fstring_inputContext):
        pass

    # Exit a parse tree produced by PythonParser#fstring_input.
    def exitFstring_input(self, ctx:PythonParser.Fstring_inputContext):
        pass


    # Enter a parse tree produced by PythonParser#statements.
    def enterStatements(self, ctx:PythonParser.StatementsContext):
        pass

    # Exit a parse tree produced by PythonParser#statements.
    def exitStatements(self, ctx:PythonParser.StatementsContext):
        pass


    # Enter a parse tree produced by PythonParser#statement.
    def enterStatement(self, ctx:PythonParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonParser#statement.
    def exitStatement(self, ctx:PythonParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonParser#statement_newline.
    def enterStatement_newline(self, ctx:PythonParser.Statement_newlineContext):
        pass

    # Exit a parse tree produced by PythonParser#statement_newline.
    def exitStatement_newline(self, ctx:PythonParser.Statement_newlineContext):
        pass


    # Enter a parse tree produced by PythonParser#simple_stmts.
    def enterSimple_stmts(self, ctx:PythonParser.Simple_stmtsContext):
        pass

    # Exit a parse tree produced by PythonParser#simple_stmts.
    def exitSimple_stmts(self, ctx:PythonParser.Simple_stmtsContext):
        pass


    # Enter a parse tree produced by PythonParser#simple_stmt.
    def enterSimple_stmt(self, ctx:PythonParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#simple_stmt.
    def exitSimple_stmt(self, ctx:PythonParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#compound_stmt.
    def enterCompound_stmt(self, ctx:PythonParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#compound_stmt.
    def exitCompound_stmt(self, ctx:PythonParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#assignment.
    def enterAssignment(self, ctx:PythonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonParser#assignment.
    def exitAssignment(self, ctx:PythonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonParser#annotated_rhs.
    def enterAnnotated_rhs(self, ctx:PythonParser.Annotated_rhsContext):
        pass

    # Exit a parse tree produced by PythonParser#annotated_rhs.
    def exitAnnotated_rhs(self, ctx:PythonParser.Annotated_rhsContext):
        pass


    # Enter a parse tree produced by PythonParser#augassign.
    def enterAugassign(self, ctx:PythonParser.AugassignContext):
        pass

    # Exit a parse tree produced by PythonParser#augassign.
    def exitAugassign(self, ctx:PythonParser.AugassignContext):
        pass


    # Enter a parse tree produced by PythonParser#return_stmt.
    def enterReturn_stmt(self, ctx:PythonParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#return_stmt.
    def exitReturn_stmt(self, ctx:PythonParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#raise_stmt.
    def enterRaise_stmt(self, ctx:PythonParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#raise_stmt.
    def exitRaise_stmt(self, ctx:PythonParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#global_stmt.
    def enterGlobal_stmt(self, ctx:PythonParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#global_stmt.
    def exitGlobal_stmt(self, ctx:PythonParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:PythonParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:PythonParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#del_stmt.
    def enterDel_stmt(self, ctx:PythonParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#del_stmt.
    def exitDel_stmt(self, ctx:PythonParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#yield_stmt.
    def enterYield_stmt(self, ctx:PythonParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#yield_stmt.
    def exitYield_stmt(self, ctx:PythonParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#assert_stmt.
    def enterAssert_stmt(self, ctx:PythonParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#assert_stmt.
    def exitAssert_stmt(self, ctx:PythonParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#import_stmt.
    def enterImport_stmt(self, ctx:PythonParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#import_stmt.
    def exitImport_stmt(self, ctx:PythonParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#import_name.
    def enterImport_name(self, ctx:PythonParser.Import_nameContext):
        pass

    # Exit a parse tree produced by PythonParser#import_name.
    def exitImport_name(self, ctx:PythonParser.Import_nameContext):
        pass


    # Enter a parse tree produced by PythonParser#import_from.
    def enterImport_from(self, ctx:PythonParser.Import_fromContext):
        pass

    # Exit a parse tree produced by PythonParser#import_from.
    def exitImport_from(self, ctx:PythonParser.Import_fromContext):
        pass


    # Enter a parse tree produced by PythonParser#import_from_targets.
    def enterImport_from_targets(self, ctx:PythonParser.Import_from_targetsContext):
        pass

    # Exit a parse tree produced by PythonParser#import_from_targets.
    def exitImport_from_targets(self, ctx:PythonParser.Import_from_targetsContext):
        pass


    # Enter a parse tree produced by PythonParser#import_from_as_names.
    def enterImport_from_as_names(self, ctx:PythonParser.Import_from_as_namesContext):
        pass

    # Exit a parse tree produced by PythonParser#import_from_as_names.
    def exitImport_from_as_names(self, ctx:PythonParser.Import_from_as_namesContext):
        pass


    # Enter a parse tree produced by PythonParser#import_from_as_name.
    def enterImport_from_as_name(self, ctx:PythonParser.Import_from_as_nameContext):
        pass

    # Exit a parse tree produced by PythonParser#import_from_as_name.
    def exitImport_from_as_name(self, ctx:PythonParser.Import_from_as_nameContext):
        pass


    # Enter a parse tree produced by PythonParser#dotted_as_names.
    def enterDotted_as_names(self, ctx:PythonParser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by PythonParser#dotted_as_names.
    def exitDotted_as_names(self, ctx:PythonParser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by PythonParser#dotted_as_name.
    def enterDotted_as_name(self, ctx:PythonParser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by PythonParser#dotted_as_name.
    def exitDotted_as_name(self, ctx:PythonParser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by PythonParser#dotted_name.
    def enterDotted_name(self, ctx:PythonParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by PythonParser#dotted_name.
    def exitDotted_name(self, ctx:PythonParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by PythonParser#block.
    def enterBlock(self, ctx:PythonParser.BlockContext):
        pass

    # Exit a parse tree produced by PythonParser#block.
    def exitBlock(self, ctx:PythonParser.BlockContext):
        pass


    # Enter a parse tree produced by PythonParser#decorators.
    def enterDecorators(self, ctx:PythonParser.DecoratorsContext):
        pass

    # Exit a parse tree produced by PythonParser#decorators.
    def exitDecorators(self, ctx:PythonParser.DecoratorsContext):
        pass


    # Enter a parse tree produced by PythonParser#class_def.
    def enterClass_def(self, ctx:PythonParser.Class_defContext):
        pass

    # Exit a parse tree produced by PythonParser#class_def.
    def exitClass_def(self, ctx:PythonParser.Class_defContext):
        pass


    # Enter a parse tree produced by PythonParser#class_def_raw.
    def enterClass_def_raw(self, ctx:PythonParser.Class_def_rawContext):
        pass

    # Exit a parse tree produced by PythonParser#class_def_raw.
    def exitClass_def_raw(self, ctx:PythonParser.Class_def_rawContext):
        pass


    # Enter a parse tree produced by PythonParser#function_def.
    def enterFunction_def(self, ctx:PythonParser.Function_defContext):
        pass

    # Exit a parse tree produced by PythonParser#function_def.
    def exitFunction_def(self, ctx:PythonParser.Function_defContext):
        pass


    # Enter a parse tree produced by PythonParser#function_def_raw.
    def enterFunction_def_raw(self, ctx:PythonParser.Function_def_rawContext):
        pass

    # Exit a parse tree produced by PythonParser#function_def_raw.
    def exitFunction_def_raw(self, ctx:PythonParser.Function_def_rawContext):
        pass


    # Enter a parse tree produced by PythonParser#params.
    def enterParams(self, ctx:PythonParser.ParamsContext):
        pass

    # Exit a parse tree produced by PythonParser#params.
    def exitParams(self, ctx:PythonParser.ParamsContext):
        pass


    # Enter a parse tree produced by PythonParser#parameters.
    def enterParameters(self, ctx:PythonParser.ParametersContext):
        pass

    # Exit a parse tree produced by PythonParser#parameters.
    def exitParameters(self, ctx:PythonParser.ParametersContext):
        pass


    # Enter a parse tree produced by PythonParser#slash_no_default.
    def enterSlash_no_default(self, ctx:PythonParser.Slash_no_defaultContext):
        pass

    # Exit a parse tree produced by PythonParser#slash_no_default.
    def exitSlash_no_default(self, ctx:PythonParser.Slash_no_defaultContext):
        pass


    # Enter a parse tree produced by PythonParser#slash_with_default.
    def enterSlash_with_default(self, ctx:PythonParser.Slash_with_defaultContext):
        pass

    # Exit a parse tree produced by PythonParser#slash_with_default.
    def exitSlash_with_default(self, ctx:PythonParser.Slash_with_defaultContext):
        pass


    # Enter a parse tree produced by PythonParser#star_etc.
    def enterStar_etc(self, ctx:PythonParser.Star_etcContext):
        pass

    # Exit a parse tree produced by PythonParser#star_etc.
    def exitStar_etc(self, ctx:PythonParser.Star_etcContext):
        pass


    # Enter a parse tree produced by PythonParser#kwds.
    def enterKwds(self, ctx:PythonParser.KwdsContext):
        pass

    # Exit a parse tree produced by PythonParser#kwds.
    def exitKwds(self, ctx:PythonParser.KwdsContext):
        pass


    # Enter a parse tree produced by PythonParser#param_no_default.
    def enterParam_no_default(self, ctx:PythonParser.Param_no_defaultContext):
        pass

    # Exit a parse tree produced by PythonParser#param_no_default.
    def exitParam_no_default(self, ctx:PythonParser.Param_no_defaultContext):
        pass


    # Enter a parse tree produced by PythonParser#param_no_default_star_annotation.
    def enterParam_no_default_star_annotation(self, ctx:PythonParser.Param_no_default_star_annotationContext):
        pass

    # Exit a parse tree produced by PythonParser#param_no_default_star_annotation.
    def exitParam_no_default_star_annotation(self, ctx:PythonParser.Param_no_default_star_annotationContext):
        pass


    # Enter a parse tree produced by PythonParser#param_with_default.
    def enterParam_with_default(self, ctx:PythonParser.Param_with_defaultContext):
        pass

    # Exit a parse tree produced by PythonParser#param_with_default.
    def exitParam_with_default(self, ctx:PythonParser.Param_with_defaultContext):
        pass


    # Enter a parse tree produced by PythonParser#param_maybe_default.
    def enterParam_maybe_default(self, ctx:PythonParser.Param_maybe_defaultContext):
        pass

    # Exit a parse tree produced by PythonParser#param_maybe_default.
    def exitParam_maybe_default(self, ctx:PythonParser.Param_maybe_defaultContext):
        pass


    # Enter a parse tree produced by PythonParser#param.
    def enterParam(self, ctx:PythonParser.ParamContext):
        pass

    # Exit a parse tree produced by PythonParser#param.
    def exitParam(self, ctx:PythonParser.ParamContext):
        pass


    # Enter a parse tree produced by PythonParser#param_star_annotation.
    def enterParam_star_annotation(self, ctx:PythonParser.Param_star_annotationContext):
        pass

    # Exit a parse tree produced by PythonParser#param_star_annotation.
    def exitParam_star_annotation(self, ctx:PythonParser.Param_star_annotationContext):
        pass


    # Enter a parse tree produced by PythonParser#annotation.
    def enterAnnotation(self, ctx:PythonParser.AnnotationContext):
        pass

    # Exit a parse tree produced by PythonParser#annotation.
    def exitAnnotation(self, ctx:PythonParser.AnnotationContext):
        pass


    # Enter a parse tree produced by PythonParser#star_annotation.
    def enterStar_annotation(self, ctx:PythonParser.Star_annotationContext):
        pass

    # Exit a parse tree produced by PythonParser#star_annotation.
    def exitStar_annotation(self, ctx:PythonParser.Star_annotationContext):
        pass


    # Enter a parse tree produced by PythonParser#default_assignment.
    def enterDefault_assignment(self, ctx:PythonParser.Default_assignmentContext):
        pass

    # Exit a parse tree produced by PythonParser#default_assignment.
    def exitDefault_assignment(self, ctx:PythonParser.Default_assignmentContext):
        pass


    # Enter a parse tree produced by PythonParser#if_stmt.
    def enterIf_stmt(self, ctx:PythonParser.If_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#if_stmt.
    def exitIf_stmt(self, ctx:PythonParser.If_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#elif_stmt.
    def enterElif_stmt(self, ctx:PythonParser.Elif_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#elif_stmt.
    def exitElif_stmt(self, ctx:PythonParser.Elif_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#else_block.
    def enterElse_block(self, ctx:PythonParser.Else_blockContext):
        pass

    # Exit a parse tree produced by PythonParser#else_block.
    def exitElse_block(self, ctx:PythonParser.Else_blockContext):
        pass


    # Enter a parse tree produced by PythonParser#while_stmt.
    def enterWhile_stmt(self, ctx:PythonParser.While_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#while_stmt.
    def exitWhile_stmt(self, ctx:PythonParser.While_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#for_stmt.
    def enterFor_stmt(self, ctx:PythonParser.For_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#for_stmt.
    def exitFor_stmt(self, ctx:PythonParser.For_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#with_stmt.
    def enterWith_stmt(self, ctx:PythonParser.With_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#with_stmt.
    def exitWith_stmt(self, ctx:PythonParser.With_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#with_item.
    def enterWith_item(self, ctx:PythonParser.With_itemContext):
        pass

    # Exit a parse tree produced by PythonParser#with_item.
    def exitWith_item(self, ctx:PythonParser.With_itemContext):
        pass


    # Enter a parse tree produced by PythonParser#try_stmt.
    def enterTry_stmt(self, ctx:PythonParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#try_stmt.
    def exitTry_stmt(self, ctx:PythonParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#except_block.
    def enterExcept_block(self, ctx:PythonParser.Except_blockContext):
        pass

    # Exit a parse tree produced by PythonParser#except_block.
    def exitExcept_block(self, ctx:PythonParser.Except_blockContext):
        pass


    # Enter a parse tree produced by PythonParser#except_star_block.
    def enterExcept_star_block(self, ctx:PythonParser.Except_star_blockContext):
        pass

    # Exit a parse tree produced by PythonParser#except_star_block.
    def exitExcept_star_block(self, ctx:PythonParser.Except_star_blockContext):
        pass


    # Enter a parse tree produced by PythonParser#finally_block.
    def enterFinally_block(self, ctx:PythonParser.Finally_blockContext):
        pass

    # Exit a parse tree produced by PythonParser#finally_block.
    def exitFinally_block(self, ctx:PythonParser.Finally_blockContext):
        pass


    # Enter a parse tree produced by PythonParser#match_stmt.
    def enterMatch_stmt(self, ctx:PythonParser.Match_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#match_stmt.
    def exitMatch_stmt(self, ctx:PythonParser.Match_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#subject_expr.
    def enterSubject_expr(self, ctx:PythonParser.Subject_exprContext):
        pass

    # Exit a parse tree produced by PythonParser#subject_expr.
    def exitSubject_expr(self, ctx:PythonParser.Subject_exprContext):
        pass


    # Enter a parse tree produced by PythonParser#case_block.
    def enterCase_block(self, ctx:PythonParser.Case_blockContext):
        pass

    # Exit a parse tree produced by PythonParser#case_block.
    def exitCase_block(self, ctx:PythonParser.Case_blockContext):
        pass


    # Enter a parse tree produced by PythonParser#guard.
    def enterGuard(self, ctx:PythonParser.GuardContext):
        pass

    # Exit a parse tree produced by PythonParser#guard.
    def exitGuard(self, ctx:PythonParser.GuardContext):
        pass


    # Enter a parse tree produced by PythonParser#patterns.
    def enterPatterns(self, ctx:PythonParser.PatternsContext):
        pass

    # Exit a parse tree produced by PythonParser#patterns.
    def exitPatterns(self, ctx:PythonParser.PatternsContext):
        pass


    # Enter a parse tree produced by PythonParser#pattern.
    def enterPattern(self, ctx:PythonParser.PatternContext):
        pass

    # Exit a parse tree produced by PythonParser#pattern.
    def exitPattern(self, ctx:PythonParser.PatternContext):
        pass


    # Enter a parse tree produced by PythonParser#as_pattern.
    def enterAs_pattern(self, ctx:PythonParser.As_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#as_pattern.
    def exitAs_pattern(self, ctx:PythonParser.As_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#or_pattern.
    def enterOr_pattern(self, ctx:PythonParser.Or_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#or_pattern.
    def exitOr_pattern(self, ctx:PythonParser.Or_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#closed_pattern.
    def enterClosed_pattern(self, ctx:PythonParser.Closed_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#closed_pattern.
    def exitClosed_pattern(self, ctx:PythonParser.Closed_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#literal_pattern.
    def enterLiteral_pattern(self, ctx:PythonParser.Literal_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#literal_pattern.
    def exitLiteral_pattern(self, ctx:PythonParser.Literal_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#literal_expr.
    def enterLiteral_expr(self, ctx:PythonParser.Literal_exprContext):
        pass

    # Exit a parse tree produced by PythonParser#literal_expr.
    def exitLiteral_expr(self, ctx:PythonParser.Literal_exprContext):
        pass


    # Enter a parse tree produced by PythonParser#complex_number.
    def enterComplex_number(self, ctx:PythonParser.Complex_numberContext):
        pass

    # Exit a parse tree produced by PythonParser#complex_number.
    def exitComplex_number(self, ctx:PythonParser.Complex_numberContext):
        pass


    # Enter a parse tree produced by PythonParser#signed_number.
    def enterSigned_number(self, ctx:PythonParser.Signed_numberContext):
        pass

    # Exit a parse tree produced by PythonParser#signed_number.
    def exitSigned_number(self, ctx:PythonParser.Signed_numberContext):
        pass


    # Enter a parse tree produced by PythonParser#signed_real_number.
    def enterSigned_real_number(self, ctx:PythonParser.Signed_real_numberContext):
        pass

    # Exit a parse tree produced by PythonParser#signed_real_number.
    def exitSigned_real_number(self, ctx:PythonParser.Signed_real_numberContext):
        pass


    # Enter a parse tree produced by PythonParser#real_number.
    def enterReal_number(self, ctx:PythonParser.Real_numberContext):
        pass

    # Exit a parse tree produced by PythonParser#real_number.
    def exitReal_number(self, ctx:PythonParser.Real_numberContext):
        pass


    # Enter a parse tree produced by PythonParser#imaginary_number.
    def enterImaginary_number(self, ctx:PythonParser.Imaginary_numberContext):
        pass

    # Exit a parse tree produced by PythonParser#imaginary_number.
    def exitImaginary_number(self, ctx:PythonParser.Imaginary_numberContext):
        pass


    # Enter a parse tree produced by PythonParser#capture_pattern.
    def enterCapture_pattern(self, ctx:PythonParser.Capture_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#capture_pattern.
    def exitCapture_pattern(self, ctx:PythonParser.Capture_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#pattern_capture_target.
    def enterPattern_capture_target(self, ctx:PythonParser.Pattern_capture_targetContext):
        pass

    # Exit a parse tree produced by PythonParser#pattern_capture_target.
    def exitPattern_capture_target(self, ctx:PythonParser.Pattern_capture_targetContext):
        pass


    # Enter a parse tree produced by PythonParser#wildcard_pattern.
    def enterWildcard_pattern(self, ctx:PythonParser.Wildcard_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#wildcard_pattern.
    def exitWildcard_pattern(self, ctx:PythonParser.Wildcard_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#value_pattern.
    def enterValue_pattern(self, ctx:PythonParser.Value_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#value_pattern.
    def exitValue_pattern(self, ctx:PythonParser.Value_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#attr.
    def enterAttr(self, ctx:PythonParser.AttrContext):
        pass

    # Exit a parse tree produced by PythonParser#attr.
    def exitAttr(self, ctx:PythonParser.AttrContext):
        pass


    # Enter a parse tree produced by PythonParser#name_or_attr.
    def enterName_or_attr(self, ctx:PythonParser.Name_or_attrContext):
        pass

    # Exit a parse tree produced by PythonParser#name_or_attr.
    def exitName_or_attr(self, ctx:PythonParser.Name_or_attrContext):
        pass


    # Enter a parse tree produced by PythonParser#group_pattern.
    def enterGroup_pattern(self, ctx:PythonParser.Group_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#group_pattern.
    def exitGroup_pattern(self, ctx:PythonParser.Group_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#sequence_pattern.
    def enterSequence_pattern(self, ctx:PythonParser.Sequence_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#sequence_pattern.
    def exitSequence_pattern(self, ctx:PythonParser.Sequence_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#open_sequence_pattern.
    def enterOpen_sequence_pattern(self, ctx:PythonParser.Open_sequence_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#open_sequence_pattern.
    def exitOpen_sequence_pattern(self, ctx:PythonParser.Open_sequence_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#maybe_sequence_pattern.
    def enterMaybe_sequence_pattern(self, ctx:PythonParser.Maybe_sequence_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#maybe_sequence_pattern.
    def exitMaybe_sequence_pattern(self, ctx:PythonParser.Maybe_sequence_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#maybe_star_pattern.
    def enterMaybe_star_pattern(self, ctx:PythonParser.Maybe_star_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#maybe_star_pattern.
    def exitMaybe_star_pattern(self, ctx:PythonParser.Maybe_star_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#star_pattern.
    def enterStar_pattern(self, ctx:PythonParser.Star_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#star_pattern.
    def exitStar_pattern(self, ctx:PythonParser.Star_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#mapping_pattern.
    def enterMapping_pattern(self, ctx:PythonParser.Mapping_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#mapping_pattern.
    def exitMapping_pattern(self, ctx:PythonParser.Mapping_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#items_pattern.
    def enterItems_pattern(self, ctx:PythonParser.Items_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#items_pattern.
    def exitItems_pattern(self, ctx:PythonParser.Items_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#key_value_pattern.
    def enterKey_value_pattern(self, ctx:PythonParser.Key_value_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#key_value_pattern.
    def exitKey_value_pattern(self, ctx:PythonParser.Key_value_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#double_star_pattern.
    def enterDouble_star_pattern(self, ctx:PythonParser.Double_star_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#double_star_pattern.
    def exitDouble_star_pattern(self, ctx:PythonParser.Double_star_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#class_pattern.
    def enterClass_pattern(self, ctx:PythonParser.Class_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#class_pattern.
    def exitClass_pattern(self, ctx:PythonParser.Class_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#positional_patterns.
    def enterPositional_patterns(self, ctx:PythonParser.Positional_patternsContext):
        pass

    # Exit a parse tree produced by PythonParser#positional_patterns.
    def exitPositional_patterns(self, ctx:PythonParser.Positional_patternsContext):
        pass


    # Enter a parse tree produced by PythonParser#keyword_patterns.
    def enterKeyword_patterns(self, ctx:PythonParser.Keyword_patternsContext):
        pass

    # Exit a parse tree produced by PythonParser#keyword_patterns.
    def exitKeyword_patterns(self, ctx:PythonParser.Keyword_patternsContext):
        pass


    # Enter a parse tree produced by PythonParser#keyword_pattern.
    def enterKeyword_pattern(self, ctx:PythonParser.Keyword_patternContext):
        pass

    # Exit a parse tree produced by PythonParser#keyword_pattern.
    def exitKeyword_pattern(self, ctx:PythonParser.Keyword_patternContext):
        pass


    # Enter a parse tree produced by PythonParser#type_alias.
    def enterType_alias(self, ctx:PythonParser.Type_aliasContext):
        pass

    # Exit a parse tree produced by PythonParser#type_alias.
    def exitType_alias(self, ctx:PythonParser.Type_aliasContext):
        pass


    # Enter a parse tree produced by PythonParser#type_params.
    def enterType_params(self, ctx:PythonParser.Type_paramsContext):
        pass

    # Exit a parse tree produced by PythonParser#type_params.
    def exitType_params(self, ctx:PythonParser.Type_paramsContext):
        pass


    # Enter a parse tree produced by PythonParser#type_param_seq.
    def enterType_param_seq(self, ctx:PythonParser.Type_param_seqContext):
        pass

    # Exit a parse tree produced by PythonParser#type_param_seq.
    def exitType_param_seq(self, ctx:PythonParser.Type_param_seqContext):
        pass


    # Enter a parse tree produced by PythonParser#type_param.
    def enterType_param(self, ctx:PythonParser.Type_paramContext):
        pass

    # Exit a parse tree produced by PythonParser#type_param.
    def exitType_param(self, ctx:PythonParser.Type_paramContext):
        pass


    # Enter a parse tree produced by PythonParser#type_param_bound.
    def enterType_param_bound(self, ctx:PythonParser.Type_param_boundContext):
        pass

    # Exit a parse tree produced by PythonParser#type_param_bound.
    def exitType_param_bound(self, ctx:PythonParser.Type_param_boundContext):
        pass


    # Enter a parse tree produced by PythonParser#expressions.
    def enterExpressions(self, ctx:PythonParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by PythonParser#expressions.
    def exitExpressions(self, ctx:PythonParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by PythonParser#expression.
    def enterExpression(self, ctx:PythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonParser#expression.
    def exitExpression(self, ctx:PythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonParser#yield_expr.
    def enterYield_expr(self, ctx:PythonParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by PythonParser#yield_expr.
    def exitYield_expr(self, ctx:PythonParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by PythonParser#star_expressions.
    def enterStar_expressions(self, ctx:PythonParser.Star_expressionsContext):
        pass

    # Exit a parse tree produced by PythonParser#star_expressions.
    def exitStar_expressions(self, ctx:PythonParser.Star_expressionsContext):
        pass


    # Enter a parse tree produced by PythonParser#star_expression.
    def enterStar_expression(self, ctx:PythonParser.Star_expressionContext):
        pass

    # Exit a parse tree produced by PythonParser#star_expression.
    def exitStar_expression(self, ctx:PythonParser.Star_expressionContext):
        pass


    # Enter a parse tree produced by PythonParser#star_named_expressions.
    def enterStar_named_expressions(self, ctx:PythonParser.Star_named_expressionsContext):
        pass

    # Exit a parse tree produced by PythonParser#star_named_expressions.
    def exitStar_named_expressions(self, ctx:PythonParser.Star_named_expressionsContext):
        pass


    # Enter a parse tree produced by PythonParser#star_named_expression.
    def enterStar_named_expression(self, ctx:PythonParser.Star_named_expressionContext):
        pass

    # Exit a parse tree produced by PythonParser#star_named_expression.
    def exitStar_named_expression(self, ctx:PythonParser.Star_named_expressionContext):
        pass


    # Enter a parse tree produced by PythonParser#assignment_expression.
    def enterAssignment_expression(self, ctx:PythonParser.Assignment_expressionContext):
        pass

    # Exit a parse tree produced by PythonParser#assignment_expression.
    def exitAssignment_expression(self, ctx:PythonParser.Assignment_expressionContext):
        pass


    # Enter a parse tree produced by PythonParser#named_expression.
    def enterNamed_expression(self, ctx:PythonParser.Named_expressionContext):
        pass

    # Exit a parse tree produced by PythonParser#named_expression.
    def exitNamed_expression(self, ctx:PythonParser.Named_expressionContext):
        pass


    # Enter a parse tree produced by PythonParser#disjunction.
    def enterDisjunction(self, ctx:PythonParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by PythonParser#disjunction.
    def exitDisjunction(self, ctx:PythonParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by PythonParser#conjunction.
    def enterConjunction(self, ctx:PythonParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by PythonParser#conjunction.
    def exitConjunction(self, ctx:PythonParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by PythonParser#inversion.
    def enterInversion(self, ctx:PythonParser.InversionContext):
        pass

    # Exit a parse tree produced by PythonParser#inversion.
    def exitInversion(self, ctx:PythonParser.InversionContext):
        pass


    # Enter a parse tree produced by PythonParser#comparison.
    def enterComparison(self, ctx:PythonParser.ComparisonContext):
        pass

    # Exit a parse tree produced by PythonParser#comparison.
    def exitComparison(self, ctx:PythonParser.ComparisonContext):
        pass


    # Enter a parse tree produced by PythonParser#compare_op_bitwise_or_pair.
    def enterCompare_op_bitwise_or_pair(self, ctx:PythonParser.Compare_op_bitwise_or_pairContext):
        pass

    # Exit a parse tree produced by PythonParser#compare_op_bitwise_or_pair.
    def exitCompare_op_bitwise_or_pair(self, ctx:PythonParser.Compare_op_bitwise_or_pairContext):
        pass


    # Enter a parse tree produced by PythonParser#eq_bitwise_or.
    def enterEq_bitwise_or(self, ctx:PythonParser.Eq_bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#eq_bitwise_or.
    def exitEq_bitwise_or(self, ctx:PythonParser.Eq_bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#noteq_bitwise_or.
    def enterNoteq_bitwise_or(self, ctx:PythonParser.Noteq_bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#noteq_bitwise_or.
    def exitNoteq_bitwise_or(self, ctx:PythonParser.Noteq_bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#lte_bitwise_or.
    def enterLte_bitwise_or(self, ctx:PythonParser.Lte_bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#lte_bitwise_or.
    def exitLte_bitwise_or(self, ctx:PythonParser.Lte_bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#lt_bitwise_or.
    def enterLt_bitwise_or(self, ctx:PythonParser.Lt_bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#lt_bitwise_or.
    def exitLt_bitwise_or(self, ctx:PythonParser.Lt_bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#gte_bitwise_or.
    def enterGte_bitwise_or(self, ctx:PythonParser.Gte_bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#gte_bitwise_or.
    def exitGte_bitwise_or(self, ctx:PythonParser.Gte_bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#gt_bitwise_or.
    def enterGt_bitwise_or(self, ctx:PythonParser.Gt_bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#gt_bitwise_or.
    def exitGt_bitwise_or(self, ctx:PythonParser.Gt_bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#notin_bitwise_or.
    def enterNotin_bitwise_or(self, ctx:PythonParser.Notin_bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#notin_bitwise_or.
    def exitNotin_bitwise_or(self, ctx:PythonParser.Notin_bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#in_bitwise_or.
    def enterIn_bitwise_or(self, ctx:PythonParser.In_bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#in_bitwise_or.
    def exitIn_bitwise_or(self, ctx:PythonParser.In_bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#isnot_bitwise_or.
    def enterIsnot_bitwise_or(self, ctx:PythonParser.Isnot_bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#isnot_bitwise_or.
    def exitIsnot_bitwise_or(self, ctx:PythonParser.Isnot_bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#is_bitwise_or.
    def enterIs_bitwise_or(self, ctx:PythonParser.Is_bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#is_bitwise_or.
    def exitIs_bitwise_or(self, ctx:PythonParser.Is_bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#bitwise_or.
    def enterBitwise_or(self, ctx:PythonParser.Bitwise_orContext):
        pass

    # Exit a parse tree produced by PythonParser#bitwise_or.
    def exitBitwise_or(self, ctx:PythonParser.Bitwise_orContext):
        pass


    # Enter a parse tree produced by PythonParser#bitwise_xor.
    def enterBitwise_xor(self, ctx:PythonParser.Bitwise_xorContext):
        pass

    # Exit a parse tree produced by PythonParser#bitwise_xor.
    def exitBitwise_xor(self, ctx:PythonParser.Bitwise_xorContext):
        pass


    # Enter a parse tree produced by PythonParser#bitwise_and.
    def enterBitwise_and(self, ctx:PythonParser.Bitwise_andContext):
        pass

    # Exit a parse tree produced by PythonParser#bitwise_and.
    def exitBitwise_and(self, ctx:PythonParser.Bitwise_andContext):
        pass


    # Enter a parse tree produced by PythonParser#shift_expr.
    def enterShift_expr(self, ctx:PythonParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by PythonParser#shift_expr.
    def exitShift_expr(self, ctx:PythonParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by PythonParser#sum.
    def enterSum(self, ctx:PythonParser.SumContext):
        pass

    # Exit a parse tree produced by PythonParser#sum.
    def exitSum(self, ctx:PythonParser.SumContext):
        pass


    # Enter a parse tree produced by PythonParser#term.
    def enterTerm(self, ctx:PythonParser.TermContext):
        pass

    # Exit a parse tree produced by PythonParser#term.
    def exitTerm(self, ctx:PythonParser.TermContext):
        pass


    # Enter a parse tree produced by PythonParser#factor.
    def enterFactor(self, ctx:PythonParser.FactorContext):
        pass

    # Exit a parse tree produced by PythonParser#factor.
    def exitFactor(self, ctx:PythonParser.FactorContext):
        pass


    # Enter a parse tree produced by PythonParser#power.
    def enterPower(self, ctx:PythonParser.PowerContext):
        pass

    # Exit a parse tree produced by PythonParser#power.
    def exitPower(self, ctx:PythonParser.PowerContext):
        pass


    # Enter a parse tree produced by PythonParser#await_primary.
    def enterAwait_primary(self, ctx:PythonParser.Await_primaryContext):
        pass

    # Exit a parse tree produced by PythonParser#await_primary.
    def exitAwait_primary(self, ctx:PythonParser.Await_primaryContext):
        pass


    # Enter a parse tree produced by PythonParser#primary.
    def enterPrimary(self, ctx:PythonParser.PrimaryContext):
        pass

    # Exit a parse tree produced by PythonParser#primary.
    def exitPrimary(self, ctx:PythonParser.PrimaryContext):
        pass


    # Enter a parse tree produced by PythonParser#slices.
    def enterSlices(self, ctx:PythonParser.SlicesContext):
        pass

    # Exit a parse tree produced by PythonParser#slices.
    def exitSlices(self, ctx:PythonParser.SlicesContext):
        pass


    # Enter a parse tree produced by PythonParser#slice.
    def enterSlice(self, ctx:PythonParser.SliceContext):
        pass

    # Exit a parse tree produced by PythonParser#slice.
    def exitSlice(self, ctx:PythonParser.SliceContext):
        pass


    # Enter a parse tree produced by PythonParser#atom.
    def enterAtom(self, ctx:PythonParser.AtomContext):
        pass

    # Exit a parse tree produced by PythonParser#atom.
    def exitAtom(self, ctx:PythonParser.AtomContext):
        pass


    # Enter a parse tree produced by PythonParser#group.
    def enterGroup(self, ctx:PythonParser.GroupContext):
        pass

    # Exit a parse tree produced by PythonParser#group.
    def exitGroup(self, ctx:PythonParser.GroupContext):
        pass


    # Enter a parse tree produced by PythonParser#lambdef.
    def enterLambdef(self, ctx:PythonParser.LambdefContext):
        pass

    # Exit a parse tree produced by PythonParser#lambdef.
    def exitLambdef(self, ctx:PythonParser.LambdefContext):
        pass


    # Enter a parse tree produced by PythonParser#lambda_params.
    def enterLambda_params(self, ctx:PythonParser.Lambda_paramsContext):
        pass

    # Exit a parse tree produced by PythonParser#lambda_params.
    def exitLambda_params(self, ctx:PythonParser.Lambda_paramsContext):
        pass


    # Enter a parse tree produced by PythonParser#lambda_parameters.
    def enterLambda_parameters(self, ctx:PythonParser.Lambda_parametersContext):
        pass

    # Exit a parse tree produced by PythonParser#lambda_parameters.
    def exitLambda_parameters(self, ctx:PythonParser.Lambda_parametersContext):
        pass


    # Enter a parse tree produced by PythonParser#lambda_slash_no_default.
    def enterLambda_slash_no_default(self, ctx:PythonParser.Lambda_slash_no_defaultContext):
        pass

    # Exit a parse tree produced by PythonParser#lambda_slash_no_default.
    def exitLambda_slash_no_default(self, ctx:PythonParser.Lambda_slash_no_defaultContext):
        pass


    # Enter a parse tree produced by PythonParser#lambda_slash_with_default.
    def enterLambda_slash_with_default(self, ctx:PythonParser.Lambda_slash_with_defaultContext):
        pass

    # Exit a parse tree produced by PythonParser#lambda_slash_with_default.
    def exitLambda_slash_with_default(self, ctx:PythonParser.Lambda_slash_with_defaultContext):
        pass


    # Enter a parse tree produced by PythonParser#lambda_star_etc.
    def enterLambda_star_etc(self, ctx:PythonParser.Lambda_star_etcContext):
        pass

    # Exit a parse tree produced by PythonParser#lambda_star_etc.
    def exitLambda_star_etc(self, ctx:PythonParser.Lambda_star_etcContext):
        pass


    # Enter a parse tree produced by PythonParser#lambda_kwds.
    def enterLambda_kwds(self, ctx:PythonParser.Lambda_kwdsContext):
        pass

    # Exit a parse tree produced by PythonParser#lambda_kwds.
    def exitLambda_kwds(self, ctx:PythonParser.Lambda_kwdsContext):
        pass


    # Enter a parse tree produced by PythonParser#lambda_param_no_default.
    def enterLambda_param_no_default(self, ctx:PythonParser.Lambda_param_no_defaultContext):
        pass

    # Exit a parse tree produced by PythonParser#lambda_param_no_default.
    def exitLambda_param_no_default(self, ctx:PythonParser.Lambda_param_no_defaultContext):
        pass


    # Enter a parse tree produced by PythonParser#lambda_param_with_default.
    def enterLambda_param_with_default(self, ctx:PythonParser.Lambda_param_with_defaultContext):
        pass

    # Exit a parse tree produced by PythonParser#lambda_param_with_default.
    def exitLambda_param_with_default(self, ctx:PythonParser.Lambda_param_with_defaultContext):
        pass


    # Enter a parse tree produced by PythonParser#lambda_param_maybe_default.
    def enterLambda_param_maybe_default(self, ctx:PythonParser.Lambda_param_maybe_defaultContext):
        pass

    # Exit a parse tree produced by PythonParser#lambda_param_maybe_default.
    def exitLambda_param_maybe_default(self, ctx:PythonParser.Lambda_param_maybe_defaultContext):
        pass


    # Enter a parse tree produced by PythonParser#lambda_param.
    def enterLambda_param(self, ctx:PythonParser.Lambda_paramContext):
        pass

    # Exit a parse tree produced by PythonParser#lambda_param.
    def exitLambda_param(self, ctx:PythonParser.Lambda_paramContext):
        pass


    # Enter a parse tree produced by PythonParser#fstring_middle.
    def enterFstring_middle(self, ctx:PythonParser.Fstring_middleContext):
        pass

    # Exit a parse tree produced by PythonParser#fstring_middle.
    def exitFstring_middle(self, ctx:PythonParser.Fstring_middleContext):
        pass


    # Enter a parse tree produced by PythonParser#fstring_replacement_field.
    def enterFstring_replacement_field(self, ctx:PythonParser.Fstring_replacement_fieldContext):
        pass

    # Exit a parse tree produced by PythonParser#fstring_replacement_field.
    def exitFstring_replacement_field(self, ctx:PythonParser.Fstring_replacement_fieldContext):
        pass


    # Enter a parse tree produced by PythonParser#fstring_conversion.
    def enterFstring_conversion(self, ctx:PythonParser.Fstring_conversionContext):
        pass

    # Exit a parse tree produced by PythonParser#fstring_conversion.
    def exitFstring_conversion(self, ctx:PythonParser.Fstring_conversionContext):
        pass


    # Enter a parse tree produced by PythonParser#fstring_full_format_spec.
    def enterFstring_full_format_spec(self, ctx:PythonParser.Fstring_full_format_specContext):
        pass

    # Exit a parse tree produced by PythonParser#fstring_full_format_spec.
    def exitFstring_full_format_spec(self, ctx:PythonParser.Fstring_full_format_specContext):
        pass


    # Enter a parse tree produced by PythonParser#fstring_format_spec.
    def enterFstring_format_spec(self, ctx:PythonParser.Fstring_format_specContext):
        pass

    # Exit a parse tree produced by PythonParser#fstring_format_spec.
    def exitFstring_format_spec(self, ctx:PythonParser.Fstring_format_specContext):
        pass


    # Enter a parse tree produced by PythonParser#fstring.
    def enterFstring(self, ctx:PythonParser.FstringContext):
        pass

    # Exit a parse tree produced by PythonParser#fstring.
    def exitFstring(self, ctx:PythonParser.FstringContext):
        pass


    # Enter a parse tree produced by PythonParser#string.
    def enterString(self, ctx:PythonParser.StringContext):
        pass

    # Exit a parse tree produced by PythonParser#string.
    def exitString(self, ctx:PythonParser.StringContext):
        pass


    # Enter a parse tree produced by PythonParser#strings.
    def enterStrings(self, ctx:PythonParser.StringsContext):
        pass

    # Exit a parse tree produced by PythonParser#strings.
    def exitStrings(self, ctx:PythonParser.StringsContext):
        pass


    # Enter a parse tree produced by PythonParser#list.
    def enterList(self, ctx:PythonParser.ListContext):
        pass

    # Exit a parse tree produced by PythonParser#list.
    def exitList(self, ctx:PythonParser.ListContext):
        pass


    # Enter a parse tree produced by PythonParser#tuple.
    def enterTuple(self, ctx:PythonParser.TupleContext):
        pass

    # Exit a parse tree produced by PythonParser#tuple.
    def exitTuple(self, ctx:PythonParser.TupleContext):
        pass


    # Enter a parse tree produced by PythonParser#set.
    def enterSet(self, ctx:PythonParser.SetContext):
        pass

    # Exit a parse tree produced by PythonParser#set.
    def exitSet(self, ctx:PythonParser.SetContext):
        pass


    # Enter a parse tree produced by PythonParser#dict.
    def enterDict(self, ctx:PythonParser.DictContext):
        pass

    # Exit a parse tree produced by PythonParser#dict.
    def exitDict(self, ctx:PythonParser.DictContext):
        pass


    # Enter a parse tree produced by PythonParser#double_starred_kvpairs.
    def enterDouble_starred_kvpairs(self, ctx:PythonParser.Double_starred_kvpairsContext):
        pass

    # Exit a parse tree produced by PythonParser#double_starred_kvpairs.
    def exitDouble_starred_kvpairs(self, ctx:PythonParser.Double_starred_kvpairsContext):
        pass


    # Enter a parse tree produced by PythonParser#double_starred_kvpair.
    def enterDouble_starred_kvpair(self, ctx:PythonParser.Double_starred_kvpairContext):
        pass

    # Exit a parse tree produced by PythonParser#double_starred_kvpair.
    def exitDouble_starred_kvpair(self, ctx:PythonParser.Double_starred_kvpairContext):
        pass


    # Enter a parse tree produced by PythonParser#kvpair.
    def enterKvpair(self, ctx:PythonParser.KvpairContext):
        pass

    # Exit a parse tree produced by PythonParser#kvpair.
    def exitKvpair(self, ctx:PythonParser.KvpairContext):
        pass


    # Enter a parse tree produced by PythonParser#for_if_clauses.
    def enterFor_if_clauses(self, ctx:PythonParser.For_if_clausesContext):
        pass

    # Exit a parse tree produced by PythonParser#for_if_clauses.
    def exitFor_if_clauses(self, ctx:PythonParser.For_if_clausesContext):
        pass


    # Enter a parse tree produced by PythonParser#for_if_clause.
    def enterFor_if_clause(self, ctx:PythonParser.For_if_clauseContext):
        pass

    # Exit a parse tree produced by PythonParser#for_if_clause.
    def exitFor_if_clause(self, ctx:PythonParser.For_if_clauseContext):
        pass


    # Enter a parse tree produced by PythonParser#listcomp.
    def enterListcomp(self, ctx:PythonParser.ListcompContext):
        pass

    # Exit a parse tree produced by PythonParser#listcomp.
    def exitListcomp(self, ctx:PythonParser.ListcompContext):
        pass


    # Enter a parse tree produced by PythonParser#setcomp.
    def enterSetcomp(self, ctx:PythonParser.SetcompContext):
        pass

    # Exit a parse tree produced by PythonParser#setcomp.
    def exitSetcomp(self, ctx:PythonParser.SetcompContext):
        pass


    # Enter a parse tree produced by PythonParser#genexp.
    def enterGenexp(self, ctx:PythonParser.GenexpContext):
        pass

    # Exit a parse tree produced by PythonParser#genexp.
    def exitGenexp(self, ctx:PythonParser.GenexpContext):
        pass


    # Enter a parse tree produced by PythonParser#dictcomp.
    def enterDictcomp(self, ctx:PythonParser.DictcompContext):
        pass

    # Exit a parse tree produced by PythonParser#dictcomp.
    def exitDictcomp(self, ctx:PythonParser.DictcompContext):
        pass


    # Enter a parse tree produced by PythonParser#arguments.
    def enterArguments(self, ctx:PythonParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by PythonParser#arguments.
    def exitArguments(self, ctx:PythonParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by PythonParser#args.
    def enterArgs(self, ctx:PythonParser.ArgsContext):
        pass

    # Exit a parse tree produced by PythonParser#args.
    def exitArgs(self, ctx:PythonParser.ArgsContext):
        pass


    # Enter a parse tree produced by PythonParser#kwargs.
    def enterKwargs(self, ctx:PythonParser.KwargsContext):
        pass

    # Exit a parse tree produced by PythonParser#kwargs.
    def exitKwargs(self, ctx:PythonParser.KwargsContext):
        pass


    # Enter a parse tree produced by PythonParser#starred_expression.
    def enterStarred_expression(self, ctx:PythonParser.Starred_expressionContext):
        pass

    # Exit a parse tree produced by PythonParser#starred_expression.
    def exitStarred_expression(self, ctx:PythonParser.Starred_expressionContext):
        pass


    # Enter a parse tree produced by PythonParser#kwarg_or_starred.
    def enterKwarg_or_starred(self, ctx:PythonParser.Kwarg_or_starredContext):
        pass

    # Exit a parse tree produced by PythonParser#kwarg_or_starred.
    def exitKwarg_or_starred(self, ctx:PythonParser.Kwarg_or_starredContext):
        pass


    # Enter a parse tree produced by PythonParser#kwarg_or_double_starred.
    def enterKwarg_or_double_starred(self, ctx:PythonParser.Kwarg_or_double_starredContext):
        pass

    # Exit a parse tree produced by PythonParser#kwarg_or_double_starred.
    def exitKwarg_or_double_starred(self, ctx:PythonParser.Kwarg_or_double_starredContext):
        pass


    # Enter a parse tree produced by PythonParser#star_targets.
    def enterStar_targets(self, ctx:PythonParser.Star_targetsContext):
        pass

    # Exit a parse tree produced by PythonParser#star_targets.
    def exitStar_targets(self, ctx:PythonParser.Star_targetsContext):
        pass


    # Enter a parse tree produced by PythonParser#star_targets_list_seq.
    def enterStar_targets_list_seq(self, ctx:PythonParser.Star_targets_list_seqContext):
        pass

    # Exit a parse tree produced by PythonParser#star_targets_list_seq.
    def exitStar_targets_list_seq(self, ctx:PythonParser.Star_targets_list_seqContext):
        pass


    # Enter a parse tree produced by PythonParser#star_targets_tuple_seq.
    def enterStar_targets_tuple_seq(self, ctx:PythonParser.Star_targets_tuple_seqContext):
        pass

    # Exit a parse tree produced by PythonParser#star_targets_tuple_seq.
    def exitStar_targets_tuple_seq(self, ctx:PythonParser.Star_targets_tuple_seqContext):
        pass


    # Enter a parse tree produced by PythonParser#star_target.
    def enterStar_target(self, ctx:PythonParser.Star_targetContext):
        pass

    # Exit a parse tree produced by PythonParser#star_target.
    def exitStar_target(self, ctx:PythonParser.Star_targetContext):
        pass


    # Enter a parse tree produced by PythonParser#target_with_star_atom.
    def enterTarget_with_star_atom(self, ctx:PythonParser.Target_with_star_atomContext):
        pass

    # Exit a parse tree produced by PythonParser#target_with_star_atom.
    def exitTarget_with_star_atom(self, ctx:PythonParser.Target_with_star_atomContext):
        pass


    # Enter a parse tree produced by PythonParser#star_atom.
    def enterStar_atom(self, ctx:PythonParser.Star_atomContext):
        pass

    # Exit a parse tree produced by PythonParser#star_atom.
    def exitStar_atom(self, ctx:PythonParser.Star_atomContext):
        pass


    # Enter a parse tree produced by PythonParser#single_target.
    def enterSingle_target(self, ctx:PythonParser.Single_targetContext):
        pass

    # Exit a parse tree produced by PythonParser#single_target.
    def exitSingle_target(self, ctx:PythonParser.Single_targetContext):
        pass


    # Enter a parse tree produced by PythonParser#single_subscript_attribute_target.
    def enterSingle_subscript_attribute_target(self, ctx:PythonParser.Single_subscript_attribute_targetContext):
        pass

    # Exit a parse tree produced by PythonParser#single_subscript_attribute_target.
    def exitSingle_subscript_attribute_target(self, ctx:PythonParser.Single_subscript_attribute_targetContext):
        pass


    # Enter a parse tree produced by PythonParser#t_primary.
    def enterT_primary(self, ctx:PythonParser.T_primaryContext):
        pass

    # Exit a parse tree produced by PythonParser#t_primary.
    def exitT_primary(self, ctx:PythonParser.T_primaryContext):
        pass


    # Enter a parse tree produced by PythonParser#del_targets.
    def enterDel_targets(self, ctx:PythonParser.Del_targetsContext):
        pass

    # Exit a parse tree produced by PythonParser#del_targets.
    def exitDel_targets(self, ctx:PythonParser.Del_targetsContext):
        pass


    # Enter a parse tree produced by PythonParser#del_target.
    def enterDel_target(self, ctx:PythonParser.Del_targetContext):
        pass

    # Exit a parse tree produced by PythonParser#del_target.
    def exitDel_target(self, ctx:PythonParser.Del_targetContext):
        pass


    # Enter a parse tree produced by PythonParser#del_t_atom.
    def enterDel_t_atom(self, ctx:PythonParser.Del_t_atomContext):
        pass

    # Exit a parse tree produced by PythonParser#del_t_atom.
    def exitDel_t_atom(self, ctx:PythonParser.Del_t_atomContext):
        pass


    # Enter a parse tree produced by PythonParser#type_expressions.
    def enterType_expressions(self, ctx:PythonParser.Type_expressionsContext):
        pass

    # Exit a parse tree produced by PythonParser#type_expressions.
    def exitType_expressions(self, ctx:PythonParser.Type_expressionsContext):
        pass


    # Enter a parse tree produced by PythonParser#func_type_comment.
    def enterFunc_type_comment(self, ctx:PythonParser.Func_type_commentContext):
        pass

    # Exit a parse tree produced by PythonParser#func_type_comment.
    def exitFunc_type_comment(self, ctx:PythonParser.Func_type_commentContext):
        pass


    # Enter a parse tree produced by PythonParser#soft_kw_type.
    def enterSoft_kw_type(self, ctx:PythonParser.Soft_kw_typeContext):
        pass

    # Exit a parse tree produced by PythonParser#soft_kw_type.
    def exitSoft_kw_type(self, ctx:PythonParser.Soft_kw_typeContext):
        pass


    # Enter a parse tree produced by PythonParser#soft_kw_match.
    def enterSoft_kw_match(self, ctx:PythonParser.Soft_kw_matchContext):
        pass

    # Exit a parse tree produced by PythonParser#soft_kw_match.
    def exitSoft_kw_match(self, ctx:PythonParser.Soft_kw_matchContext):
        pass


    # Enter a parse tree produced by PythonParser#soft_kw_case.
    def enterSoft_kw_case(self, ctx:PythonParser.Soft_kw_caseContext):
        pass

    # Exit a parse tree produced by PythonParser#soft_kw_case.
    def exitSoft_kw_case(self, ctx:PythonParser.Soft_kw_caseContext):
        pass


    # Enter a parse tree produced by PythonParser#soft_kw_wildcard.
    def enterSoft_kw_wildcard(self, ctx:PythonParser.Soft_kw_wildcardContext):
        pass

    # Exit a parse tree produced by PythonParser#soft_kw_wildcard.
    def exitSoft_kw_wildcard(self, ctx:PythonParser.Soft_kw_wildcardContext):
        pass


    # Enter a parse tree produced by PythonParser#soft_kw__not__wildcard.
    def enterSoft_kw__not__wildcard(self, ctx:PythonParser.Soft_kw__not__wildcardContext):
        pass

    # Exit a parse tree produced by PythonParser#soft_kw__not__wildcard.
    def exitSoft_kw__not__wildcard(self, ctx:PythonParser.Soft_kw__not__wildcardContext):
        pass



del PythonParser
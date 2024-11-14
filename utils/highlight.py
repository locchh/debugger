import os
import sys
sys.path.append(os.path.join("..",os.getcwd()))


from termcolor import colored

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from parser.MyLanguageLexer import MyLanguageLexer  # Replace with your actual lexer class
from parser.MyLanguageParser import MyLanguageParser  # Replace with your actual parser class

# Custom error listener to capture syntax errors with row and column information
class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []  # Store errors as tuples (line, column, message)
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Store syntax error details
        self.errors.append((line, column, msg))

# Function to highlight code based on syntax errors, with row and column granularity
def highlight_code(file_path):
    # Set up the input stream and lexer
    input_stream = FileStream(file_path)
    lexer = MyLanguageLexer(input_stream)  # Use your generated lexer
    stream = CommonTokenStream(lexer)
    parser = MyLanguageParser(stream)  # Use your generated parser
    
    # Attach custom error listener to capture syntax errors
    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()  # Remove default error listener
    parser.addErrorListener(error_listener)

    # Parse the input file (top rule should be your language's main rule, like 'program')
    parser.program()  # Replace 'program' with the actual entry point rule of your grammar
    
    # Read the file line-by-line, and apply detailed highlighting based on errors
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line_num, line_content in enumerate(lines, start=1):
            # Find errors for the current line
            line_errors = [err for err in error_listener.errors if err[0] == line_num]
            
            if not line_errors:
                # No errors on this line, print it in green
                print(colored(line_content.strip(), 'green'))
            else:
                # Highlight each error segment in red
                highlighted_line = ""
                last_index = 0
                for _, column, msg in line_errors:
                    # Add the portion before the error in normal color
                    highlighted_line += line_content[last_index:column]
                    # Highlight the error portion in red
                    highlighted_line += colored(line_content[column:column+1], 'red')
                    last_index = column + 1

                # Add any remaining part of the line
                highlighted_line += line_content[last_index:].strip()
                print(highlighted_line)

# Example usage
if __name__ == "__main__":
    file_path = sys.argv[1]
    highlight_code(file_path)

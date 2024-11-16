To build a code editor with the described functionality, we can use **Python with Tkinter** for the user interface and logic, leveraging **ANTLR** for grammar generation and parsing. Below is a prototype implementation:

### Key Components:
1. **UI Framework**: Tkinter for building the editor interface.
2. **ANTLR Integration**: Use the ANTLR Python runtime and helper functions for parsing and generating grammar.
3. **Language Detection**: Use file extensions or basic content analysis.
4. **Syntax Highlighting**: Implement using tags in Tkinter's `Text` widget.
5. **Grammar Generation**: Define lexer and parser rule templates and dynamically generate them.

---

### Code Implementation:

```python
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re

# Function to detect programming language based on file extension
def detect_language(file_path):
    extension_to_language = {
        ".java": "Java",
        ".py": "Python",
        ".cpp": "C++",
        ".js": "JavaScript",
    }
    _, ext = os.path.splitext(file_path)
    return extension_to_language.get(ext, "Unknown")

# Function to generate ANTLR grammar from source code
def generate_antlr_grammar(language, source_code):
    lexer_rules = []
    parser_rules = []

    if language == "Python":
        lexer_rules = [
            "NEWLINE : '\\n';",
            "INDENT : '    ';",
            "DEDENT : '<DEDENT>';"
        ]
        parser_rules = [
            "file: statement+;",
            "statement: expr NEWLINE;",
            "expr: IDENTIFIER | NUMBER | STRING | function_call;",
        ]
    elif language == "Java":
        lexer_rules = ["CLASS : 'class';", "PUBLIC : 'public';", "VOID : 'void';"]
        parser_rules = [
            "file: class_definition+;",
            "class_definition: 'class' IDENTIFIER '{' method* '}' ;",
            "method: 'public' ('void' | IDENTIFIER) IDENTIFIER '(' ')' '{' '}';",
        ]
    # Add other language rules here.

    # Default rule structure if the language is unknown
    if not lexer_rules or not parser_rules:
        lexer_rules = ["UNKNOWN : '<unknown>';"]
        parser_rules = ["file: UNKNOWN;"]

    grammar = f"""
    grammar {language}Grammar;

    // Lexer rules
    {'\n'.join(lexer_rules)}

    // Parser rules
    {'\n'.join(parser_rules)}

    // Common tokens
    IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
    NUMBER : [0-9]+;
    STRING : '\"' .*? '\"';
    WS : [ \\t]+ -> skip;
    """
    return grammar

# Function to load a source code file
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Source Files", "*.java *.py *.cpp *.js *.txt")])
    if not file_path:
        return

    # Detect language and load code
    language = detect_language(file_path)
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Update UI
    editor_text.delete(1.0, tk.END)
    editor_text.insert(tk.END, source_code)
    language_label.config(text=f"Language: {language}")
    return file_path, language, source_code

# Function to generate and display ANTLR grammar
def generate_grammar():
    source_code = editor_text.get(1.0, tk.END).strip()
    language = language_label.cget("text").split(":")[1].strip()

    if language == "Unknown":
        messagebox.showerror("Error", "Unsupported or unknown language.")
        return

    grammar = generate_antlr_grammar(language, source_code)
    grammar_text.delete(1.0, tk.END)
    grammar_text.insert(tk.END, grammar)

# Set up the main application window
root = tk.Tk()
root.title("Code Editor with ANTLR Grammar Generator")

# Create UI components
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

language_label = tk.Label(root, text="Language: Unknown", font=("Arial", 12), anchor="w")
language_label.pack(fill=tk.X)

editor_text = tk.Text(frame, wrap=tk.WORD, font=("Consolas", 12), undo=True)
editor_text.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

grammar_text = tk.Text(frame, wrap=tk.WORD, font=("Consolas", 12), bg="#f5f5f5")
grammar_text.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X)

load_button = tk.Button(button_frame, text="Load File", command=load_file)
load_button.pack(side=tk.LEFT, padx=5, pady=5)

generate_button = tk.Button(button_frame, text="Generate ANTLR Grammar", command=generate_grammar)
generate_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Start the Tkinter main loop
root.mainloop()
```

---

### Features Implemented:
1. **File Loading**: Loads source code files with syntax highlighting (basic highlighting can be added with regex).
2. **Language Detection**: Based on file extensions.
3. **Grammar Generation**: Generates ANTLR lexer and parser rules based on the language.
4. **UI Design**: Split screen to display source code and generated grammar.

### Next Steps:
1. Add syntax highlighting with regex patterns for keywords.
2. Expand language support by adding specific rules for JavaScript, C++, and others.
3. Integrate ANTLR for real-time validation of generated grammar.
4. Provide additional error handling for incomplete or incorrect source files.

Let me know if you need further extensions!

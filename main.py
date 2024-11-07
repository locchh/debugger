import tkinter as tk
from tkinter import filedialog, messagebox
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from MyLanguageLexer import MyLanguageLexer
from MyLanguageParser import MyLanguageParser

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Syntax error at line {line}, column {column}: {msg}")

class CodeEditorDebugger:
    def __init__(self, root):
        self.root = root
        self.filename = None
        self.create_ui()
        self.bind_shortcuts()

    def create_ui(self):
        # Create a menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Create File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Open", command=self.load_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)

        # Add Debug button directly in the menu bar
        debug_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="🐞 Debug", menu=debug_menu)
        debug_menu.add_command(label="Run Debug", command=self.run_debug)

        # Line Number Text Area
        self.line_numbers = tk.Text(self.root, width=4, padx=4, takefocus=0, border=0, background="lightgray", state="disabled")
        self.line_numbers.pack(side="left", fill="y")

        # Create a scrollbar for the text area
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side="right", fill="y")

        # Editor Area with undo enabled for keyboard shortcuts
        self.text_area = tk.Text(self.root, wrap="none", undo=True, yscrollcommand=self.scrollbar.set)
        self.text_area.pack(fill="both", expand=True, side="right")

        # Attach the scrollbar to the text area
        self.scrollbar.config(command=self.text_area.yview)
        
        self.text_area.bind("<KeyRelease>", self.update_line_numbers)

    def bind_shortcuts(self):
        # Bind keyboard shortcuts
        self.root.bind("<Control-z>", lambda event: self.text_area.edit_undo())
        self.root.bind("<Control-y>", lambda event: self.text_area.edit_redo())
        self.root.bind("<Control-x>", lambda event: self.cut_text())
        self.root.bind("<Control-c>", lambda event: self.copy_text())
        self.root.bind("<Control-v>", lambda event: self.paste_text())
        self.root.bind("<Control-a>", lambda event: self.select_all_text())  # Add Select All shortcut

    def select_all_text(self):
        # Select all text in the text_area
        self.text_area.tag_add("sel", "1.0", "end")
        self.text_area.mark_set("insert", "end")  # Move the cursor to the end
        self.text_area.see("insert")  # Ensure the cursor is visible

    def update_line_numbers(self, event=None):
        # Update the line numbers in the line_numbers widget
        self.line_numbers.config(state="normal")
        self.line_numbers.delete(1.0, tk.END)
        
        # Insert line numbers
        lines = self.text_area.index(tk.END).split('.')[0]
        line_numbers_string = "\n".join(str(i) for i in range(1, int(lines)))
        self.line_numbers.insert("1.0", line_numbers_string)
        self.line_numbers.config(state="disabled")

    def load_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not self.filename:
            return
        with open(self.filename, "r") as file:
            content = file.read()
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", content)
        self.update_line_numbers()

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))
            messagebox.showinfo("Save", "File saved successfully!")
        else:
            self.save_file_as()

    def save_file_as(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))
            messagebox.showinfo("Save As", "File saved successfully!")

    def run_debug(self):
        code = self.text_area.get("1.0", tk.END)
        input_stream = InputStream(code)
        
        lexer = MyLanguageLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = MyLanguageParser(token_stream)

        # Adding custom error listener
        error_listener = SyntaxErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        # Parse and check for syntax errors
        try:
            tree = parser.program()  # Assuming 'program' is the start rule
            if error_listener.errors:
                messagebox.showerror("Syntax Error", "\n".join(error_listener.errors))
                return
            
            # Debugging: Step through parsed tokens (for a basic demo)
            for token in token_stream.tokens:
                print(f"Token: {token.text}, Line: {token.line}")
                # Add breakpoints and step-by-step execution logic here

            messagebox.showinfo("Debug", "Debugging completed successfully!")
        
        except Exception as e:
            messagebox.showerror("Error", f"Error during parsing: {str(e)}")

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Code Editor with Debugger")
    editor = CodeEditorDebugger(root)
    root.geometry("800x600")
    root.mainloop()

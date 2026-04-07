import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Basic Calculator")
        self.root.geometry("320x560")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')
        
        # Variables
        self.current = "0"
        self.previous = ""
        self.operation = ""
        self.should_reset = False
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="🧮 Calculator", 
                        font=('Arial', 24, 'bold'), 
                        bg='#2c3e50', fg='#ecf0f1')
        title.pack(pady=10)
        
        # Display Frame
        display_frame = tk.Frame(self.root, bg='#34495e', relief='ridge', bd=2)
        display_frame.pack(pady=10, padx=20, fill='x')

        # Line 1: Expression label (e.g., "12 + 5")
        self.expression_var = tk.StringVar(value="")
        self.expression_label = tk.Label(
            display_frame,
            textvariable=self.expression_var,
            font=('Arial', 14),
            bg='#34495e',
            fg='#95a5a6',   # muted gray for the expression
            anchor='e',
            padx=15,
            pady=10
        )
        self.expression_label.pack(fill='x')

        # Line 2: Result / current number
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=('Arial', 28, 'bold'),
            bg='#34495e',
            fg='#ecf0f1',
            anchor='e',
            padx=15,
            pady=10
        )
        self.display.pack(fill='x')
        
        # Buttons Frame
        buttons_frame = tk.Frame(self.root, bg='#2c3e50')
        buttons_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Button layout
        buttons = [
            ('C', 1), ('±', 1), ('%', 1), ('÷', 1),
            ('7', 1), ('8', 1), ('9', 1), ('×', 1),
            ('4', 1), ('5', 1), ('6', 1), ('-', 1),
            ('1', 1), ('2', 1), ('3', 1), ('+', 1),
            ('0', 2), ('.', 1), ('=', 1)
        ]
        
        row, col = 0, 0
        for (text, span) in buttons:
            if text == '0':
                btn = tk.Button(buttons_frame, text=text, font=('Arial', 18, 'bold'),
                               bg='#3498db', fg='white', bd=0, padx=30, pady=20,
                               command=lambda t=text: self.button_click(t),
                               relief='flat', activebackground='#2980b9')
                btn.grid(row=row, column=col, columnspan=span, sticky='nsew', padx=2, pady=2)
                col += span
            else:
                btn = tk.Button(buttons_frame, text=text, font=('Arial', 18, 'bold'),
                               bg='#95a5a6' if text.isdigit() or text == '.' else '#e74c3c',
                               fg='white', bd=0, padx=30, pady=20,
                               command=lambda t=text: self.button_click(t),
                               relief='flat',
                               activebackground='#7f8c8d' if text.isdigit() else '#c0392b')
                btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
                col += 1
            
            if col >= 4:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
    
    def button_click(self, char):
        if char.isdigit() or char == '.':
            self.input_number(char)
        elif char in '+-×÷':
            self.input_operation(char)
        elif char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        elif char == '±':
            self.toggle_sign()
        elif char == '%':
            self.percentage()
    
    def update_expression(self):
        """Update the top expression line."""
        if self.previous and self.operation:
            op_display = self.operation.replace('*', '×').replace('/', '÷')
            if self.should_reset:
                # Operator just pressed — show: previous op _
                self.expression_var.set(f"{self.previous} {op_display}")
            else:
                # User is typing second operand — show: previous op current
                self.expression_var.set(f"{self.previous} {op_display} {self.current}")
        else:
            self.expression_var.set("")

    def input_number(self, num):
        if self.should_reset or self.current == "0":
            self.current = num
            self.should_reset = False
        elif num == '.' and '.' in self.current:
            return
        else:
            self.current += num
        self.display_var.set(self.current)
        self.update_expression()
    
    def input_operation(self, op):
        if self.operation and not self.should_reset:
            self.calculate(finalize=False)
        self.previous = self.current
        self.operation = op.replace('×', '*').replace('÷', '/')
        self.should_reset = True
        self.update_expression()
    
    def calculate(self, finalize=True):
        if self.previous and self.operation:
            try:
                op_display = self.operation.replace('*', '×').replace('/', '÷')
                full_expr = f"{self.previous} {op_display} {self.current}"
                result = eval(f"{self.previous}{self.operation}{self.current}")
                # Format result: remove unnecessary decimals
                result_str = str(int(result)) if isinstance(result, float) and result.is_integer() else str(result)
                if finalize:
                    # Show full expression on top, result on bottom
                    self.expression_var.set(full_expr + " =")
                self.current = result_str
                self.operation = ""
                self.previous = ""
                self.should_reset = True
                self.display_var.set(self.current)
            except:
                self.expression_var.set("")
                self.current = "Error"
                self.display_var.set(self.current)
                self.should_reset = True
    
    def clear(self):
        self.current = "0"
        self.previous = ""
        self.operation = ""
        self.should_reset = False
        self.display_var.set("0")
        self.expression_var.set("")
    
    def toggle_sign(self):
        if self.current not in ("0", "Error"):
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
            self.display_var.set(self.current)
            self.update_expression()
    
    def percentage(self):
        if self.current not in ("0", "Error"):
            self.current = str(float(self.current) / 100)
            self.display_var.set(self.current)
            self.update_expression()

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
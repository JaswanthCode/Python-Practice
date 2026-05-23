import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("360x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self.expression = ""

        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.create_display()
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#1e1e2f")
        display_frame.pack(fill="both", padx=15, pady=15)

        display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 24),
            bd=0,
            bg="#2d2d44",
            fg="white",
            justify="right"
        )
        display.pack(fill="both", ipady=20)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#1e1e2f")
        button_frame.pack(expand=True, fill="both", padx=15, pady=(0, 15))

        buttons = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for row_index, row in enumerate(buttons):
            for col_index, button_text in enumerate(row):
                if button_text == "0":
                    btn = tk.Button(
                        button_frame,
                        text=button_text,
                        font=("Arial", 18, "bold"),
                        bg="#3b3b5c",
                        fg="white",
                        bd=0,
                        command=lambda value=button_text: self.on_button_click(value)
                    )
                    btn.grid(row=row_index, column=col_index, columnspan=2, sticky="nsew", padx=5, pady=5)
                    continue

                if row_index == 4 and col_index > 0:
                    actual_col = col_index + 1
                else:
                    actual_col = col_index

                color = "#ff9f43" if button_text in {"/", "*", "-", "+", "="} else "#3b3b5c"
                if button_text in {"C", "⌫", "%"}:
                    color = "#575fcf"

                btn = tk.Button(
                    button_frame,
                    text=button_text,
                    font=("Arial", 18, "bold"),
                    bg=color,
                    fg="white",
                    bd=0,
                    command=lambda value=button_text: self.on_button_click(value)
                )
                btn.grid(row=row_index, column=actual_col, sticky="nsew", padx=5, pady=5)

        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)

        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "C":
            self.expression = ""
            self.display_var.set("0")

        elif value == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")

        elif value == "=":
            try:
                result = str(eval(self.expression))
                self.display_var.set(result)
                self.expression = result
            except:
                self.display_var.set("Error")
                self.expression = ""

        else:
            if self.display_var.get() == "0" and value not in {"+", "-", "*", "/", "%", "."}:
                self.expression = value
            else:
                self.expression += value
            self.display_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

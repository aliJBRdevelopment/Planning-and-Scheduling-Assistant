from tkinter import *

class RegLog():
    def __init__(self):
        self.root = Tk()
        self.root.title("PSA")
        self.root.geometry("200x200")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        self.reg_log_frame = Frame(self.root, bg="white")
        self.reg_log_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.reg_button = Button(self.reg_log_frame, text="Register", bg="white", font=("Times New Roman", 15), command=self.register)
        self.reg_button.grid(row=1, column=0, padx=10, pady=10)

        self.log_button = Button(self.reg_log_frame, text="Login", bg="white", font=("Times New Roman", 15), command=self.login)
        self.log_button.grid(row=1, column=1, padx=10, pady=10)

        self.root.mainloop()
    
    def register(self):
        pass

    def login(self):
        pass
    

test = RegLog()
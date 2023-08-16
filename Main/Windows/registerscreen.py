from tkinter import *
#class for registration screen
class Register():
    def __init__(self):
        #window setup
        self.root = Tk()
        self.root.title("PSA - Register")
        self.root.geometry("750x500")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        
        #labels setup
        self.reg_name_label = Label(self.root, text="Name:", bg="white", font=("Times New Roman", 25))
        self.reg_name_label.grid(row=1, column=0, padx=10, pady=50)

        self.reg_email_label = Label(self.root, text="Email:", bg="white", font=("Times New Roman", 25))
        self.reg_email_label.grid(row=2, column=0, padx=10, pady=50)

        self.reg_password_label = Label(self.root, text="Password:", bg="white", font=("Times New Roman", 25))
        self.reg_password_label.grid(row=3, column=0, padx=10, pady=50)

        #input setup
        self.reg_name_input = Entry(self.root, width=50, bg="lightgray", font=("Times New Roman", 15))
        self.reg_name_input.grid(row=1, column=2, padx=10, pady=50)

        self.reg_email_input = Entry(self.root, width=50, bg="lightgray", font=("Times New Roman", 15))
        self.reg_email_input.grid(row=2, column=2, padx=10, pady=50)

        self.reg_pword_input = Entry(self.root, width=50, bg="lightgray", font=("Times New Roman", 15))
        self.reg_pword_input.grid(row=3, column=2, padx=10, pady=50)


        #return to previous screen
        self.ret_button = Button(self.root, text="Return", bg="red", font=("Times New Roman", 15), command=self.return_decider)
        self.ret_button.place(x=625,y=450)
        self.ret_button.configure(width=7, height = 1)

        #register new user
        self.reg_button = Button(self.root, text="Register", bg="green", font=("Times New Roman", 15), command=self.return_decider)
        self.reg_button.place(x=25,y=450)
        self.reg_button.configure(width=7, height = 1)

        self.root.mainloop()
    
    def register(self):
        pass

    def return_decider(self):
        pass
    

test = Register()
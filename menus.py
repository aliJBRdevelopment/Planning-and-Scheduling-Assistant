import random
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import User
import datamgr
#class for registration screen
class MainMenu():
    def __init__(self, email):
        #window setup
        self.email = email.lower()
        self.root = Tk()
        self.root.title("PSA")
        self.root.geometry("750x500")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        self.task_listbox = Listbox(self.root, width=70, height=15, bg="lightgray", font=("Times New Roman", 15))
        self.task_listbox.grid(row=0, column=0, padx=25, pady=50, columnspan=2, rowspan=1)

        #logout
        self.logout_button = Button(self.root, text="Logout", bg="red", fg="black", font=("Times New Roman", 15), command=self.return_decider)
        self.logout_button.place(x=625,y=450)
        self.logout_button.configure(width=7, height = 1)

        #add task
        self.add_task_button = Button(self.root, text="Add Task", bg="green", font=("Times New Roman", 15), command=self.add_task_button)
        self.add_task_button.place(x=25,y=450)
        self.add_task_button.configure(width=7, height = 1)

        t = User.Tasks()
        for i,task in enumerate(t.current_tasks):
            print(task)
            if email in task[2]:
                self.task_listbox.insert(END, [task[0], task[1], task[2]])

        self.root.mainloop()
    
    def add_task_button(self):
        temp_title = sd.askstring("Add Task", "Enter task name")
        temp_date = sd.askstring("Add Task", "Enter task date")
        temp_part = sd.askstring("Add Task", "Enter task partcipants, separated by a comma").split(",")
        for part in temp_part:
            part.lower()
        temp_id = random.randint(1,1000000)
        User.Tasks.save_task([temp_title, temp_date,temp_part, temp_id])
        self.task_listbox.insert(END, temp_title, temp_date, temp_part, temp_id)

    def return_decider(self):
        self.root.destroy()
        regLogScreen = RegLog()
    
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

        self.reg_pword_input = Entry(self.root, width=50, bg="lightgray", font=("Times New Roman", 15), show="*")
        self.reg_pword_input.grid(row=3, column=2, padx=10, pady=50)


        #return to previous screen
        self.ret_button = Button(self.root, text="Return", bg="red", font=("Times New Roman", 15), command=self.return_decider)
        self.ret_button.place(x=625,y=450)
        self.ret_button.configure(width=7, height = 1)

        #register new user
        self.reg_button = Button(self.root, text="Register", bg="green", font=("Times New Roman", 15), command=self.register)
        self.reg_button.place(x=25,y=450)
        self.reg_button.configure(width=7, height = 1)


        self.root.mainloop()

    
    def register(self):
        tmp_name = self.reg_name_input.get()
        tmp_email = self.reg_email_input.get()
        tmp_password = self.reg_pword_input.get()

        if datamgr.UserDetails.register_user(tmp_email, tmp_name, tmp_password):
            self.root.destroy()
            menu = MainMenu(tmp_email)
        else:
            mb.showerror("UNABLE TO REGISTER", "Email already in use for another accoount")

    def return_decider(self):
        self.root.destroy()
        regLogScreen = RegLog()

class Login():
    def __init__(self):
        #window setup
        self.root = Tk()
        self.root.title("PSA - Login")
        self.root.geometry("750x500")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        
        #labels setup
        self.log_email_label = Label(self.root, text="Email:", bg="white", font=("Times New Roman", 25))
        self.log_email_label.grid(row=1, column=0, padx=10, pady=50)

        self.log_pword_label = Label(self.root, text="Password:", bg="white", font=("Times New Roman", 25))
        self.log_pword_label.grid(row=2, column=0, padx=10, pady=50)

        #input setup
        self.log_email_input = Entry(self.root, width=50, bg="lightgray", font=("Times New Roman", 15))
        self.log_email_input.grid(row=1, column=2, padx=10, pady=50)

        self.log_pword_input = Entry(self.root, width=50, bg="lightgray", font=("Times New Roman", 15), show="*")
        self.log_pword_input.grid(row=2, column=2, padx=10, pady=50)


        #return to previous screen
        self.ret_button = Button(self.root, text="Return", bg="red", font=("Times New Roman", 15), command=self.return_decider)
        self.ret_button.place(x=625,y=450)
        self.ret_button.configure(width=7, height = 1)

        #login user
        self.log_button = Button(self.root, text="Login", bg="green", font=("Times New Roman", 15), command=self.login)
        self.log_button.place(x=25,y=450)
        self.log_button.configure(width=7, height = 1)

        self.root.mainloop()
    
    def login(self):
        tmp_email = self.log_email_input.get()
        tmp_pword = self.log_pword_input.get()
        if datamgr.UserDetails.verify_login(tmp_email, tmp_pword):
            self.root.destroy()
            menu = MainMenu(tmp_email)
        else:
            mb.showerror("UNABLE TO LOGIN", "Incorrect email or password")
        

    def return_decider(self):
        self.root.destroy()
        regLogScreen = RegLog()

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
        self.root.destroy()
        reg_screen = Register()
    def login(self):
        self.root.destroy()
        log_screen = Login()


main = RegLog()
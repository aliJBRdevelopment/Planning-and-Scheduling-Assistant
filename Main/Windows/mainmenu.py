from tkinter import *
#class for registration screen
class Register():
    def __init__(self):
        #window setup
        self.root = Tk()
        self.root.title("PSA")
        self.root.geometry("750x500")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        
        #listbox for current tasks
        self.task_listbox = Listbox(self.root, width=70, height=15, bg="lightgray", font=("Times New Roman", 15))
        self.task_listbox.grid(row=0, column=0, padx=25, pady=50, columnspan=2, rowspan=1)

        #logout
        self.logout_button = Button(self.root, text="Logout", bg="red", fg="black", font=("Times New Roman", 15), command=self.return_decider)
        self.logout_button.place(x=625,y=450)
        self.logout_button.configure(width=7, height = 1)

        #add task
        self.add_task_button = Button(self.root, text="Add Task", bg="green", font=("Times New Roman", 15), command=self.return_decider)
        self.add_task_button.place(x=25,y=450)
        self.add_task_button.configure(width=7, height = 1)

        self.root.mainloop()
    
    def register(self):
        pass

    def return_decider(self):
        pass
    

test = Register()
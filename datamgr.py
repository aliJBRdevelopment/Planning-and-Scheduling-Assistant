import csv
import random
import hashlib
import re

class PasswordManager:
    def hash_password(pword):
        __enc_pword = hashlib.sha256(pword.encode()).hexdigest()
        return __enc_pword
    
    def compare_password(entered_pword, stored_pword):
        if PasswordManager.hash_password(entered_pword) == stored_pword:
            return True
        else:
            return False
    

class EmailManager:
    #check if input is valid email
    def is_valid_email(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            return False
    
    def unique_email(email):
        #check if email is already in csv file
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(email + " ::: " + row[1])
                if email.lower() in row:
                    return False
        return True
    
class UserDetails:
    def verify_login(email, password):
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if email.lower() in row:
                    if PasswordManager.compare_password(password, row[2]):
                        return True
                    else:
                        return False
        return False
    
    def register_user(email,name,password):
        if EmailManager.is_valid_email(email) & EmailManager.unique_email(email):
            pword = PasswordManager.hash_password(password)
            with open('data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, email.lower(), pword])
            return True
        else: 
            return False


class EventMgr:
    def save_task(title, date, participants, sub_tasks, completed_sub_tasks,id):
        with open('tasks.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(title, date, participants, sub_tasks, id)
        return True
    
    def get_task_byemail(email):
        tasks = []
        with open('tasks.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if email in row[2]:
                    tasks.append(row)
        return tasks
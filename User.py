import csv
class Tasks:
    def __init__(self):
        #title, date, participants, id
        self.current_tasks = self.load_tasks()

    def load_tasks(self):
        current_tasks = []
        with open('tasks.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                current_tasks.append(row)
        return current_tasks

    def save_task(task):
        with open('tasks.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([task[0], task[1], task[2], task[3]])
import os
import subprocess
import time
from datetime import datetime, timedelta
import json

class WinCron:
    def __init__(self, task_file='tasks.json'):
        self.task_file = task_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.task_file):
            with open(self.task_file, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.task_file, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, name, command, interval_minutes):
        task = {
            "name": name,
            "command": command,
            "interval": interval_minutes,
            "last_run": None
        }
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, name):
        self.tasks = [task for task in self.tasks if task['name'] != name]
        self.save_tasks()

    def run_pending_tasks(self):
        now = datetime.now()
        for task in self.tasks:
            last_run = datetime.strptime(task['last_run'], '%Y-%m-%d %H:%M:%S') if task['last_run'] else None
            if last_run is None or (now - last_run) >= timedelta(minutes=task['interval']):
                print(f"Running task: {task['name']}")
                subprocess.run(task['command'], shell=True)
                task['last_run'] = now.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()

    def start(self, check_interval_seconds=60):
        try:
            while True:
                self.run_pending_tasks()
                time.sleep(check_interval_seconds)
        except KeyboardInterrupt:
            print("Stopping WinCron")

if __name__ == "__main__":
    cron = WinCron()
    # Example: Add a new task
    # cron.add_task("notepad_task", "notepad.exe", 5)
    cron.start()
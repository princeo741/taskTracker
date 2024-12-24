from flask import Flask, request, render_template
import os
from datetime import datetime

app = Flask(__name__)

# Path to the shared tasks file
TASKS_FILE = "/mnt/shared_storage/tasks.txt"

# Ensure the tasks file exists
def ensure_file():
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            f.write("")

@app.route('/')
def home():
    # Read existing tasks
    ensure_file()
    with open(TASKS_FILE, 'r') as f:
        tasks = f.readlines()
    return render_template('index.html', tasks=[task.strip() for task in tasks])

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    if task.strip():
        # Append task to the file with a timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ensure_file()
        with open(TASKS_FILE, 'a') as f:
            f.write(f"[{timestamp}] {task}\n")
    return home()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

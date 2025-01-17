# WinCron

WinCron is a Python program that automates and schedules regular system tasks using cron-like scheduling on Windows. It allows you to define tasks with specific commands and intervals, and it will execute these tasks at the specified times.

## Features

- Schedule tasks with a specified interval in minutes.
- Automatically run tasks at the defined intervals.
- Manage tasks with add and remove functionalities.
- Simple JSON-based task storage.

## Requirements

- Python 3.x
- Windows operating system

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/wincron.git
   ```

2. Navigate to the project directory:
   ```bash
   cd wincron
   ```

3. Install required packages (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Add a new task:
   ```python
   cron = WinCron()
   cron.add_task("example_task", "echo 'Hello, World!'", 10)
   ```

2. Remove a task:
   ```python
   cron.remove_task("example_task")
   ```

3. Start the scheduler:
   ```python
   cron.start()
   ```

## Example

To create a task that opens Notepad every 5 minutes, you can use the following code:

```python
cron = WinCron()
cron.add_task("notepad_task", "notepad.exe", 5)
cron.start()
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any feature requests or bugs.

## License

This project is licensed under the MIT License.
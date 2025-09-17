# Python Command-Line Todo App

A simple yet powerful command-line todo application written in Python that helps you manage your tasks efficiently. The app uses JSON for persistent storage and provides an interactive interface for task management.

## Features

- Create new tasks with names and descriptions
- View all current tasks and their status
- Mark tasks as completed
- Delete existing tasks
- Case-insensitive task management
- Persistent storage using JSON
- User-friendly command interface

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone this repository:
```bash
git clone https://github.com/AFG473319/python-todo-app.git
cd python-todo-app
```

### Usage

Run the application:
```bash
python to_do.py
```

### Available Commands

The app provides the following commands:
1. Create a new task (Command: 1)
2. Delete a task (Command: 2)
3. View current tasks (Command: 3)
4. Get help (Command: 4)
5. Mark a task as done (Command: 5)
6. Exit the app (Command: 6)

## How It Works

### Task Creation
- Enter command '1' to create a new task
- Provide a unique task name
- Add an optional description (enter '0' for no description)
- Tasks are automatically saved with a 'not done' status

### Task Management
- View all tasks with their descriptions and completion status
- Mark tasks as complete using command '5'
- Delete unwanted tasks using command '2'
- All changes are automatically saved to `tasks.json`

## Project Structure

- `to_do.py` - Main application file containing all functionality
- `test_to_do.py` - Test suite for the application

## Testing

The application includes a test suite that verifies core functionality:
- JSON read/write operations
- Task creation
- Task completion marking

Run the tests using:
```bash
pytest -v
```

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.

## License

This project is open source and available for anyone to use and modify.
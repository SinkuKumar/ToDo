# Todo App

This is a simple Todo application built using Flask, Bootstrap, Jinja, SQLite, and SQLAlchemy.

## Demo
You can try out the application by visiting the following link: [Todo App Demo](https://todo.sinkukumar.repl.co)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/SinkuKumar/ToDo.git
   ```

2. Change to the project directory:

   ```
   cd ToDo
   ```

3. Create a virtual environment (optional but recommended):

   ```
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask development server:

   ```
   flask run
   ```

2. Open your web browser and visit `http://localhost:5000` to access the Todo app.

## Features

- Add new tasks: Enter a task in the input field and press Enter or click the "Add" button.
- Mark tasks as completed: Click on a task to toggle its completion status.
- Delete tasks: Click on the trash bin icon to remove a task from the list.

## Database

The application uses a SQLite database named `todos.db` to store the tasks. The `Todo` table in the database has the following columns:

- `id`: Integer (primary key)
- `task`: String (200 characters, non-null)
- `completed`: Boolean (default: False)
- `timestamp`: String (20 characters, default: current date and time)

## Code Overview

- The `app` object is created using Flask and the `SQLALCHEMY_DATABASE_URI` configuration is set to use the SQLite database `todos.db`.
- The `Todo` class represents a Todo item and defines the structure of the `Todo` table in the database.
- The `index` route handles both GET and POST requests. For GET requests, it retrieves all the todos from the database and renders the `index.html` template with the todos. For POST requests, it adds a new todo to the database and redirects to the index page.
- The `delete` route handles the deletion of a todo item. It retrieves the todo with the given `id` from the database and deletes it. Then, it redirects to the index page.
- The `update` route handles updating the completion status of a todo item. It retrieves the todo with the given `id` from the database, toggles its `completed` attribute, and saves the changes. Then, it redirects to the index page.

## Templates

The application uses the following templates located in the `templates` directory:

- `index.html`: Displays the list of todos. It includes a form to add new todos and shows the existing todos with options to mark them as completed or delete them.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/SinkuKumar/ToDo/blob/master/LICENSE) file for more information.
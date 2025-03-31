HW3-Python-Flask
 Flask Recipe Web Application

This web application was developed as a project for CMPE 131: Software Engineering I at San José State University. The app allows users to register, log in, and manage their own food recipes through a clean and functional interface. It was built using Flask and several of its extensions to handle routing, forms, authentication, and database integration.

Project Overview
This application provides the following functionality:

- Display all submitted recipes on the homepage
- Allow authenticated users to add new recipes
- View individual recipe details
- Delete recipes (only by the user who submitted them)
- User registration, login, and logout functionality
- Flash messages for feedback (successful actions, errors, etc.)

Implemented Routes

- `/` – Homepage that lists all recipes in an unordered list
- `/recipe/new` – Submit a new recipe (login required)
- `/recipe/<id>` – View full details of a specific recipe
- `/recipe/<id>/delete` – Delete a recipe (only the author)
- `/register`, `/login`, `/logout` – User authentication routes
Technologies Used

- Flask (Python web framework)
- Flask-SQLAlchemy (ORM for database interactions)
- Flask-WTF (Form handling and validation)
- Flask-Login (User session management)
- SQLite (Local development database)

 Database Models

User
- `id`: Primary key
- `username`: Unique string
- `password`: Hashed password
- `recipes`: One-to-many relationship to Recipe

Recipe
- `id`: Primary key
- `title`: String (max length 80)
- `description`: Text
- `ingredients`: Text
- `instructions`: Text
- `created`: Datetime (auto-generated)
- `user_id`: Foreign key to User
 Forms

The application includes the following forms:

- `RecipeForm`: For creating new recipes
- `LoginForm`: For logging in
- `RegisterForm`: For creating a new user account
How to Run the App

1. Clone the repository:

   ```bash
   git clone https://github.com/Seaphant/HW3-Python-Flask.git
   cd HW3-Python-Flask
2. Set up VE
   python3 -m venv venv
source venv/bin/activate
3. Initialize the database

flask shell
>>> from app import db
>>> db.create_all()
>>> exit()

4. Start the Flask server:
   python run.py



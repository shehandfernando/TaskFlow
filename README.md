# TaskFlow Manager 🚀

A modular, professional Task Management web application built with **Flask** and **SQLAlchemy**. This project demonstrates clean MVC (Model-View-Controller) architecture, database persistence, and a modern responsive UI with Dark Mode support.

## ✨ Features
* **Task Management:** Create, toggle completion, and delete tasks seamlessly.
* **Priority System:** Assign **High, Medium, or Low** priority levels with color-coded badges.
* **Dynamic Filtering:** View tasks based on status: *All, Active,* or *Completed*.
* **Responsive UI:** Built with Bootstrap 5 for a clean look on mobile and desktop.
* **Dark Mode:** Built-in toggle for late-night productivity.
* **Modular Architecture:** Structured using the Flask Factory pattern for scalability and better code organization.

## 🛠️ Tech Stack
* **Backend:** Python 3.x, Flask.
* **Database:** SQLite (managed via SQLAlchemy ORM).
* **Frontend:** HTML5, Jinja2, Bootstrap 5, JavaScript.

## 🚀 Getting Started

### 1. Clone the repository
    git clone https://github.com/shehandfernando/TaskFlow.git
    cd TaskFlow

### 2. Install dependencies
Ensure you have Python installed, then run:
    pip install flask-sqlalchemy

### 3. Run the application
    python run.py

Open your browser and navigate to http://127.0.0.1:5000.

## 📁 Project Structure
    taskflow/
    ├── app/                # Core application logic
    │   ├── __init__.py     # App factory & Database initialization
    │   ├── models.py       # Database schemas (SQLAlchemy Models)
    │   └── routes.py       # URL routing & Controller logic
    ├── templates/          # Jinja2 UI templates (HTML)
    ├── config.py           # Application configurations & Secret Keys
    └── run.py              # Entry point to start the Flask server

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).

---
*Developed by [Shehan Fernando](https://github.com/shehandfernando)*

🏛️ Django Library Management System

A Library Management System built with Django that allows users to manage books, authors, and borrowers efficiently.
This system helps libraries track available books, manage user borrowing records, and organize catalog data digitally.

📚 Features

🧑‍💼 Admin Dashboard — Manage books, members, and borrowing records

📖 Book Management — Add, update, delete, and search for books

👥 Member Management — Register and manage users

🔄 Borrow & Return System — Track book loans and returns

🔒 Authentication System — Login, logout, and user permissions

🐳 Docker Support — Easy setup using Docker

⚙️ Technologies Used

Backend: Django (Python)

Database: SQLite (default, easily swappable for PostgreSQL/MySQL)

Frontend: HTML, CSS (Django Templates)

Containerization: Docker

Other: Django ORM, Django Admin, Bootstrap (if used)

🚀 Getting Started
1️⃣ Prerequisites

Make sure you have the following installed:

Python 3.10+

pip

Docker
 (optional for containerized setup)

2️⃣ Installation (Local)
# Clone the repository
git clone https://github.com/<your-username>/Django-Library-Management-System.git
cd Django-Library-Management-System/LMS

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r ../requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver


Access the app at http://127.0.0.1:8000/
 🎉

3️⃣ Run with Docker
# Build Docker image
docker build -t django-library .

# Run container
docker run -p 8000:8000 django-library

🧩 Project Structure
Django-Library-Management-System/
│
├── Dockerfile
├── requirements.txt
├── LMS/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── LMS/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── < app folders>/
│   └── templates/
│
└── README.md

🧪 Usage

Login to the admin panel: /admin/

Add or manage books and users.

Borrow or return books via the user interface.

🤝 Contributing

Contributions are welcome!
Feel free to fork this repository, create a new branch, and submit a pull request.

📜 License

This project is licensed under the MIT License — see the LICENSE file for details.

👤 Author

Yazid Riadh Chelmouni
🌍 Fullstack Developer — Django & React
📧 chelmouni.yazidriadh@gmail.com

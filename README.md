\# User Management System (Django CRUD)



\## Description

This is a User Management System built using Django that performs full CRUD (Create, Read, Update, Delete) operations. The application allows managing user records through a clean and responsive web interface built with HTML, CSS, Bootstrap, and JavaScript.



\## Tech Stack

\- Backend: Python, Django

\- Frontend: HTML, CSS, Bootstrap, JavaScript

\- Database: SQLite (Development)

\- Version Control: Git, GitHub



\## Features

\- Create new users

\- View user list

\- Update user details

\- Delete users

\- Responsive UI using Bootstrap

\- Server-side rendering using Django templates



\## Project Structure

project-root/

│

├── README.md

├── venv/ # Virtual environment (ignored)

│

├── management\_system/

│ ├── manage.py

│ ├── db.sqlite3

│ │

│ ├── management\_system/

│ │ ├── settings.py

│ │ ├── urls.py

│ │ ├── wsgi.py

│ │

│ ├── app/ # Django app (users / management)

│ │ ├── models.py

│ │ ├── views.py

│ │ ├── urls.py

│ │

│ ├── templates/

│ ├── static/

Create and activate virtual environment



python -m venv venv

venv\\Scripts\\activate



Install dependencies



pip install -r requirements.txt





Run the server



python manage.py runserver



Open your browser and visit:



http://127.0.0.1:8000/



Learning Outcomes



Implemented CRUD operations using Django



Gained understanding of Django MVT architecture



Integrated frontend with Django templates



Used Bootstrap for responsive UI design



Practiced Git and GitHub version control



Author



Shubhada Wani



License



This project is for learning and educational purposes.


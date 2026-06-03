# Freelancing Web Application

A full-stack Freelancing Web Application built using **Django**, designed to connect clients and freelancers on a single platform. The system allows clients to post projects, freelancers to submit proposals, manage contracts, communicate, and track project progress efficiently.

---

## 🚀 Features

### 👤 User Management

* User Registration & Login
* Role-based Authentication (Client / Freelancer)
* Profile Management
* Secure Password Reset

### 📂 Project Management

* Create, Edit, and Delete Projects
* Browse Available Projects
* Project Categories and Skills
* Project Search & Filtering

### 💼 Proposal System

* Submit Project Proposals
* View Proposal Status
* Accept or Reject Proposals
* Contract Creation

### 💬 Communication

* Real-time Messaging
* Notifications
* Project Discussions

### ⭐ Reviews & Ratings

* Freelancer Ratings
* Client Feedback
* Review Management

### 💳 Payment Management

* Payment Tracking
* Transaction History
* Project Budget Management

### 📊 Dashboard

* Client Dashboard
* Freelancer Dashboard
* Project Statistics
* Activity Monitoring

---

## 🛠️ Tech Stack

### Backend

* Django
* Django REST Framework
* SQLite / PostgreSQL

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Other Tools

* Git & GitHub
* Postman
* VS Code

---

## 📁 Project Structure

```bash
freelancing-app/
│
├── accounts/
├── projects/
├── proposals/
├── messaging/
├── payments/
├── reviews/
├── static/
├── templates/
├── media/
├── freelancing_app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/freelancing-web-app.git
cd freelancing-web-app
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key
DEBUG=True

DATABASE_NAME=freelancing_db
DATABASE_USER=postgres
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```


## API Endpoints

| Endpoint         | Method | Description       |
| ---------------- | ------ | ----------------- |
| /register        | POST   | User Registration |
| /login           | POST   | User Login        |
| /projects        | GET    | View Projects     |
| /projects/create | POST   | Create Project    |
| /proposals       | GET    | View Proposals    |
| /messages        | GET    | View Messages     |

---

## Future Enhancements

* AI-based Freelancer Recommendation
* Video Interview Integration
* Real-time Chat using WebSockets
* Online Payment Gateway Integration
* Project Analytics Dashboard
* Mobile Application Support

---

## Testing

Run tests using:

```bash
python manage.py test
```

---

## Contributing

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Author

**Siddhesh More**

Final Year Diploma Computer Engineering Student

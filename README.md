# Expense Tracker REST API

A secure Expense Tracker REST API built using Flask, SQLAlchemy, SQLite, and JWT Authentication.  
This project supports user authentication and complete CRUD operations for expense management.



#  Features

- User Registration
- User Login with JWT Authentication
- Password Hashing using Flask-Bcrypt
- Protected Routes using JWT
- Create Expense
- Get All Expenses
- Get Single Expense
- Update Expense
- Delete Expense
- Category-Based Expense Filtering
- Monthly Expense Summary
- RESTful API Architecture
- Blueprint-Based Project Structure



#  Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flask-Bcrypt
- SQLite
- Postman

---

#  Project Structure

expense_tracker_api/
│
├── app/
│   ├── auth/
│   │   └── routes.py
│   │
│   ├── expenses/
│   │   └── routes.py
│   │
│   ├── __init__.py
│   ├── extensions.py
│   └── models.py
│
├── config.py
├── run.py
├── requirements.txt
└── README.md





#  Authentication
This project uses JWT Authentication.

After login, copy the token and add it to request headers:

```bash
Authorization: Bearer YOUR_TOKEN
```

---

#  API Endpoints

## Auth Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /register | Register User |
| POST | /login | Login User |

---

## Expense Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /expenses | Create Expense |
| GET | /expenses | Get All Expenses |
| GET | /expenses/<id> | Get Single Expense |
| PUT | /expenses/<id> | Update Expense |
| DELETE | /expenses/<id> | Delete Expense |
| GET | /expenses/category/<category> | Filter By Category |
| GET | /expenses/monthly-summary | Monthly Expense Summary |

---

#  Sample Request

## Register User

```json
{
    "username": "vitthal",
    "password": "1234"
}
```

---

#  Sample Expense Request

```json
{
    "title": "Pizza",
    "amount": 500,
    "category": "Food"
}
```

---

#  Concepts Used

- REST APIs
- JWT Authentication
- CRUD Operations
- SQLAlchemy ORM
- Flask Blueprints
- Application Factory Pattern
- Password Hashing
- Database Relationships
- Authentication & Authorization

---

#  Future Improvements

- Pagination
- Search & Sorting
- Docker Support
- PostgreSQL Integration
- Swagger Documentation
- Refresh Tokens
- Rate Limiting
- Unit Testing

---

#  Author

Vitthal Ganesh
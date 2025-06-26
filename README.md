
# GraphQL CRUD API with Flask, Ariadne, and PostgreSQL

This project is a simple **GraphQL API** built with **Flask**, **Ariadne**, and **PostgreSQL**, designed to perform full CRUD operations on an Employee database.

---

## 🚀 Features

- GraphQL API with Ariadne
- PostgreSQL integration via SQLAlchemy
- Full CRUD operations on `Employee` model
- Flask-based server for easy deployment
- Simple and lightweight project structure

---

## 📦 Technologies Used

- Python 3.10+
- Flask
- Ariadne (for GraphQL)
- SQLAlchemy
- PostgreSQL
- psycopg2

---

## ⚙️ Installation & Running

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/EmekaIwuagwu/1971assignment.git
```

### 2. Navigate into the Project Directory

```bash
cd 1971assignment
```

### 3. Install Required Python Packages

Make sure you have a Python virtual environment active, then run:

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL

Create a PostgreSQL database and update the connection URI in your `.env` or directly in your `database.py` or `app.py` (depending on where DB config is located).

Example URI:
```bash
postgresql://username:password@localhost:5432/employees_db
```

### 5. Run the Application

```bash
python app.py
```

Your API will be live at: [http://localhost:5000/graphql](http://localhost:5000/graphql)

---

## 📬 GraphQL Playground

Once the server is running, navigate to:

```
http://localhost:5000/graphql
```

There, you can interact with your API using the GraphQL Playground UI.

---

## 📘 Sample GraphQL Queries

### ✅ Create an Employee
```graphql
        mutation {
        createUser(input: {
            fullname: "John Doe"
            dateofbirth: "1990-01-01"
            gender: "Male"
            email: "john@example.com"
            address: "123 Main St"
            city: "New York"
            zip: "10001"
            telephone: "1234567890"
            occupation: "Engineer"
        }) {
            id
            fullname
            email
        }
        }

```

### 🔄 Update an Employee
```graphql
        mutation {
        updateUser(id: 1, input: {
            fullname: "John Smith"
            email: "johnsmith@example.com"
            occupation: "Senior Engineer"
        }) {
            id
            fullname
            email
            occupation
        }
    }

```

### ❌ Delete an Employee
```graphql
        mutation {
        deleteUser(id: 1)
    }

```

### 📄 Fetch All Employees
```graphql
        query {
        getUsers {
            id
            fullname
            email
        }
    }

```

---

## 🧾 License

This project is licensed under the MIT License.

---

## 👤 Author

**Emeka Iwuagwu**  
GitHub: [@EmekaIwuagwu](https://github.com/EmekaIwuagwu)

---

## 💬 Contributions

Feel free to fork this repo and open a pull request. Issues and suggestions are welcome!

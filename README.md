
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
        createPerson(input: {
            fullname: "Jane Doe"
            dateofbirth: "1990-01-01"
            gender: "Female"
            email: "jane@example.com"
            address: "123 Street"
            city: "Lagos"
            zip: "100001"
            telephone: "08012345678"
            occupation: "Engineer"
        }) {
            message
            data {
            id
            fullname
            }
        }
    }


```

### 🔄 Update an Employee
```graphql
        mutation {
        updatePerson(id: 1, input: {
            fullname: "John Doe Jr"
            city: "Kampala"
        }) {
            message
            data {
            id
            fullname
            city
            }
        }
    }

```

### ❌ Delete an Employee
```graphql
        mutation {
        deletePerson(id: 1) {
            message
            success
        }
    }
```

### 📄 Fetch All Employees
```graphql
            query {
            persons {
                message
                data {
                id
                fullname
                email
                }
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


# 🎓 FastAPI Student Management API

A simple **Student Management REST API** built using **FastAPI** to demonstrate:
- Path parameters
- Query parameters
- CRUD operations (GET, POST, PUT, PATCH, DELETE)
- Pydantic models for request validation

---

## 🚀 Features

- Create a student
- Get student by ID
- Get student by name
- Get all students
- Combine Path & Query parameters
- Full update (PUT)
- Partial update (PATCH)
- Delete a student

---

## 🛠 Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## 📦 Installation

```bash
pip install fastapi uvicorn
````

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

* API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📚 API Endpoints

### Home

```
GET /
```

---

### Get Student by ID

```
GET /get-student/{student_id}
```

---

### Get Student by Name

```
GET /get-by-name?name=James
```

---

### Get All Students

```
GET /get-all
```

---

### Get Student by ID and Name (Both Required)

```
GET /get-by-combine/{student_id}?name=James
```

---

### Get Student by ID or Name (Any One Enough)

```
GET /get-by-any/{student_id}?name=James
```

---

### Create Student

```
POST /create-student/{student_id}
```

**Body**

```json
{
  "Name": "Alex",
  "Age": 23,
  "Education": "BSc"
}
```

---

### Update Student (PUT – Full Update)

```
PUT /put-update-student/{student_id}
```

---

### Update Student (PATCH – Partial Update)

```
PATCH /update-student/{student_id}
```

**Body (Optional fields)**

```json
{
  "Age": 25
}
```

---

### Delete Student

```
DELETE /delete-student?student_id=1
```

---

## 🧱 Student Model

```json
{
  "Name": "string",
  "Age": "integer",
  "Education": "string"
}
```

---

## ⚠️ Notes

* Uses in-memory storage (data resets on restart)
* For learning and practice purposes
* No database connected

---

## 👨‍💻 Author

**Mohamed Jamaludeen J**
Learning FastAPI & Backend Development

```

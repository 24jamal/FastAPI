from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):

    Name : str
    Age : int
    Education : str

class UpdateStudent(BaseModel):
    Name : Optional[str] = None
    Age : Optional[int] = None
    Education : Optional[str] = None

students = {
    1 : {
        "Name" : "James",
        "Age" : "22",
        "Education" : "BCA"
    },
    2 : {
        "Name" : "Fredrick",
        "Age" : "25",
        "Education" : "BE"
    }
}

@app.get("/")
def index():
    return {"name" : "Jamal"}

# Get Data by Path Parameter (http://127.0.0.1:8000/get-student/1)
@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(..., description = "The ID of the student you want to view",gt =0)):
    return students[student_id]

# Get Data by Query Parameter (http://127.0.0.1:8000/get-by-name?name=James)
@app.get("/get-by-name")
def get_student_name(*,name : Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["Name"] == name:
            return students[student_id]
        return {"Data" : "Not found"}

#Get all dict data
@app.get("/get-all")
def get_all():

    return students;    

# Get Data by Combining (needs both) Path and Query Parameter (http://127.0.0.1:8000/get-by-name?name=James/1)
@app.get("/get-by-combine/{student_id}")
def get_student_name(*,student_id : int,name : Optional[str] = None):
    
    student = students.get(student_id)

    if not student:
        return {"Data" :"Student Id not found"}
    
    if student["Name"] != name:

        return {"Data" : "Name not match with Given Id"}
    
    else:

        return {"Data" : student}
    
# Get Data by Combining (needs one enough) Path and Query Parameter (http://127.0.0.1:8000/get-by-any/99?name=James)
@app.get("/get-by-any/{student_id}")
def get_by_any(*,student_id : Optional[int] =None,name : Optional[str] = None):

    if student_id in students:
        return students[student_id]
    
    if name:
        for student_id in students:
            if students[student_id]["Name"] == name:
                return students[student_id]
    return {"data" : "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error" : "Already this student id exists!!"}
    
    students[student_id] = student

    return students[student_id]

@app.put("/put-update-student/{student_id}")
def update_student(student_id : int, student : Student):

    if student_id not in students:
        return students[student_id]
    
    students[student_id] = student

    return students[student_id]

@app.patch("/update-student/{student_id}")
def update_student(student_id : int, student : UpdateStudent):

    if student_id not in students:

        return {"data" : "not found"}
    
    stored_student = students[student_id]

    if student.Name != None:

        stored_student["Name"] = student.Name
    
    if student.Age != None:

        stored_student["Age"] = student.Age

    
    if student.Education != None:

        stored_student["Education"] = student.Education

    students[student_id] = stored_student

    return {"Result" : "Success","Data" : students[student_id]}


@app.delete("/delete-student")
def delete_student(student_id : int):

    if student_id not in students:
        return {"Data" : "Not found"}
    
    del students[student_id]

    return {"result" : "Deleted successfully"}
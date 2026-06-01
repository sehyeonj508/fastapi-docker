from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

FILE_NAME = "courses.json"


class Course(BaseModel):
    course_name: str
    year: int
    semester: int
    grade: str


if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)


@app.get("/courses")
def get_courses():
    with open(FILE_NAME, "r") as f:
        courses = json.load(f)
    return courses


@app.post("/courses")
def add_course(course: Course):
    with open(FILE_NAME, "r") as f:
        courses = json.load(f)

    courses.append(course.dict())

    with open(FILE_NAME, "w") as f:
        json.dump(courses, f, indent=4)

    return {"message": "Course added successfully"}

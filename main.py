from fastapi import FastAPI
from pydantic import BaseModel
import json
import uvicorn

app = FastAPI()

FILE_NAME = "courses.json"


class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str


def load_courses():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_courses(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.get("/courses")
def get_courses():
    return load_courses()


@app.post("/courses")
def add_course(course: Course):
    data = load_courses()
    new_course = course.dict()
    data.append(new_course)
    save_courses(data)

    return {
        "message": "Course added successfully",
        "course": new_course
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
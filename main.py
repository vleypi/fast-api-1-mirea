from fastapi import FastAPI
from fastapi.responses import FileResponse

from models import CalcInput, Feedback, FeedbackBasic, User, UserAge, UserAgeResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

@app.get("/html")
def get_html():
    return FileResponse("index.html")


@app.post("/calculate")
def calculate(data: CalcInput):
    return {"result": data.num1 + data.num2}


current_user = User(name="Иван Иванов", id=1)

@app.get("/users")
def get_users():
    return current_user


@app.post("/user", response_model=UserAgeResponse)
def create_user(user: UserAge):
    return UserAgeResponse(
        name=user.name,
        age=user.age,
        is_adult=user.age >= 18,
    )


feedbacks_basic: list[FeedbackBasic] = []


@app.post("/feedback/basic")
def submit_feedback_basic(feedback: FeedbackBasic):
    feedbacks_basic.append(feedback)
    return {"message": f"Отзыв получен. Спасибо, {feedback.name}."}


feedbacks: list[Feedback] = []


@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}

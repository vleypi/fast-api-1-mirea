import re
from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    name: str
    id: int

class UserAge(BaseModel):
    name: str
    age: int


class UserAgeResponse(BaseModel):
    name: str
    age: int
    is_adult: bool

class CalcInput(BaseModel):
    num1: float
    num2: float

class FeedbackBasic(BaseModel):
    name: str
    message: str

BANNED_WORDS = [r"кринж\w*", r"рофл\w*", r"вайб\w*"]


class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator("message")
    @classmethod
    def check_banned_words(cls, v: str) -> str:
        text_lower = v.lower()
        for pattern in BANNED_WORDS:
            if re.search(pattern, text_lower):
                raise ValueError("Использование недопустимых слов")
        return v

from pydantic import BaseModel, computed_field, model_validator, field_validator
from datetime import date
from dateutil.relativedelta import relativedelta

class User(BaseModel):
    id: int
    name: str
    surname: str
    birthday_date: date

    @field_validator('name', mode='before')
    def validate_name(cls, v):
        if isinstance(v, int):
            return str(v)
        elif isinstance(v, str):
            return v
        else:
            raise ValueError("Имя должно быть строкой или числом")
    
    @field_validator('surname', mode='before')
    def validate_name(cls, v):
        if isinstance(v, int):
            return str(v)
        elif isinstance(v, str):
            return v
        else:
            raise ValueError("Имя должно быть строкой или числом")

    @computed_field
    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    @computed_field
    def age(self) -> str:
        today = date.today()
        delta = relativedelta(today, self.birthday_date)
        return f"{delta.years} лет, {delta.months} месяцев и {delta.days} дней"

    @model_validator(mode='after')
    def check_age(self):
        today = date.today()
        age = today.year - self.birthday_date.year - (
            (today.month, today.day) < (self.birthday_date.month, self.birthday_date.day))

        if age < 18:
            raise ValueError("Пользователь должен быть старше 18 лет")
        if age > 120:
            raise ValueError("Возраст не может превышать 120 лет")
        return self

    @model_validator(mode='after')
    def set_default_name(self):
        if self.name.strip() == '':
            self.name = f"User_{self.id}"
        return self

alex = User(id=1, name="Алексей", surname="Яковенко", birthday_date="1993-02-19")

to_json = alex.model_dump_json()

print(to_json, type(to_json))
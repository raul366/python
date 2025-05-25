from pydantic import BaseModel, Field, ConfigDict
from typing_extensions import Annotated

class User(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    id: int = Field(default=1, description="Уникальный идентификатор пользователя")
    name: str = Field(default="John Doe", title="Имя пользователя", description="Полное имя")
    role: str = Field(default="user", alias="user_role", description="Роль пользователя в системе")

class User2(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    id: Annotated[int, Field(gt=0)]
    name: Annotated[str, Field(min_length=2, max_length=50)]
    email: Annotated[str, Field(pattern=r"[^@]+@[^@]+\.[^@]+")]
    role: Annotated[str, Field(default="user")]

class ParentModel(BaseModel):
    name: str
    age: int

class ChildModel(ParentModel):
    school: str

parent = ParentModel(name="Alex", age=40)
child = ChildModel(name="Bob", age=12, school="Greenwood High")
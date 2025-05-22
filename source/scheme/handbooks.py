import uuid

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }
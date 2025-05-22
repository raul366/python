import uuid

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }
from sqlalchemy import Column, Integer, String, create_engine #, select
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel, ConfigDict

# Шаг 1: Описание модели SQLAlchemy
Base = declarative_base()

class UserORM(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Шаг 2: Создание Pydantic-модели
class UserPydantic(BaseModel):
    id: int
    name: str
    email: str
    
    model_config = ConfigDict(from_attributes=True)

# Настройка базы данных и сессии
engine = create_engine("sqlite:///source/Pydantic/Pydantic.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Шаг 3: Запрос данных
def get_user(user_id: int):
    with Session() as session:
        user = session.select(UserORM).filter_by(id = user_id).scalar_one_or_none() #session.scalar(select(UserORM).filter_by(id=user_id))
        
        # Шаг 4: Преобразование объекта SQLAlchemy в Pydantic
        if user:
            user_pydantic = UserPydantic.model_validate(user)
            
            # Шаг 5: Получение данных в нужном формате
            return user_pydantic.model_dump()
        return None

# Пример использования
user_data = get_user(1)
print(user_data)
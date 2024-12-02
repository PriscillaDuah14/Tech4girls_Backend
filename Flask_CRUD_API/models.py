from config import session
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String

Base = declarative_base()

class Backend(Base):
    __tablename__ = 'backend_class'
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50),nullable=False)
    last_name = Column(String(50),nullable=False)
    age = Column(Integer,nullable=False)
    email = Column(String(255),nullable=False,unique=True)


    def __str__(self):
     return f"student's ID : {self.student_id}, Name: {self.first_name} ,{self.last_name} "
   

class Laptops(Base):
    __tablename__ = 'laptops'
    laptop_name = Column(String(50),nullable=False,unique=True)
    laptop_number = Column(Integer)
    student_id = Column(Integer,primary_key=True)

    def __str__(self):
     return f"student's ID : {self.student_id}, Name: {self.laptop_name} ,Number: {self.laptop_number}"
    
if __name__ == "__main__":
    try:
        Base.metadata.create_all(session.bind)
        print('Tables created')
    except Exception as e:
        print(f'An error occured: {e}')
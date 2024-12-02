from config import session
from models import Laptops

class Laptop_Crud:
    def __init__(self,session):
        self.session = session

    def insert_laptops(self,laptop_name,laptop_number):
        new_laptops = Laptops(laptop_name=laptop_name,laptop_number=laptop_number)
        session.add(new_laptops)
        session.commit()
        return f'New laptop with these details {new_laptops} was added'
    
    def get_all_laptops(self):
        return self.session.query(Laptops).all()
    
    def get_laptop_by_first(self,laptop_name):
        return self.session.query(Laptops).filter_by(laptop_name=laptop_name).first()

    def get_laptop_by_Id(self,student_id):
        return self.session.query(Laptops).filter_by(student_id=student_id).first()
    
    def update_laptop(self,student_id,laptop_name=None,laptop_number=None):
        selected_laptops =self.session.query(Laptops).filter_by(student_id=student_id).first()
        if selected_laptops:
            if laptop_name:
                selected_laptops.laptop_name = laptop_name
            if laptop_number:
                selected_laptops.laptop_number = laptop_number
            
            self.session.commit()
        return selected_laptops
    
    def delete_laptop(self,student_id):
        selected_laptop = self.session.query(Laptops).filter_by(student_id=student_id).first()
        if selected_laptop:
            self.session.delete(selected_laptop)
            self.session.commit()
            return f'laptop with student id {student_id} has been deleted'




laptop_crud = Laptop_Crud(session) 
#new_laptop = laptop_crud.insert_laptops("muimui",107)
#print(new_laptop)
all_laptops = laptop_crud.get_all_laptops()
for laptop in all_laptops:
    print(laptop) 
#select_laptop = laptop_crud.get_laptop_by_Id(1)
#print(select_laptop)

#updated_laptop = laptop_crud.update_laptop(5,laptop_name='Lenova')
#print(updated_laptop)

#selected_laptop = laptop_crud.delete_laptop(8)
#print(selected_laptop)

    
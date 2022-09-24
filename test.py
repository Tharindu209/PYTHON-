class student():
    def __init__(self,name,house):
        if house != "bar" :
            raise ValueError("missing value")
        self.name = name
        self.house = house
    def __str__(self):
        return f"finish"    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    print(student)
    del student
   
    
def get_student():
    return student("foo","bar")
    
main()
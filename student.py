student={}

def add(roll_no,name,dept):
    student[roll_no]={'name':name,'dept':dept}
    student.count+=1 
    print(f"student{name} added to database")

def display(roll_no):
    if student[roll_no]:
        print(f"{student[roll_no]}.get()")
    else:
        print("Wrong roll no or student not found.")

    return True

def check(roll_no):
    if student[roll_no].get("name"):
        print(f"{student.items(roll_no)}")
    else:
        print("No such student exists in database.")
    return True 

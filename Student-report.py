student_report={}
student_report={
       "Name":input("Enter a Name :"),
       "Age":input("Enter a Age :"),
    "Marks":{
     "Math":input("Enter a Math marks:"),
     "Computer":input("Enter a Computer marks:"),
     "Physics":input("Enter a Physics marks:"),
     "English":input("Enter a Engish marks:")
    

    }
}
print("Computer :",student_report["Marks"]["Computer"])
print(len(student_report))
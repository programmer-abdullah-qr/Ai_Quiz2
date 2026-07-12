#input
Name = input("Enter a Name :")
Father_name= input("Enter a father name :")
Rollnumber = int(input("Enter a Roll number :"))
Age =int( input("Enter a Age :"))
City = input("Enter a City :")
Subject_marks=[]
Subject_marks.append(int(input("Enter a 1st subject Marks :")))
Subject_marks.append(int(input("Enter a 2nd subject Marks :")))
Subject_marks.append(int(input("Enter a 3rd subject Marks :")))
Subject_marks.append(int(input("Enter a 4rt subject Marks :")))
Subject_marks.append(int(input("Enter a 5th subject Marks :")))

#Output
print ("===== Student Report =====")
print("Student name :",Name)
print("Father name :",Father_name)
print("Roll number:",Rollnumber)
print("Age :",Age)
print("City :",City)
#Marks Program
Total_marks = Subject_marks[0]+Subject_marks[1]+Subject_marks[2]+Subject_marks[3]+Subject_marks[4]
print ("Total mark is :", Total_marks)
Averge = Total_marks/2
print("Averge :",Averge)
#higest Division
Highest=max(Subject_marks)
print ("Highest marks:",Highest)
#Lowest Division
Lowest=min(Subject_marks)
print ("Lowest marks:",Lowest)
#percentage 
Percentage = (Total_marks/500)*100
print ("Total Percentage is :",Percentage)
#Grading
if(Percentage>=90 and Percentage<=100):
    print("Student Grade is :A+")
elif(Percentage>=80 and Percentage<=90):
    print("Student Grade is :A")
elif(Percentage>=70 and Percentage<=80):
    print("Student Grade is :B")
elif(Percentage>=60 and Percentage<=70):
    print("Student Grade is :C")
elif(Percentage>=50 and Percentage<=60):
    print("Student Grade is :D")
else:
   print("Student Grade is :F")

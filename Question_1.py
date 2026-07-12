Name = input("Enter a Name :")
Age =int( input("Enter a Age :"))
City = input("Enter a City :")
Subject_marks=[]
Subject_marks.append(int(input("Enter a 1st subject Marks :")))
Subject_marks.append(int(input("Enter a 2nd subject Marks :")))
Subject_marks.append(int(input("Enter a 3rd subject Marks :")))
Subject_marks.append(int(input("Enter a 4rt subject Marks :")))
Subject_marks.append(int(input("Enter a 5th subject Marks :")))
print("Student name :",Name)
print("Age :",Age)
print("City :",City)
#Marks Program
Total_marks = Subject_marks[0]+Subject_marks[1]+Subject_marks[2]+Subject_marks[3]+Subject_marks[4]
print ("Total mark is :", Total_marks)
Averge = Total_marks/2
print("Averge :",Averge)
#higest Division
if(Subject_marks[0]>=Subject_marks[1]and Subject_marks[0]>=Subject_marks[2]and Subject_marks[0]>=Subject_marks[3]and Subject_marks[0]>=Subject_marks[4]):
    print("Highest marks in 1st subject :",Subject_marks[0])
elif( Subject_marks[1]>=Subject_marks[2]and Subject_marks[1]>=Subject_marks[3]and Subject_marks[1]>=Subject_marks[4]):
    print("Highest marks in 2nd subject :",Subject_marks[1])
elif(Subject_marks[2]>=Subject_marks[3]and Subject_marks[2]>=Subject_marks[4]):
    print("Highest marks in 3rd subject :",Subject_marks[2])
elif( Subject_marks[3]>=Subject_marks[4]):
    print("Highest marks in 4rt subject :",Subject_marks[3])
else:
    print("Highest marks in 4rt subject :",Subject_marks[4])
#Lowest Division
if(Subject_marks[0]<=Subject_marks[1]and Subject_marks[0]<=Subject_marks[2]and Subject_marks[0]<=Subject_marks[3]and Subject_marks[0]<=Subject_marks[4]):
    print("Lowest marks in 1st subject :",Subject_marks[0])
elif( Subject_marks[1]<=Subject_marks[2]and Subject_marks[1]<=Subject_marks[3]and Subject_marks[1]<=Subject_marks[4]):
    print("Lowest marks in 2nd subject :",Subject_marks[1])
elif(Subject_marks[2]<=Subject_marks[3]and Subject_marks[2]<=Subject_marks[4]):
    print("Lowest marks in 3rd subject :",Subject_marks[2])
elif( Subject_marks[3]<=Subject_marks[4]):
    print("Lowest marks in 4rt subject :",Subject_marks[3])
else:
    print("lowest marks in 4rt subject :",Subject_marks[4])

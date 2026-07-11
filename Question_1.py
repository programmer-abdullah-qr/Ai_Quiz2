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
Total_marks = Subject_marks[0]+Subject_marks[1]+Subject_marks[2]+Subject_marks[3]+Subject_marks[4]
print ("Total mark is :", Total_marks)
Averge = Total_marks/2
print("Averge :",Averge)
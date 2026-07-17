# fruit_set = set()

# fruit_set.add(input("Enter 1st fruit: "))
# fruit_set.add(input("Enter 2nd fruit: "))
# fruit_set.add(input("Enter 3rd fruit: "))
# fruit_set.add(input("Enter 4th fruit: "))
# fruit_set.add(input("Enter 5th fruit: "))

# print("Your fruit list:", fruit_set)

A = {10,20,30,40}
B = {30,40,50,60}
print(A.union(B))
print(A.intersection(B))
print(A-B)
print(B-A)

#Taking marks from each student
std1=int(input("Enter marks of 1st student: "))
std2=int(input("Enter marks of 2nd student: "))
std3=int(input("Enter marks of 3rd student: "))
std4=int(input("Enter marks of 4th student: "))
std5=int(input("Enter marks of 5th student: "))
#presenting these marks in a list and sorting them
marks_list=[std1,std2,std3,std4,std5]
marks_list.sort()
print("Sorted list (increasing order)")
print(marks_list)
marks_list.reverse()
print("Sorted list (decreasing order)")
print(marks_list)

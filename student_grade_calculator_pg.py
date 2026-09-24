name = input("enter student name")
m1 = int(input("maths: "))
m2 = int(input("physics: "))
m3 = int(input("chemistry: "))
total = m1+m2+m3
average = total/3
if average >=90:
    grade = "A+"
elif average >=75:
    grade = "A"
elif average >=60:
    grade = "B"
else:
    grade = "C"
    print("\n---RESULT---")
    print("Name",name)
    print("Total",total)
    
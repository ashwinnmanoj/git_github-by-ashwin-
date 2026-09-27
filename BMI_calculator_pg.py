weight = float(input("weight(kg):"))
height = float(input("height(m):"))
bmi = weight/(height**2)
print("BMI=",round(bmi,2))
if bmi<18.5:
    print("underweiight")
elif bmi <25:
    print("normal weight")
elif bmi <30:
    print("overweight")
else:
    print("obese")
                      


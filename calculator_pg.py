num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
op = input("choose the operation (+, -, *, /):")
if op =="+":
    print("aqnswer=",num1+num2)
elif op =="-":
    print("answer=",num1-num2)
elif op =="*":
    print("answer=",num1*num2)
elif op =="/":
    if num2!=0:
        print ("answer=",num1/num2)
    else:
        print("sorry cannot divide by 0")
else:
    print("invalid operator")
    
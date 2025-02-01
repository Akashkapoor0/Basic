grade = lambda n:"A" if n>=90 else "B" if n>=80 else "C"
a = int(input("Enter Percentage: "))
print("Your Grade is",grade(a))
a= int(input("subject 1: "))
b = int(input("subject 2: "))
c = int(input("subject 3: "))
branch = input("Enter your branch: ")
tm = a + b + c
percentage = (tm / 300) * 100

if percentage >= 90 and (branch.lower() in "it,cs"):
    print("Eligible")
else:
    print("Not eligible")
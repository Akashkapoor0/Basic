a = int(input("Enter Physics Mark: "))
b = int(input("Enter chemistry Mark: "))
c = int(input("Enter Math Mark: "))
per = (a+b+c)/3
if a>=90:
    print("Grade: A" )
elif a>=80:
    print("Grade: B" )
elif a>=70:
    print("Grade: C" )
else:
    print("Grade: D" )
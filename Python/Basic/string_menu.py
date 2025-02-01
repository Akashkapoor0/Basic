def upp(s):
    return s.upper()

def low(s):
    return s.lower()

def cap(s):
    return s.capitalize()

def tit(s):
    return s.title()

def sub(st, a):
    return st.find(a)

def lastsub(st, a):
    return st.rfind(a)

def indexat(st, a):
    try:
        return st.index(a)
    except ValueError:
        return -1

def alpha(st, a):
    return st.count(a)

def replace_sub(st, old, new):
    return st.replace(old, new)

def split_str(st, d):
    return st.split(d)

def split_list(st, d, n):
    return st.rsplit(d, n)

def starts_with(st, prefix):
    return st.startswith(prefix)

def ends_with(st, suffix):
    return st.endswith(suffix)

def is_alpha(st):
    return st.isalpha()

def is_digit(st):
    return st.isdigit()

def is_alnum(st):
    return st.isalnum()

def is_space(st):
    return st.isspace()

def str_len(st):
    return len(st)


a = "Y"
while a == "Y":
    print("Hi! Here You Can Convert Your String in Anyform")
    print("1: Lowercase")
    print("2: Uppercase")
    print("3: Titlecase")
    print("4: Capitalize")
    print("5: Search First Alphabet in String")
    print("6: Search Last Alphabet in String")
    print("7: Search Index of Alphabet in String")
    print("8: Count Alphabet in String")
    print("9: Replace Substring in String")
    print("10: Split String")
    print("11: Split String From Last")
    print("12: Starts With")
    print("13: Ends With")
    print("14: Is Alpha")
    print("15: Is Digit")
    print("16: Is Alnum")
    print("17: Is Space")
    print("18: Length of String")
    print("19: Format String")
    choice = input("Enter Your Choice: ")
    s = input("Enter Your String: ")
    
    if choice == "1":
        print("Lowercase: ", low(s))
    elif choice == "2":
        print("Uppercase: ", upp(s))
    elif choice == "3":
        print("Titlecase: ", tit(s))
    elif choice == "4":
        print("Capitalize: ", cap(s))
    elif choice == "5":
        su = input("Enter Alphabet: ")
        print("First Alphabet", "Not present" if sub(s, su) == -1 else "Present at", sub(s, su))
    elif choice == "6":
        su = input("Enter Alphabet: ")
        print("Last Alphabet", "Not present" if lastsub(s, su) == -1 else "Present at", lastsub(s, su))
    elif choice == "7":
        i = input("Enter Alphabet: ")
        print("Index Present at", indexat(s, i))
    elif choice == "8":
        i = input("Enter Alphabet: ")
        print("Alphabet", "Not present" if alpha(s, i) == -1 else "Present:", alpha(s, i))
    elif choice == "9":
        old = input("Enter the substring to replace: ")
        new = input("Enter the new substring: ")
        print("Replaced String: ", replace_sub(s, old, new))
    elif choice == "10":
        d = input("Enter the delimiter: ")
        print("Split String:", split_str(s, d))
    elif choice == "11":
        d = input("Enter the delimiter: ")
        n = int(input("Enter the splitting Number: "))
        print("Split List:", split_list(s, d, n))
    elif choice == "12":
        prefix = input("Enter the prefix: ")
        print("Starts With:", starts_with(s, prefix))
    elif choice == "13":
        suffix = input("Enter the suffix: ")
        print("Ends With:", ends_with(s, suffix))
    elif choice == "14":
        print("Is Alpha:", is_alpha(s))
    elif choice == "15":
        print("Is Digit:", is_digit(s))
    elif choice == "16":
        print("Is Alnum:", is_alnum(s))
    elif choice == "17":
        print("Is Space:", is_space(s))
    elif choice == "18":
        print("Length of String:", str_len(s))
    elif choice == "19":
        print("Format String:", str_len(s))
    else:
        print("Invalid Choice")

    a = input("Do You Want To Continue? (Y/N): ").upper()
print("Thank You For using This Program!")
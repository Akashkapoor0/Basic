def Add(n):
    a = (input("Enter the element to remove: "))
    n.add(a)
    return n

def Remove(n):
    a = (input("Enter the element to remove: "))
    n.remove(a)
    return n

def Discard(n):
    a = (input("Enter the element to discard: "))
    n.discard(a)
    return n

def Pop(n):
    n.pop()
    return n

def Union(n):
    a = set(map(str, input("Enter the Second Set by space: ").split()))
    return n.union(a)

def Intersection(n):
    a = set(map(str, input("Enter the Second Set by space: ").split()))
    return n.intersection(a)

def Difference(n):
    a = set(map(str, input("Enter the Second Set by space: ").split()))
    return n.difference(a)

def Difference(n):
    a = set(map(str, input("Enter the Second Set by space: ").split()))
    return n.difference(a)

def Difference(n):
    a = set(map(str, input("Enter the Second Set by space: ").split()))
    return n.difference(a)

def Symmetric_difference(n):
    a = set(map(str, input("Enter the Second Set by space: ").split()))
    return n.symmetric_difference(a)

def IsSubSet(n):
    a = set(map(str, input("Enter the Second Set by space: ").split()))
    return n.issubset(a)

def IsSuperSet(n):
    a = set(map(str, input("Enter the Second Set by space: ").split()))
    return n.issuperset(a)

def display_menu(n):
    print("Your set is",n)
    print("Menu:")
    print("1. Add")
    print("2. Remove")
    print("3. Discard")
    print("4. Pop")
    print("5. Union")
    print("6. Intersection")
    print("7. Difference")
    print("8. Symmetri Difference")
    print("9. Is SubSet")
    print("10. Is SuperSet")
    print("0. Exit")

n = set(map(str, input("Enter the Set by space: ").split()))
while True:
    display_menu(n)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Set after Add:", Add(n))
    elif choice == 2:
        print("Set after Remove:", Remove(n))
    elif choice == 3:
        print("Set after Discard:", Discard(n))
    elif choice == 4:
        print("Set after Pop:", Pop(n))
    elif choice == 5:
        print("Set after Union:", Union(n))
    elif choice == 6:
        print("Set after Intersection:", Intersection(n))
    elif choice == 7:
        print("Set after Difference:", Difference(n))
    elif choice == 8:
        print("Set after Symmetric_Difference:", Symmetric_difference(n))
    elif choice == 9:
        if IsSubSet(n):
            print("Set is SubSet of B")
        else:
            print("Set is not SubSet of B")
    elif choice == 10:
        if IsSubSet(n):
            print("Set is SuperSet of B")
        else:
            print("Set is not SuperSet of B")
    elif choice == 0:
        print("ThankYou For Using This Program")
        break
    else:
        print("Invalid choice. Please try again.")
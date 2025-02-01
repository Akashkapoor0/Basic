a = input("Enter String: ")
vowels = [i for i in a if i.lower() in 'aeiou']
print("Vowels in the string:", vowels)
text=input("enter the text")
vowels="IUOAEiuoae"
solution={}

for char in text:
    if char not in vowels:
        solution=char
        print("text with out vowel:",solution)
con=input("enter came case")
def convert(con):
    chars=list(con)
    words=[]
    for char in chars :
        if char .isupper():
            words.append("_")
            words.append(char.lower())
        else:
            words.append(char)
    conve=''.join(words)
    print(conve)
convert(con)
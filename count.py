def stri(a):
    d=0
    e=0
    f=0
    h=0
    for i in a:
        if i.isdigit():
            d+=1
        elif i.isupper():
            e+=1
        elif i.islower():
            f+=1
        else:
            h+=1
    print(f"Upper case letters is: {e}")
    print(f"Lower case letters is: {f}")
    print(f"Digits are: {d}")
    print(f"Special Characters are: {h}")
a=input("enter:- ")
stri(a)

def sumofdigits(a):
    d=0
    for i in a:
        if i.isdigit():
            d+=1
    print(d)
a=input("Enter : ")
sumofdigits(a)

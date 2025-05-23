def sumofdigits1(a):
    d=''
    e=0
    for i in a:
        if i.isdigit():
            e+=1
            d+=i
    print(f"The Digits is {d}, and the count of digits is {e}")


a=input("Enter : ")
sumofdigits1(a)

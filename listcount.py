def repeat(b,a):
    c=0
    for i in a:
        if i==b:
            c+=1
        else:
            pass
    return f"The number {b} is present in list {c} times "
b=int(input("Enter the number: "))
a=[23,12,34,23,14,23]
print(repeat(b,a))

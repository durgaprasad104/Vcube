def calculator():
        count=0
        for i in range(count,100):
            a=input("Enter the Operation:- \n 1. Addition \n 2. Subtraction \n 3.Division \n 4.Multiplication \n 5.Expontential \n 6.Floor Division \n 7.Modulus \n 8.Percentage \n :-")
            if a=="1":
                b=int(input("Enter the 1st Number:-"))
                c=int(input("Enter the 2nd Number:-"))
                print(f"Addition is {b+c}")
                count+=1
            elif a=="2":
                b=int(input("Enter the 1st Number:-"))
                c=int(input("Enter the 2nd Number:-"))
                print(f"Subtraction is {b-c}")
                count+=1
            elif a=="3":
                b=int(input("Enter the 1st Number:-"))
                c=int(input("Enter the 2nd Number:-"))
                print(f"Division is {b/c}")
                count+=1
            elif a=="4":
                b=int(input("Enter the 1st Number:-"))
                c=int(input("Enter the 2nd Number:-"))
                print(f"Multiplication is {b*c}")
                count+=1
            elif a=="5":
                b=int(input("Enter the 1st Number:-"))
                c=int(input("Enter the 2nd Number:-"))
                print(f"Exponential is {b**c}")
                count+=1
            elif a=="6":
                b=int(input("Enter the 1st Number:-"))
                c=int(input("Enter the 2nd Number:-"))
                count+=1
                print(f"Floor Division is {b//c}")
            elif a=="7":
                b=int(input("Enter the 1st Number:-"))
                c=int(input("Enter the 2nd Number:-"))
                count+=1
                print(f"Modulus is {b%c}")
            elif a=="8":
                b=int(input("Enter the Number:-"))
                print(f"Percentage is {(b/100)*100}")
                count+=1
            else:
                print("Invalid Input")
                break
calculator()

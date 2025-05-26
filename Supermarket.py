def market(items,cost,stock,a):
    if a==1:
        for i in range (len(items)):
            print(f"{items[i],cost[i],stock[i]}")
    elif a==2:
        s=input("Enter the Product name: ") 
        b=s.capitalize()
        c=int(input("Enter the choice 1.Update Price or 2.Update Stock :")) #update price
        if c==1:
            if b in items: #milk
                d=items.index(b) #0
                e=int(input("Enter the Updated Price for this product: ")) #e ==90
                cost[d]=e
                print("The updated Super market Prices is ")
                for i in range (len(items)):
                    print(f"{items[i],cost[i],stock[i]}")
        elif c==2:
            if b in items:
                g=items.index(b)
                h=int(input("Enter the Updated stock number: "))
                stock[g]=h
                print("The Updated Super Market Stock is ")
                for i in range (len(items)):
                    print(f"{items[i],cost[i],stock[i]}")
    else:
        print("Invalid Choice")
    #return
items=['Milk','Bread','Rice','Cooldrinks','Curd']
cost=[60,30,600,100,30]
stock=[10,8,9,11,7]
a=int(input("Enter the choice: 1.Display Data  or 2.Update Data :"))
market(items,cost,stock,a)

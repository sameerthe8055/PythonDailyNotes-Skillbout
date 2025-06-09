def print_table():
    base = int(input("Enter the num to prit the table: "))
    for i in range(1,11):
        print(f"{base} * {i} = {base * i}")

def seq():  # 0 1 2 3 4 3 2 1 0 
    for i in range(9):
        if i<5:
            print(i, end=" ")
        else:
            print(9-i-1, end=" ")
    print() # for new line

# seq() 

def tablewithoutsymbol():
    base = int(input("Enter the the integer to print table: "))
    a = base
    # for approach ---->
    for i in range(10):
        print(f"{base} * {i} = { a }")
        a += base

    #while apprach ------>
    # i = 0
    # while(i != 10): 
    #     i += 1
    #     print(f"{base} * {i} = { a }")
    #     a += base
# tablewithoutsymbol()

def ord_rev(): # ip: 6 op: 0 1 2 3 4 5 6 5 4 3 2 1 0 
    n = int(input("enter the value to generate the sequence: "))
    for i in range(n+n+1):
        if i <=n :
            print(i, end=" ")
        else:
            print((n+n)-i, end=" ")
    print() # for new line
# ord_rev()

def find_middle_value():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    if a<b and a>c:
        print("a")
    elif a<c and a>b:
        print("a")
    elif b<a and b>c:
        print("b")
    elif b<c and b>a:
        print("b")
    else:
        print("c")
find_middle_value()
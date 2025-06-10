def sum_of_n_nat_nums(n):
    n = int(n*(n+1)/2)
    return n
# print(sum_of_n_nat_nums(5))

def fact(n):
    if n<1:
        return "err.. factorial invalid, number must be greater than Zero"
    if n==1:
        return 1
    return n*fact(n-1)

def inv_fact(n):
    if n<1:
        return "err.. factorial invalid, number must be greater than Zero"
    n=fact(n)
    return 1/n
# print(inv_fact(0))

def pattern_of_fact(x,n):
    if not( type(x) == int and type(n) == int ):
        return "err.. x or n value type is invalid"
    elif n<1:
        return "err.. factorial invalid, n must be greater than Zero"
    else:
        return x**(n/fact(n))
# print(pattern_of_fact(2,5))

def int_len(n):
    # print("ip n:",n)
    if n<0:
         n = n * (-1)
        #  print("n after *(-1):",n)
    count = 0
    while not(n<=0):
        n=n//10
        # print("n:",n)
        count+=1
    return count

# print(int_len(2222))

def sum_digitsof_int(n):
    if n<0:
        n = n * (-1)
    sum = 0
    while not(n<=0):
        sum = sum + n%10
        n = n//10
    return sum
# print(sum_digitsof_int(-2345))

def int_rev(n):
    comp = 1
    if n<0:
        n = n * (-1)
        comp = -1
    rev = 0
    while not(n<=0):
        rev = (rev*10) + (n%10)
        n=n//10
    return rev*comp
# print(int_rev(-505609667))


## gcd or hcf
def gcd(n1, n2):
    while(n2 != n1):
        if n1 > n2: 
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    return n1

## lcm = (n1 * n2) // gcd(n1, n2)
def lcm (n1, n2):
    return (n1 * n2) // gcd(n1, n2)

print(gcd(5, 3))
print(lcm(5,3))



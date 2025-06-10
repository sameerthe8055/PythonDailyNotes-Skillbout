# 1️⃣ ip: 1234 op: 4 ------------>
def reminder_of_ten(n):
    if n<0:
        n = n * (-1)
    return n%10

def int_len(n):
    if n<0:
        n = n*-1
    count = 0
    while not(n<=0):
        n=n//10
        count +=1
    return count
# print(int_len(0))


# 2️⃣ ip: 1234 op: 1 #
def printfirst(n):
    comp = 1
    if n<0:
        n = n * (-1)
        comp =-1
    # while not(n < 11):
        n=n//10
    return n*comp
# print(printfirst(-357909234))

# 3 ip1: 1234 ip: 77 op: 123477
def seq3(n,m):
    comp = 1
    if n<0:
        n = n * (-1)
        comp =-1
    return (n*(10**int_len(m)) + m)*comp


# 4 ip1: 1234 ip: 77 op: 1277
def seq4(n,m):
    comp = 1
    if n<0:
        n = n * (-1)
        comp = -1
    m_len = int_len(m)
    if n<m_len:
        return("err.. values error")        
    tens = 10**m_len 
    return ((n // tens )*tens + m)*comp
# print(seq4(1234,77))

# 5 ip: 1234 op: 1 #
def seq5(n):
    comp = 1
    if n<0:
        n = n * (-1)
        comp =-1
    while not(n < 11):
        n=n//10
    return n*comp
# print(seq5(-357909234))
# 6 ip1: 1234 op: 234
def seq6(n):
    if n<0:
        n = n*-1
    tens = 10**(int_len(n) - 1)
    n = n % tens
    return n
# print(seq6(-1234))

# 7 ip: 1234 ip: 77 op: 771234
def seq7(n,m):
    if n<0:
        n = n * -1
    if m<0:
        m = m * -1
    return  m * 10**int_len(n) + n
# print(seq7(-1263733,-77))

# 8 ip: 1234 ip: 77 op: 7734
def seq8(n,m):
    if n<0:
        n = n * -1
    if m<0:
        m = m * -1
    tens = (10 ** (int_len(n) - int_len(m) ) )
    res = m * tens # 7700
    res = res + n % tens  #7734
    return res
print(seq8(-12335654,-77))
    




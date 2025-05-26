# PythonDailyNotes-Skillbout

## GCD AND LCM - 26-05-2025
```python

## gcd
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

print(lcm(2, 3))

```
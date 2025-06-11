# LeetCode question
### 2520. Count the Digits That Divide a Number
```python
class Solution:
    def countDigits(self, num: int) -> int:
        ip = num
        temp = 0
        count = 0
        while not(num <= 0):
            temp = num%10 
            if ip%temp == 0:
                count+=1
            num = num // 10 
        return count 
```

### 231. Power of Two
```python
class Solution:
    def countDigits(self, num: int) -> int:
        ip = num
        temp = 0
        count = 0
        while not(num <= 0):
            temp = num%10 
            if ip%temp == 0:
                count+=1
            num = num // 10 
        return count 
```

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if  n & (n-1) == 0:
            return True
        else :
            return False       
         
```
### 326. Power of Three
```python
class Solution:
    def isPowerOfThree(self, n: float) -> bool:
        if n == 0:
            return False
        while not(n <= 0):
            n = n/3.0
        if n == 0:
            return True
        else :
            return False
    
```
```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        temp = 1.0
        while n > 3:#
            n = n / 3
        print(n)
        if n == 3:
            return True
        else:
            return False
```
### 367. Valid Perfect Square
```python
class Solution:
    def isPerfectSquare(self, num: float) -> bool:
        if num < 0:
            return False
        elif num == 1 or num == 4 or num == 0 :
            return True
        else:
            i = 2
            while( True):
                temp = i*i
                if temp == num:
                    # print(f"temp: { temp }")
                    return True
                elif temp > num:
                    # print(f"temp: { temp }")
                    return False
                else:
                    i =i +1   
        
```       
### 263. Ugly Number
```python
class Solution:
    def isUgly(self, n: int) -> bool:
        i =2
        while(i<=n/2 and n>1):
            if n%2 == 0:
                n  = n/2
            elif n%3 == 0:
                n  = n/3
            elif n%5 == 0:
                n  = n/5
            else:
                return False
        return True   
        
```       
### 1952. Three Divisors
```python
class Solution:
    def isThree(self, n: int) -> bool:
        if n <0:
            n = n*-1
        if n ==1 or n ==2 or n == 0:
            return False
        count = 2
        i=2
        
        while(i < (n/2 +1)):
            if n%i == 0:
                count += 1
                i+=1
            else:
                i+=1
            if count >3:
                return False
        if count == 3:
            return True
        else:
            return False
```       
### 1342. Number of Steps to Reduce a Number to Zero
```python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps =0
        while(num > 0 ):
            steps += 1
            if num%2 ==0:
                num /= 2
            else:
                num -= 1
        return steps
```       
### 9. Palindrome Number
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        result = 0
        while(x>0):
            result = result*10 + x % 10
            x = x//10
        if temp == result:
            return True  
        else:
            print(result)
            return False
```   
### 50. Pow(x, n)
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

```    
### 2119. A Number After a Double Reversal
```python
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp = num
        result1 = 0
        while(temp>0):
            result1 = result1*10 + temp%10
            temp = temp// 10
        result2 = 0
        temp = result1
        while(temp>0):
            result2 = result2*10 + temp%10
            temp = temp//10
        if num == result2:
            return True
        else:
            print(f"result1: {result1} result2: {result2}")
            return False
```    
### 2544. Alternating Digit Sum
```python
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        val = n
        len = 0
        while(n >0):
            len +=1
            n //=10
        sign = 1
        if len%2 == 0:
            sign = -1
        sum = 0
        while(val>0):
            sum = sum + (val%10 )*sign
            sign = sign  * -1
            val = val//10 
        return sum
```    
### 7. Reverse Integer
```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x<0:
            x = x*-1
            sign = -1
        res = 0
        while(x>0):
            res = res*10 + x%10
            x = x//10
        res = res*sign
        max = 1 << 31
        if 0 > res < -max or 0 < res > (max - 1):
            return 0
        else:
            return res    
        
```    
###
```python

```    
###
```python

```    

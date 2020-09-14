# Question 1
def is_prime(number):

    for element in range(number):
        if number % element == 0:
            return False

    return True
def print_next_prime(number):
   
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
   
    def test_is_five_prime(self):
       
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()

# Question 2
def arm(lower,upper):
    for num in range(lower,upper+1):
        order=len(str(num))
        sum1=0
        temp=num
        while temp>0:
            digit=temp%10
            sum1=sum1+digit**order
            temp=temp//10
        if num==sum1:
           yield(sum1)

l=1
u=1000
x=arm(l,u)
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())

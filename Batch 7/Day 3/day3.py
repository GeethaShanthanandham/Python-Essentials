#Question 1
altitude=input("enter the altitude")
if(altitude==1000):
    print("Safe to Land")
elif(altitude > 1000 and altitude <5000):
    print("Bring down to 1000")
else:
    print("Turn Around")

# Question 2
lower = 1
upper = 200
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


  #Question 1
test_list = [1,5,6,4,1,2,3,5]
sub_list = [1,1,5]
flag = 0
if(all(x in test_list for x in sub_list)):
    flag = 1
if (flag) :
    print ("it's a match")
else :
    print ("it's gone")
list1 = [1,5,6,5,1,2,3.6]
list2 = [1,1,5]
if(all(i in list2 for i in list1)):
    print ("it's a match")
else:
    print ("it's gone")

# Question 2
def prime()
nums = range(1, 2500)
for i in range(2, 8):
      nums = filter(lambda x: x == i or x % i, nums)
print nums
prime()

# Question 3
out = map(lambda x:x.title(), ['hey this is sai', 'I am in mumbai'])
output = list(out)
print(output) 

#Question 1 List and its functions
l=[2,1,3,4]
print(len(l))
print(max(l))
print(min(l))
print(sum(l))
l.sort()
print(l)
l.append(8)
print(l)
l.extend([7,55])
print(l)
l.pop()
print(l)
#Question 2 Dictionary and its functions
d={1:'a',2:'b',3:'c'}
print(d.items())
print(d.keys())
print(d.values())
print(d.has_key(2))
d.clear()
print(d)
#Question 3 Sets and its functions
s={1,2,3}
s.add(4)
print(s)
s.update([6,7,8])
print(s)
s.remove(6)
print(s)
s.discard(2)
print(s)
s.pop()
print(s)
#Question 4 Tuples and its functions
l=(1,3,4,4)
print(len(l))
print(max(l))
print(min(l))
print(sum(l))
print(l.count(4))
#Question 5 Strings and its functions
st="Hello"
print(len(st))
print(st.upper())
print(st.lower())
print(st.swapcase())
print(st.replace("H","r"))

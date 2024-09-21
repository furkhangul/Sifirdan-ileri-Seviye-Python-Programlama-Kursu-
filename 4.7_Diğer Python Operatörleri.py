"""
Bu derste is ve in operatörlerini çalıştım
"""

#Identity operator : is

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y) # => true
print(y==z) # => true
print(x is y) # => true
print(x is z) # => false

a = [1,2,3]
b = [2,4]
y[1] = 1
print(x is y) # => false
print(x is not y)


# Membership operator: in

x = ["apple", "banana"]
print("apple" in x) # =>true
"""
burada apple kelimesinin x in içinde olup olmadığını soruyoruz."""

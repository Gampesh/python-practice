# lamnda should return a value

#def a(x):
#    return x=1

a = lambda x:x+1
print (a(1))


sum = lambda x,y:x+y
print (sum(1,2))

print (lambda x: x+100 if x<10 else x+1000, [1,2,11])


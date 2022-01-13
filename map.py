#map(function, itrative structure)
def boom(x):
    print x

a = map(boom,[1,2]) # return list
print (type(a))

print ("============================================")
print (map(lambda x: x+100, [1,2]))
print (type(map(lambda x: x+100, [1,2]))) # returns list

print ("============================================")
print (map(lambda x: x+100 if x<10 else x+1000, [1, 2, 11]))

print ("============================================")
print (map(None, [1, 2, 11]))

print ("============================================")
print(map(lambda x:x if x%2==0 else None, [1,2,3,4,5,6,7,8,9]))

print ("============================================")
print(map(lambda x:x*x, filter(lambda x: x%2, [1,2,3,4,5,6,7,8,9])))


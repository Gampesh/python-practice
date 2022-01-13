def boom():
    print ('Hi there!!')

boom()

a = 1
def boom():
    print ("val ", a)

boom()

def boom(a=7):
    print ("val ", a)

boom()
boom(4)

def boom(a=7, b=None):
    print ("a, b ", a, b)

boom(6)
boom(6,8)

a = range(10)
for i in a:
    print i

# one * is positional
# two ** is hascode based (Keywordsw)
def boom(*args, **kwargs):
    print ('args', args)
    print ('args', args[3])
    print ('kwargs', kwargs)
    print ('kwargs', kwargs['a'])
    #args[1] = 1000 // this will throw error because its tuple and tuple are immutable
    kwargs['a'] = 'Gampesh'
    print ('kwargs', kwargs)
    print ('args', args[:-1]) # [start:stop:step]

    print (type(args))
    print (type(args[3]))
    print (type(kwargs))

boom(1,2,3,4, a= 10, b=20)

print ("============================================")

def boomKwargs(**kwargs):
    print ('kwargs', kwargs)
    print (type(kwargs))
    return  'boom Called'
a = boomKwargs(a=1, c=2) #Dictionry
print (a)

print(even([1,2,3,4,5,6,7,8,9]))

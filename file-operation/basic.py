file_read = open('./boom.txt', 'r')

for a in file_read:
    print(a)

file_write = open('boom.txt', 'w')
file_write.write('Gampesh sahu')

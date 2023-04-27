mylist = ['banana' , 'apple', 'orange']

# IN generates boolean value
# 1

if 'banana' in mylist:
    print('1')
else:
    print('0')

# 2

print('banana' in mylist)
print({True: '1', False: '0'}['banana' in mylist])
print(('0', '1')['banana' in mylist])
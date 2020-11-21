"""
How Can we read and write a file?

read mode   r
write mode  w
add/create  a

DIR ('../','./')  or ('C:\\...')

f = open('dir', 'mode')
"""

f = open('C:\\Users\\wonju\\OneDrive\\Documents\\test.txt','r') 
contents = f.read()
print(contents)

# You must always close the file after opening.
f.close()

# another way to open a file
with open('C:\\Users\\wonju\\OneDrive\\Documents\\test.txt', 'r' ) as f:
    content = f.read()
    print(iter(content))
    print(iter(content))
    print(content)

print()
    
# third example to open a file
with open('C:\\Users\\wonju\\OneDrive\\Documents\\test.txt', 'r') as f:
    content = f.read()
    print('>', content)
    content = f.read()
    print('>', content) # there will be no printing cuz there is nothing to read
    
    # seek will allow the cursor to point at 0 station again.
    f.seek(0,0)
    content = f.read()
    print('>', content) # hense there is something to read now 

# readline : reads only one line
# if readline is used readline(integer) then the readline method will read only the integer
# amount of letters

print()

with open('C:\\Users\\wonju\\OneDrive\\Documents\\test.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

#readkubes : reads all the lines then saves and returns a list divided by lines

print()
print("###############################################################################")

with open('C:\\Users\\wonju\\OneDrive\\Documents\\test.txt', 'r') as f:
    content = f.readlines()
    print("readlines :",content) # content is a list
    print()
    for c in content:
        print(c, end='')

print()
print()
with open('C:\\Users\\wonju\\OneDrive\\Documents\\test.txt', 'r') as f:
    for line in f:
        print(line)


# writelines : list -> file and save
with open('C:\\Users\\wonju\\OneDrive\\Documents\\test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

with open('C:\\Users\\wonju\\OneDrive\\Documents\\test2.txt', 'r') as f:
    for cnt in f:
        print(cnt)
#3.1
names=['zhang','dong','guo','wu','zhu','chen']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])

print('happy birthday '+names[4].title())
names.append('yu'.title())
print(names)
del names[0]
print(names)

nameA=names.pop()
print(nameA)
print(names)
print(sorted(names))
print(len(names))
for name in names:
	print(name.title() + ' is great')

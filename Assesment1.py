#sort
a = [9, 4, 1, 35, 99, 3.3, 5.5, 9.3, 98.34, 456, 4.32, 5.63, 8.8, 76, 999, 2.11, 237, 4.11, 3.2, 2.57]
a.sort()
print(a)

#highest and lowest
print(max(a))
print(min(a))

#add 5 elements
a.extend([34, 2, 7.8, 28, 17])
print(a)

#extract num
print(a[4], a[7], a[14], a[23])

# remove 10th
a.pop(9)
print(a)

#reverse list
a.reverse()
print(a)

# extract last six
print(a[-6:])

# eliminate highest and lowest
print(a.remove(max(a)))
print(a.remove(min(a)))

#extract from 3rd element to last 3rd element
print(a[2:-3])
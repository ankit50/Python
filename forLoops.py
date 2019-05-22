number = '1, 2, 34, 56, 77, 88, 90'
for i in range(0,len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')

cleanedNumber = ''
for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char
newNumber = int(cleanedNumber)
print('\n')
print(newNumber)

movie = ['SULTAN', 'DABAANG', 'EK THA TIGER', 'WANTED']
for name in movie:
    print("SALMAN KHAN MOVIE IS:" + name)

for i in range(0, 20, 5):
    print(i)

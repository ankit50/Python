import statistics as sts
from functools import reduce
lists = [1, 2, 3, 4, 5, 6]
# MAP
output = list(map(lambda x: x*x, lists))
print(output)

# FILTER
avg = sts.mean(lists)
print(avg)
output1 = list(filter(lambda x: x > avg, lists))
print(output1)

name = ['ankit', 'raj', '', 'ashmita', '', 'ganga', 'ram', '']
name = list(filter(None, name))
print(name)

# REDUCE
output2 = reduce(lambda x, y: x+y, lists)
print(output2)


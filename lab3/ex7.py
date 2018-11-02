#print(map(lambda i: i*i))

x={1,2,3,4,5}

print([el*el for el in x])
print(list(map(lambda el: el*el,x)))
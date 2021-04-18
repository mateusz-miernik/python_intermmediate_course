text_list = ['x', 'xxx', 'xxxxx', 'xxxxxx', '']

f = lambda x: len(x)
print(f('gsgsgs'))

print(list(map(lambda x: len(x), text_list)))

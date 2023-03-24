a = 'text'
b = list(a)
print(b)

a = 'text-/text-/text'
b = a.split('-/')
print(b)
print('-/'.join(b))
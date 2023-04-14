def reader():
    for i in range(4):
        yield '%s' % i


def reader_wrapper(g):
    for v in g:
        yield v


wrap = reader_wrapper(reader())
for i in wrap:
    print(i)
# 0
# 1
# 2
# 3
####################################

for i in reader():
    print(i)
# 0
# 1
# 2
# 3

for i in reader_wrapper("heretic"):
    print(i)
# h
# e
# r
# e
# t
# i
# c

print(list(reader_wrapper(reader())))


# ['0', '1', '2', '3']

def reader_wrapper(g):
    yield from g


print(list(reader_wrapper((reader()))))
# ['0', '1', '2', '3']

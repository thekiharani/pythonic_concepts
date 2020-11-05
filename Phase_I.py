# sequence
def sequence(*iterables):
    # instantiate empty string
    l = ''
    # deconstruct/spread the iterables
    for iterable in iterables:
        # loop through the iterables and append each to the empty string l
        for item in iterable:
            l = l + str(item)
    yield l


# group_when
def group_when(iterable, predicate):
    # convert to iteratormin_key_order
    items = iter(iterable)
    b = []
    c = []
    for n in items:
        b.append(n)
        if predicate(n):
            c.append(b)
            b = []
    if b:
        c.append(b)
    yield c


# drop_last
def drop_last(iterable, n):
    _iterable = iter(iterable)
    try:
        current = [next(_iterable) for i in range(n)]
        index = 0
        for val in _iterable:
            yield current[index]
            current[index] = val
            index = (index + 1) % n
    except StopIteration:
        yield iterable


# yield_and_skip
def yield_and_skip(iterable, skip):
    _iterable = iter(iterable)
    for n in _iterable:
        for _ in range(skip(n)):
            next(_iterable, None)
        yield n


# alternate_all
def alternate_all(*iterables):
    max_len = max(len(x) for x in list(iterables))
    for index in range(max_len):
        for _iterable in iterables:
            try:
                yield _iterable[index]
            except IndexError:
                continue

# min_key_order
def min_key_order(adict):
    new_adict = {k: v for k, v in adict.items()}
    for k, v in new_adict.items():
        yield k, v


'''for i in sequence('abc', '123', 'm700', 'jkgjggv'):
    print(i, end='')'''

'''for i in group_when('combustibles', lambda x: x in 'aeiou'):
    print(i, end='')'''

'''for i in drop_last('combustibles', 5):
    print(i, end='')'''

'''for i in yield_and_skip('abbabxcabbcaccabb', lambda x: {'a': 1, 'b': 2, 'c': 3}.get(x, 0)):
    print(i, end='')'''

'''for i in alternate_all('abcde', 'fg', 'hijk'):
    print(i, end='')'''

for i in alternate_all('abcde87h', 'fg', 'hijk'):
    print(i, end='')

'''d = {1: 'a', 2: 'x', 4: 'm', 8: 'd'}
i = min_key_order(d)
print(next(i))
print(next(i))
del d[8]
print(next(i))
d[16] = 'f'
d[32] = 'z'
print(next(i))
print(next(i))'''

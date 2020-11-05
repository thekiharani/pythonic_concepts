# Generators must be able to iterate through any kind of iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


# The combination of return and yield None make each of the following
#   a generator (yield None) that immediately raises the StopIteration
#   exception (return)

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
    # max_len = max(len(x) for x in list(iterables))
    for _iterable in iterables:
        for _item in _iterable:
            try:
                yield _item
            except IndexError:
                continue




# min_key_order
def min_key_order(adict):
    new_adict = {k: v for k, v in adict.items()}
    for k, v in new_adict.items():
        yield k, v

 
           
         
if __name__ == '__main__':
    from goody import irange
    
    # Test sequence; you can add any of your own test cases
    print('Testing sequence')
    for i in sequence('abc', 'd', 'ef', 'ghi'):
        print(i,end='')
    print('\n')

    print('Testing sequence on hidden')
    for i in sequence(hide('abc'), hide('d'), hide('ef'), hide('ghi')):
        print(i,end='')
    print('\n')


    # Test group_when; you can add any of your own test cases
    print('Testing group_when')
    for i in group_when('combustibles', lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')

    print('Testing group_when on hidden')
    for i in group_when(hide('combustibles'), lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')


    # Test drop_last; you can add any of your own test cases
    print('Testing drop_last')
    for i in drop_last('combustible', 5):
        print(i,end='')
    print('\n')

    print('Testing drop_last on hidden')
    for i in drop_last(hide('combustible'), 5):
        print(i,end='')
    print('\n')


    # Test sequence; you can add any of your own test cases
    print('Testing yield_and_skip')
    for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')

    print('Testing yield_and_skip on hidden')
    for i in yield_and_skip(hide('abbabxcabbcaccabb'),lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')


    # Test alternate_all; you can add any of your own test cases
    print('Testing alternate_all')
    for i in alternate_all('abcde','fg','hijk'):
        print(i,end='')
    print('\n')
    
    print('Testing alternate_all on hidden')
    for i in alternate_all(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print('\n\n')
       
         
    # Test min_key_order; add your own test cases
    print('\nTesting Ordered')
    d = {1:'a', 2:'x', 4:'m', 8:'d', 16:'f'}
    i = min_key_order(d)
    print(next(i))
    print(next(i))
    del d[8]
    print(next(i))
    d[32] = 'z'
    print(next(i))
    print(next(i))
    


         
         
    import driver
    driver.default_file_name = "bscq4F20.txt"
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    

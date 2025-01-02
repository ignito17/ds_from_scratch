# When passing functions around, sometimes we’ll want to partially apply (or curry)
# functions to create new functions


def exp(base,power):
    return base ** power

# This works like a partial function of fn-exp
def two_to_the(power):
    return exp(2, power)
# print(exp(3,4))

from functools import partial,reduce
three_to_the=partial(exp,3)         # This is also a partial function of fn-exp(done easliy)

# print(three_to_the(2))

squre_of=partial(exp,power=2)

# print("Square of 2=",squre_of(2),sep='')


# We will also occasionally use map, reduce, and filter, which provide functional
# alternatives to list comprehensions:
def double(x):
    return 2*x

xs=[1,2,3,4]
twice_xs=[double(x) for x in xs]
thrice_xs=map(double,xs)                # same as above maps a fucntion to a list.
list_doubler=partial(map,double)        # a fucntion that runs map on double function
# print(*twice_xs,*thrice_xs,*list_doubler(xs))

# You can use map with multiple-argument functions if you provide multiple lists:
def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5])            # [1 * 4(x1,y1), 2 * 5(x2,y2)] = [4, 10]
# print(*products)


# Similarly, filter does the work of a list-comprehension if:
def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 == 0

x_evens=[x for x in xs if is_even(x)]               # [2,4]
x_evens1=filter(is_even,xs)                         # Same as above
list_evener=partial(filter, is_even)               # funtion that filters even from a list
x_evens2=list_evener(xs)

# print(*x_evens,*x_evens1,*x_evens2)


# And reduce combines the first two elements of a list, then that result with the third, that
# result with the fourth, and so on, producing a single result:
x_product = reduce(multiply, xs) # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply) # *function* that reduces a list
x_product = list_product(xs) # again = 24
# print(x_product,list_product(xs))


# enumerate
# Not infrequently, you’ll want to iterate over a list and use both its elements and their
# indexes:

documents=[x for x in range(100) if x%2==0 and x%3!=0]
# not Pythonic
# for i in range(len(documents)):
#     document = documents[i]
#     print(i, document)
# # also not Pythonic
# i = 0
# for document in documents:
#     print(i, document)
#     i += 1
# The Pythonic solution is enumerate, which produces tuples (index, element):
# for i, document in enumerate(documents):
    # print(i, document)

# for i, _ in enumerate(documents): print(i) # Pythonic

# zip and Argument Unpacking
# Often we will need to zip two or more lists together. 
# zip transforms multiple lists into a single list of tuples of corresponding elements:

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
# print(*zip(list1, list2))

# If the lists are different lengths, zip stops as soon as the first list ends.
# You can also “unzip” a list using a strange trick:
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
# print(letters,numbers)
# print(*pairs,type(pairs),sep='\n')

# The asterisk performs argument unpacking, which uses the elements of pairs as
# individual arguments to zip. It ends up the same as if you’d called:
# zip(('a', 1), ('b', 2), ('c', 3))

def add(a, b): return a + b
# add(1, 2)               # returns 3
# add([1, 2])           # TypeError!
# add(*[1, 2])            # returns 3

# What we need is a way to specify a function that takes arbitrary arguments. We can do this
# with argument unpacking and a little bit of magic:
def magic(*args, **kwargs):
    print("unnamed args:", args)            # args is a tuple of its unnamed arguments
    print("keyword args:", kwargs)          # kwargs is a dict of its named arguments.
# magic(1, 2, key="word", key2="word2")

# It works the other way too, if you want to use a
# list (or tuple) and dict to supply arguments to a function:
def other_way_magic(x, y, z):
    return x + y + z
x_y_list = [1, 2]
z_dict = { "z" : 3 }
# print(other_way_magic(*x_y_list, **z_dict)) 


def f2(x, y):
    return x + y

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g
g = doubler_correct(f2)
print(g(*x_y_list)) # 6

def func_max(f,g):
    def h(x):
        return max(f(x), g(x))

    return h

def double(x):
    return 2 * x

def square(x):
    return x * x


h1 = func_max(double, square)
assert(h1(1) == 2)  # must be True
assert(h1(3) == 9)  # must be True
h2 = func_max(double, abs)
# abs is standard Python function computing absolute value of number
assert(h2(-2) == 2)  # must be True
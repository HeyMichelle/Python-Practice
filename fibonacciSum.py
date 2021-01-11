# For a given positive integer n, determine if it can be represented as a sum of two Fibonacci numbers (possibly equal)

### Understand
    # example: if n was 60
    # fibonnacci, what two numbers add up to 60
    # lets say the list gives you [0,1,2....55] until 55
    # if chose 0 as first number
        # dont just +1 because obv 0 + 1 is 1, not 60
        # approach it as 1 + x = 60
        # if chose 8, the next number must be 52 to = 60
            # only need to check if 52 is in the provided list of numbers
        # only need two numbers that add to 60 that are in the given list
    # The output only wants True/false, is there a fibonacci number
    # the target is n
        # we are looking for: target - num = compliment - num
        # check if compliment exists:
            # return true
        # when do we finally stop? If we pass the target fibonacci number

### Plan
    # don't use recursion, it's exponential in size and not a good way to approach the problem
    # existing conditions from problem:
    # f(i) = f(i-1) + f(i-2) but can't start at 0:
        # i = 0 
        # f(0) = 0
        # f(1) = 1 
        # the 0 and 1 is hardcoded, should be true (given by problem)
        # n = 11 the output should be true
        # don't have to find the two numbers and return them
        # no need for recursion or binary search
        # take only what you need from the fibonacci sequence

# solution 1 thoughts and notes:
    # O(fib(n)) runtime
    # Finding something in an array is O(n) complexity
    # after looking at solution below, ask: is there a data structure that finds items in O(1) time?
        # searching in dictionaries is O(1) and would be an improvement
        # a set removes duplicates and search is also O(1) but you can't loop over a set
            # in a set: use add instead of append and fib_set = {0,1} for fib_set
        # what if you looped over the array and SEARCHED through the set? 
            # see solution two below, will avoid O(n) * O(n) in loops and instead* (O)(1)

# solution 1: brute force
# def fibonacciSimpleSum2(n):
#     fibs = [0, 1]
#     i = 2

#     # generate list of fibonacci
#     while True:
#         new_fib_num = fibs[i-1] + fibs[i-2] # will generate next num in sequence
#         if new_fib_num > n:
#             break # no variables outside the while loop, may seem like a bad break but everything is local
#         fibs.append(new_fib_num)
#         i += 1 # i will advance further so you're not just pushing 1's into the array

#     # let's try each number
#     # get its compliment
#     # check if compliment exists or not
#     for fib_num in fibs: ## O(n) 
#         compliment = n - fib_num
#         # check if compliment exists in fib array
#         # most pythonic way looks like psuedo code:
#         if compliment in fibs: ## O(n)
#             return True

#     return False # if you didn't find it

# soluion 2
def fibonacciSimpleSum2(n):
    fibs = [0, 1]
    fibs_set = {0, 1}
    i = 2

    # generate list of fibonacci
    while True:
        new_fib_num = fibs[i-1] + fibs[i-2] # will generate next num in sequence
        if new_fib_num > n:
            break # no variables outside the while loop, may seem like a bad break but everything is local
        fibs.append(new_fib_num)
        fibs_set.add(new_fib_num)
        i += 1 # i will advance further so you're not just pushing 1's into the array

    # let's try each number
    # get its compliment
    # check if compliment exists or not
    for fib_num in fibs: ## O(n) 
        compliment = n - fib_num
        # check if compliment exists in fib array
        # most pythonic way looks like psuedo code:
        if compliment in fibs_set: ## O(1) no long n^2
            return True

    return False # if you didn't find it



# notes on sets:
    # no order
    # just finding if something exists
    # able to see clearly "oh there's my number"
    # like a dictionary with just keys
    # no duplicates
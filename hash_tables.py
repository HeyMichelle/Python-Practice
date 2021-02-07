# making a hash function:
    # be consistent (should always have same output)
    # should be fast
    # should take strings and convert to numbers
        # with encoding
my_array = ['apple is a fruit', 'banana is a fruit', 'fruit', 'veggie']

def my_hash(str, table_size):
    # do stuff to convert string to a number/encode
    bytes_str = str.encode()
    print(bytes_str)
    bytes_sum = 0
    for byte in bytes_str:
        print(f'{byte}')
        bytes_sum += byte
    
    return bytes_sum % table_size
    #  % table_size is to resize the array according to how much space they actually need, if # was 604 but only neded 10 spaces in array, then you would need a smaller index # to store the hashed info
    # so you need to add table_size as a param to has function

my_hash('banana', 4)
my_hash('apple', 4)
print(my_hash('banana', 4))
print(my_array[my_hash('banana', 4)])
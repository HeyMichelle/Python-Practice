# making a hash function:
    # be consistent (should always have same output)
    # should be fast
    # should take strings and convert to numbers
        # with encoding
my_array = [('apple, apple is a fruit'), 'banana is a fruit', 'fruit', 'veggie']


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity            
    def my_hash(self, key):
        # do stuff to convert this str to a number
        bytes_str = key.encode()
        bytes_sum = 0
        for byte in bytes_str:
            bytes_sum += byte
        return bytes_sum % self.capacity 
    def insert(self, key, value):
        # convert the key to an index for our storage  
        index = self.my_hash(key)
        print(f'{key} hashed to {index}')
        # Store the value in storage 
        self.storage[index] = value
    def get(self, key):
        # convert the key to an index for our storage  
        index = self.my_hash(key) 
        return self.storage[index]
my_dict = HashTable(8)
my_dict.insert('banana', 'banana is a fruit')
# my_dict['banana'] = 'banana is a fruit'
# print my_dict['banana']
my_dict.insert('apple', 'apple is also a fruit')
my_dict.insert('cucumber', 'cucumber is a vegetable')
my_dict.insert('tomato', 'no one can agree on tomato')
# print(my_dict.get('banana'))
# print(my_dict.get('apple'))
# print(my_dict.get('tomato'))
# print(my_dict.get('cucumber'))
my_dict.insert('peach', 'Definitely not a banana')
print(my_dict.get('banana'))



# def my_hash(str, table_size):
#     # do stuff to convert string to a number/encode
#     bytes_str = str.encode()
#     print(bytes_str)
#     bytes_sum = 0
#     for byte in bytes_str:
#         print(f'{byte}')
#         bytes_sum += byte
    
#     return bytes_sum % table_size
#     #  % table_size is to resize the array according to how much space they actually need, if # was 604 but only neded 10 spaces in array, then you would need a smaller index # to store the hashed info
#     # so you need to add table_size as a param to has function

# my_hash('banana', 4)
# my_hash('apple', 4)
# print(my_hash('banana', 4))
# print(my_array[my_hash('banana', 4)])

# # get index for banana
# index = my_hash('banana', 4)
# # store the value for banana
# my_array[index] = 'is_fruit'

# print(my_array[my_hash('banana', 4)])

my_tuple = (1, 2, 3)

your_tuple = 1, 2, 3



my_list = [9, 8, 7]
converted_tuple = tuple(my_list)

def divide_and_reminder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

result = divide_and_reminder(22, 3)
print(result)

tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
comb_tuple = tuple_a + tuple_b
print(comb_tuple)

location = (40.7128, -74.0060)
locations = {
    "New York": location,
    "Los Angeles": (34.0522, -118.2437)
}



my_tuple = ("ahmet", 10, 30)
x, y, z = my_tuple 

my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[:3] + (10, 20) + my_tuple[3:]  # 3. elemana kadar, sonra 10 ve 20 eklenir, sonra geri kalan elemanlar eklenir
# new_tuple: (1, 2, 3, 10, 20, 4, 5)


# Membership test in tuple
my_tup = ('a', 'p', 'p', 'l', 'e',)

# In operation
#print('a' in my_tup)
#print('b' in my_tup)

# Not in operation
#print('g' not in my_tup)

for x in my_tup:
    print(x)



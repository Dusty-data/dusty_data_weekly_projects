dusty = [1, 2, 3, 4,]

blank_list = []

numbers = [1, 2, 3, 4, 5, 6, 7, 1]

print(1 in numbers)
numbers.remove(1)


fruchten = ["apple", "banana", "mandarijn", "peren", "peer"]

mixed_list = [1, "apple", False, 2.72]

mixed_list.insert(3,5)





my_numbers = list([1, 2, 3, 4, 5])

my_numbers.extend(mixed_list)





my_numbers_range = list(range(1,11))

popped_element = my_numbers_range.pop()


vierkante_numbers = [x**2 for x in range(1, 6)]

repeated_numbers = ["hello"] * 3 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]



flattend = [num for row in matrix for num in row]



students = [
    ["Metin", 23, "Computer Engineering"],
    ["Kerem", 21, "Mathematics"],
    ["Havva", 20, "Econemetry"]
]

sub_list_1_1 = students[1][1]

del sub_list_1_1

numbers = [i for i in range(1,11)]

odd_numbers = [x for x in numbers if x % 2 == 1]

word = "Python"
letters = [char for char in word]

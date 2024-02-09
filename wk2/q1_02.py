students = {
    'Simon Hoeve': [85, 90, 78],
    'Joshua Winkel': [79, 65, 72],
    'Aylin Yazici': [75, 90, 82],
    'Karen Yilmaz': [84, 72, 83],
    'Ahu Baysal': [96, 67, 88],
    'Jip Holte': [65, 80, 72],
    'Janneke Groot': [88, 68, 92],
    'John Karizma': [45, 67, 75],
    'Elif Winkie': [86, 79, 74],
}


# Calculate average grades and store students with average grade below 70 in a set
below_70_set = set()
for full_name, grades in students.items():
    name, surname = full_name.split(" ")
    average_grade = sum(grades) / len(grades)
    if average_grade < 100:  # Corrected condition to check if the average grade is less than 70
        below_70_set.add((name, surname))

# Print the set of students with average grade below 70
print("Students with an average grade below 70:")
for name, surname in below_70_set:
    print(f"{name} {surname}")

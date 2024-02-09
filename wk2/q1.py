"""
1-Her öğrencinin not ortalamasını hesaplayın ve sözlüğe ekleyin.

2-En yüksek not ortalamasına sahip öğrenciyi bulun ve ekrana yazdırın.

3-Her öğrencinin adını soyadından ayırarak ayrı bir tuple içinde saklayın ve bunları bir listeye ekleyin.

4-Adları alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın.

5-Not ortalaması 70'in altında olan öğrencileri bir küme (set) içinde saklayın.
"""


# Store information and notes of 10 students using a dictionary. Let each student have their name, surname and grades (Midterm, Final and Viva grades).

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
    'Kerem Salman': [68, 42, 78] 
}

# Calculate each student's GPA and add it to the dictionary.

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    students[student].append(avg_grade)



# Finding the student with the highest average grade and print screen

highest_avg_grade_student = max(students, key=lambda x: students[x][-1])

print("En yüksek not ortalamasına sahip öğrenci:", highest_avg_grade_student)
print("Not ortalaması:", students[highest_avg_grade_student][-1])

# Separate each student's name from their surname and store them in a separate tuple and add them to a list.

student_names = [(student.split()[0], student.split()[1]) for student in students]


# Sort the names alphabetically and print the sorted list to the screen.

sorted_student_names = sorted(student_names)

print("Sıralanmış öğrenci adları:")
for name in sorted_student_names:
    print(name[0], name[1])


# Keep students with GPA below 70 in a cluster (set).

below_70_set = {student for student, grades in students.items() if grades[-1] < 70}

print("Not ortalaması 70'in altında olan öğrencilerin kümesi:", below_70_set)



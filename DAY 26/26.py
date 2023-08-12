# list comprehension used to cut down on code
import random as rd
num = [1, 2, 3]
new_num = [(n+1) for n in num]
print(new_num)


list_num = [2*i for i in range(1, 5)]
print(list_num)


# conditional list comprehension
even = [x for x in range(0, 13) if x % 2 == 0]
print(even)

names = ['Shreya', 'Archana', 'Nischal', 'Babu', 'Tata']
new_names = [name.upper() for name in names if len(name) <= 6]
print(new_names)

# Dictionary comprehension
# new_dict={new_key:new_value for (key,value) if test}
students = {student: rd.randint(0, 101) for student in names}
print(students)
passed_students = {name: students[name]
                   for name in names if students[name] >= 60}
print(passed_students)
# OR
pass_stud = {student: score for (
    student, score) in students.items() if score >= 60}
print(pass_stud)

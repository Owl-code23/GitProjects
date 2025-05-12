# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# # new_list = [new_item for item in list]
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# # new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names = [n.upper() for n in names if len(n) > 4]
# print(long_names)

# # new_dict = {new_key:new_value for item in list if test}
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student:random.randint(0, 100) for student in names}
# print(students_scores)

# # new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)


import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    if row.student == "Angela":
        print(row.score)
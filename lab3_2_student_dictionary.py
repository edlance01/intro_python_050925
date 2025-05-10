students = {
    1: {"name": "John", "age": 24, "fin_grades": [3.0, 4.0, 2.0, 4.0]},
    2: {"name": "Sam", "age": 19, "fin_grades": [4.0, 4.0, 4.0, 3.0]},
    3: {"name": "Lester", "age": 21, "fin_grades": [3.0, 3.0, 4.0, 3.0]},
    4: {"name": "Suzie", "age": 22, "fin_grades": [4.0, 2.0, 4.0, 4.0]},
}

avg = 0.0
for student in students.keys():
    # find the avg
   #print(students.get(student).get("fin_grades")) # equivalent to next line
   total = sum(students[student]["fin_grades"])
   avg = total / len(students[student]["fin_grades"])
   print(avg)

   # add the avg
   students[student]["gpa"] = avg

print(f"\nAll student entries: {students}\n")

# print the student and their gpa
for values in students.values():
   print(values["name"] + ": " + str(values["gpa"]))
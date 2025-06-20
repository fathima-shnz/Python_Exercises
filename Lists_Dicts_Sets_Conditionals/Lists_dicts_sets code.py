#1
age_list = [24, 25, 26, 27, 28]
name_list = ["Arya", "Sansa", "Rob", "Bran", "John"]

#2
name_list.append("Yazhini")

age_list.insert(2,30)

name_list.remove("Yazhini")

age_list.pop()

a_list2 = [29, 30, 26]
age_list.extend(a_list2)

age_list.sort()

max_age = age_list[-1]
min_age = age_list[0]
(sum(age_list))

#3
print(name_list[0])

print(name_list[-1])

print(name_list[2:4])

print(name_list[::-1])

#Dictionary
student_marks = {"Aiswarya": 67, "Anjana": 98, "Shana": 77, "Nazira": 89, "Faiza": 60}

print(student_marks["Shana"])

student_marks["Janani"] = 80

student_marks.update({"Shana": 82})

print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())

#Sets
my_set = {"a","e","i","o","u","a","a","i"}
print(my_set)
#sets automatically sort and deletes duplicate values

#my_set[4] = "a"
#print(my_set)
#sets do not allow assignment using index

set1 = {1,3,5,7,9}
set2 = {2,3,5,8,10}

union_set = set1.union(set2)
print("Union:", union_set)
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

#Operators & Conditional Statements
score = int(input("Enter a number from 0 to 10: "))

if score > 7:
    print("Above Average: Excellent work!")
elif score >=4:
    print("Average: Good effort! Keep practicing.")
else:
    print("Below Average: Needs lot of work to improve")









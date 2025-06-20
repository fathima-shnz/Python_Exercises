#1
str1 = "Hello"
str2 = input("Enter your Name: ")
greet = (str1 + " " + str2)
print(greet)

str3 = ", welcome to Python programming"
greet = (greet + str3)
print(greet)

#2
print(greet[0])
print(greet[-1])
print(greet[:5])
print(greet[-11:])
print(greet[::-1])
print(greet[24:30])

#3
strM = "Python beginner tutorial"
strM.upper()
strM.lower()
strM.capitalize()
strM.count("t")
strM.replace("Python", "Machine Learning")

#4
tup1 = (10, 20, 30)
tup2 = (40, 50, 60)
t_combine = tup1 + tup2

t_thrice = t_combine * 3

print(t_combine[2])

print(t_combine[:3])

print(t_combine[-3:])





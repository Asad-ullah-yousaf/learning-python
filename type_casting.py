# Type Casting: The conversion of one data type into another is known as type casting
#  String , Integer , Boolean , Float
#  It can be Implicit or Explicit

name = "Asad"
age = 20
gpa = 3.69
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# converting a string into boolean always results in True, except for an empty string which results in False.
name = bool(name)
print (name)

gpa = int(gpa)
print(gpa)
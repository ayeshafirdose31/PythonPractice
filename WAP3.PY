#WAP to print grades of student 

marks=int(input("Enter your marks to know grade: "))

if marks>=90:
    print("Your grade is ='A'")
elif marks >=80 and marks<90:
    print("Your grade is ='B'")
elif marks>=70 and marks<80:
    print("Your grade is ='C'")
else:
    print("Your grade is ='D'")

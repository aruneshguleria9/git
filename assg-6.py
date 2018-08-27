#ques_1.
a=int(input())
def area(a):
    ar=12.56*a*a
    print(ar)
area(a)
#ques_2.
def perf(n):
    j=0
    for i in range(1,n):
     if n%i=0:
         j=j+1
    if n==j:
        print(n)
for n in range (1,1000):
    perf(n)
#ques_3.
a=int(input())
def mult(a):
    for i in range (1,11):
     print(a,"X",i,a*i,"")
mult(a)
#ques_4.
a=int(input())
b=int(input())
def pow(a,b):
    if b==1:
        return a
    else:
        return(a*pow(a,b-1))
print(pow(a,b))
#old link submutted by mistake so thats why merging the two files
#assignment7.
#ques_1.
age=int(input("enter age to find "))
l={'ashu':20,'aru':21,'bidu':19,'papu':22}
for k,j in l.items():
    if j==age:
     print(k)
#ques_2.
students = {'ash': {'english': 20, 'maths': 40, 'science': 60},
          'jeet': {'english': 30, 'maths': 50, 'science': 70},
         'ashu': {'english': 89, 'maths': 78, 'science': 88},
         'dawat': {'english': 45, 'maths': 55, 'science': 75}}
name=input('enter name \n')
for n,s in students.items():
        if name==n:
            print("\nName",n)
            for marks in s:
                print(marks+':',s[marks])


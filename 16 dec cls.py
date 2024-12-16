school examination are completed to assaign a grade by calculating the percentage given total marks 600 and each
subject is 200. hence take a marks from user for 3 subjects (maths,phy,chemistry)if the user getting less than 
35% considers as fail ,if it is (35-50) consider as c-grade ,if it is (50-90) consider as b-grade , if it is 
(90-100)as a-grade

maths=int(input('enter maths marks:'))
phy=int(input('enter phy marks:'))
chem=int(input('enter chem marks:'))
total_marks=600
sum_marks=maths+phy+chem
per=(sum_marks/total_marks)*100
print(per)
if per<35:
    print('grade is f')
elif per>35 and per<=50:
    print('grade is c')
elif per in range (51,91):
    print('grade is b')
elif per in range (91,101):
    print('grade is a')
else:
     print('invalid per')
# quiz application

corr_ans=0
wrong_ans=0
print('1.what is the capital of india?')
user_ans=input('enter_ans:').lower()
print(user_ans)
if user_ans=='delhi':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong ans')
print('2.who is the famous indian cricketer of india?')
user_ans=input('enter_ans:').lower()
print(user_ans)
if user_ans=='dhoni':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong ans')
print('3.what is the national bird of india?')
user_ans=input('enter_ans:').lower()
print(user_ans)
if user_ans=='peacock':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong ans')
print('4.what is the most loved  game in india?')
user_ans=input('enter_ans:').lower()
print(user_ans)
if user_ans=='cricket':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong ans')
print('5.what is the loved work  in india?')
user_ans=input('enter_ans:').lower()
print(user_ans)
if user_ans=='farming':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong ans')
print('percentage',((corr_ans/(corr_ans+wrong_ans))*100))

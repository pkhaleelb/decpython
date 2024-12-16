there is a football match going on and to attend the match ticket is compulsory based on the age ,
if the age is between 18-30 is 5 dollars ,if age 30-50 is 20 dollars and age is more than 50 is free
 but printing the value calculate it as Indian rupees . write the python code using elif 

USD_TO_INR = 83
age = int(input("Enter your age: "))

if age>18 and age<= 30:
    ticket_price_usd = 5
    ticket_price_inr = ticket_price_usd * USD_TO_INR
    print(f"The ticket price is {ticket_price_inr} INR.")
elif age in range (31,51):
    ticket_price_usd = 20
    ticket_price_inr = ticket_price_usd * USD_TO_INR
    print(f"The ticket price is {ticket_price_inr} INR.")
elif age > 50:
    print("The ticket is free.")
else:
    print("You are not eligible to purchase a ticket.")

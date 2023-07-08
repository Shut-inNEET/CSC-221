#Chapter 2 Exercise 8
#Jake Schrecengost

#This program takes user's input for the meal cost at a restaurant. With this information, it proceeds to calculate the total cost of the meal along with 7% sales tax and 18 percent tip. 

#inputs: meal_purchased
#constants: tax, tip
#calculate: total_tax, total_tip, overall_total
#outputs: meal_purchased, total_tax, total_tip, overall_total


#ask for the cost of the meal
meal_purchased = float(input('How much was the meal? $'))

#tax is 7%
tax = 0.07
#tip is 18%
tip = 0.18

#calculate the meal tax
total_tax = tax * meal_purchased
#calculate the tip of the meal
total_tip = tip * meal_purchased
#calculate the sum of meal, meal tax, and meal tip 
overall_total = meal_purchased + total_tax + total_tip

#display meal cost, meal tax, meal tip, and overall total 
print(f'Your meal cost was: ${meal_purchased:.2f}\nYour tax total is: ${total_tax:.2f}\nYour tip total is: ${total_tip:.2f}\nYour overall total is: ${overall_total:.2f}')

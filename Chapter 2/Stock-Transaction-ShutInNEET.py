#Chapter 2 Exercise 12
#Jake Schrecengost

#This program will take the amount of stocks Joe has bought and calculate the amount of money that is left over after Joe has sold his stocks at a different price along with commission fees. If the resulting amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.

#constants: share_amount, stockbuyingprice, stocksellingprice, commission
#calculate: buying_commission, totalbuyingprice selling_commission, totalsellingprice
#outputs: totalbuyingprice, buying_commission, totalsellingprice, selling_commission, amountgained_orloss 


#shares Joe bought
share_amount = 2000
#price per stock when bought
stockbuyingprice = 40.00
#price per stock when sold
stocksellingprice = 42.75
#commission fee is 3% for total buying and selling price
commission = 0.03

#calculate total buying price 
totalbuyingprice = share_amount * stockbuyingprice
#calculate commission fee of total buying price
buying_commission = share_amount * stockbuyingprice * commission
#calculate total selling price 
totalsellingprice = share_amount * stocksellingprice
#calculate commission fee of total selling price
selling_commission = share_amount * stocksellingprice * commission
#calculate profit or loss by subtracting total buying price from both buying and selling commission fees
amountgained_orloss = totalsellingprice - selling_commission - buying_commission

#display amount of shares and initial price per share along with commission
print('Joe has bought 2000 shares of Acme Software, Inc. at $40.00 per share with a 3% commission fee.')
#display a blank line for clarity and neatness
print('')
#display total price of stocks bought
print(f'The total buying price is ${totalbuyingprice:.2f} when he bought the stocks.') 
print('')
#display commission fee when shares are bought
print(f'The total commission price is ${buying_commission:.2f} when he bought the stocks.') 
print('')
#display total price of stocks sold
print(f'The total selling price is ${totalsellingprice:.2f} when he sold the stocks.')
print('')
#display commission fee when shares are sold
print(f'The total commission price is ${selling_commission:.2f} when he sold the stocks.')
print('')
#display remaining profit
print(f'Joe profited with a remainder of ${amountgained_orloss:.2f}.')
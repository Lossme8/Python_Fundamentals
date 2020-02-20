'''This module is for the sum of money made over the years as per the vegetable type'''
#All this figures in rands
tomatoes_total = 1439089
onions_total = 1301279
beetroot_total = 1080883
carrots_total = 727572
cabbage_total = 564283

sum = tomatoes_total + onions_total + beetroot_total + carrots_total + cabbage_total
print(str(sum) + ' in Rands')

profit = sum - (sum * float(.15)) #0.15 is the tax value
print(str(profit) + ' in Rands')

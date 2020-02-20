import sum_of_prices

profit = sum_of_prices.sum - (sum_of_prices.sum * float(.15)) #0.15 is the tax value
#print(str(profit) + ' in Rands')

actual_cost = float(input("Please enter the actual stock price: "))
sale_amount = float(input("Please enter the sale amount: "))

if actual_cost > sale_amount:
    amount = (actual_cost - sale_amount) * 0.15
    #profit = sum_of_prices - amount
    print("Total profit amount = {0}".format(amount))

elif sale_amount > actual_cost:
    amount = float(sale_amount - actual_cost) * 0.15
    #profit = float(sum_of_prices) - amount
    print("Total loss  = {0}".format(amount))

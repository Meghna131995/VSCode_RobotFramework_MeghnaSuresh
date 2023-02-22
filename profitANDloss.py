# actual_cost = float(input(" Please Enter the Actual Product Price: "))
# sale_amount = float(input(" Please Enter the Sales Amount: "))
#
# if (actual_cost > sale_amount):
#     amount1 = actual_cost - sale_amount
#     print("Total Loss Amount = {0}".format(amount1))
# elif (sale_amount > actual_cost):
#     amount2 = sale_amount - actual_cost
#     print("Total Profit = {0}".format(amount2))
# else:
#     print("No Profit No Loss")

print("----------------")
actual_cost=[100,150,200,700]
sale_amount=[500,600,80,700]
sale=zip(actual_cost,sale_amount)
for x,y in sale:
    if x<y:
        amount1 = y - x
        print("Total profit = {0}".format(amount1))
    elif x>y:
        amount2 = x - y
        print("Loss = {0}".format(amount2))
    else:
        print("No Profit No Loss")
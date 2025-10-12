#Calculate and return the total delivery fee with any distance and rate input
def delivery_fee(rate, dist):
    return f'₱{rate*dist:.2f}'

#Assign the variables of the distance and rate from user input
dist = int(input("Enter distance in kilometers: "))
rate = int(input("Enter rate per kilometer (₱): "))

#Display the total delivery fee
print("Total Delivery Fee:", delivery_fee(rate, dist))
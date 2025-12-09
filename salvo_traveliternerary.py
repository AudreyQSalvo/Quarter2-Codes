import array

count = 0
travel_itinerary = []

print("Please enter your 5 travel destinations:")

for i in range(1, 6, 1):
    travel_itinerary.append(str(input(f"Destination {i}: ")))

print("Original Travel Itinerary:")
for i in range(0, 5, 1):
    count = count + 1
    print(f"{count}. {travel_itinerary[i]}")

print("Let's update your 2nd and 5th destinations.")
travel_itinerary[1] = str(input("Enter a new destination for position 2: "))
travel_itinerary[4] = str(input("Enter a new destination for position 5: "))

count = 0

print("Updated Travel Itinerary:")
for i in range(0, 5, 1):
    count = count + 1
    print(f"{count}. {travel_itinerary[i]}")
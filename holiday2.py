def hotel_cost(num_nights, price_per_night):
    return num_nights * price_per_night

def plane_cost(city_flight): # The function is defined by keyword def and is named plane_cost. It takes the parameter city_flight as input.
    flight_cost = {'Alicante': 500, 'Barcelona': 540, 'Madrid': 600}
    return flight_cost.get(city_flight, 0)

def car_rental(rental_days, daily_rental_cost):
    return rental_days * daily_rental_cost

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# User has to input required data. 
city_flight = input("Please enter your destination (Alicante, Barcelona, Madrid): ")
rental_days = int(input("Please enter the number of a car hire days (7  or 14 days): "))
duration_of_stay = int(input("Please enter the duration of stay at a hotel (7 or 14 days): "))# For calculation 'car_rental_total_cost' use 'duration_of_stay value'.
# If the user is staying 7 nights at a hotel, the rental will be 7 days. If the user stays 14 days, the rental could be 7 or 14 days.

# Prices for hotel and car rental. User can adjust these values.
price_per_night = 220
daily_rental_cost = 170

# Calculate costs using these functions:
num_nights = duration_of_stay
hotel_total_cost = hotel_cost(num_nights, price_per_night)
plane_total_cost = plane_cost(city_flight)
car_rental_total_cost = car_rental(duration_of_stay, daily_rental_cost)
total_holiday_cost = holiday_cost(hotel_total_cost, plane_total_cost, car_rental_total_cost)

# Print details about your total holiday cost.
print(f"\nInformation about your holiday in {city_flight} for {duration_of_stay} days: ")# OUTPUT => Information about your holiday in Madrid for 7 days:
print(f"Flight cost: £{plane_total_cost}")# OUTPUT => Flight cost: £600.
print(f"Hotel cost: £{hotel_total_cost}")# OUTPUT => Hotel cost: £1540.
print(f"Car rental cost: £{car_rental_total_cost}")# OUTPUT => Car rental cost: £1190.
print(f"Total holiday cost: £{total_holiday_cost}")# OUTPUT => Total holiday cost: £3330.


"""
Given 3 args. 1-an array of cities (their ints repping the miles to next city). 2-an array of positive ints repping available fuel at that city. 3-an int repping your MPG. Return the index of the valid starting city.

Input:
    cities = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0 3]
    mpg = 10
Output:
    4

** always 2+ cities
"""
import time


def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    # iterate straight through
    # the minute you get a negative number on arrival, exit
    # we start with city idx - 1
    # O(n2) --brute force
    for idx in range(len(distances)):
        print("starting loop with: ", idx)
        loop = idx
        count = 0
        arrive_with = 0
        trip_fuel = fuel[idx-1] * mpg
        while count < len(distances):
            last_idx = (loop-1) % (len(distances))
            last_city = distances[last_idx]
            arrive_with = trip_fuel - last_city

            # I need the real index
            real_idx = loop % (len(distances))
            print("current city: ", distances[real_idx])
            print("...arrived with: ", arrive_with)

            # I arrived w/negative number
            if arrive_with < 0:
                break

            # Reset the current fuel
            trip_fuel = arrive_with + (fuel[real_idx] * mpg)

            # Advance the index
            loop += 1

            # Advance the counter
            count += 1

        # my starting city == the 1st fuel I took
        if count == len(distances):
            return real_idx


def validStartingCityA(distances, fuel, mpg):
    # the O(N) time solution is to store the minumum
    # number recorded after looping through once on fuel
    # status. reason--there will always be a difference
    # in fuel and fuel used (miles traveled) that exhausts
    # our fuel number to its utmost, therefore, the min
    # number HAS to be the starting city to get us
    # around the array
    min_fuel = 0
    min_idx = 0
    c_fuel = fuel[0] * mpg
    for idx in range(1, len(distances)):
        c_fuel = c_fuel - distances[idx-1]
        if c_fuel < min_fuel:
            min_fuel = c_fuel
            min_idx = idx
        c_fuel += fuel[idx] * mpg

    return min_idx


cities = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10  # 4

cities = [10, 20, 10, 15, 5, 15, 25]
fuel = [0, 2, 1, 0, 0, 1, 1]
mpg = 20  # 1 (6)

print(validStartingCity(cities, fuel, mpg))
print(validStartingCityA(cities, fuel, mpg))

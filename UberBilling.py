'''The Uber Fare Construct

Base Fare : this is the flat fee that Uber charges for each ride, it varies according to the car category UberX, Uber Black, SUV, etc.

Cost per Minute : This is what Uber charges for every minute from the moment the ride begins. It takes into account traffic and other circumstances that can cause a ride to take longer than expected.

Cost per Mile : This is what Uber charges for every mile drive. Drivers usually take the fastest route, but when traffic or other instructions are foreseen, they will choose a different route. Uber charges for the shortest distance in a pre-quote fare.

Booking Fee : This is an extra fee that Uber charges to cover its operational costs. It is not included in Uber Black and SUV fares.

Surge Price : This is an additional multiplier that is added when there is a lot of strain in the system, basically a supply and demand function. So if you are in a surge area, your overall fee can multiply by up to x3.

Tipping : This is purely optional, while there is an Uber tipping platform, the passenger can give the driver cash at their discretion.

The Fare is calculated like this:

Base Fare + ((Cost per minute x time of the ride) + (cost per mile x ride distance) x surge boost multiplier) + tolls+booking fee = Passengers Ride Fare
Minimum Fare

There is a minimum fare rate that is set to assure a certain level of income for the Uber driver. This varies per city and is based on the above calculation being no lower than the minimum fee. If the total is lower, then you will be charged the minimum price.'''
import math

def Estimated_Fare(S, D):
    Base_fare = 42.00
    Minimum_fare = 73.50
    Fare_perminute = 2.31
    Fare_perKM = 9.45
    Distance = float(distance(S, D))
    tolls = float(Tolls(S, D))
    Estimated_Time = float(Estimated_time(S, D))
    surge_multiplier = (2, 3, 1, 1)
    fare = Base_fare + (
                (Fare_perminute * Estimated_Time) + (Fare_perKM * Distance * surge_multiplier[int(D) - 1])) + tolls
    if (fare < Minimum_fare):
        fare = Minimum_fare
    cars = ('Uber Bike', 'Uber Auto', 'Uber Mini', 'Uber Micro', 'Uber Prime')
    Booking_Fee = (5, 8, 10, 20, 0)
    for i in range(0, 5):
        print('{0} : {1}'.format(cars[i], round((fare + float(Booking_Fee[i])), 2)))

#Function to calculate Distance
def distance(S, D):
    # Distance to Airport from Airport,Beach,SuperMarket,Railway Station
    D_Airport = (0, 23, 13.6, 32.6)

    # Distance to Beach from Airport,Beach,SuperMarket,Railway Station
    D_Beach = (23, 0, 59, 32)

    # Distance to Super Market from Airport,Beach,SuperMarket,Railway Station
    D_SuperMarket = (13.6, 43, 0, 78)

    # Distance to Railway Sation from Airport,Beach,SuperMarket,Railway Station
    D_Railway = (32.6, 32, 78, 0)
    if D==1:
        return D_Airport[S-1]
    elif D==2:
        return D_Beach[S-1]
    elif D==3:
        return D_SuperMarket[S-1]
    else :
        return D_Railway[S-1]

#Function to calculate Estimated time
def Estimated_time(S, D):
    # Estimated Time for Airport from Airport,Beach,SuperMarket,Railway Station
    ET_Airport = (0, 20, 15, 50)

    # Estimated Time for Beach from Airport,Beach,SuperMarket,Railway Station
    ET_Beach = (20, 0, 90, 20)

    # Estimated Time for SuperMarket from Airport,Beach,SuperMarket,Railway Station
    ET_SuperMArket = (15, 56, 0, 182)

    # Estimated Time for Railway Station from Airport,Beach,SuperMarket,Railway Station
    ET_Railway = (49, 48, 181, 0)

    if D==1:
        return ET_Airport[S-1]
    elif D==2:
        return ET_Beach[S-1]
    elif D==3:
        return ET_SuperMArket[S-1]
    else :
        return ET_Railway[S-1]

#Function to calculate Tolls
def Tolls(S, D):
    # Tolls till Airport from Airport,Beach,SuperMarket,Railway Station
    toll_Airport = (0, 30, 10, 20)

    # Tolls till Beach from Airport,Beach,SuperMarket,Railway Station
    toll_Beach = (30, 0, 20, 0)

    # Tolls till SuperMarket from Airport,Beach,SuperMarket,Railway Station
    toll_SuperMarket = (45, 30, 0, 0)

    # Tolls till Railway from Airport,Beach,SuperMarket,Railway Station
    toll_Railway = (60, 10, 0, 0)
    if D==1:
        return toll_Airport[S-1]
    elif D==2:
        return toll_Beach[S-1]
    elif D==3:
        return toll_SuperMarket[S-1]
    else :
        return toll_Railway[S-1]

def CabSearch():
    Starting_location= input("Select the destination :\n Enter '1' for Airport \n Enter '2' for Beach \n Enter '3' for SuperMarket \n Enter '4' for Railway Station\n")
    Destination=input("Select the destination :\n Enter '1' for Airport \n Enter '2' for Beach \n Enter '3' for SuperMarket \n Enter '4' for Railway Station\n")
    if Starting_location in('1','2','3','4') and Destination in('1','2','3','4'):
        Estimated_Fare(int(Starting_location), int(Destination))
    else:
        print("No Cabs Available")

CabSearch()




from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

niye_jao = RideSharing('Niye Jao')
rahim = Rider('Rahim', 'rahim@gmail.com', 1234, 'Mohakhali', 1200)
niye_jao.add_riders(rahim)
kolimuddin = Driver('Kolim Uddin', 'kolim@gmail.com', 1256, 'Gulshan')
niye_jao.add_drivers(kolimuddin)
rahim.request_ride(niye_jao, 'Uttora', 'car')
kolimuddin.reach_destination(rahim.curren_ride)
rahim.show_current_ride()
print(niye_jao)

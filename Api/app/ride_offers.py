from datetime import datetime

class RideOffer:

    #contains the list of all ride offers
    rideoffers = []
    
    #method that allows users to create ride offers
    def create_ride_offer(self, driver_name, car_model, location, destination, cost, seats, route):
        self.id = 1

    #set a different id if items are more than one
        if len(self.rideoffers) != 0:
            self.id = len(self.rideoffers) + 1

        self.date_created = str(datetime.now())
        self.ride_offer = {

            'id':self.id,
            'Date_created':self.date_created,
            'Driver_name': driver_name,
            'Car_model':car_model,
            'Location': location,
            'Destination':destination,
            'Cost':cost,
            'Route': route
        }

        self.rideoffers.append(self.ride_offer)

        return self.ride_offer

        

        

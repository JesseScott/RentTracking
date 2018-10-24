from RentTrackers.models import LatLng


class HouseUnit:

    def __init__(self, type: str, location: LatLng, address: str, bedrooms: int, bathrooms: int, area: int,
                 parking_spots: int, smoking_allowed: bool, wheelchair_access: bool, laundry_onsite: bool):
        """
        
        :param type: the type of unit (Apartment, House, Boat) (String)
        :param location: the Latitude/Longitude of the unit (LatLng)
        :param address: the human readable address (String)
        :param bedrooms: the number of bedrooms (Integer)
        :param bathrooms: the number of bathrooms (Integer)
        :param area: the square root area of the unit (Integer)
        :param parking_spots: the number of parking spots (Integer)
        :param smoking_allowed: whether smoking is allowed (Boolean)
        :param wheelchair_access: whether there is wheelchair access (Boolean)
        :param laundry_onsite: whether there is laundry onsite (Boolean)
        """
        self.type = type
        self.location = location
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.area = area
        self.parking_spots = parking_spots
        self.smoking_allowed = smoking_allowed
        self.wheelchair_access = wheelchair_access
        self.laundry_onsite = laundry_onsite


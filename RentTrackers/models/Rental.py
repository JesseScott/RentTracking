from RentTrackers.models.HouseUnit import HouseUnit


class Rental:

    def __init__(self, url: str, id: str, city: str, price: str, house_unit: HouseUnit):
        """
        
        :param url: 
        :param id: 
        :param city: 
        :param price: 
        :param house_unit: 
        """
        self.url = url
        self.id = id
        self.city = city
        self.price = price
        self.house_unit = house_unit




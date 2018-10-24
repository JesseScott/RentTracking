

class RentalSource:

    def __init__(self, vendor_name, base_url):
        """
        :param vendor_name: the name of the Vendor (ie. Craigslist / Kijiji)
        :param base_url: the base url of the vendor website
        """
        self.vendor_name = vendor_name
        self.base_url = base_url


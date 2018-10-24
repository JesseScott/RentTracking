from RentTrackers.parsers.CraigslistParser import CraigslistParser


class ParserManager:
    """
    A Manager class for holding lists of different types/definitions of parsers
    Used within RentTrackers.RentTrackers.RentTrackers
    """

    rent_parsers = []

    def __init__(self):
        self.rent_parsers.append(CraigslistParser)

    def get_rent_parsers(self):
        return self.rent_parsers

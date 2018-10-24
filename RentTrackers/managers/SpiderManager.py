
from RentTrackers import settings


class SpiderManager:
    """
    A Manager class for holding a list of spiders
    """

    @staticmethod
    def get_spiders():
        """
        Gets the registered Spiders for Scrapy
    
        :return: settings.SPIDER_MODULES
        """
        return settings.SPIDER_MODULES

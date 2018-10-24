from scrapy.crawler import CrawlerProcess
from RentTrackers.parsers.RentParser import RentParser
from RentTrackers.spiders.CraigslistListingSpider import CraigslistListingSpider


class CraigslistParser(RentParser):
    """
    An implementation of a [RentTrackers.parsers.RentParser.RentParser] 
    Focused on Craiglist parsing
    """
    def __init__(self, location=None):
        super().__init__(location)
        self.spider = CraigslistListingSpider

    def configure(self, config):
        """
        Applies configuration to the job
        
        :param config: the config object
        :return: a configured parser
        """
        # TODO: apply configuration
        pass

    def parse(self, location):
        """
        Initializes the Spider process
        
        :param location: 
        :return: a blocking process 
        """
        # TODO: handle passing location
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        process.crawl(self.spider)
        process.start()

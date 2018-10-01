import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from RentTrackers.managers.LoggerManager import LoggerManager as logger


class BedBugRegistrySpider(scrapy.Spider):
    """
    Spider for http://bedbugregistry.com/
    """
    name = "bed_bug_registry"

    def start_requests(self):
        """
        Overridden method from scrapy.spiders.Spider
        Generates a series of requests with which to crawl over and parse
        
        :return: iterable of scrapy.http.request.Request
        """
        # this is the only active page with listings atm, search gives 500
        recent = "http://bedbugregistry.com/metro/vancouver/recent/"
        logger.debug(__name__, "Crawling {}".format(recent))
        yield scrapy.Request(url=recent, callback=self.parse)

    def parse(self, response):
        """
        Overridden method from scrapy.spiders.Spider
        Gets text response from web requests and is responsible for parsing and serializing them

        :param response: an instance of scrapy.http.response.Response 
        :return: Dictionary of parsed results
        """
        logger.debug(__name__, response)

        metro_title = response.css("p.metro_title::text")[0].extract()

        leftcol = response.css("id.leftcol").extract()

        entries = response.css("id.leftcol p").extract()
        print(entries)
        for entry in entries:
            print(entry)

        yield {
            "title": metro_title if metro_title else self.name,
            "url": response.url
        }



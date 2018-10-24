import scrapy
from scrapy.utils.markup import remove_tags

"""
KijijiSpider:
    [Outline] --    This spider hits up the first N-pages of kijijis "Room Rentals & Roomates"
                    section. There are multiple sections from which we need to scrape information.
                    It returns a json object with the title, url, price, description, location,
                    upload date, and a list of kijiji-specific attributesself.

    [TODO] --       (1) Remove hard coded URLs and the page-to-crawl number.
                        Allow for seeding from any kijiji url, up to N-pages
                    (2) Determine if kijiji html classes with strigns of numbers
                        are static features or regularly changing.
"""
pageToCrawl = 3

class KijijiSpider(scrapy.Spider):
    name = "kijiji"
    pages = []

    def start_requests(self):
        base = "https://www.kijiji.ca/b-room-rental-roommate/vancouver/c36l1700287"
        other = "https://www.kijiji.ca/b-room-rental-roommate/vancouver/page-{}/c36l1700287"
        urls = [other.format(str(i)) for i in range(1,pageToCrawl)]
        urls.insert(0,base)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.url)
        for i in response.css("div.info"):
            for j in i.css("a::attr(href)"):
                yield scrapy.Request(url="https://www.kijiji.ca" + j.extract(), callback=self.parse_unit)

    def parse_unit(self, response):
        print(response.url)
        title = response.css("h1.title-3283765216::text")[0].extract()
        price = response.css("span.currentPrice-2872355490")[0].css("span::text")[0].extract()
        location = response.css("span.address-2932131783::text").extract_first()
        description = remove_tags(response.css("div.descriptionContainer-2901313666").extract_first())
        attributes = [{attr.css("dt::text").extract_first(),attr.css("dd::text").extract_first()} for attr in response.css("dl.itemAttribute-2841032265")]
        uploadTime = response.css("div.datePosted-1350605722")[0].css("span::attr(title)").extract_first()
        if uploadTime == None:
            uploadTime = response.css("div.datePosted-1350605722")[0].css("time::attr(title)").extract_first()
        yield {
            "title": title,
            "url": response.url,
            "price": price,
            "location": location,
            "description": description,
            "attributes": attributes,
            "datetime": uploadTime
        }

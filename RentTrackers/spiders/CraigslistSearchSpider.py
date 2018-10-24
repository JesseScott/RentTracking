import os
import scrapy


class CraigslistSearchSpider(scrapy.Spider):
    name = "CraigslistSearch"

    def __init__(self):
        super().__init__()
        self.city = os.environ["CITY"]
        self.base_search_url = "https://" + self.city + ".craigslist.ca/search/apa?sort=date&"

    def start_requests(self):
        url = self.base_search_url
        yield scrapy.Request(
            url=url,
            callback=self.parse,
        )

    def parse(self, response):
        next_page =  response.xpath('//link[@rel="next"]/@href').extract_first()
        if next_page:
            yield scrapy.Request(
                url = next_page,
                callback = self.parse,
            )

        results = response.css("li.result-row")
        for r in results:
            url = r.css("a.result-title::attr(href)").extract_first()
            post_id = int(r.css("li.result-row::attr(data-pid)").extract_first())
            repost_id = r.css("li.result-row::attr(data-repost-of)").extract_first()
            yield {
                "post_id": post_id,
                "repost_id": "" if repost_id is None else int(repost_id),
                "url": url,
            }

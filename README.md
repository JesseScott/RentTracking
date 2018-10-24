# Rent Trackers
A collection of web scrapers for use in tracking rental prices.

Makes use of the  [Scrapy]( https://github.com/scrapy/scrapy) web crawling and scraping framework.

Please scrape responsibly.

## Running
- `run_crawl.sh`: Run a full crawl.
- `test.sh`: Runs scrapers over sample data.

## Scrapers

### Craigslist
Scraper output can be found in `output/<TIMESTAMP>/cl_output.json`
#### Output Schema

```
Format
    field_name: type {set of possible values if finite}

The Option type indicates that a field may not be present in the output.

{
    post_id:        Integer,
    post_time:      Timestamp,
    update_time:    Optin[Timestamp],
    url:            String,
    latitude:       Option[String],
    longitude:      Option[String],
    price:          Option[Integer],
    address:        Option[String],
    area:           Option[Integer],
    bathrooms:      Option[String]      {"1", "1.5", "2", ..., "8.5", "9+", "shared", "split"},
    bedrooms:       Option[Integer]     {1, 2, ..., 8},
    is_no_smoking:  Option[Boolean],
    is_furnished:   Option[Boolean],
    dogs_allowed:   Option[Boolean],
    cats_allowed:   Option[Boolean],
    housing_type:   Option[String]
        {"apartment", "condo", "cottage/cabin", "duplex", "flat", "house", "in-law",
         "loft", "townhouse", "manufactured", "land", "assisted living"},
    laundry_type:   Option[String]
        {"w/d in unit", "w/d hookups", "laundry in bldg", "laundry on site", "no laundry on site"},
    parking_type:   Option[String]
        {"carport", "attached garage", "detached garage", "off-street parking",
         "street parking", "valet parking", "no parking"},
    is_wheelchair_accessible: Option[Boolean],
}
```

### TODO
- Dockerize for portability.
- Add additional data sources.

## Disclaimer
This project is for non-commercial use.

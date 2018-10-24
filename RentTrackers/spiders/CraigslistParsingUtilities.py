import re


def extract_area(s) -> dict:
    """
    Extracts area from a string like: '1br 1ba 600'. Last number is area. May not be present.
    :param s: the string to parse
    :return: dict containing an area field if present.
    """
    match = re.search(r'\d+$', s)
    if match:
        area = match.group()
        return {"area": int(area)}
    else:
        return {}


def extract_bedrooms(s) -> dict:
    """
    Extracts # of bedrooms from a string like: '1br 1ba 600'. May not be present.
    :param s: the string to parse
    :return: dict containing a bedrooms field if present.
     """
    match = re.search(r'\d+br', s)
    if match:
        bedrooms = match.group()[:-2]
        return {"bedrooms": int(bedrooms)}
    else:
        return {}


def extract_bathrooms(s) -> dict:
    """
    Extracts bathroom type from a string like: '1br 1ba 600' or '1br splitba 600'. May not be present.
    :param s: the string to parse
    :return: dict containing a bathrooms field if present.
    """
    num_match = re.search(r'\d(\.\d)?ba', s)
    if num_match:
        bathrooms = num_match.group()[:-2]
        return {"bathrooms": bathrooms}
    type_match = re.search(r'[a-z]+ba', s)
    if type_match:
        bathrooms = type_match.group()[:-2]
        return {"bathrooms": bathrooms}
    return {}


def extract_price(response) -> dict:
    """
    Extracts price from a string like '$1000'. Prices are always integers. May not be present.
    :param response: a scrapy.http.response.Response
    :return: dict containing a price field if present.
    """
    price = response.css('span.price::text').extract_first()
    if price:
        price = int(price[1:])
        return {"price": price}
    else:
        return {}


def extract_address(response) -> dict:
    """
    Extracts address string from a response. May not be present.
    :param response: a scrapy.http.response.Response
    :return: dict containing an address field if present.
    """
    address_option = response.css("span.postingtitletext small::text").extract_first()
    # Addresses are formatted as " (ADDRESS)"
    if address_option is None:
        return {}
    else:
        clean_address = address_option.lstrip(" (").rstrip(' )')
        return {"address": clean_address}


def extract_bdrs_bths_area(response) -> dict:
    """
    Extracts bedrooms, bathrooms and area values from a response if they are present.
    :param response: a scrapy.http.response.Response
    :return: dict containing bedrooms, bathrooms and area fields if they are present.
    """
    raw_bdrs_bths_area = response.css("p.attrgroup span.shared-line-bubble b::text").extract()
    bdrs_bths_area = " ".join(raw_bdrs_bths_area).lower()

    results = {}
    results.update(extract_area(bdrs_bths_area))
    results.update(extract_bathrooms(bdrs_bths_area))
    results.update(extract_bedrooms(bdrs_bths_area))
    return results


def extract_lat_long(response) -> dict:
    """
    Extracts latitude and longitude values.
    :param response: a scrapy.http.response.Response
    :return: dict containing latitude and longitude fields.
    """
    latitude = response.css("#map::attr(data-latitude)").extract_first()
    longitude = response.css("#map::attr(data-longitude)").extract_first()
    return {
        "latitude": latitude,
        "longitude": longitude
    }


def extract_update_time(response) -> dict:
    """
    Extracts post update time. May not be present.
    :param response: a scrapy.http.response.Response
    :return: dict containing an update_time field if present.
    """
    results = {}
    update_time = response.xpath("//p[starts-with(text(), 'updated')]/time/@datetime").extract_first()
    if update_time:
        results["update_time"] = update_time
    return results


def extract_attributes(response) -> dict:
    """
    Extract attributes from a Craigslist listing.
    :param response: a scrapy.http.response.response
    :return: dict containing data from a Craigslist listing.
    """
    results = {}
    results.update(extract_price(response))
    results.update(extract_address(response))
    results.update(extract_lat_long(response))
    results.update(extract_bdrs_bths_area(response))
    results.update(extract_update_time(response))
    results.update(extract_unstructured_attributes(response))
    return results


VALID_HOUSING_TYPES = {
    "apartment",
    "condo",
    "cottage/cabin",
    "duplex",
    "flat",
    "house",
    "in-law",
    "loft",
    "townhouse",
    "manufactured",
    "land",
    "assisted living",
}

VALID_LAUNDRY_TYPES = {
    "w/d in unit",
    "w/d hookups",
    "laundry in bldg",
    "laundry on site",
    "no laundry on site",

}

VALID_PARKING_TYPES = {
    "carport",
    "attached garage",
    "detached garage",
    "off-street parking",
    "street parking",
    "valet parking",
    "no parking",
}


def extract_unstructured_attributes(response) -> dict:
    """
    Extract values stored in attrgroup tags from a Craigslist listing.
    :param response: a scrapy.http.response.response
    :return: dict containing unstructured attribute data.
    """
    attrs = response.css("p.attrgroup span::text").extract()
    attrs = [a.lower() for a in attrs]
    results = {}
    for a in attrs:
        if a in VALID_HOUSING_TYPES:
            results["housing_type"] = a
            continue
        if a in VALID_LAUNDRY_TYPES:
            results["laundry_type"] = a
            continue
        if a in VALID_PARKING_TYPES:
            results["parking_type"] = a
            continue
        if a is "no smoking":
            results["is_no_smoking"] = True
            continue
        if a is "wheelchair accessible":
            results["is_wheelchair_accessible"] = True
            continue
        if a is "furnished":
            results["is_furnished"] = True
            continue
        if a is "dogs are ok":
            results["dogs_allowed"] = True
            continue
        if a is "cats are ok":
            results["cats_allowed"] = True

    return results

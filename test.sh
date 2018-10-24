#!/usr/bin/env bash
now=`date +%Y-%m-%d.%H:%M:%S`

export TEST=true
export CL_CRAWL_SET_LOCATION=dummy

scrapy crawl --set=DOWNLOAD_DELAY=0 CraigslistListings
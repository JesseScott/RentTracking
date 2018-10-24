#!/usr/bin/env bash
set -e

now=`date +%Y-%m-%d.%H:%M:%S`
mkdir output/${now}
export CITY=vancouver

export CL_CRAWL_SET_LOCATION=output/${now}/cl_crawl_set.json

CL_CRAWL_OUTPUT_LOCATION=output/${now}/cl_output.json
cl_search_logfile=output/${now}/cl_search_log.txt
cl_listing_logfile=output/${now}/cl_listing_log.txt

scrapy crawl --set=DOWNLOAD_DELAY=0.25 --logfile=${cl_search_logfile}  --loglevel=INFO -o ${CL_CRAWL_SET_LOCATION} CraigslistSearch
scrapy crawl --set=DOWNLOAD_DELAY=2 --logfile=${cl_listing_logfile} --loglevel=INFO -o ${CL_CRAWL_OUTPUT_LOCATION} CraigslistListings
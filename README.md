# Crawler
Scrapy for crawling site.

# Requirements
Install [Homebrew](http://brew.sh) on your computer if you haven't already.

## Setup
Mac comes with Ruby and Python 2.7.5 out of the box.  You should not need to install ruby.  However do install the latest python from brew.  It gives us the latest python 2.7.6, pip, and others.

Install ruby.

    $ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

Install python.

    $ brew install python

Install virtualenv.

    $ pip install virtualenv

Clone repo.

    $ cd src
    $ git clone https://github.com/5amfung/qocrawler.git
    $ cd qocrawler

Install dependency.

    $ mkdir env
    $ virtualenv env
    $ source ./env/bin/activate
    $ pip install -r requirements.txt
    $ deactivate
    
    
# How to Start Crawling

The crawler is set up to stop after about 20 urls.  So run the following to see how it works.

    $ scrapy crawl yelp
    
The crawler is set up to stop after about downloading 20 urls and cached the downloaded content locally during development.  Disable them for production.

    $ scrapy crawl yelp --set CLOSESPIDER_PAGECOUNT=0 --set HTTPCACHE_ENABLED=False --loglevel=INFO

You may pause (ctrl-c) and resume by persisting the state.  Just add ```-s JOBDIR``` to the command line.

    $ mkdir jobs
    $ scrapy crawl yelp --set CLOSESPIDER_PAGECOUNT=0 --set HTTPCACHE_ENABLED=False --loglevel=INFO -s JOBDIR=jobs/yelp-1

To resume, run this again.

    $ scrapy crawl yelp --set CLOSESPIDER_PAGECOUNT=0 --set HTTPCACHE_ENABLED=False --loglevel=INFO -s JOBDIR=jobs/yelp-1
    
    
        
    

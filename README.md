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

For development and testing right now, the yelp crawler is set up to crawl just a few sites.

    $ cd qocrawl
    $ source ./env/bin/activate
    $ scrapy crawl testyelp
    
For crawling a big site, the crawling cannot complete in a short period of time.  You may pause (ctrl-c) and resume.

    $ make jobs
    $ scrapy crawl bigsitespider -s JOBDIR=jobs/bigsitespider-1

To resume, run this again.

    $ scrapy crawl bigsitespider -s JOBDIR=jobs/bigsitespider-1
    
    
        
    

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import scrapy

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
import html2text
import scrapy
import uuid
from scrapy.http import Request
from datetime import datetime


class ToScrapeSpiderXPath(CrawlSpider):
    name = 'crawl_ebook'
    start_urls = [
                    'https://www.ebooks.com/subjects/body-mind-spirit/',
                ]
    rules = (
    #     # Extract links for next pages

        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//div[@class= "paging bottom floatLeft"]')), callback='parse_url_contents',
         follow=True),)

    def parse_url_contents(self, response):
            yield {
                    'doc_id': uuid.uuid4().hex,
                    'url': response.url,
                    'raw_content': response.text,
                    'timestamp_crawl': datetime.now(),
                }

from urllib.parse import urljoin

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from scrapy.spiders import CrawlSpider, Rule
from ..items import ZebrsItem


class ZebrsImgSpider(CrawlSpider):
    name = "zebrs_img"
    allowed_domains = ['www.zebrs.com']
    # allowed_domains = ["www.dns-shop.ru"]
    # allowed_domains = ["www.kinopoisk.ru"]
    # allowed_domains = ["www.citilink.ru"]
    start_urls = ['https://www.zebrs.com/categories/smartphones']
    # start_urls = ["https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/"]
    # start_urls = ["https://www.kinopoisk.ru/lists/movies/top250/"]
    # start_urls = ["https://www.citilink.ru/catalog/noutbuki"]

    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths=('//div[@class="position-relative mb-4 teaser-item-div"]')),
    #          callback='parse_item',
    #          follow=True),
    # )

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='position-relative mb-4 teaser-item-div']/a")),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//a[@rel='next']")))
    )

    # rules = (Rule(LinkExtractor(restrict_xpaths='//a[@class="catalog-product__name ui-link ui-link_black"]'), callback="parse_item", follow=True),)
    # rules = (Rule(LinkExtractor(restrict_xpaths='//div[@data-test-id="movie-list-item"]/a'), callback="parse_item", follow=True),)
    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths='//div[@class="e1ex4k9s0 app-catalog-1bogmvw e1loosed0"]'),
    #          callback="parse_item",
    #          follow=True),)

    def parse_item(self, response):
        # print(response.url)
        loader = ItemLoader(item=ZebrsItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)

        loader.add_xpath('name', '//h1/text()')
        price_text_danger = response.xpath('//div[@class="me-2 product-price"]/span[@class="text - danger"]/text()').get()
        if price_text_danger:
            loader.add_value('price', price_text_danger)
        else:
            loader.add_xpath('price', '//div[@class="me-2 product-price"]/text()')

        relative_image_urls = response.xpath(
            '//div[@class="text-center d-none d-sm-block dsktp-zoomer"]/ul/li/img/@src').getall()
        absolute_image_urls = [urljoin("https://www.zebrs.com", img_url) for img_url in relative_image_urls]
        loader.add_value('image_urls', absolute_image_urls)

        yield loader.load_item()

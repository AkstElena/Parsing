import scrapy


class WikimediaSpider(scrapy.Spider):
    name = "wikimedia"
    # allowed_domains = ["commons.wikimedia.org"]
    start_urls = ["https://commons.wikimedia.org/wiki/Category:Featured_pictures_on_Wikimedia_Commons"]

    # start_urls = ["https://commons.wikimedia.org/"]

    def parse(self, response):
        for image_page in response.xpath('//*[@id="mw-category-media"]/ul/li/div/a/@href').extract():
            yield scrapy.Request(response.urljoin(image_page), self.parse_image_page)

    def parse_image_page(self, response):
        full_image_url = response.xpath('//*[contains(@class, "fullImageLink")]/a/@href').extract_first()
        if full_image_url:
            yield scrapy.Request(response.urljoin(full_image_url), self.save_image)

    def save_image(self, response):
        filename = response.url.split('/')[-1]
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.body)

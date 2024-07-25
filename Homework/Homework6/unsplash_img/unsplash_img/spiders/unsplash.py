import scrapy


class UnsplashSpider(scrapy.Spider):
    name = "unsplash"
    # allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com"]

    def parse(self, response):
        for image_page in response.xpath('//*[@itemprop="contentUrl"]/@href').extract():
            yield scrapy.Request(response.urljoin(image_page), self.parse_image_page)

    def parse_image_page(self, response):
        full_image_url = response.xpath('//*[@class="wdUrX"]/img[2]/@src').extract_first()
        if full_image_url:
            yield scrapy.Request(full_image_url, self.save_image)
            # print(full_image_url)

    def save_image(self, response):
        filename = response.url.split('/')[-1][0:20] + ".jpg"
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.body)

import scrapy


class FinanceSpiderSpider(scrapy.Spider):
    name = "finance_spider"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/trending-tickers"]

    def parse(self, response):
        tickers = response.xpath("//table/tbody/tr")
        for ticker in tickers:
            name = ticker.xpath(".//td[1]/a/text()").get()
            link = ticker.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_ticker, meta={'name': name})

    def parse_ticker(self, response):
        name = response.request.meta['name']
        rows = response.xpath("//*[@id='nimbus-app']/section/section/section/article/section[1]")
        for row in rows:
            # date = row.xpath(".//td/text()").get()
            # open = float(row.xpath(".//td[2]/text()").get())
            # high = float(row.xpath(".//td[3]/text()").get())
            # low = float(row.xpath(".//td[4]/text()").get())
            # close = float(row.xpath(".//td[5]/text()").get())
            # adj_close = float(row.xpath(".//td[6]/text()").get())
            # volume = float(row.xpath(".//td[7]/text()").get())
            name_full = row.xpath(".//h1/text()").get()

            yield {
                'name': name,
                'name_full': name_full
                # 'date': date,
                # 'open': open,
                # 'high': high,
                # 'low': low,
                # 'close': close,
                # 'adj_close': adj_close,
                # 'volume': volume

            }

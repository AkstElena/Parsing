import scrapy


class PopulationSpiderSpider(scrapy.Spider):
    name = "population_spider"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        rows = response.xpath('//*[@id="example2"]/tbody/tr')
        for row in rows:
            country = row.xpath(".//td/a/text()")[0].get(),
            # 'Population (2023)': int(columns[1].replace(',', '').strip()),
            # 'Yearly Change, %': float(columns[2].replace('%', '').strip()),
            # 'Net Change': int(columns[3].replace(',', '').strip()),
            # 'Density (P/Km²)': int(columns[4].replace(',', '').strip()),
            # 'Land Area (Km²)': int(columns[5].replace(',', '').strip()),
            # 'Migrants (net)': int(columns[6].replace(',', '').strip()),
            # 'Fert. Rate': float(columns[7].replace('N.A.', '0').strip()),
            # 'Med. Age': int(columns[8].replace('%', '').replace('.', '').strip()),
            # 'Urban Pop (%)': int(error_find(columns, 9).replace('%', '').replace('N.A.', '0').strip()),
            # 'World, %': float(error_find(columns, 10).replace('%', '').strip())
            # country_name = row.xpath(".//td[1]//a/text()").get()
            # membership = row.xpath('.//td[contains(.,"UN")]/text()').get()
            # sovereignty_dispute_info = row.xpath('.//td[3]/text()').get()
            # country_status = row.xpath('.//td[4]/text()').get()
            link = row.xpath(".//td/a/@href").get()
            yield response.follow(url=link, callback=self.parse_country,
                                  meta={
                                      'country_name': country,
                                      # 'membership': membership,
                                      # 'sovereignty_dispute_info': sovereignty_dispute_info,
                                      # 'country_status': country_status
                                  })

    def parse_country(self, response):
        rows = response.xpath("/html/body/div[2]/div[4]/div/div/div[5]/table/tbody")
        for row in rows:
            year = response.xpath('.//td/text()')[0].get()
            country = response.request.meta['country']
            # country_name = response.request.meta['country_name']
            # membership = response.request.meta['membership']
            # sovereignty_dispute_info = response.request.meta['sovereignty_dispute_info']
            # country_status = response.request.meta['country_status']
            yield {
                'country_name': country,
                'year': year.strip()
                # 'country_name': country_name.strip() if country_name else 'Zambia',
                # 'capital': capital.strip() if capital else '',
                # 'membership': membership.strip() if membership else '',
                # 'sovereignty_dispute_info': sovereignty_dispute_info.strip() if sovereignty_dispute_info else '',
                # 'country_status': country_status.strip() if country_status else ''
            }

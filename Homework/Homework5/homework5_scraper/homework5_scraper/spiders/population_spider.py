import scrapy


class PopulationSpiderSpider(scrapy.Spider):
    name = "population_spider"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        countries = response.xpath('//td/a')
        for row in countries:
            country = row.xpath(".//text()").get()
            link = row.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.parse_country,
                                  meta={
                                      'country': country,
                                  })

    def parse_country(self, response):
        country = response.request.meta['country']
        result_dict = {'country': country}

        hist_population = response.xpath("//div[@class='table-responsive'][1]/table/tbody/tr")
        hist_population_dict = {}
        for row in hist_population[0:3]:
            year = row.xpath('.//td[1]/text()').get()
            population = int(row.xpath('.//td[2]//text()').get().replace(',', ''))
            hist_population_dict[year] = population
        result_dict['population history'] = hist_population_dict

        future_population = response.xpath("//div[@class='table-responsive'][2]/table/tbody/tr")
        future_population_dict = {}
        for row in future_population[4:6]:
            year = row.xpath('.//td[1]/text()').get()
            population = int(row.xpath('.//td[2]//text()').get().replace(',', ''))
            future_population_dict[year] = population
        result_dict['population forecast'] = future_population_dict

        cities = response.xpath("//div[@class='table-responsive'][3]/table/tbody/tr")
        cities_dict = {}
        for city in cities[0:3]:
            city_name = city.xpath('.//td[2]/text()').get()
            population = int(city.xpath('.//td[3]/text()').get().replace(',', ''))
            cities_dict[city_name] = population
        result_dict['cities'] = cities_dict

        yield result_dict

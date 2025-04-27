import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'divan_lighting.csv',
        'FEED_EXPORT_FIELDS': ['name', 'price', 'link'],  # Порядок колонок
        'CONCURRENT_REQUESTS': 2,
        'DOWNLOAD_DELAY': 1,
        'USER_AGENT': 'Chrome/91.0.4472.124'
    }

    def parse(self, response):
        # Парсим товары на текущей странице
        for product in response.css('div._Ud0k'):
            yield {
                'name': product.css('div.lsooF span::text').get().strip(),
                'price': product.css('div.pY3d2 span::text').get().replace(' ', '') if product.css('div.pY3d2 span') else 'Нет цены',
                'link': response.urljoin(product.css('a::attr(href)').get())
            }

        # Обрабатываем пагинацию
        next_page = response.css('a[data-testid="pagination-next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

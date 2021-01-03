import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from imdb.items import ImdbItem


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    # start_urls = ['https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']
    # imdb_item = ImdbItem()

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating', headers={
            'User-Agent': self.user_agent
        })
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3/a'), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[1]"), process_request='set_user_agent'),
    )

    def set_user_agent(self, request, scrapy):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        # yield {
        #     'title' : response.xpath("normalize-space(//div[@class='title_wrapper']/h1/text())").get(),
        #     'realease' : response.xpath("//div[@class='title_wrapper']/h1/span/a/text()").get(),
        #     'rating' : response.xpath("//span[@itemprop='ratingValue']/text()").get(),
        #     'genre' : response.xpath("//div[@class='subtext']/a[1]/text()").get(),
        #     'duration' : response.xpath("normalize-space(//div[@class='subtext']/time/text())").get(),
        #     'url' : response.url
        # }
        
        title = response.xpath("normalize-space(//div[@class='title_wrapper']/h1/text())").get(),
        realease = response.xpath("//div[@class='title_wrapper']/h1/span/a/text()").get(),
        rating = response.xpath("//span[@itemprop='ratingValue']/text()").get(),
        genre = response.xpath("//div[@class='subtext']/a[1]/text()").get(),
        duration = response.xpath("normalize-space(//div[@class='subtext']/time/text())").get(),
        url = response.url

        imdb_item = ImdbItem(
            title = title,
            realease = realease,
            rating = rating,
            genre = genre,
            duration = duration,
            url = url
        )

        yield imdb_item
        

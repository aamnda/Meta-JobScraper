import scrapy

class PostsSpider(scrapy.Spider):
    name = "jobs"

    start_urls = [
        'https://www.metacareers.com/jobs'
    ]

    def parse(self, response):
        for job in response.css('div._af0h'):
            yield{
                'title': job.css('._8sef div::text')[0].get(),
                'location': job.css('._8sef div::text')[1].get(),
                'AreaOfWork': job.css('._8sef div::text')[2].get(),
                'category': job.css('._8sef div::text')[3].get()
            }
        next_page = response.css('._8se3 a::attr(href)')[0].get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            

            
import scrapy
from scrapy.crawler import CrawlerProcess


class TaxCrawler(scrapy.Spider):
    name = 'masothuevn'
    start_urls = ['https://masothue.vn/']
    page_index = 1
    previous_page = None

    def parse(self, response):
        for ref_link in response.css('aside li.cat-item a::attr(href)').extract():
            yield response.follow(ref_link, callback=self.parse_province)

    def parse_province(self, district_response):
        for ref_link in district_response.css('aside li.cat-item a::attr(href)').extract():
            yield district_response.follow(ref_link, callback=self.parse_district)

    def parse_district(self, ward_response):
        # print("previous_page", TaxCrawler.previous_page)
        # print("current_page", ward_response.request.url)

        if TaxCrawler.previous_page is None or TaxCrawler.previous_page == ward_response.request.url:
            company_list = ward_response.css('h3 a::attr(href)').extract()
            for content_link in company_list:
                yield ward_response.follow(content_link, callback=self.parse_content)

            if company_list:
                TaxCrawler.page_index += 1
                current_page = ward_response.request.url

                if '=' in current_page:
                    next_page = current_page.split('=')[0] + '=' + str(TaxCrawler.page_index)
                else:
                    next_page = ward_response.request.url + '?page=' + str(TaxCrawler.page_index)

                TaxCrawler.previous_page = next_page

                yield ward_response.follow(next_page, callback=self.parse_district)

    def parse_content(self, response):
        content_lst = response.css('table.table-taxinfo th::text, td::text, span a::text, td a::text, td strong::text,'
                                   ' td em::text').extract()
        content_str = '|'.join(content_lst)

        yield {
                'title': response.css('header h1::text').extract_first(),
                'link': response.request.url,
                'content': content_str
        }


if __name__ == '__main__':
    process = CrawlerProcess({
                    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                    'FEED_FORMAT': 'jl',
                    'FEED_URI': 'companies'
                })

    process.crawl(TaxCrawler)
    process.start()  # the script will block here until the crawling is finished
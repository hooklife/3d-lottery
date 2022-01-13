import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    index = 160
    start_urls = ['http://kaijiang.zhcw.com/zhcw/inc/3d/3d_wqhg.jsp?pageNum={}'.format(index)]

    custom_settings = {
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY':1,
        'DOWNLOAD_DELAY':65,
        'AUTOTHROTTLE_DEBUG':True,
        'AUTOTHROTTLE_TARGET_CONCURRENCY':1,
        'CONCURRENT_REQUESTS_PER_DOMAIN':1
    }

    def parse(self, response):
        node_list = response.xpath("//tr")
        node_list.pop(0)
        node_list.pop(0)
        node_list.pop()
        for node in node_list:
            yield {
                "date": node.xpath("./td[1]/text()").extract_first(),
                "issue": node.xpath("./td[2]/text()").extract_first(),
                "blue1": node.xpath("./td[3]/em[1]/text()").extract_first(),
                "blue2": node.xpath("./td[3]/em[2]/text()").extract_first(),
                "blue3": node.xpath("./td[3]/em[3]/text()").extract_first()
            }

        self.index += 1
        next_url = 'http://kaijiang.zhcw.com/zhcw/inc/3d/3d_wqhg.jsp?pageNum={}'.format(self.index)
        yield scrapy.Request(url=next_url, callback=self.parse)

import scrapy
from lxml import etree
from popular.items import PopularItem


class PopularSpider(scrapy.Spider):
    name = "popular"
    allowed_domains = ["github.com"]
    start_urls = [
        "https://github.com/trending"
    ]

    def parse(self, response):
        item = PopularItem()
        pathToItem = {
            'author': '//span[@class="text-normal"]/text()',
            'title': '//h3//a/text()',
            'description': '//p[@class="col-9 d-inline-block text-gray m-0 pr-4"]//text()',
            'language': '//span[@itemprop="programmingLanguage"]/text()',
            'star': '//div[@class="f6 text-gray mt-2"]/a[1]/text()',
            'network': '//div[@class="f6 text-gray mt-2"]/a[2]/text()',
            'todayStar': '//span[@class="d-inline-block float-sm-right"]/text()',
        }

        filename = response.url.split("/")[-2] + '.html'
        nodes = response.xpath('//ol[@class="repo-list"]//li').extract()
        for node in nodes:
            tree = etree.HTML(node)
            for key in pathToItem:
                result = tree.xpath(pathToItem[key])
                item[key] = ''.join(list(map((lambda x: x.strip().
                    replace(' /', '').replace(' stars today', '')), result)))
            print(item)
            yield item

        with open(filename, 'wb') as f:
            f.write(response.body)

import scrapy

class EbookSpider(scrapy.Spider):
    name  =  "ebook"
    
    start_urls = ["https://books.toscrape.com/"]
    
    def parse(self, response):
        #print("MY RESPONSE : ", response)
        print("MY PARSE ")        
        # print(response.css("h3 a::text").get()) #get turns into str
        ebooks = response.css("article")
        
        for ebook in ebooks:            
            title = ebook.css("a::text").get()
            price = ebook.css("p.price_color::text").get()
            stock = ebook.css("p.instock.availability::text").getall()
            stock = ''.join(stock).strip()
            #print(title, price, stock)
            yield {
                "title" : title,
                "price" : price,
                "stock" : stock
            }
            
from scrapy import cmdline


cmdline.execute("scrapy crawl tujia -o info.csv -t csv".split())
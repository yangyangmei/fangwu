# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import json
# from fangwu.settings import proxyServer
# from fangwu.settings import proxyAuth
from fangwu.settings import proxyMeta

class FangwuDownloaderMiddleware(object):

    def process_request(self, request, spider):
        '''对request对象加上proxy'''
        # 使用购买的代理
        # request.meta["proxy"] = "http://" + proxyServer
        # request.headers["Proxy-Authorization"] = proxyAuth
        request.meta["proxy"] = proxyMeta

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        if str(response.status).strip() != '200':
            # 使用购买的代理
            # request.meta["proxy"] = "http://" + proxyServer
            # request.headers["Proxy-Authorization"] = proxyAuth
            print(response.text)
            print('异常状态码==' + str(response.status))
            request.meta["proxy"] = proxyMeta
            return request
        else:
            res = json.loads(response.text)
            if(str(res.get("errorCode")) == '999'):
                print("截取了一个999")
                request.meta["proxy"] = proxyMeta
                return request


        return response

    def process_exception(self, request, exception, spider):
        # 使用购买的代理
        # request.meta["proxy"] = "http://" + proxyServer
        # request.headers["Proxy-Authorization"] = proxyAuth
        request.meta["proxy"] = proxyMeta

        return request
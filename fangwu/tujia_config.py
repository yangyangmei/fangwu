from fangwu.common import *

# 途家列表页请求信息
# tujia_url = 'https://mpclient.tujia.com/mpsearch/searchhouse?_fasTraceId='+getrandomstr()
tujia_url = 'https://m.tujia.com/bingo/h5/search/searchhouse/bnb?_apitsp='+current_timestr13()+'&_fasTraceId='+getrandomstr()
tujia_header = {
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "X-TJP": "23",
                    "X-TJCH":"32",
                    "X-TJTS":str(int(round(time.time()))),
                    "X-TJH":"68677137099d5b06165a3813d88a79b5bd01c463",
                    "T-INFO":"z70bYHnr7X+sv/vayOPiZO4lTTZYeWynGiTfgo+aSuw=",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Host": "m.tujia.com",
                    "Referer": "https://m.tujia.com/hotel_jinan/?ssr=off",
                    "User-Agent": 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
                    "LL-INFO":"wprDtcOLwqEDXxBNw7wDwr7Dv2PDsxcXwrnClMKiKxJQBlHDtcKfwr1ic8OpC8OMw5BpOcOkw7MFeVd0UnVEwoYbwqJ8NsO3w5oawpLDu8KZbMOTZ8OAw7jDnsKtw4EpG0fDkTjCs8O+CTbDpMOKwqvDk3zCpkExw7Y3w4HDrMKEGMOHJMKzOy/Ck8OKw6bCrsK7w6t9w5LDrFBBw6srKsONQ8OJwqYmHkR0w4rDiMOeAMO5QHvDjsO8wrLCm8OwwoDDrWPChsOCwrTChsK8IsOIwq7DgWU3wo7CqsOlw77CoAXCii5fwoPCrsKdbCApfADDo0TCunc8wpbCpcOVG8KdVMKMAMKDwptdwrZ9wo/Ch8KvUCIJVFbDsQHCt8OXKcOgLMKVwpYZwobDuRBXwrLDmsOOw7LCmV0OH8KUw6Rlwp7CnMKewobCqiPCtMOfwqoiwrjCrMO2Pi0aVsOTw7t3ERPCvnfCt8KtXMObFsOUw5ApJcKNXsK7OzZ8DzUwCcKBwqxWYnbCthPCt8OaTcO1w4YFScOVQsKXw7XCvB3Dunw4FcOxw77DocOKV3XDh3Edwq0AByAjd8KIw4wswr3Du8OGccKnwpc4CBJowqteDMOqwqzDr8OZIsKtTVHClzQNwp5lw6pUYcOow6s0Ikg2eMKRw5chZDvDjFkdK8KPb8OXw6fDuVPDrcKxVDRcB8OPwr1ZBcKdWy5NwobCm3QEwoY2w7x7LwTCr8O8w5DDqMOqwq3CpsOMY8Kiw65ow5VhQsOGwo/Cr8OsLzcXw6o/wpZFw6DCm1fCmwjDscOfw7MSKwp9wpfDsjPCh3t4QMK/wrPCgBHCrcOhwqXDqcOVw4QNwrnCsQJGw7Jre15jNsK8I0/CokEmKyDCl8Olw47CoMKOw70cwp9pU8OsNwDCv8Kcw58uwpPCnMOjYMK/wrk4w4jDmkBoamHCsz/Cr8OJwqPCisK/w4sxw408McKawpHCucKZPFTCscO/XcOzIMKAw4w2WTo3wo85cGNyFFjCnUEGwqUKwrBZNMK8wqhSEHMNwow8w70QdMOrIHXCrsK9w5QHw5cGIcKm",

                    "Origin": "https://m.tujia.com",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    }

# 途家详情请求信息 POST
tujia_detail_url = 'https://mpclient.tujia.com/mphouse/gethouse?_fasTraceId='+getrandomstr()

tujia_detail_header = {"Accept": "*/*",
                       "Accept-Encoding": "gzip, deflate, br",
                       "Accept-Language": "zh-cn",
                       "Connection": "keep-alive",
                       "Content-Type": "application/json",
                       "Host": "mpclient.tujia.com",
                       "Referer": "https://servicewechat.com/wx5df0be7c6bb02397/232/page-frame.html",
                       "User-Agent": getrandom_useragent(),
                       "X-Tingyun-Id": "-EoKhdMl0Dc;r=192834425",
                       "mpVersion": "5",
                       "openId": "o3aH50OjFJAWX1H_1Gl9Ha8WjERk",
                       "userId": "","userToken": "",
                       "wrapperId": "waptujia005",}



# 根据房东获取房源
tujia_fangdong_url = 'https://mpclient.tujia.com/mpsearch/searchhousebyhotel?_fasTraceId='+getrandomstr()

tujia_fangdong_header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Length": "49","Content-Type": "application/json","Host": "mpclient.tujia.com","Referer": "https://servicewechat.com/wx5df0be7c6bb02397/232/page-frame.html","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c30) NetType/WIFI Language/zh_CN","X-App-Client": "LON=116.88980102539062;LAT=36.62954330444336","X-Tingyun-Id": "-EoKhdMl0Dc;r=193707016","mpVersion": "5","openId": "o3aH50OjFJAWX1H_1Gl9Ha8WjERk","userId": "118970947","userToken": "84608dc1-6bed-4fd2-8216-5f2e97983cd0","wrapperId": "waptujia005",}

tujia_fangdong_formdata = {
 "hotelId": "2889588",
 "pageSize": 20,
 "pageIndex": 0
}

# uniteID ,hotleID,


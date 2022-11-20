import requests
import sys
import time
import os


filename = "data.csv"
headers = {
    'Host': 'www.mohurd.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def printList(dataList: list):
    for item in dataList:
        print(item)


def save(dataList: list, page: int):
    data = []
    for item in dataList:
        # item
        title = item['title']
        content = item['content']
        url = item['url']
        unit = item['publishUnit']
        try:
            content = content.replace("<html>", "")
            content = content.replace("<body>", "")
            content = content.replace("<head>", "")
            content = content.replace("</head>", "")
            content = content.replace("<p style=\"text-align: justify;\">", "")
            content = content.replace("<p>", "")
            content = content.replace("</html>", "")
            content = content.replace("</p>", "")
            content = content.replace("</body>", "")
            content = content.replace("<hr>", "")
            content = content.replace("<hr/>", "")
            content = content.replace("<br>", "")
            content = content.replace("<br/>", "")
            content = content.replace("&nbsp;", "")
            wdata = "{0}\n{1}\n{2}\n{3}\n".format(title, url, unit, content)
            wdata = wdata + "=" * 100
            wdata = wdata + "\n"
            data.append(wdata)
        except:
            print(title, url)

    with open(filename, mode='a+', encoding='utf-8') as fpw:
        fpw.writelines(data)
    print("第{0}页爬取成功！".format(page))


def run(current=1):
    data = {
        'oc': 7,
        'bt': 2,
        'lt': 1,
        'pageSize': 30,
        'currentPageNum': current
    }
    url = 'https://www.mohurd.gov.cn/dynamic/document/search'
    response = requests.post(url=url, data=data, headers=headers)
    if response.status_code != 200:
        print("请求失败！")
    else:
        res_json = response.json()
        if 'data' in res_json:
            # print(res_json['data'])
            if 'total' in res_json['data']:
                print("Total: {}".format(res_json['data']['total']))
            if 'list' in res_json['data']:
                # print(res_json['data']['list'])
                # printList(res_json['data']['list'])
                save(dataList=res_json['data']['list'], page=current)


if __name__ == '__main__':
    # page = 1
    # if len(sys.argv) > 1:
    #     try:
    #         page = int(sys.argv[1])
    #     except:
    #         pass
    if os.path.exists(filename):
        os.remove(filename)
    for i in range(67):
        run(current=i)
        time.sleep(1.5)

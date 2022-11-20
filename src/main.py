import requests
import sys

headers = {
    'Host': 'www.mohurd.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def printList(dataList: list):
    for item in dataList:
        print(item)


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
                printList(res_json['data']['list'])


if __name__ == '__main__':
    current = 1
    if len(sys.argv) > 1:
        try:
            current = int(sys.argv[1])
        except:
            pass
    run(current=current)

import requests
import time

#---需修改区域
cookie=''
id=''
#---
url = "https://ks.cqsdx.cn/exam/user/exam/saveTime"

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": cookie,
    "origin": "https://ks.cqsdx.cn",
    "priority": "u=1, i",
    "referer": "https://ks.cqsdx.cn/exam/user/exam/video",
    "sec-ch-ua": '"Not-A.Brand";v="99", "Microsoft Edge";v="157", "Chromium";v="157"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36 Edg/157.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}

# 初始参数
post_data = {
    "id": id,
    "currentTime": 120
}

interval = 120

if __name__ == "__main__":
    while True:
        try:
            resp = requests.post(url, headers=headers, data=post_data, timeout=15)
            print(f"【请求时间】{time.ctime()}")
            print(f"发送参数: {post_data}")
            print(f"响应状态码: {resp.status_code}")
            print(f"响应内容: {resp.text}\n")

            # currentTime累加120秒
            post_data["currentTime"] += 120

        except Exception as e:
            print(f"请求异常：{str(e)}\n")

        time.sleep(interval)

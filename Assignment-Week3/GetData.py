import urllib.request as request
import json

# Get raw data
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
# src = "https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"
with request.urlopen(src) as response:
    rawData = json.load(response)

results = rawData["result"]["results"]
resultsLen = len(results)
itemArr = [""] * resultsLen
# Get each data
i = 0
for data in results:
    stitle = data["stitle"]
    longitude = data["longitude"]
    latitude = data["latitude"]
    urlStr = data["file"]
    # 取得第一張圖檔網址
    searchStr = "http://"
    indexOfSecondHttp = urlStr.find(searchStr, len(searchStr) - 1, len(urlStr))
    if indexOfSecondHttp == -1:  # 只有一個網址
        url = searchStr
    else:
        url = urlStr[0:indexOfSecondHttp]

    # 根據題目要求的格式存進array: 景點名稱,經度,緯度,第一張圖檔網址
    itemArr[i] = stitle + "," + longitude + "," + latitude + "," + url
    i += 1

# 存檔
with open("data.txt", "w", encoding="utf-8") as file:
    i = 0
    for item in itemArr:
        if i == resultsLen - 1:
            file.write(item)  # 最後一行不換行
        else:
            file.write(item + "\n")
        i += 1

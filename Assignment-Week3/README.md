# Assignment03

## Introduction

此專案主要目的為透過 Ajax 跟伺服器溝通，取得景點資料。並加上"Load More"按鈕讀取更多景點。

總共有兩個`.html`檔案，使用了兩種取得資料的方式:

1. index.html (Using `Fetch`)
2. index_XMLHttpRequest.html (Using `XMLHttpRequest(XHR)`)

接下來會簡述這兩種取得資料的方式和使用上的差異，以及實作的 code。

## XHR v.s. Fetch [(ref)](https://eyesofkids.gitbooks.io/javascript-start-from-es6/content/part4/ajax_fetch.html)

|            | XHR                                                                                                               | Ajax                                                                                                                                                                            |
| :--------: | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    定義    | 送出 httpRequest(要求)的物件                                                                                      | 送出 httpRequest(要求)的物件，一個 `HTML5` 的 `API`                                                                                                                             |
|    流程    | 建立一個 `XMLHttpRequest(XHR)`，物件，打開網址然後送出要求，成功時最後由回調函式處理伺服器傳回的 `Response`(回應) | `fetch()`方法是一個位於全域 `window` 物件的方法，它會被用來執行送出 `Request`(要求)的工作，如果成功得到回應的話，它會回傳一個帶有 `Response`(回應)物件的已實現 `Promise` 物件。 |
|    特色    | -                                                                                                                 | 使用`Promise`機制                                                                                                                                                               |
| 取得的資料 | `this.responseText`(字串)                                                                                         | 用 then 接收 response: `.then(function(response) { } )`，之後透過`response.text()`轉成字串                                                                                      |

## Code

### XMLHttpRequest

```js
function getData() {
  let url =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json";
  let req = new XMLHttpRequest();
  req.open("get", url);
  req.onload = function () {
    //連線完成
    itemArr = ParseData(this.responseText); //取得伺服器的回應
    /* //此部分為實作顯示景點資料。並加上"Load More"按鈕
    createBoxes(itemArr, currentIndex, 8);
    createLoadMoreBtn();
    */
  };
  req.send();
}
```

### Fetch [(ref)](https://www.youtube.com/watch?v=ZNBwugL-u1o)

```js
function getData() {
  let url =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json";
  fetch(url)
    .then(function (response) {
      //response物件，代表伺服器的回應
      return response.text(); //用字串的方式取回資料。因為return的內容不是 promise 函式，所以在下一個 then 便可以取得結果
    })
    .then(function (result) {
      //取得前一個then return的資料內容
      itemArr = ParseData(result);

      /* //此部分為實作顯示景點資料。並加上"Load More"按鈕
      createBoxes(itemArr, currentIndex, 8);
      createLoadMoreBtn();
      */
    });
}
```

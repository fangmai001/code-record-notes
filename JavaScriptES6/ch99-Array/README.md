# 陣列(Array)

是陣(ㄓㄣ ˋ)列，別一直打錯

## 可以研究議題

- 標籤是怎麼被 js 定義成物件的? 我可以用 js 產生 html 標籤嗎?
- 想想有沒有比較好的 key value 檢索方式。
- array.map 是甚麼鬼?
- 學 bootstrap

```javascript
handleFilter = (data) => {
  data.map((val) => {
    const temp = val;
    temp.y3 = val.y3 > 1000 ? 0 : val.y3;
    return temp;
  });
  return data;
};
```

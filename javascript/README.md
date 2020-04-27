# JavaScript ES6 程式筆記

自己記一些，想要研究看看的東西。

## 可以研究議題

- 標籤是怎麼被 js 定義成物件的? 我可以用 js 產生 html 標籤嗎?
- 想想有沒有比較好的 key value 檢索方式。
- array.map是甚麼鬼?

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

# JavaScript ES6 程式筆記

自己記一些，想要研究看看的東西。

## 參考資料

- React全方位基礎入門實戰，張至寧，上奇出版，2019年5月。
- 30天React從入門到入坑，IT邦幫忙
  - <https://ithelp.ithome.com.tw/users/20107317/ironman/1261>
- 從零開始學 ReactJS（ReactJS 101）
  - <https://kdchang.gitbooks.io/react101/content/>
- React - DOM界的彼方(繁中)
  - <https://eyesofkids.gitbooks.io/react-basic-zh-tw/content>

## 可以研究議題

- 標籤是怎麼被 js 定義成物件的? 我可以用 js 產生 html 標籤嗎?
- 想想有沒有比較好的 key value 檢索方式。
- array.map是甚麼鬼?
- 學bootstrap

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

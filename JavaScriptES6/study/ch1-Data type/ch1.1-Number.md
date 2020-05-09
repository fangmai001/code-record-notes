# ch1.1 數字(Number)

## 產生方法

跟 `Java` 類似道理，能用基本資料型態來產生，也能用物件來產生。相對的，用基本資料型態產生的物件就屬基本資料型態，用物件產生就屬物件。

```javascript
let a = 25;
let b = new Number(25);

typeof a; // "number"
Object.prototype.toString.call(a); // "[object Number]"

typeof b; // "object"
Object.prototype.toString.call(b); // "[object Number]"
```

## 範圍

範圍：`2^53-1`  
最大範圍：`9007199254740991`  
最小範圍：`-9007199254740991`

## 精準度問題

`Number` 超過 `2^53-1` 仍可以進行宣告、運算等基本運作，但是會有精準度問題。為了避免該問題，需要使用 `Bigint` 來宣告。

## 強制轉型

```javascript
Number("123"); // 123
Number("12.3"); // 12.3
Number(""); // 0
Number("0x11"); // 17
Number("0b11"); // 3
Number("0o11"); // 9
Number("foo"); // NaN
Number("100a"); // NaN
```

## 參考資料

[前端工程研究：關於 JavaScript 中 Number 型別的常見地雷與建議作法](https://blog.miniasp.com/post/2020/02/21/JavaScript-Numbers-Deep-Dive)

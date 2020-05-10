# ch1.5 物件(Object)

- Null
- Array

## 建立物件的方法

產生新物件時， `new` 可加可不加。

```javascript
let a = new Number(25);
let a = Number(25);
```

這種不加 `new` 的產生方法，稱為宣告式（declarative）字面值（literal）。

```javascript
const obj = { name: 'Jack' };
```

加 `new` 的產生方法，稱為建構形式（constructed form）。

```javascript
const obj = new Object();
obj.name = 'Jack'
```

不過這種建構形式不是完全建議就對了。

```javascript
const isValid = new Boolean(false);

if (isValid) {
  console.log('可以繼續運作...');
} else {
  console.log('不合規則，等待處理...');
}

// 可以繼續運作...
```

### 物件中可以包含多種資料型態

```javascript
const a = {
  aaa: "ha ha ha",
  bbb: [1, 2, 3],
  ccc: () => {
    console.log("ccc");
    return "empty";
  },
};
console.log(a.ccc());
```

### 物件內的資料型態，有點像是屬性的概念

```javascript
const a = {
  a: 20,
};

console.log(Object.prototype.toString.call(a.a));
```

## 標準內建物件(Standard built-in objects)

在 js 裡面，有些方法可以直接呼叫使用，如： `parseInt()`

[Mozillz 對標準內建物件的說明](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects)

## window

- setTimeout
  - 到了 n 時間執行一次

- setInterval
  - 每 n 時間執行一次

[談談 JavaScript 的 setTimeout 與 setInterval](https://kuro.tw/posts/2019/02/23/%E8%AB%87%E8%AB%87-JavaScript-%E7%9A%84-setTimeout-%E8%88%87-setInterval/)
[setTimeout 文件](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/setTimeout)
[setInterval 文件](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/setInterval)

[qwe](../images/pic_htmltree.gif)
[qwe](../images/螢幕快照%202018-12-19%20上午1.09.32.png)

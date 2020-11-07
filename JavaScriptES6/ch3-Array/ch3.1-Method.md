# ch3.1 方法(Method)

[說明文件 MDN](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Array)
[做得更好的整理](https://www.oxxostudio.tw/articles/201908/js-array.html)

## 索引

- 不用建物件的方法
  - isArray()
- 改變原始陣列
  - push(): 存項目到尾端
  - pop(): 取尾端項目
  - unshift(): 存項目到前端
  - shift(): 取前端項目
- 回傳新的陣列
- 回傳 null
  - forEach()
- 回傳 boolean

- 常見資料結構運算
  - push(): 存項目到尾端
  - pop(): 取尾端項目
  - unshift(): 存項目到前端
  - shift(): 取前端項目

## 會改變原始陣列

### push()

- param: nope?
- return: 加入項目後的 length
- 說明：
  - 增加項目到陣列

```javascript
const arr = ["a", "b", "c"];

const length = arr.push("d");
console.log(length); // 4
console.log(arr); // ["a", "b", "c", "d"]

arr.push("d", "e", "f");
console.log(arr); // ["a", "b", "c", "d", "d", "e", "f"]
```

### pop()

- param: nope?
- return: 最尾端的項目
- 說明：
  - 取出陣列中最尾端的項目

```javascript
const arr = ["a", "b", "c"];

const pop = arr.pop();
console.log(pop); // "c"
console.log(arr); // ["a", "b"]

arr.pop();
console.log(arr); // ["a"]
```

### shift()

- param: nope?
- return: 最前端的項目
- 說明：
  - 取出陣列中最前端的項目

```javascript
const arr = ["a", "b", "c"];

const shift = arr.shift();
console.log(shift); // "a"
console.log(arr); // ["b", "c"]

arr.shift();
console.log(arr); // ["c"]
```

### unshift()

- param: nope?
- return: 加入項目後的 length
- 說明：
  - 增加項目到陣列的最前端

```javascript
const arr = ["a", "b", "c"];

const unshift = arr.unshift("d");
console.log(unshift); // 4
console.log(arr); // ["d", "a", "b", "c"]

arr.unshift("e", "f");
console.log(arr); // ["e", "f", "d", "a", "b", "c"]
```

### splice()

- param: nope?
- return: 新的 `Array`，如果有項目被刪除，就會把那些刪除項目用 `Array` 包，如果沒有項目被刪，就回傳空 `Array` 。
- 說明：
  - 可以任意改變陣列項目的方法，可以新增或刪除
param: 開始位置(Number), 刪除數目(Number), 要加入的項目(Object)

刪除 index 1 後，補上 "zzz" 。

```javascript
const arr = ["a", "b", "c"];
const arrNew = arr.splice(1, 1, "zzz");

console.log(arr); // ["a", "zzz", "c"]
console.log(arrNew); // ["b"]
```

不會隔空新增項目

```javascript
const arr = ["a", "b", "c"];
const arrNew = arr.splice(99, 0, "zzz");
console.log(arr); // ["a", "b", "c", "zzz"]
```

### reverse()

- param: `undefined`
- return: `Array`
- 說明：
  - 逆轉後的陣列

```javascript
const arr = ["a", "b", "c"];
const reverse = arr.reverse();

console.log(reverse); // ["c", "b", "a"]
console.log(arr); // ["c", "b", "a"]
```

### sort()

- param: 能定義排序原則的方法(compareFunction) `function`  
- return: 排序好的 `Array`
- 說明：
  - 針對陣列中的所有項目進行排序。
  - 預設是用 Unicode 的編碼位置進行排序。
  - 據說，該方法有些問題，不建議太依賴使用。
  - [聊聊 sort](https://medium.com/@realdennis/javascript-%E5%BE%9Earray%E7%9A%84sort%E6%96%B9%E6%B3%95-%E8%81%8A%E5%88%B0%E5%90%84%E5%AE%B6%E7%80%8F%E8%A6%BD%E5%99%A8%E7%9A%84%E5%AF%A6%E4%BD%9C%E7%AE%97%E6%B3%95-c23a335b1b80)

```javascript
const arr = ["c", "b", "a"];
const arrNew = arr.sort();

console.log(arr); // ["a", "b", "c"]
console.log(arrNew); // ["a", "b", "c"]
```

自定義排序方法(compareFunction)

```javascript
const arr = [3, 0, 1, 2];

arr.sort((a, b) => a - b);
console.log(arr); // [0, 1, 2, 3]

arr.sort((a, b) => b - a);
console.log(arr); // [3, 2, 1, 0]
```

若中文字想按照筆畫排序，可以使用 `localeCompare` 。  
[實戰中的案例](https://blog.darkthread.net/blog/javascript-chinese-char-sorting/)  
[localeCompare](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)

```javascript
const arr = ["甲", "乙", "丙", "丁", "戊"];

const compareFunction = (a, b) => {
    return a.localeCompare(b, 'zh-Hant')
}

// 預設不會是傳統認知的筆劃排序
arr.sort()
console.log(arr) // ["丁", "丙", "乙", "戊", "甲"]

// 設區域才會按筆畫排序
arr.sort(compareFunction)
console.log(arr) // ["乙", "丁", "丙", "戊", "甲"]
```

## 會回傳新的陣列

### concat()

- param: `Array`
- return: `Array`
- 說明：
  - 新陣列合併到原本陣列的尾端
  - 不會改變原陣列

```javascript
const arrA = [1, 3, 5];
const arrB = ["a", "b", "c"];
const arrC = ["e", "f"];
const arrNewA = arrA.concat(arrB);
const arrNewB = arrA.concat(arrB, arrC);
console.log(arrNewA); // [1, 3, 5, "a", "b", "c"]
console.log(arrNewB); // [1, 3, 5, "a", "b", "c", "e", "f"]
console.log(arrA); // [1, 3, 5]
```

### map()

- param: `function`
- return: `Array`
- 說明：
  - 不會改變原陣列

```javascript
const arr = ["a", "b", "c"];

const newArr = arr.map((value, index, oldArr) => {
  return "Q" + value + "Q";
});

console.log(arr); // ["a", "b", "c"]
console.log(newArr); // ["QaQ", "QbQ", "QcQ"]

```

---

## 回傳 null

### forEach()

forEach() 方法會將陣列內的每個元素，皆傳入並執行給定的函式一次。
return: `undefined`

```javascript
const arr = ["qwe", "asd", "asd"];
const newArr = arr.forEach((value, index, array) => {
  console.log(value);
});
console.log(newArr); // "qwe" "asd" "asd"
```

return 沒用。

```javascript
const arr = ["qwe", "asd", "asd"];
const newArr = arr.forEach((value, index, array) => {
  return value;
});
console.log(newArr); // undefined
```

## 回傳 boolean

### includes()

includes() 方法會判斷陣列是否包含特定的元素，並以此來回傳 true 或 false。
return Boolean

```javascript
const pets = ["cat", "dog", "bat"];

console.log(pets.includes("cat"));
// expected output: true
```

### every()

every() 方法會測試陣列中的所有元素是否都通過了由給定之函式所實作的測試。
陣列中，全部都是 true ，就為 true 。
return Boolean

```javascript
const arr = ["qwe", "asd", "asd"];
const newArr = arr.every((value, index, array) => {
  return value.length >= 3;
});
console.log(newArr); // true
```

### some()

some() 方法會透過給定函式、測試陣列中是否至少有一個元素，通過該函式所實作的測試。這方法回傳的是布林值。
陣列中，其中一個 true ，就為 true 。
return Boolean

```javascript
const arr = ["qweqwe", "asd", "asd"];
const newArr = arr.some((value, index, array) => {
  return value.length === 3;
});
console.log(newArr); // true
```

## 檢索尋找

### filter()

回傳陣列，條件是 return 的 true 的物件。
return Array

```javascript
const arr = ["qwe", "asd", "asd"];
const newArr = arr.filter((value, index, array) => {
  return value == "asd";
});
console.log(newArr); // ["asd", "asd"]
```

### find()

find() 方法會回傳第一個滿足所提供之測試函式的元素值。否則回傳 undefined。
return Object

```javascript
const arr = ["qwe", "asd", "asd"];
const newArr = arr.find((value, index, array) => {
  return value == "asd";
});
console.log(newArr); // "asd"
```

### indexOf()

indexOf() 方法會回傳給定元素於陣列中第一個被找到之索引，若不存在於陣列中則回傳 -1。

return Number

```javascript
const beasts = ["ant", "bison", "camel", "duck", "bison"];

console.log(beasts.indexOf("bison"));
// expected output: 1
```

## 特殊

### reduce()

reduce() 方法將一個累加器及陣列中每項元素（由左至右）傳入回呼函式，將陣列化為單一值。

```javascript
const array1 = [1, 2, 3, 4];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

// 1 + 2 + 3 + 4
console.log(array1.reduce(reducer));
// expected output: 10

// 5 + 1 + 2 + 3 + 4
console.log(array1.reduce(reducer, 5));
// expected output: 15
```

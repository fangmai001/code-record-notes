# ch3.1 方法(Method)

[說明文件 MDN](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Array)
[做得更好的整理](https://www.oxxostudio.tw/articles/201908/js-array.html)

## 索引

- 不用建物件的方法
  - isArray()
- 改變原始陣列
  - [push()](#push()): 存項目到尾端
  - [pop()](#pop()): 取尾端項目
  - [shift()](#shift()): 取前端項目
  - [unshift()](#unshift()): 存項目到前端
  - [splice()](#splice()): 替換項目
  - [reverse()](#reverse()): 逆轉
  - [sort()](#sort()): 排序
  - fill(): !!! 未完成 !!!
- 回傳新的陣列
  - [concat()](#concat()): 陣列合併
  - [map()](#map()): 項目修改
  - copyWithin(): !!! 未完成 !!!
- 回傳 null
  - [forEach()](#forEach()): 項目走訪
- 回傳 boolean
  - [includes()](#includes()): 是否包含指定項目
  - [every()](#every()): 是否「都」符合指定方法
  - [some()](#some()): 是否「有」符合指定方法
- 回傳 String
  - toString()
  - join()
- 未完成
  - filter()
  - find()
  - indexOf()
  - reduce()
  - findIndex()
  - lastIndexOf()
  - slice()
  - reduce()
  - reduceRight()
  - flat()
  - flatMap()
  - Array.from()
  - Array.of()
  - Array.isArray()
  - keys()
  - valueOf()

- 常見資料結構運算
  - push(): 存項目到尾端
  - pop(): 取尾端項目
  - unshift(): 存項目到前端
  - shift(): 取前端項目

## 會改變原始陣列

### push()

- param: 任何
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

- param: undefined?
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

- param: undefined?
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

- param: 任何
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

- param: 開始位置(Number), 刪除數目(Number), 要加入的項目(Object)
- return: 新的 `Array`，如果有項目被刪除，就會把那些刪除項目用 `Array` 包，如果沒有項目被刪，就回傳空 `Array` 。
- 說明：
  - 可以任意改變陣列項目的方法，可以新增或刪除

```javascript
// 刪除 index 1 後，補上 "zzz" 。
const arr = ["a", "b", "c"];
const arrNew = arr.splice(1, 1, "zzz");

console.log(arr); // ["a", "zzz", "c"]
console.log(arrNew); // ["b"]
```

```javascript
// 不會隔空新增項目
const arr = ["a", "b", "c"];
const arrNew = arr.splice(99, 0, "zzz");
console.log(arr); // ["a", "b", "c", "zzz"]
```

### reverse()

- param: undefined
- return: 新的 Array 。
- 說明：
  - 逆轉後的陣列

```javascript
const arr = ["a", "b", "c"];
const reverse = arr.reverse();

console.log(reverse); // ["c", "b", "a"]
console.log(arr); // ["c", "b", "a"]
```

### sort()

- param: 能定義排序原則(compareFunction)的 function 。
- return: 排序好的 Array 。
- 說明：
  - 針對陣列中的所有項目進行排序。
  - 關於 compareFunction 可以到 ch3.2 常見應用(Common Application) 看看

```javascript
const arr = ["c", "b", "a"];
const arrNew = arr.sort();

console.log(arr); // ["a", "b", "c"]
console.log(arrNew); // ["a", "b", "c"]
```

### fill()

<!-- !!!!!! -->
<!-- TODO -->
<!-- !!!!!! -->

## 會回傳新的陣列

### concat()

- param: 多個 Array ，或說 「`*Array`」。
- return: 新的 Array 。
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

### copyWithin()

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

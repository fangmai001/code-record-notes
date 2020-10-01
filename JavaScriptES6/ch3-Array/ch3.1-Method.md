# Method

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
- 回傳 null
  - forEach()
- 回傳新的陣列
- 回傳 boolean

- 常見資料結構運算
  - push(): 存項目到尾端
  - pop(): 取尾端項目
  - unshift(): 存項目到前端
  - shift(): 取前端項目

## 會改變原始陣列

### push()

增加項目到陣列
return: 加入項目後的 length

```javascript
const arr = ["a", "b", "c"];

const length = arr.push("d");
console.log(length); // 4
console.log(arr); // ["a", "b", "c", "d"]

arr.push("d", "e", "f");
console.log(arr); // ["a", "b", "c", "d", "d", "e", "f"]
```

### pop()

取出陣列中最尾端的項目
return: 最尾端的項目

```javascript
const arr = ["a", "b", "c"];

const pop = arr.pop();
console.log(pop); // "c"
console.log(arr); // ["a", "b"]

arr.pop();
console.log(arr); // ["a"]
```

### shift()

取出陣列中最前端的項目
return: 最前端的項目

```javascript
const arr = ["a", "b", "c"];

const shift = arr.shift();
console.log(shift); // "a"
console.log(arr); // ["b", "c"]

arr.shift();
console.log(arr); // ["c"]
```

### unshift()

增加項目到陣列的最前端
return: 加入項目後的 length

```javascript
const arr = ["a", "b", "c"];

const unshift = arr.unshift("d");
console.log(unshift); // 4
console.log(arr); // ["d", "a", "b", "c"]

arr.unshift("e", "f");
console.log(arr); // ["e", "f", "d", "a", "b", "c"]
```

### splice()

可以任意改變陣列項目的方法，可以新增或刪除
param: 開始位置(Number), 刪除數目(Number), 要加入的項目(Object)
return: 新的 `Array`，如果有項目被刪除，就會把那些刪除項目用 `Array` 包，如果沒有項目被刪，就回傳空 `Array` 。

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

### sort()

針對陣列中的所有項目進行排序。
預設是用 Unicode 的編碼位置進行排序。
據說，該方法有些問題，不建議太依賴使用。
param: 能定義排序原則的方法(compareFunction) `function`
return: 排序好的 `Array`

```javascript
const arr = ["c", "b", "a"];
const arrNew = arr.sort();

console.log(arr); // ["a", "b", "c"]
console.log(arrNew); // ["a", "b", "c"]
```

中文字無解，不會是用我們傳統認知的筆畫順序來排序。

```javascript
const arr = ["一", "二", "三", "四", "五"];
arr.sort();

console.log(arr); // ["一", "三", "二", "五", "四"]
```

## 會回傳新的陣列

### concat()

新陣列合併到原本陣列的尾端
不會改變原陣列
return: `Array`

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

---

## forEach()

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

## 元素判斷

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

## 元素調整

### map()

map() 方法會建立一個新的陣列，其內容為原陣列的每一個元素經由回呼函式運算後所回傳的結果之集合。
可以用於重新組合新陣列。
return Array

```javascript
const arr = ["qwe", "asd", "asd"];
const newArr = arr.map((value, index, array) => {
  return value + "QQQQ";
});
console.log(newArr); // ["qweQQQQ", "asdQQQQ", "asdQQQQ"]
```

### splice()

新增/交換/刪除元素

[文件](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)

刪除指定位置

```javascript
const months = ["Jan", "March", "April", "June"];
months.splice(0, 1);
//  ["March", "April", "June"]
```

從索引 2 的位置開始，刪除 0 個元素並插入「drum」

```javascript
var myFish = ["angel", "clown", "mandarin", "sturgeon"];
var removed = myFish.splice(2, 0, "drum");

// myFish 為 ["angel", "clown", "drum", "mandarin", "sturgeon"]
// removed 為 [], 沒有元素被刪除
```

從索引 3 的位置開始，刪除 1 個元素

```javascript
var myFish = ["angel", "clown", "drum", "mandarin", "sturgeon"];
var removed = myFish.splice(3, 1);

// removed 為 ["mandarin"]
// myFish 為 ["angel", "clown", "drum", "sturgeon"]
```

### push()

push() 方法會添加一個或多個元素至陣列的末端，並且回傳陣列的新長度。

return Number

```javascript
const animals = ["pigs", "goats", "sheep"];

const count = animals.push("cows");
console.log(count);
// expected output: 4
console.log(animals);
// expected output: Array ["pigs", "goats", "sheep", "cows"]
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

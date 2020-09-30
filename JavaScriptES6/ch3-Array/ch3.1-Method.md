# Method

[說明文件 MDN](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Array)
[做得更好的整理](https://www.oxxostudio.tw/articles/201908/js-array.html)

## 索引

- 回傳 null
  - forEach()
- 回傳新的陣列
- 回傳 boolean
- 改變原始陣列

- 常見資料結構運算
  - push()
  - pop()
  - shift()
  - unshift()

## forEach()

forEach() 方法會將陣列內的每個元素，皆傳入並執行給定的函式一次。
return undefined

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

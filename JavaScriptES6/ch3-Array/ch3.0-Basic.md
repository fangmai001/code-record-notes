# ch3.0 基本用法(Basic)

## 產生

加`new`或不加`new`，都可以，我是習慣不加`new`。不過現在比較少人會用傳統的`= new Array()`了，一般建議用`= []`。

```javascript
const arr = ["a", "b"]; // ['a', 'b']
const arr = new Array("a", "b"); // ['a', 'b']
const arr = new Array(3); // [undefined, undefined, undefined]
```

## 建立項目

建立項目(item)到陣列的尾端。

```javascript
const arr = [];
arr.push("a"); // ['a']
```

可以直接指定 index 來設定項目，也可以跳躍設定項目，不用依循第一的 index 循序增加項目。

```javascript
const arr = [];
arr[0] = "qwe"; // ['qwe']
arr[2] = "asd"; // ['qwe', undefined ,'asd']
```

## 刪除元素

刪除`index`起的第`n`個項目。

```javascript
const n = 1;
const index = 1;
const arr = ["a", "b", "c"];
arr.splice(index, n); // ["a", "c"]
```

## 展開運算子(Spread Operator)

這是 ES6 新增的功能。

```javascript
const arrA = [1, 3, 5];
const arrB = ["a", "b", "c"];
const arrNew = [...arrA, ...arrB]; // [1, 3, 5, "a", "b", "c"]
```

拆解後，不會有重複的項目

```javascript
const arr = ["qwe", "asd", "asd"];
const arrNew = [...arr, ...arr]; // ["qwe", "asd", "asd"]
```

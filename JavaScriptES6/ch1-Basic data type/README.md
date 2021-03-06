# ch1. 基本資料型態(Basic data type)

## 常見的資料型態

認真實驗一下，發現基本型態真的只有分成 6 種。不過這也只是我簡單用程式檢查出來的結果，細節或是其他的討論，就沒有深入研究了。

有趣的是 `null` 、 `array` 也是被分為 object。至於 `null` 是不是基本資料型態，這問題好像是很大的爭議。

然後...  
Mozilla 提出兩個我比較少看到的基本資料型態：BigInt、Symbol，可以研究看看。

<https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Data_structures>

## 基本資料型態 (primitive data types)

1. Number
2. Boolean
3. String
4. Function
5. Object
6. Undefined
7. Bigint (new)
8. Symbol (new)

```javascript
const funcA = function () {};
const funcB = () => {};
class funcC {}

const a = [
  0, // "number" "[object Number]"
  25, // "number" "[object Number]"
  25.125, // "number" "[object Number]"
  true, // "boolean" "[object Boolean]"
  false, // "boolean" "[object Boolean]"
  "", // "string" "[object String]"
  funcA, // "function" "[object Function]"
  funcB, // "function" "[object Function]"
  funcC, // "function" "[object Function]"
  undefined, // "undefined" "[object Undefined]"
  null, // "object" "[object Null]"
  [], // "object" "[object Array]"
  {}, // "object" "[object Object]"
  new Date(), // "object" "[object Date]"
  new Error("oops!.."), // "object" "[object Error]"
  /a-z/, // "object" "[object RegExp]"
];

a.forEach((val) => {
  let a = typeof val;
  let b = Object.prototype.toString.call(val);
  console.log(a, b);
});
```

## 檢查型態方法

`typeof` 跟 `Object.prototype.toString.call()` 都是輸出文字。
`typeof`: 原本的檢查方法。
`Object.prototype.toString.call()`: 如果 `typeof` 還是輸出 `Object` ，就要用這個方法。

```javascript
a = typeof 25;
b = Object.prototype.toString.call(25);
console.log(a, typeof a); // number string
console.log(b, typeof b); // [object Number] string
```

# ch1. 資料型態與宣告(Data type and declare scope)

## 1. 資料型態(Data Type)

### 常見的資料型態

認真實驗一下，發現基本型態真的只有分成6種。不過這也只是我簡單用程式檢查出來的結果，細節或是其他的討論，就沒有深入研究了。

有趣的是 `null` 、 `array` 也是被分為object。至於 `null` 是不是基本資料型態，這問題好像是很大的爭議。

然後...  
Mozilla 提出兩個我比較少看到的基本資料型態：BigInt、Symbol，可以研究看看。

<https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Data_structures>

### 基本資料型態 (primitive data types)

1. Number
2. Boolean
3. String
4. Function
5. Object
6. Undefined
7. Bigint (new)
8. Symbol (new)

```javascript
const funcA = function(){}
const funcB = () => {}
class funcC {}

const a = [
    0,                      // "number" "[object Number]"
    25,                     // "number" "[object Number]"
    25.125,                 // "number" "[object Number]"
    true,                   // "boolean" "[object Boolean]"
    false,                  // "boolean" "[object Boolean]"
    '',                     // "string" "[object String]"
    funcA,                  // "function" "[object Function]"
    funcB,                  // "function" "[object Function]"
    funcC,                  // "function" "[object Function]"
    undefined,              // "undefined" "[object Undefined]"
    null,                   // "object" "[object Null]"
    [],                     // "object" "[object Array]"
    {},                     // "object" "[object Object]"
    new Date(),             // "object" "[object Date]"
    new Error('oops!..'),   // "object" "[object Error]"
    /a-z/,                  // "object" "[object RegExp]"
]

a.forEach(
    (val) => {
        let a = typeof val
        let b = Object.prototype.toString.call(val)
        console.log(a, b);
    }
)
```

### Number

#### 產生方法

跟 `Java` 類似道理，能用基本資料型態來產生，也能用物件來產生。相對的，用基本資料型態產生的物件就屬基本資料型態，用物件產生就屬物件。

```javascript
let a = 25;
let b = new Number(25);

typeof a                            // "number"
Object.prototype.toString.call(a)   // "[object Number]"

typeof b                            // "object"
Object.prototype.toString.call(b)   // "[object Number]"
```

#### 範圍

範圍：`2^53-1`  
最大範圍：`9007199254740991`  
最小範圍：`-9007199254740991`

#### 精準度問題

`Number` 超過 `2^53-1` 仍可以進行宣告、運算等基本運作，但是會有精準度問題。為了避免該問題，需要使用 `Bigint` 來宣告。

#### 強制轉型

```javascript
Number("123")     // 123
Number("12.3")    // 12.3
Number("")        // 0
Number("0x11")    // 17
Number("0b11")    // 3
Number("0o11")    // 9
Number("foo")     // NaN
Number("100a")    // NaN
```

### Boolean

- 0與1的意義?

### String

### Function

### Object

- Null
- Array

產生新物件時， `new` 可加可不加。

```javascript
let a = new Number(25);
let a = Number(25);
```

物件中可以包含多種資料型態

```javascript
const a = {
    aaa: 'ha ha ha',
    bbb: [
        1,2,3
    ],
    ccc: () => {
        console.log('ccc');
        return 'empty'
    }
}
console.log(a.ccc());
```

物件內的資料型態，有點像是屬性的概念

```javascript
const a = {
    a: 20,
}

console.log(Object.prototype.toString.call(a.a));
```

### Undefined

### Bigint (new)

### Symbol (new)

## 2. 檢查型態方法

`typeof` 跟 `Object.prototype.toString.call()` 都是輸出文字。

```javascript
a = typeof 25;
b = Object.prototype.toString.call(25);
console.log(a, typeof a); // number string
console.log(b, typeof b); // [object Number] string
```

## 3. 宣告的作用域(Scope)

- 屬於區塊作用域(Block scope)
  - 只能在區域內存在，離開區域內就無法呼叫變數，如：if, for...
  - 宣告：let, const
- 函式作用域(Function scope)
  - 在函式內存在，如：function
  - 宣告：var

## 4. 宣告方法

### const

- 常數，不能變更
- 通常用於宣告物件

### let

- 變數，可以改
- 通常用於常常需要改的數字，或是暫時要用的數字

## 參考資源

[Mozillz 對標準內建物件的說明](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects)

[前端工程研究：關於 JavaScript 中 Number 型別的常見地雷與建議作法](https://blog.miniasp.com/post/2020/02/21/JavaScript-Numbers-Deep-Dive)

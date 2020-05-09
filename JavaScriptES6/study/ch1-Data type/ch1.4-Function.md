# ch1.4 函式(Function)

## 型態

```javascript
const funcA = function () {};
const funcB = () => {};
class funcC {}

typeof funcA; // "function"
Object.prototype.toString.call(funcA); // "[object Function]"

typeof funcB; // "function"
Object.prototype.toString.call(funcB); // "[object Function]"

typeof funcC; // "function"
Object.prototype.toString.call(funcC); // "[object Function]"
```

## 函式定義(FD: Function Declaration)

使用有名稱的函式。

```javascript
function test(a, b) {
  return "hey";
}
```

## 函式表達式(FE: Function Expression)

常數指定為匿名函式。

```javascript
const test = function (a, b) {
  return "hey";
};
```

## 立即調用的函數表達式(IIFE: Immediately Invoked Function Expression)

是一個定義完馬上就執行的 JavaScript function。

```javascript
(function IIFE() {
  console.log("Hello!");
})();
// "Hello!"
```

## 箭頭函式

這是 FE 的簡寫語法

```javascript
const test = (a, b) => {
  return "hey";
};
```

可以寫成單行。

```javascript
const test = (a, b) => "hey";
```

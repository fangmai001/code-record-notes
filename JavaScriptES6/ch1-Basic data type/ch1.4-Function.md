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

## 其餘運算子(Rest Operator)

如果不確定 function 的參數會有多少，可以用`...`加在參數前，就能包成陣列。

```javascript
const avgFunc = (...arr) => {
  console.log(arr); // [1, 3, 5, 7, 9]
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum / arr.length;
};

console.log(avgFunc(1, 3, 5, 7, 9)); // 5
```

## 展開運算子(Spread Operator)

在導入 function 前，加上`...`在參數前，形同把陣列拆開成`1, 3, 5`。

```javascript
const func = (parm) => {
  console.log(parm);
};

const arr = [1, 3, 5];
func(...arr); // 1
func(1, 3, 5); // 1
```

# ch2. 宣告(Declare)

## 宣告的作用域(Declare Scope)

- 屬於區塊作用域(Block scope)
  - 只能在區域內存在，離開區域內就無法呼叫變數，如：if, for...
  - 宣告：let, const
- 函式作用域(Function scope)
  - 在函式內存在，如：function
  - 宣告：var

## 宣告方法

### const

- 常數，不能變更
- 通常用於宣告物件

### let

- 變數，可以改
- 通常用於常常需要改的數字，或是暫時要用的數字

## 提升(Hoisting)

課本有，不過寫得有點難，可以先看看影片教學，會比較簡單。

[影片教學](https://www.youtube.com/watch?v=1Cpt6f9_Phg)

舉例：宣告變數

```javascript
console.log(a); // 輸出: undefined 應該是: a is not defined
var a = 10;
```

`var a = 10` 等於三行程式行為，這個變數被宣告到最上面了。

```javascript
var a;
console.log(a);
a = 10;
```

# Day1. 宣告作用域(Declare Scope)

## 1. 迴圈內的宣告(Declare variables on for loop)

### 緣起

在 python 裡，迴圈內的宣告的變數會變成全域變數。

如果只是寫 50 幾行的 code ，可能不會成大問題，但有時候，可能原本只是處裡簡單的問題，到後來越改越多，就很不小心把 py 檔寫到500多行。

```python
// python 會變成 全域變數
for i in range(10):
  a = 'hi'

print(a)  // hi
```

本來可能只是想要在迴圈中宣告某格變數，舉例 a ，然後扁扁好死不死，我很愛用 a 這個變數，當做我暫時使用的變數，就會發現怎麼已經被賦值了？

就從這個經驗，之後coding就會小心一點，避免上述問題發生。

### Javascript

```javascript
for (let i = 0; i < 10; i++) {
  const a = "hi";
  let b = "hi";
  var c = "hi";
  d = "hi";
}

console.log(a);   // not defined
console.log(b);   // not defined
console.log(c);   // hi
console.log(d);   // hi
```

基本上在 ES6 中，乖乖使用 const 或 let 來宣告變數，應該是不會有甚麼問題，他也會乖乖消失在迴圈外。

---

## 2. 方法內的宣告(Declare variables on for loop)

```javascript
func = () => {
    let a = 'hihi';
    const b = 'hihi';
    var c = 'hihi';
    d = 'hi';
}

func()
console.log(a);     // not defined
console.log(b);     // not defined
console.log(c);     // not defined
console.log(d);     // hi
```

---


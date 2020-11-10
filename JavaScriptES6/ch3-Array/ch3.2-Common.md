# ch3.2 常見應用(Common Application)

## 合併陣列

```javascript
const arrA = [1, 3, 5];
const arrB = ["a", "b", "c"];
const arrNew = [...arrA, ...arrB]; // [1, 3, 5, "a", "b", "c"]
console.log(arrNew);
```

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

## 合併陣列可能會有的問題

[在 MDN 提到的範例](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)

合併巢狀陣列，會保留原本的參考(references)

```javascript
const arrA = [[1]];
const arrB = [2, [3]];
const arrNew = arrA.concat(arrB);
console.log(arrNew); // [[1], 2, [3]]
debugger; // 加上這個，才能正常顯示
arrA[0].push(4);
console.log(arrNew); // [[1, 4], 2, [3]]
```

改成 Object 不會有這問題，不太懂，可以再觀察看看

```javascript
const arrA = [{ a: "qwe" }];
const arrB = [{ c: "zxc" }];
const arrNew = arrA.concat(arrB);
console.log(arrNew); // [{ a: "qwe" }, { c: "zxc" }]
debugger;
arrA.b = "123";
console.log(arrNew); // [{ a: "qwe" }, { c: "zxc" }]
```

## 關於陣列排序(sort)

- 針對陣列中的所有項目進行排序。
- 預設是用 Unicode 的編碼位置進行排序。
- 據說，該方法有些問題，不建議太依賴使用。
- [聊聊 sort](https://medium.com/@realdennis/javascript-%E5%BE%9Earray%E7%9A%84sort%E6%96%B9%E6%B3%95-%E8%81%8A%E5%88%B0%E5%90%84%E5%AE%B6%E7%80%8F%E8%A6%BD%E5%99%A8%E7%9A%84%E5%AF%A6%E4%BD%9C%E7%AE%97%E6%B3%95-c23a335b1b80)

```javascript
const arr = ["c", "b", "a"];
const arrNew = arr.sort();

console.log(arr); // ["a", "b", "c"]
console.log(arrNew); // ["a", "b", "c"]
```

自定義排序方法(compareFunction)

```javascript
const arr = [3, 0, 1, 2];

arr.sort((a, b) => a - b);
console.log(arr); // [0, 1, 2, 3]

arr.sort((a, b) => b - a);
console.log(arr); // [3, 2, 1, 0]
```

若中文字想按照筆畫排序，可以使用 `localeCompare` 。  
[實戰中的案例](https://blog.darkthread.net/blog/javascript-chinese-char-sorting/)  
[localeCompare](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)

```javascript
const arr = ["甲", "乙", "丙", "丁", "戊"];

const compareFunction = (a, b) => {
    return a.localeCompare(b, 'zh-Hant')
}

// 預設不會是傳統認知的筆劃排序
arr.sort()
console.log(arr) // ["丁", "丙", "乙", "戊", "甲"]

// 設區域才會按筆畫排序
arr.sort(compareFunction)
console.log(arr) // ["乙", "丁", "丙", "戊", "甲"]
```

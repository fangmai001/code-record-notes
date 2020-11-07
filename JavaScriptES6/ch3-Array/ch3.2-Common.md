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

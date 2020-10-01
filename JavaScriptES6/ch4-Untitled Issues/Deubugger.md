# debugger

有些值在程式跑完的時候，不能正確顯示，下面的例子，如果不加`debugger`，兩個`console.log()`顯示的結果都會是一樣。

```javascript
const arrA = [[1]];
const arrB = [2, [3]];
const arrNew = arrA.concat(arrB);
console.log(arrNew); // [[1], 2, [3]]
debugger; // 加上這個，才能正常顯示
arrA[0].push(4);
console.log(arrNew); // [[1, 4], 2, [3]]
```

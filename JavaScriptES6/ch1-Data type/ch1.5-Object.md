# ch1.5 物件(Object)

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
  aaa: "ha ha ha",
  bbb: [1, 2, 3],
  ccc: () => {
    console.log("ccc");
    return "empty";
  },
};
console.log(a.ccc());
```

物件內的資料型態，有點像是屬性的概念

```javascript
const a = {
  a: 20,
};

console.log(Object.prototype.toString.call(a.a));
```

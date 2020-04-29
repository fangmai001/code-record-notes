# 其他的

## 物件

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

## 快速的條件指派

最近學到的，還不是很清楚用法。

```javascript
console.log(true && "hey"); // "hey"
console.log("hey" || true); // "hey"
```

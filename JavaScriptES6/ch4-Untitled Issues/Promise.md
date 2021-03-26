# Promise

```javascript
const func = async () => {             // ~ 開頭表示直接執行這個 function，結尾有 ()
  const delay = (s) => {
    return new Promise((resolve) => {  // 回傳一個 promise
      // setTimeout(resolve('test'), s);           // 等待多少秒之後 resolve()
      setTimeout(resolve, s);           // 等待多少秒之後 resolve()
      
    });
  };

  console.log(1) // 顯示 1
  await delay(1000) // 延遲ㄧ秒
  console.log(2) // 顯示 2
  await delay(2000) // 延遲二秒
  console.log(3) // 顯示 3
}

func()
```

```javascript
const funcA = async () => {
  const delay = (s) => {
    return new Promise((resolve) => {
      setTimeout(resolve, s)
    })
  }

  await delay(2000)
  console.log('wait')

}

const funcB = async () => {

  const task = (resolve, index) => {
    setTimeout(() => {
      console.log(`${index}: do something.`)
      resolve()
    }, 1000)
  }

  const delay = (index) => {
    return new Promise((resolve) => {
      task(resolve, index)
    })
  }

  // delay(0).then(() => {
  //   delay(1).then(() => {
  //     delay(2)
  //   })
  // })
  // await delay(1)
  // await delay(2)

  // [0, 1, 2, 3].map(async (index) => {
  //   return await delay(index)
  // });

  const taskArr = []
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      taskArr.push(delay(`i${i}, j${j}`))
    }
  }
  taskArr.push(undefined)
  console.log('start')
  console.log('taskArr', taskArr)
  await Promise.all(taskArr)
  console.log('end')

}

funcB()
// for (let i = 0; i < 2; i ++) {
//   funcB()
// }
```

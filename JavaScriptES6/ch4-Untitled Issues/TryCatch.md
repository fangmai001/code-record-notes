# TryCatch

```javascript
function getMonthName(mo) {
  mo = mo - 1; // Adjust month number for array index (1 = Jan, 12 = Dec)
  var months = ["Jan","Feb","Mar","Apr","May","Jun","Jul",
                "Aug","Sep","Oct","Nov","Dec"];
  if (months[mo]) {
    return months[mo];
  } else {
    throw "InvalidMonthNo"; //throw 關鍵字在這裏被使用
  }
}

try { // statements to try
  monthName = getMonthName(myMonth); // 函式可以丟出例外
}
catch (e) {
  console.log(`error: ${e}`); // 將例外傳至例外處理機制
}
```
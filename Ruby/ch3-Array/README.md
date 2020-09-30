# Array

只有最後一個變數，才會真正存進去。

```ruby
arr = ['s', 's', 's', 's', 's']

temp = arr.map do |i|
    i + 'a'
    i + 'b'
    'c'
end

p temp # ["c", "c", "c", "c", "c"]
```

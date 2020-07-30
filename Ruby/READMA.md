# 隨便記

## Array

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

## Hash

each

```ruby
hash = {apple: "pen", pen: "pineapple"}

hash.each do |key, value|
    puts "Key: #{key}, Value: #{value}"
end
```

each_key

```ruby
hash = {apple: "pen", pen: "pineapple"}

hash.each_key do |key|
    puts key
end
```

each_value

```ruby
hash.each_value do |value|
    puts value
end
```

## String

each_char  
顯示每個字元

```ruby
"ABC".each_char do |val|
 p val
end
# "A" "B" "C"
```

## Enumerator (或稱 Loop)

---

什麼是 Enumerator ?  
又稱「迭代」，這個類似迴圈的類別，會把需迭代的變數儲存起來，然後由參數指定的方法應用。

time  
number 的 method。

```ruby
10.times do |i|
    p i
end
```

upto  
number 的 method。

```ruby
0.upto(10) do |i|
    p i
end
```

downto  
number 的 method。

```ruby
10.downto(0) do |i|
    p i
end
```



# 隨便記

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

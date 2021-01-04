# Array

## map

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

## 效率比較

```ruby
require 'benchmark'

n = 5000000
Benchmark.bm(15) do |x|
  x.report("for") do
    a = [*0..n]
    for i in 0...a.size
        b = a[i] + 1
    end
  end
  x.report("times") do
    a = [*0..n]
    (a.size).times do |i|
        b = a[i] + 1
    end
  end
  x.report("upto") do
    a = [*0..n]
    0.upto(a.size - 1) do |i|
        b = a[i] + 1
    end
  end
  x.report("each_with_index") do
    a = [*0..n]
    a.each_with_index do |_, i|
        b = a[i] + 1
    end
  end
  x.report("each()") do
    a = [*0..n]
    (0..(a.size - 1)).each do |i|
        b = a[i] + 1
    end
  end
  x.report("each[*]") do
    a = [*0..n]
    [*0..(a.size - 1)].each do |i|
        b = a[i] + 1
    end
  end
end
```

```
user     system      total        real
for               0.360000   0.047000   0.407000 (  0.408292)
times             0.375000   0.015000   0.390000 (  0.391367)
upto              0.359000   0.063000   0.422000 (  0.422400)
each_with_index   0.437000   0.078000   0.515000 (  0.511011)
each()            0.375000   0.031000   0.406000 (  0.403688)
each[*]           0.547000   0.016000   0.563000 (  0.575982)
```

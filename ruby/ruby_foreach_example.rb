# don't do foreach like this normally!
def foreach(arr)
  puts "block given? #{block_given?}"
  for i in 0...arr.size
    yield arr[i] # passes arr[i] to the block
  end
end

foreach([1,2,3]) { |x| puts x**2 }

foreach([1,2,3]) do |x|
  puts x**2
end

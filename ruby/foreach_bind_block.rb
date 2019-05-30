def foreach(arr, &block)
  puts "block class: #{block.class}"
  for i in 0...arr.size
    block.call(arr[i]) # passes arr[i] to the block
  end
end

foreach([10,9,30]) { |x| puts x }

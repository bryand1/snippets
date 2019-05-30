def multiply(arr, &block)
  for i in 0...arr.size
    block.call(arr[i])
  end
end

multiply([1, 2, 3, 4, 5]) { |x| puts x * 3}


exam = Proc.new do |x,y|
  puts "#{x.inspect}, #{y.inspect} "
end

exam.call(1, 2)      # "1, 2"
exam.call(1)         # "1, nil"
exam.call(1, 2, 3)   # "1, 2"


# This is the equivalent in python to doing
# double = lambda x: x * 2
# print(double(3))
double = Proc.new { |x| x * 2 }
puts double.call(3)  # 6


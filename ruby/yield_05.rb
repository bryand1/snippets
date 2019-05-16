# https://medium.com/rubycademy/the-yield-keyword-603a850b8921
def yield_with_return_value
  hello_world = yield
  puts hello_world
end

yield_with_return_value { "Hello World!" }  # => Hello World!

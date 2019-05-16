def yield_with_arguments
  hello = 'Hello'
  world = 'World!'

  yield(hello, world)
end

yield_with_arguments { |hello, world| puts "#{hello} #{world}" }  # => Hello World!

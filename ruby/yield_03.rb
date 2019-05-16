def optional_block
  yield if block_given?
end

optional_block  # => nil
optional_block { puts 'optional block' }  # => optional block

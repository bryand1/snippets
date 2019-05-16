def yield_without_block
  yield
end

yield_without_block  # => LocalJumpError (no block given(yield))

=begin
Traceback (most recent call last):
	1: from yield_02.rb:5:in `<main>'
yield_02.rb:2:in `yield_without_block': no block given (yield) (LocalJumpError)
=end

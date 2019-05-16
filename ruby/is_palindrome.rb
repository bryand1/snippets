def is_palindrome(s)
  if s.length == 0 || s.length == 1
    true
  elsif s.length == 2
    s[0] == s[1]
  elsif s[0] == s[-1]
    is_palindrome(s[1,s.length-2])
  else
    false
  end
end

puts is_palindrome("")
puts is_palindrome("1")
puts is_palindrome("22")
puts is_palindrome("32")    # => false
puts is_palindrome("353")
puts is_palindrome("3555")  # => false
puts is_palindrome("123454321")

# Ruby closures
# https://www.hackerrank.com/challenges/ruby-closures/problem
# Blocks, Procs, and Lambdas are closures in Ruby

def plus_1(y)
  x = 100
  y.call    # remembers the value of x = 1
end

x = 1
y = -> { x + 1 }

puts plus_1(y)


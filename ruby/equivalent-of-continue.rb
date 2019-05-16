# Equivalent of the C and Python `continue` statement
# https://stackoverflow.com/questions/4010039/equivalent-of-continue-in-ruby?rq=2
(1..5).each do |x|
    next if x < 2
    puts x
end


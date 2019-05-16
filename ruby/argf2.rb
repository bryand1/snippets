# https://stackoverflow.com/questions/273262/best-practices-with-stdin-in-ruby
ARGF.each do |line|
  puts line if line =~ /cat/
end

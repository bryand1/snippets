ARGF.each_with_index do |line, idx|
  print ARGF.filename, ":", idx, ":", line
end

def switch(x)
  case x
  when 0..40
    "Fail"
  when 41..60
    "Pass"
  when 61..70
    "Pass with Merit"
  when 71..100
    "Pass with Distinction"
  else
    "Invalid score"
  end
end

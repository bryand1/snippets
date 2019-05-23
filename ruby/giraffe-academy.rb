
# name = gets.chomp()
# puts ("Hello " + name + ", you are cool")

# friends = Array.new
# friends[0] = "Holly"
# friends[5] = "Steven"

# def sayhi(name="Bryan")
#   puts "Hello #{name}"
# end

# sayhi "Mike"

# def cube(num)
#   num * num * num
# end

# puts cube(2)

# ismale = true
# if ismale
#   puts "You are male"
# end

# num1 = gets.chomp.to_f
# op = gets.chomp
# num2 = gets.chomp.to_f

# if op == "+"
#   puts num1 + num2
# elsif op == "-"
#   puts num1 - num2
# end

# index = 1
# while index <= 5
#   puts index
#   index += 1
# end

# for friend in ["Kevin", "Karen", "Oscar"]
#   puts friend
# end

# friends = ["Kevin", "Karen", "Oscar"]
# friends.each do |friend|
#   puts friend
# end

# for index in 0..5
#   puts index
# end

# def pow(base, exp)
#   result = 1
#   exp.times do
#     result *= base
#   end
#   result
# end


# puts pow 2, 3

# File.open("employees.txt", "r") do |file|
#   puts file.readlines()
# end

# file = File.open("employees.txt", "r")
# puts file.read
# file.close

# File.open("employees.txt", "a") do |file|
#   file.write("\nOscar, Accounting")
# end

# lucky = [1, 2, 3]
# begin
#   lucky["dog"]
# rescue TypeError => e
#   puts e
# end

# class Book
#   attr_accessor :title, :author, :pages
# end

# book1 = Book.new
# book1.title = "Harry Potter"
# book1.author = "JK Rowling"
# book1.pages = 400

# puts book1.title

# class Book
#   attr_accessor :title, :author, :pages
#   def initialize(title, author, pages)
#     @title = title
#     @author = author
#     @pages = pages
#   end
# end

# book1 = Book.new "Mike"
# book2 = Book.new "Bill"

class Student
  attr_accessor :name, :major, :gpa
  def initialize(name, major, gpa)
    @name = name
    @major = major
    @gpa = gpa
  end

  def has_honors
    if @gpa >= 3.5
      return true
    end
    false
  end
end

s1 = Student.new("Jim", "History", 2.6)
s2 = Student.new("Pam", "Engineering", 3.5)

puts s1.has_honors
puts s2.has_honors


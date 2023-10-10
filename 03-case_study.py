import turtle
bob = turtle.Turtle()
print(bob)

bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

# using the for keyword
for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()

# The turtle module (lowercase 't') provides a function called Turtle that creates a Turtle object, which is assigned
# to a variable named bob.

# You can call a Turtle with different methods to move it around a window like so: `bob.fd(100)` will move a turtle
# forward by 100 pixels depending on your screen size, `bob.bk(100) will move it back by 100 pixels`.

# Other methods includes: lt: left turn, rt: right turn, which both take in an argument of angles in degrees.
# Also, each turtle is holding down a pen that can be used to draw on the canvas using pu: 'pen up' and pd: 'pen down'

# Here's an example that draws a right angle.
# bob.fd(100) moves the turtle forward by 100 pixels
# bob.lt(90) turns the turtle to the left by 90 degrees
# bob.fd(100) moves the turtle forward by 100 pixels

# Here's an example that draws a square.
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

# The for keyword allows us to perform repetitive tasks. The example below will print "Hello World" 4 times.
for i in range(4):
    print('Hello World')
# using the for statement, we can draw the same square concisely.

for i in range(4):
    bob.fd(100)
    bob.lt(90)

# The syntax of the for statement is similar to a function definition. It has a header that ends with a colon and an
# indented body of any number of statements. The for statement is also called a loop because the flow of execution runs
# through the body and then loops back to the top. In this case, it runs the body four times.


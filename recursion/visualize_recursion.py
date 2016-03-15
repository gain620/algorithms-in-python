import turtle
import time

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()


def drawSpiral(turtle, lineLen):
    if lineLen > 0:
        time.sleep(0.1)
        turtle.forward(lineLen)
        turtle.right(90)
        drawSpiral(turtle, lineLen - 5)

# drawSpiral(myTurtle, 300)
# myWin.exitonclick()


def drawTree(tree, branchLen):
    if branchLen > 5:
    	time.sleep(1)
    	tree.forward(branchLen)
    	tree.right(20)
    	drawTree(tree, branchLen - 10)
    	tree.left(40)
    	drawTree(tree, branchLen - 10)
    	tree.right(20)
    	tree.backward(branchLen)

def main():
	tree = turtle.Turtle()
	myWin = turtle.Screen()
	tree.left(70)
	tree.up()
	tree.backward(100)
	tree.down()
	tree.color("green")
	drawTree(tree, 75)
	myWin.exitonclick()

main()
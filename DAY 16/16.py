import turtle

obj1=turtle.Turtle()
obj1.shape('turtle')
obj1.color('green')
print(obj1)
obj1.forward(100.00)
screen=turtle.Screen()
print(screen.canvheight)
screen.exitonclick()

#importing from PyPi
import prettytable
table=prettytable.PrettyTable()
table.field_names=['First Name','Last Name','Age','Gender','Degree','Year']
table.add_row(['Shreya','Shastry','19','Female','AIML','II'])
table.align='l'
print(table)


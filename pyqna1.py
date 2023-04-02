//1 Multiply list
list = [1,2,3,4,5,6]
ans = 1
for i in list:
    ans *= i
print(ans)

//2 String Count
List = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in List:
    if i.isalpha():
        count += 1
print(count)

//3 Move Zero
list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
print(list)
c = 0
for i in list:
    if i == 0:
        list.remove(i)
        list.append(0)
print(list)

//4 shape turtle
from turtle import *
speed(0)
# square
penup()
goto(-300,-50)
pendown()
fillcolor('red')
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()


#rectangle
penup()
goto(-100,-50)
pendown()
fillcolor('blue')
begin_fill()
for i in range(2):
    forward(200)
    left(90)
    forward(100)
    left(90)
end_fill()

#hexagon with triangle
penup()
goto(240,-60)
pendown()
fillcolor('green')
begin_fill()
left(30)
for i in range(6):
    forward(60)  
    left(60)
end_fill()
left(120)
forward(60)
right(150)

fillcolor('yellow')
begin_fill()
for i in range(3):
    forward(105)
    left(120)
end_fill()
hideturtle()
done()

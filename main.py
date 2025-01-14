from turtle import Turtle,Screen
import random
line1=Turtle()
line2=Turtle()
def start_line():
    line2.hideturtle()
    line1.penup()
    line1.goto(-210,-105)

    line1.setheading(90)
    line1.pendown()
    line1.color('white')
    line1.forward(310)
    line1.hideturtle()

def finish_line():
    line2.hideturtle()
    line2.penup()
    line2.goto(210, -105)

    line2.setheading(90)
    line2.pendown()
    line2.color('white')
    line2.forward(310)

start_line()
finish_line()
screen=Screen()
screen.title('a')
players=[]
done=True
finish=False

x = -200
y = -100
speed=[1,2,3,4,5]
colors=['red','orange','yellow','green','blue','indigo','violet']
dic={
    'red':'red',
    'orange':'orange',
    'yellow':'yellow',
     'green':'green',
     'blue':'blue',
     'indigo':'indigo',
    'violet':'violet'



}
color_choice=0
player_count_float=screen.numinput(title='Number of players',
                             prompt='How many players do you want(7)')
win=screen.textinput(title='Rainbow',prompt='Who will win?')
player_count=int(player_count_float)
screen.bgcolor('brown')
for each in range(player_count):
    player=Turtle('turtle')
    player.penup()
    player.color(colors[color_choice])
    players.append(player)
    color_choice+=1
player_num=1
while done:
    for player in players:
        player.goto(x,y)
        y+=50
        player_num+=1
        if player_num==player_count:
            done=False


while finish==False:
    



    for player in players:
        if finish!=True:
            player.forward(random.choice(speed))
        if player.xcor()>=190:

            
            finish=True  
            winner=player.color()[1]
            line2.penup()
            line2.goto(-90,200)
            line2.color(dic[winner])
            line2.pendown()

            line2.write(arg=f'{winner.upper()} WINS',font=('Times New Roman',24,'bold'))

            line2.penup()
            line2.goto(-79,150)

            line2.pendown()
            if win==winner:
                line2.write(arg=f'YOU WIN ',font=('Times New Roman',24,'bold'))
            else:
                line2.write(arg=f'YOU LOSE ',font=('Times New Roman',24,'bold'))









screen.exitonclick()
import turtle as t
import math

pen = t.Turtle()
pen.hideturtle()
pen.speed(0)

def draw_circle(radius):
    """Draws a circle with given radius, centred on current pen position."""
    pen.teleport(pen.xcor(), pen.ycor() - radius)
    pen.circle(radius)
    pen.teleport(pen.xcor(), pen.ycor() + radius)


n = 5 # number of circles
scale_factor = 100
central_distance = scale_factor * 2/math.sqrt(1-math.cos(2*math.pi/n)) # distance of circle centres to the origin
angle_offset = math.pi/2 # rotates everything pi/2 radians


# finding circle centres:
centres = []
for k in range(0, n):
    centres.append((central_distance * math.cos(2*(k+1)*math.pi/n + angle_offset), central_distance * math.sin(2*(k+1)*math.pi/n + angle_offset)))

# drawing circles:
for centre in centres:
    pen.teleport(centre[0], centre[1])
    draw_circle(scale_factor)


# outer point generating functions:
def pO_A1(k):
    x = centres[k][0] - (0.25*math.sqrt(2))*(centres[(k+1)%n][1] - centres[k][1])
    y = centres[k][1] + (0.25*math.sqrt(2))*(centres[(k+1)%n][0] - centres[k][0])
    return (x,y)
def pO_A2(k):
    x = centres[(k+1)%n][0] - (0.25*math.sqrt(2))*(centres[(k+1)%n][1] - centres[k][1])
    y = centres[(k+1)%n][1] + (0.25*math.sqrt(2))*(centres[(k+1)%n][0] - centres[k][0])
    return (x,y)
def pO_B1(k):
    x = centres[k][0] + (0.25*math.sqrt(2))*(centres[(k+1)%n][1] - centres[k][1])
    y = centres[k][1] - (0.25*math.sqrt(2))*(centres[(k+1)%n][0] - centres[k][0])
    return (x,y)
def pO_B2(k):
    x = centres[(k+1)%n][0] + (0.25*math.sqrt(2))*(centres[(k+1)%n][1] - centres[k][1])
    y = centres[(k+1)%n][1] - (0.25*math.sqrt(2))*(centres[(k+1)%n][0] - centres[k][0])
    return (x,y)

# inner point generating functions:
def pI_A1(k):
    x = centres[k][0] + 0.25*((centres[(k+1)%n][0]-centres[k][0]) - (centres[(k+1)%n][1]-centres[k][1]))
    y = centres[k][1] + 0.25*((centres[(k+1)%n][0]-centres[k][0]) + (centres[(k+1)%n][1]-centres[k][1]))
    return (x,y)
def pI_A2(k):
    x = centres[k][0] + 0.25*(3*(centres[(k+1)%n][0]-centres[k][0]) + (centres[(k+1)%n][1]-centres[k][1]))
    y = centres[k][1] + 0.25*(3*(centres[(k+1)%n][1]-centres[k][1]) - (centres[(k+1)%n][0]-centres[k][0]))
    return (x,y)
def pI_B1(k):
    x = centres[k][0] + 0.25*((centres[(k+1)%n][0]-centres[k][0]) + (centres[(k+1)%n][1]-centres[k][1]))
    y = centres[k][1] + 0.25*((centres[(k+1)%n][1]-centres[k][1]) - (centres[(k+1)%n][0]-centres[k][0]))
    return (x,y)
def pI_B2(k):
    x = centres[k][0] + 0.25*(3*(centres[(k+1)%n][0]-centres[k][0]) -   (centres[(k+1)%n][1]-centres[k][1]))
    y = centres[k][1] + 0.25*(  (centres[(k+1)%n][0]-centres[k][0]) + 3*(centres[(k+1)%n][1]-centres[k][1]))
    return (x,y)


# connecting outer points:
for k in range(0, n):
    pen.teleport(pO_A1(k)[0], pO_A1(k)[1])
    pen.goto(pO_A2(k)[0], pO_A2(k)[1])
    pen.teleport(pO_B1(k)[0], pO_B1(k)[1])
    pen.goto(pO_B2(k)[0], pO_B2(k)[1])

# connecting inner points:
for k in range(0, n):
    pen.teleport(pI_A1(k)[0], pI_A1(k)[1])
    pen.goto(pI_A2(k)[0], pI_A2(k)[1])
    pen.teleport(pI_B1(k)[0], pI_B1(k)[1])
    pen.goto(pI_B2(k)[0], pI_B2(k)[1])


t.done() # keeps window open

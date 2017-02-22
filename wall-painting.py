import math

running_wall_area_total = 0
wall_area = 0
more_walls = 'y'

# get the wall's width and height from user
while  more_walls == 'y' or 'Y':
    wall_width = float(input("How wide is the wall (in feet)? >"))
    wall_height = float(input("How high is the wall (in feet)? >"))

    # calculate the area of the wall
    wall_area = int(wall_width) * int(wall_height)

    print("wall_area: " + str(wall_area))

    # keep a running total of the wall_area
    running_wall_area_total += wall_area

    # find out if there are more walls to include in calculation
    more_walls = str(input('Are there more walls? (y/n) >'))


# get the cost of paint and coats of paint from user
paint_cost = float(input("How much is a gallon of paint? >"))
coats_of_paint = float(input("How many coats are you painting? >"))


# calculate how many cans of paint the wall will need
# (math.ceil finds the smallest integer greater than or equal to)
cans_of_paint = math.ceil((wall_area * coats_of_paint) / 400)

# calculate how much the paint will cost
cost_of_paint = cans_of_paint * paint_cost

print('That is ' + str(wall_area) + ' square feet to cover.')
print('You will need ' + str(int(cans_of_paint)) + ' cans of paint '
      + 'to paint ' + str(int(coats_of_paint)) + ' coats.')
print('This will cost $' + str('{0:.2f}'.format(cost_of_paint)) + '.')

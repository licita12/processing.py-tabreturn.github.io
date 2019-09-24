# https://github.com/pybox2d/pypybox2d
# https://github.com/pybox2d/pybox2d/wiki/manual

import pypybox2d as b2
from pypybox2d.common import *

def setup():
    size(600,600)
    frameRate(60)
    ernest = createFont('Ernest.ttf', 3)
    textFont(ernest)

    # create bodies

    global world
    world = b2.World( gravity=(0,-9.8) )

    global ground
    ground = world.create_static_body(
      position = (20, 20)
    )
    ground.create_polygon_fixture(
      vertices = [(0,0), (20,0), (20,10), (0,10)],
      user_data = ['ground', '#FF9900']
    )

    global ball
    ball = world.create_dynamic_body(
      position=(20, 55)
    )
    ball.create_circle_fixture(
      1, density=1.0,
      user_data = ['ball', '#FF0000']
    )

    global trapezoid
    trapezoid = world.create_dynamic_body(
      position=(24, 40),
      #angle = HALF_PI
    )
    trapezoid.create_polygon_fixture(
      vertices = [(-1,0), (8,0), (6,6), (0,6)],
      density = 0.1,
      friction = 0.1,
      user_data = ['trapezoid', '#00FF00']
    )
    trapezoid.apply_linear_impulse( impulse=(1,0), point=(10,10) )



def draw():
    background('#004477')
    noFill()

    world.step(1.0/frameRate, 10, 10) # (time_step, velocity_iterations, position_iterations)
    world.clear_forces()

    scale(1,-1)          # vetically flip the display to match the box2d y-axis (opposite of processing)
    translate(0,-height) # after flipping, offset the y-position to bring the shapes back into view
    scale(10)            # box2d is tuned for meters-kilogram-second units -- thus works best for sizes between soup cans and buses

    # x/y corner marker

    stroke('#0099FF'); strokeWeight(3.0/10); fill('#0099FF')
    pushMatrix()
    scale(1,-1); text('x:1, y:1',2,-3); line(1,-1,1,-10); line(1,-1,12,-1)
    popMatrix()
    noFill(); noStroke()

    # render bodies

    pushMatrix()
    translate(ground.position.x, ground.position.y)
    fill(ground.fixtures[0].user_data[1])
    beginShape()
    vertex(ground.fixtures[0].shape._vertices[0].x, ground.fixtures[0].shape._vertices[0].y)
    vertex(ground.fixtures[0].shape._vertices[1].x, ground.fixtures[0].shape._vertices[1].y)
    vertex(ground.fixtures[0].shape._vertices[2].x, ground.fixtures[0].shape._vertices[2].y)
    vertex(ground.fixtures[0].shape._vertices[3].x, ground.fixtures[0].shape._vertices[3].y)
    endShape(CLOSE)
    popMatrix()

    pushMatrix()
    fill(ball.fixtures[0].user_data[1])
    translate(ball.position.x, ball.position.y)
    rotate(ball.angle)
    r = ball.fixtures[0].shape.radius;
    ellipse(0, 0, r*2, r*2)
    stroke('#FFFFFF'); strokeWeight(3.0/10); line(0,0,0,0.8); noStroke()
    popMatrix()
    ball.apply_force_to_center(force=(5,0))

    pushMatrix()
    fill(trapezoid.fixtures[0].user_data[1])
    translate(trapezoid.position.x, trapezoid.position.y)
    rotate(trapezoid.angle)
    beginShape()
    vertex(trapezoid.fixtures[0].shape._vertices[0].x, trapezoid.fixtures[0].shape._vertices[0].y)
    vertex(trapezoid.fixtures[0].shape._vertices[1].x, trapezoid.fixtures[0].shape._vertices[1].y)
    vertex(trapezoid.fixtures[0].shape._vertices[2].x, trapezoid.fixtures[0].shape._vertices[2].y)
    vertex(trapezoid.fixtures[0].shape._vertices[3].x, trapezoid.fixtures[0].shape._vertices[3].y)
    endShape(CLOSE)
    popMatrix()

    # collisions

    cm = world.contact_manager

    for contact in ball.contact_list:
        if contact.touching:
            #print('fixture a: ' + contact.fixture_a.user_data[0])
            #print('fixture b: ' + contact.fixture_b.user_data[0])
            if contact.fixture_a.user_data[0] == 'ground':
                ball.fixtures[0].user_data[1] = ground.fixtures[0].user_data[1]
            elif contact.fixture_a.user_data[0] == 'trapezoid':
                ball.fixtures[0].user_data[1] = trapezoid.fixtures[0].user_data[1]

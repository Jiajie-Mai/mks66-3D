from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 0, 0 ]
edges = []
transform = new_matrix()

clear_screen(screen)

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

#add_box(edges,0,200,0,200,100,400)
i = 0
while i <= 500:
    add_sphere( edges, 250, 250, 250, 100 + i, 0.1 )
    add_torus( edges, 250, 250, 250, 100 + i, 50 + i / 2, 0.1 )
    draw_lines(edges, screen, color)
    edges = []
    i += 100

draw_lines(edges, screen, color)
display(screen)
save_extension(screen, args[0])

parse_file( 'script', edges, transform, screen, color )

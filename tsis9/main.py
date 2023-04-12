# importing necessary packages
import pygame, sys
import math


# general game configueration
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# global objects list to work with it inside classes without implicitly importing through arguments
objects = []

# color pallete
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}
# setting the global variable for current_color in order to be able to assign and change new color for new object
current_color = colors['black']



# class for Point of a brush
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# general game object that other classes will inherit
class GameObject:
    def update(self, curr_point):
        return
    
    def draw(self):
        return
    

# class for Rectangle Button
class RectButton(GameObject):
    def __init__(self):
        # attributes of rectangle button
        self.width = 50
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - self.width, 20, self.width, self.width)
        self.isButton = True
        self.tool = Rectangle
    
    # draw rectangle button on the surface
    def draw(self, surf):
        pygame.draw.rect(surf, (255, 0, 0), self.rect, width = 5)

# class for Circle button
class CircleButton(GameObject):
    def __init__(self):
        # attributese of a circle button
        self.radius = 25
        self.rect = pygame.draw.circle(screen, (255, 0, 0), (SCREEN_WIDTH // 2 + 3 * self.radius, self.radius + 20), self.radius)
        self.isButton = True
        self.tool = Circle

    # drawing circle button on the surface
    def draw(self, surf):
        pygame.draw.circle(screen, (255, 0, 0), (SCREEN_WIDTH // 2 + 3 * self.radius, self.radius + 20), self.radius, width = 5)



# class for Brush button
class BrushButton(GameObject):
    def __init__(self):
        # attributes of a brush button
        self.width = 50
        # importing brush png image for button
        self.image = pygame.transform.scale(pygame.image.load('brush.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topright = (SCREEN_WIDTH // 2 + self.width, 20)
        self.isButton = True
        self.tool = Pen

    # drawing brush button on the surface
    def draw(self, surf):
        surf.blit(self.image, self.rect)


# class for eraser button
class EraserButton(GameObject):
    # attributes of the eraser button
    def __init__(self):
        #
        self.width = 50
        # importing png image of an eraser
        self.image = pygame.transform.scale(pygame.image.load('eraser.png'), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.topright = (SCREEN_WIDTH // 2 + 3 * self.width, 20)
        self.isButton = True
        self.tool = Eraser

    # drawing eraser button on the screen
    def draw(self, surf):
        surf.blit(self.image, self.rect)

class ColorButton(GameObject):
    def __init__(self, *args, **kwargs):
        self.width = 20
        self.color = kwargs['color']
        self.rect = pygame.Rect(*kwargs['pos'], self.width, self.width)

    def draw(self, surf):
        pygame.draw.rect(surf, colors[self.color], self.rect)


class RightTriangleButton(GameObject):
    def __init__(self):
        self.width = 50
        self.image = pygame.transform.scale(pygame.image.load('right_triangle.png'), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.topright = (SCREEN_WIDTH // 2 + 4 * self.width, 20)
        self.isButton = True
        self.tool = RightTriangle

    def draw(self, surf):
        surf.blit(self.image, self.rect)


class SquareButton(GameObject):
    def __init__(self):
        self.width = 50
        self.image = pygame.transform.scale(pygame.image.load('square.png'), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.topright = (SCREEN_WIDTH // 2 + 5 * self.width, 20)
        self.isButton = True
        self.tool = Square

    def draw(self, surf):
        surf.blit(self.image, self.rect)

class EquilateralTriangleButton(GameObject):
    def __init__(self):
        self.width = 50
        self.image = pygame.transform.scale(pygame.image.load('equalitarial_triangle.png'), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.topright = (SCREEN_WIDTH // 2 + 6 * self.width, 20)
        self.isButton = True
        self.tool = EquilateralTriangle

    def draw(self, surf):
        surf.blit(self.image, self.rect)

class RhombusButton(GameObject):
    def __init__(self):
        self.width = 50
        self.image = pygame.transform.scale(pygame.image.load('rhombus.png'), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.topright = (SCREEN_WIDTH // 2 + 7 * self.width, 20)
        self.isButton = True
        self.tool = Rhombus

    def draw(self, surf):
        surf.blit(self.image, self.rect)


        

# class for Brush(Pen) drawing tool
class Pen(GameObject):
    # attributes of an Pen class
    def __init__(self, *args, **kwargs):
        # list of points that Pen will draw
        self.points: list(Point, ...) = []
        # image to replace mouse cursor with brush
        self.image = pygame.transform.scale(pygame.image.load('brush.png'), (40, 40))
        self.pos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.pos
        self.color = current_color

    def draw(self, surf, *args, **kwargs):
        # looping thorugh list of points and drawing lines between them
        for id, curr_point in enumerate(self.points[:-1]):
            next_point = self.points[id + 1]
            pygame.draw.line(surf, self.color, 
                             (curr_point.x, curr_point.y), (next_point.x, next_point.y), width = 5)


    # updating current pen class
    def update(self, curr_point):
        # appending new points into the points list
        self.points.append(Point(*curr_point))
        # changing the rect coordinates of an brush cursor
        self.rect.bottomleft = curr_point
        # drawing brush cursor on the position of cursor
        screen.blit(self.image, self.rect)
    
    
# class for Rectangle drawing tool
class Rectangle(GameObject):
    def __init__(self, init_point, *args, **kwargs):
        # attributes
        self.start_point = Point(*init_point)
        self.end_point = Point(*init_point)
        self.color = current_color
        self.rect = pygame.Rect(self.start_point.x, self.start_point.y, 0, 0)
        

    def draw(self, surf, *args, **kwargs):
        # getting the start (top left) and end (bottom right) points of a rectangle
        start_point_x = min(self.start_point.x, self.end_point.x)
        start_point_y = min(self.start_point.y, self.end_point.y)

        end_point_x = max(self.start_point.x, self.end_point.x)
        end_point_y = max(self.start_point.y, self.end_point.y)

        # drawing rectangle based on the start and end points and updating rect attribute
        self.rect = pygame.draw.rect(surf, self.color, (start_point_x, start_point_y, end_point_x - start_point_x, end_point_y - start_point_y), width = 5)
    
    # updating end points of an rectangle
    def update(self, curr_point):
        self.end_point.x, self.end_point.y = curr_point


# class for Circle drawing tool
class Circle(GameObject):
    def __init__(self, init_point, *args, **kwargs):
        # attributes of a circle
        self.center_point = Point(*init_point)
        self.radius = 0
        self.rect = pygame.draw.circle(screen, (0, 0, 0), init_point, self.radius, width = 5)
        self.color = current_color


    def draw(self, surf, *args, **kwargs):
        # drawing circle on the surface and updating its rect object
        self.rect = pygame.draw.circle(surf, self.color, (self.center_point.x, self.center_point.y), self.radius, width = 5)


    # update radius attribute of a circle
    def update(self, curr_point):
        self.radius = math.fabs(curr_point[0]- self.center_point.x)

# class for Eraser tool
class Eraser(GameObject):
    def __init__(self, *args, **kwargs):
        self.pos = pygame.mouse.get_pos()
        self.image = pygame.transform.scale(pygame.image.load('eraser.png'), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.pos
        

    # method for erasing (deleting) objects
    def draw(self, surf):
        # looping through all the objects on the screen
        for i, obj in enumerate(objects):
            # check if the object is not a button object
            if not hasattr(obj, 'isButton'):
                # checking if rect attribute of an object collides with current position of eraser
                if obj.rect.collidepoint(self.pos):
                    objects.remove(obj)
                # checking if it is pen object by checking does the object has points attribute
                if hasattr(obj, 'points'):
                    # looping through each point in a list of points
                    for point in obj.points:
                        # if a point in a list collides with a eraser rectangle in the cursor position, empty the list of points
                        if self.rect.collidepoint(point.x, point.y):
                            obj.points = []
        # return modified list of objects
        return objects


    # update the current poisiton of the eraser
    def update(self, curr_point):
        self.pos = curr_point
        self.rect.bottomright = self.pos
        screen.blit(self.image, self.rect)



class RightTriangle(GameObject):
    def __init__(self, init_point, *args, **kwargs):
        self.start_point = Point(*init_point)
        self.color = current_color
        self.end_point = Point(*init_point)
        self.rect = pygame.Rect(self.start_point.x, self.start_point.y, self.end_point.x - self.start_point.x, self.end_point.y - self.start_point.y)

    def draw(self, surf):

        third_point_x = self.start_point.x
        third_point_y = self.end_point.y

        pygame.draw.line(surf, self.color, (self.start_point.x, self.start_point.y),(third_point_x, third_point_y), width=5)
        pygame.draw.line(surf, self.color, (third_point_x, third_point_y), (self.end_point.x, self.end_point.y), width=5)
        pygame.draw.line(surf, self.color, (self.start_point.x, self.start_point.y), (self.end_point.x, self.end_point.y), width=5)




    def update(self, curr_point):
        self.end_point.x, self.end_point.y = curr_point
        start_point_x = min(self.start_point.x, self.end_point.x)
        start_point_y = min(self.start_point.y, self.end_point.y)
        self.rect = pygame.Rect(start_point_x, start_point_y, abs(self.end_point.x - self.start_point.x), abs(self.end_point.y - self.start_point.y))


        
class Square(GameObject):
    def __init__(self, init_point, *args, **kwargs):
        self.start_point = Point(*init_point)
        self.end_point = Point(*init_point)
        self.color = current_color
        self.rect = pygame.Rect(self.start_point.x, self.start_point.y, abs(self.start_point.x - self.end_point.x), abs(self.start_point.y - self.end_point.y))
        self.width = abs(self.start_point.x - self.end_point.x)

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, width = 5)

    def update(self, curr_point):
        self.end_point.x, self.end_point.y = curr_point
        start_point_x = min(self.start_point.x, self.end_point.x)
        start_point_y = min(self.start_point.y, self.end_point.y)

        x_diff = abs(self.start_point.x - self.end_point.x)
        y_diff = abs(self.start_point.y - self.end_point.y)
        self.width = min(x_diff, y_diff)

        self.rect = pygame.Rect(start_point_x, start_point_y, self.width, self.width)


class EquilateralTriangle(GameObject):
    def __init__(self, init_point, *args, **kwargs):
        self.start_point = Point(*init_point)
        self.end_point = Point(*init_point)
        self.color = current_color
        self.rect = pygame.Rect(self.start_point.x, self.start_point.y, 0, 0)
        self.width = 0
    
    def draw(self, surf):
        point1 = (self.rect.left, self.rect.bottom) 
        point2 = (self.rect.centerx, self.rect.top)
        point3 = (self.rect.right, self.rect.bottom)
        pygame.draw.line(surf, self.color, point1, point2, width=5)
        pygame.draw.line(surf, self.color, point2, point3, width=5)
        pygame.draw.line(surf, self.color, point1, point3, width=5)

    def update(self, curr_point):
        self.end_point.x, self.end_point.y = curr_point

        x_diff = self.end_point.x - self.start_point.x
        y_diff = self.end_point.y - self.start_point.y
        self.width = min(abs(x_diff), abs(y_diff))

        start_point_x= min(self.start_point.x, self.end_point.x)
        start_point_y = min(self.start_point.y ,self.end_point.y)

        self.rect = pygame.Rect(start_point_x, start_point_y, self.width, self.width)


class Rhombus(GameObject):
    def __init__(self, init_point, *args, **kwargs):
        self.start_point = Point(*init_point)
        self.end_point = Point(*init_point)
        self.color = current_color
        self.rect = pygame.Rect(self.start_point.x, self.start_point.y, 0, 0)

    def draw(self, surf):

        point1 = (self.rect.left, self.rect.centery)
        point2 = (self.rect.centerx, self.rect.top)
        point3 = (self.rect.right, self.rect.centery)
        point4 = (self.rect.centerx, self.rect.bottom)
        pygame.draw.line(surf, self.color, point1, point2, width=5)
        pygame.draw.line(surf, self.color, point2, point3, width=5)
        pygame.draw.line(surf, self.color, point3, point4, width=5)
        pygame.draw.line(surf, self.color, point4, point1, width=5)


    def update(self, curr_point):
        self.end_point.x, self.end_point.y = curr_point

        x_diff = abs(self.start_point.x - self.end_point.x)
        y_diff = abs(self.start_point.y - self.end_point.y)

        start_point_x = min(self.start_point.x, self.end_point.x)
        start_point_y = min(self.start_point.y ,self.end_point.y)

        self.rect = pygame.Rect(start_point_x, start_point_y, x_diff, y_diff)


        


def main():
    # set objects global to be able to modify it outside of the main function
    global objects
    global current_color
    # initializing all objects and buttons
    game_obj = GameObject()
    active_obj = game_obj
    curr_shape = Pen
    rect_button = RectButton()
    circle_button = CircleButton()
    eraser_button = EraserButton()
    brush_button = BrushButton()
    right_triangle_button = RightTriangleButton()
    square_button = SquareButton()
    eq_triangle_button = EquilateralTriangleButton()
    rhombus_button = RhombusButton()
    red_button = ColorButton(color = 'red', pos = (100, 20))
    blue_button = ColorButton(color = 'blue', pos = (120, 20))
    green_button = ColorButton(color = 'green', pos = (100, 40))
    black_button = ColorButton(color = 'black', pos = (120, 40))
    objects = [rect_button, circle_button, eraser_button, brush_button, right_triangle_button, square_button, eq_triangle_button, rhombus_button, red_button, blue_button, green_button, black_button]

    menu_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT // 4))


    # main game cycle
    while True:
        # filling screen with white colro
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            # if mouse button is pressed down
            if event.type == pygame.MOUSEBUTTONDOWN:
                # set default mouse cursor invisible
                pygame.mouse.set_visible(False)
                # if cursor pressed on specific button, change the current object to the buttons

                if rect_button.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = Rectangle
                elif circle_button.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = Circle
                elif eraser_button.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = Eraser
                elif brush_button.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = Pen
                elif right_triangle_button.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = right_triangle_button.tool
                elif square_button.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = square_button.tool
                elif eq_triangle_button.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = eq_triangle_button.tool
                elif rhombus_button.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = rhombus_button.tool
                elif red_button.rect.collidepoint(pygame.mouse.get_pos()):
                    current_color = colors[red_button.color]
                elif blue_button.rect.collidepoint(pygame.mouse.get_pos()):
                    current_color = colors[blue_button.color]
                elif green_button.rect.collidepoint(pygame.mouse.get_pos()):
                    current_color = colors[green_button.color]
                elif black_button.rect.collidepoint(pygame.mouse.get_pos()):
                    current_color = colors[black_button.color]
                else:
                    # adding the object into the general objects list to draw it on the screen
                    active_obj = curr_shape(init_point=pygame.mouse.get_pos())
                    objects.append(active_obj)

            if event.type == pygame.MOUSEMOTION:
                # update the attributes of an current active drawing tool
                active_obj.update(curr_point=pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                # after pressing up mouse button, set the active object to default game object
                active_obj = game_obj
                pygame.mouse.set_visible(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # change the color of an object
                    current_color = colors['red']
                if event.key == pygame.K_b:
                    current_color = colors['black']
                if event.key == pygame.K_g:
                    current_color= colors['green']
            

            
            for obj in objects:
                if obj == Eraser:
                    objects = obj.draw(screen)
                else:
                    obj.draw(screen)


            pygame.display.flip()
            clock.tick(FPS)
            
    

if __name__ == "__main__":
    main()
import pygame
import math
import time
from pygame.locals import *
pygame.init()

width, height = 800, 600

colors = {
    'white': (255, 255, 255),
    'blackish' : (113, 113, 194),
    'black': (0, 0, 0),
    'green': (0, 255, 0),
    'red': (255, 0, 0),
    'brown': (255, 136, 0),
    'yellow': (255, 255, 0)
}

fps = 60
surf = pygame.display.set_mode((width, height))

#buttons and icons
brush = pygame.image.load("brush.png")
erase = pygame.image.load("eraser.png")
brush_icon = pygame.transform.scale(brush, (65, 65))
pygame.display.set_caption("Paint")
buttons_here = pygame.Rect(100,100, 0, 0)

objects = []
current_color = colors['blackish']
run = True

class mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class buttons:

    def __init__(self):
        pass

    def update(self, curr_point):
        return
    
    def draw(self):
        return
    
class rectangle(buttons):
    def __init__(self):
        self.width = 69
        self.rect = pygame.Rect(width // 2 - self.width, 20, self.width, self.width)
        self.isButton = True
        self.tool = Rectangle
    def draw(self, surf):
        pygame.draw.rect(surf, colors['blackish'], self.rect, width = 5)

class circle(buttons):
    def __init__(self):
        self.radius = 25
        self.rect = pygame.draw.circle(surf, (255, 0, 0), (width // 2 + 3 * self.radius, self.radius + 20), self.radius)
        self.isButton = True
        self.tool = Circle
    def draw(self, surf):
        pygame.draw.circle(surf, colors['blackish'], (width // 2 + 3 * self.radius, self.radius + 20), self.radius, width = 10)


class brush(buttons):
    def __init__(self):
        self.width = 50
        self.image = pygame.transform.scale(pygame.image.load('brush.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topright = (width// 2 + self.width, 20)
        self.isButton = True
        self.tool = Brush
    def draw(self, surf):
        surf.blit(self.image, self.rect)

class erase(buttons):
    def __init__(self):
        self.width = 50
        self.image = pygame.transform.scale(pygame.image.load('eraser.png'), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.topright = (width // 2 + 3 * self.width, 20)
        self.isButton = True
        self.tool = Eraser
    def draw(self, surf):
        surf.blit(self.image, self.rect)

class color(buttons):
    def __init__(self, *args, **kwargs):
        self.width = 20
        self.color = kwargs['color']
        self.rect = pygame.Rect(*kwargs['pos'], self.width, self.width)
    def draw(self, surf):
        pygame.draw.rect(surf, colors['black'], self.rect)

class right_three(buttons):
    def __init__(self):
        self.width = 50
        self.image = pygame.transform.scale(pygame.image.load('right_triangle.png'), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.topright = (width // 2 + 4 * self.width, 20)
        self.isButton = True
        self.tool = Right_three
    def draw(self, surf):
        surf.blit(self.image, self.rect)

class square(buttons):
    def __init__(self):
        self.width = 50
        self.image = pygame.transform.scale(pygame.image.load('square.png'), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.topright = (width // 2 + 5 * self.width, 20)
        self.isButton = True
        self.tool = square
    def draw(self, surf):
        surf.blit(self.image, self.rect)

class triangle(buttons):
    def __init__(self):
        self.width = 50
        self.image = pygame.transform.scale(pygame.image.load('equalitarial_triangle.png'), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.topright = (width // 2 + 6 * self.width, 20)
        self.isButton = True
        self.tool = Three
    def draw(self, surf):
        surf.blit(self.image, self.rect)

class rhomb(buttons):
    def __init__(self):
        self.width = 50
        self.image = pygame.transform.scale(pygame.image.load('rhombus.png'), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.topright = (width// 2 + 7 * self.width, 20)
        self.isButton = True
        self.tool = Rhomb
    def draw(self, surf):
        surf.blit(self.image, self.rect)

class Brush(buttons):
    def __init__(self, *args, **kwargs):
        self.points: list(mouse, ...) = []
        self.image = pygame.transform.scale(pygame.image.load('brush.png'), (40, 40))
        self.pos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.pos
        self.color = current_color

    def draw(self, surf, *args, **kwargs):
        for id, curr_point in enumerate(self.points[:-1]):
            next_point = self.points[id + 1]
            pygame.draw.line(surf, self.color,(curr_point.x, curr_point.y), (next_point.x, next_point.y), width = 5)
    def update(self, curr_point):
        self.points.append(mouse(*curr_point))
        self.rect.bottomleft = curr_point
        surf.blit(self.image, self.rect)


class Rectangle(buttons):
    def __init__(self, init_point, *args, **kwargs):
        # attributes
        self.start_point = mouse(*init_point)
        self.end_point = mouse(*init_point)
        self.color = current_color
        self.rect = pygame.Rect(self.start_point.x, self.start_point.y, 0, 0)
        

    def draw(self, surf, *args, **kwargs):
        start_point_x = min(self.start_point.x, self.end_point.x)
        start_point_y = min(self.start_point.y, self.end_point.y)
        end_point_x = max(self.start_point.x, self.end_point.x)
        end_point_y = max(self.start_point.y, self.end_point.y)
        self.rect = pygame.draw.rect(surf, self.color, (start_point_x, start_point_y, end_point_x - start_point_x, end_point_y - start_point_y), width = 5)
    def update(self, curr_point):
        self.end_point.x, self.end_point.y = curr_point

class Circle(buttons):
    def __init__(self, init_point, *args, **kwargs):
        self.center_point = mouse(*init_point)
        self.radius = 0
        self.rect = pygame.draw.circle(surf, (0, 0, 0), init_point, self.radius, width = 5)
        self.color = current_color
    def draw(self, surf, *args, **kwargs):
        self.rect = pygame.draw.circle(surf, self.color, (self.center_point.x, self.center_point.y), self.radius, width = 5)
    def update(self, curr_point):
        self.radius = math.fabs(curr_point[0]- self.center_point.x)

class Eraser(buttons):
    def __init__(self, *args, **kwargs):
        self.pos = pygame.mouse.get_pos()
        self.image = pygame.transform.scale(pygame.image.load('eraser.png'), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.pos
    def draw(self, surf):
        for i, obj in enumerate(objects):
            if not hasattr(obj, 'isButton'):
                if obj.rect.collidepoint(self.pos):
                    objects.remove(obj)
                if hasattr(obj, 'points'):
                    for point in obj.points:
                        if self.rect.collidepoint(point.x, point.y):
                            obj.points = []
        return objects
    def update(self, curr_point):
        self.pos = curr_point
        self.rect.bottomright = self.pos
        surf.blit(self.image, self.rect)

class Right_three(buttons):
    def __init__(self, init_point, *args, **kwargs):
        self.start_point = mouse(*init_point)
        self.color = current_color
        self.end_point = mouse(*init_point)
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

class Square(buttons):
    def __init__(self, init_point, *args, **kwargs):
        self.start_point = mouse(*init_point)
        self.end_point = mouse(*init_point)
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

class Three(buttons):
    def __init__(self, init_point, *args, **kwargs):
        self.start_point = mouse(*init_point)
        self.end_point = mouse(*init_point)
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

class Rhomb(buttons):
    def __init__(self, init_point, *args, **kwargs):
        self.start_point = mouse(*init_point)
        self.end_point = mouse(*init_point)
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
    global objects
    global current_color, active_obj, curr_shape, menu_surface
    active_obj= buttons()
    curr_shape = Brush()
    rect_button = rectangle()
    circle_button = circle()
    eraser_button = brush()
    brush_button = erase()
    right_triangle_button = right_three()
    square_button = square()
    eq_triangle_button = triangle()
    rhombus_button = rhomb()
    red_button = color(color = 'red', pos = (100, 20))
    blue_button = color(color = 'blue', pos = (120, 20))
    green_button = color(color = 'green', pos = (100, 40))
    black_button = color(color = 'black', pos = (120, 40))
    objects = [rect_button, circle_button, eraser_button, brush_button, right_triangle_button, square_button, eq_triangle_button, rhombus_button, red_button, blue_button, green_button, black_button]

    menu_surface = pygame.Surface((width, height // 4))



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                  
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_visible(False)
                if rectangle.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = Rectangle
                elif circle.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = Circle
                elif brush.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = Eraser
                elif erase.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = Brush
                elif right_three.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = right_three.tool
                elif square.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = square.tool
                elif triangle.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = triangle.tool
                elif rhomb.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = rhomb.tool
                else:
                    active_obj = curr_shape(init_point=pygame.mouse.get_pos())
                    objects.append(active_obj)
        if event.type == pygame.MOUSEMOTION:
                active_obj.update(curr_point=pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
                active_obj = buttons()
                pygame.mouse.set_visible(True)
                surf.fill(colors['white'])

    
    pygame.draw.rect(surf, colors['blackish'], pygame.Rect(0, 0, 900, 100))
    pygame.draw.rect(surf, colors['green'], pygame.Rect(250, 30, 47, 47), 0, 13)
    pygame.draw.rect(surf, colors['red'], pygame.Rect(310, 30, 47, 47), 0, 13)
    pygame.draw.rect(surf, colors['brown'], pygame.Rect(370, 30, 47, 47), 0 , 13)
    pygame.draw.rect(surf, colors['yellow'], pygame.Rect(430, 30, 47, 47), 0, 13)

    pygame.draw.rect(surf, colors['black'], pygame.Rect( 180 , 26, 50, 50))
    pygame.draw.circle(surf, colors['black'], (120, 45), 30)
    surf.blit(brush_icon, (10 , 10))

    for obj in objects:
                if obj == Eraser:
                    objects = obj.draw(surf)
                else:
                    obj.draw(surf)


    pygame.display.flip()
            
    

    if __name__ == "__main__":
            main()
    surf.fill(colors['white'])

    
    pygame.draw.rect(surf, colors['blackish'], pygame.Rect(0, 0, 900, 100))
    pygame.draw.rect(surf, colors['green'], pygame.Rect(250, 30, 47, 47), 0, 13)
    pygame.draw.rect(surf, colors['red'], pygame.Rect(310, 30, 47, 47), 0, 13)
    pygame.draw.rect(surf, colors['brown'], pygame.Rect(370, 30, 47, 47), 0 , 13)
    pygame.draw.rect(surf, colors['yellow'], pygame.Rect(430, 30, 47, 47), 0, 13)

    pygame.draw.rect(surf, colors['black'], pygame.Rect( 180 , 26, 50, 50))
    pygame.draw.circle(surf, colors['black'], (120, 45), 30)
    surf.blit(brush_icon, (10 , 10))
    


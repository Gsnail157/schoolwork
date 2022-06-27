import pygame
import abc

LENGTH = 500


class Drawable(metaclass=abc.ABCMeta):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getLoc(self):
        return (self.__x, self.__y)

    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]

    @abc.abstractmethod
    def draw(self, surface):
        pass


class Rectangle(Drawable):
    def __init__(self, x, y, width, height, color):
        Drawable.__init__(self, x, y)
        self.__width = width
        self.__height = height
        self.__color = color

    def draw(self, surface):
        x, y = self.getLoc()
        pygame.draw.rect(surface, self.__color,
                         (x, y, self.__width, self.__height))


class Snowflake(Drawable):
    def __init__(self, x, y, color):
        Drawable.__init__(self, x, y)
        self.__color = color
        self.__y = y
        self.__x = x

    def fall(self):

        if self.__y > LENGTH - 100:
            self.__y += 0
        else:
            self.__y += 1

    def draw(self, surface):

        pygame.draw.line(surface, self.__color, (self.__x - 5,
                         self.__y), (self.__x + 5, self.__y), 1)
        pygame.draw.line(surface, self.__color, (self.__x,
                         self.__y - 5), (self.__x, self.__y + 5), 1)
        pygame.draw.line(surface, self.__color, (self.__x - 5,
                         self.__y - 5), (self.__x + 5, self.__y + 5), 1)
        pygame.draw.line(surface, self.__color, (self.__x - 5,
                         self.__y + 5), (self.__x + 5, self.__y - 5), 1)

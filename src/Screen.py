import pygame 

class Screen( object ):
    def __init__( self, size ):
        self.size = size 
        self.screen = None 
        self.image = pygame.Surface( self.size )


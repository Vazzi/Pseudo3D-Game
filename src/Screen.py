import pygame 

class Screen( object ):
    def __init__( self, size ):
        self.size = size 
        self.screen = None 
        self.surface = pygame.Surface( self.size )

    def eventHandle( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            elif event.type == pygame.KEYDOWN:
                return self.eventKeyDown( event.key )
        return 0


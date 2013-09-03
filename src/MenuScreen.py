import pygame
from Screen import Screen

class MenuScreen( Screen ):
    def __init__( self, size ):
        super( MenuScreen, self).__init__( size )

    def render( self ):

        self.image.fill(( 255,255,255 ))
        return self.image

    def eventHandle( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    return 2 
        return 0

    
    def update( self ):
        return self.eventHandle()


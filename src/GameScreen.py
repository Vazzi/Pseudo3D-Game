import pygame
from Screen import Screen

class GameScreen( Screen ):
    def __init__( self, size ):
        super( GameScreen, self ).__init__( size )

    def render( self ):
        pixels = pygame.PixelArray( self.surface ) 
        width = self.size[0]
        height = self.size[1]
        for y in range( 0, height ):
            for x in range( 0, width ):
                color = pixels[x, y]
                color = ( color + x ) 
                pixels[x, y ] = color 
        self.surface = pixels.make_surface()

        return self.surface 
    

    def eventKeyDown( self, key ):
        if key == pygame.K_ESCAPE: 
            return 2 
        return 0

    def update( self ): 
        return self.eventHandle()

    def restart( self ):
        self.surface.fill(( 0,0,0 ))

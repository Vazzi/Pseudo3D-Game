import pygame
from Screen import Screen

class GameScreen( Screen ):
    def __init__( self, size ):
        super( GameScreen, self ).__init__( size )

    def render( self ):
        pixels = pygame.PixelArray( self.image ) 
        width = self.size[0]
        height = self.size[1]
        for y in range( 0, height ):
            for x in range( 0, width ):
                color = pixels[x, y]
                color = ( color + x ) 
                pixels[x, y ] = color 
        self.image = pixels.make_surface()

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

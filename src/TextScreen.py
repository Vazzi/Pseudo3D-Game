import pygame
from Screen import Screen
from Font import Font

class TextScreen( Screen ):
    def __init__( self, size, title ):
        super( TextScreen, self ).__init__( size )
        self.surface.fill(( 0,0,0 ))
        self.text = Font()
        self.text.createTextAt( self.surface, title, 5 )
        self.text.createTextAt( self.surface, "-" * ( len( title ) + 2 ), 14 )
        

    def setText( self, text ):
        lines = text.splitlines()
        y = 25 
        for line in lines:
            self.text.createTextAt( self.surface, line, y)
            y += 10

    def render( self ):
        return self.surface

    def update( self ):
        return self.eventHandle()

    def eventKeyDown( self, key ):
        if key == pygame.K_ESCAPE:
            return 1
        elif key == pygame.K_SPACE or key == pygame.K_RETURN:
            return 1
        return 0

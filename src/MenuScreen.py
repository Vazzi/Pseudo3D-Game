import pygame
from Screen import Screen
from Font import Font

class MenuScreen( Screen ):
    def __init__( self, size ):
        super( MenuScreen, self ).__init__( size )
        self.title = Font()
        self.image.fill((0,0,0))
        self.options = ( 25,  40, 55, 70 )
        self.title.createTextAt( self.image, "MENU", 5 )
        self.title.createTextAt( self.image, "------", 14 )
        self.title.createTextAt( self.image, "Resume", self.options[0] )
        self.title.createTextAt( self.image, "New Game", self.options[1] )
        self.title.createTextAt( self.image, "About", self.options[2] )
        self.title.createTextAt( self.image, "Exit", self.options[3] )
        self.selected = 0
        self.selCol = ( 255, 0, 0 )
        self.unselCol = ( 255, 255, 255 )
        self.title.changeTextColorAt( self.image, 25, self.unselCol, self.selCol )

    def render( self ):
        return self.image

    def eventHandle( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    return 2 
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    return self.optionPicked()
                elif event.key == pygame.K_UP:
                    self.changeOption( len( self.options ) - 1  )
                elif event.key == pygame.K_DOWN:
                    self.changeOption( 1 )
        return 0

    def changeOption( self, orientation ):
        self.title.changeTextColorAt( self.image, self.options[self.selected], self.selCol, self.unselCol )
        self.selected = ( self.selected + orientation ) % len( self.options )
        self.title.changeTextColorAt( self.image, self.options[self.selected], self.unselCol, self.selCol)

    def update( self ):
        return self.eventHandle()

    def optionPicked( self ):
        if self.selected == 0:
            return 2
        elif self.selected == 1:
            return 3
        elif self.selected == 2:
            return 0
        elif self.selected == 3:
            return 1
        return 0
            
    

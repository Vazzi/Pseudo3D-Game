import pygame
from Screen import Screen
from Font import Font
from TextScreen import TextScreen

class MenuScreen( Screen ):
    def __init__( self, size ):
        super( MenuScreen, self ).__init__( size )
        self.title = Font()
        self.surface.fill((0,0,0))
        self.options = ( 25,  40, 55, 70 )
        self.title.createTextAt( self.surface, "MENU", 5 )
        self.title.createTextAt( self.surface, "------", 14 )
        self.title.createTextAt( self.surface, "Resume", self.options[0] )
        self.title.createTextAt( self.surface, "New Game", self.options[1] )
        self.title.createTextAt( self.surface, "About", self.options[2] )
        self.title.createTextAt( self.surface, "Exit", self.options[3] )
        self.selected = 0
        self.selCol = ( 255, 0, 0 )
        self.unselCol = ( 255, 255, 255 )
        self.title.changeTextColorAt( self.surface, 25, self.unselCol, self.selCol )
        self.setAbout( size )
        
    def setAbout( self, size ):
        self.aboutScreen = TextScreen( size, "ABOUT" )
        aboutText = "This game is a pseudo3D\n"
        aboutText += "game. I made it because\n"
        aboutText += "I wanted to make an \n"
        aboutText += "old school game like\n"
        aboutText += "DOOM.\n"
        aboutText += "\n"
        aboutText += "Jakub Vlasak 2013"
        self.aboutScreen.setText( aboutText )
        self.isAbout = False

    def render( self ):
        if self.isAbout == True:
            return self.aboutScreen.render()
        else: 
            return self.surface


    def eventKeyDown( self, key ):
        if key == pygame.K_ESCAPE: 
            return 2 
        elif key == pygame.K_SPACE or key == pygame.K_RETURN:
            return self.optionPicked()
        elif key == pygame.K_UP:
            self.changeOption( len( self.options ) - 1  )
        elif key == pygame.K_DOWN:
            self.changeOption( 1 )
        return 0

    def changeOption( self, orientation ):
        self.title.changeTextColorAt( self.surface, self.options[self.selected], self.selCol, self.unselCol )
        self.selected = ( self.selected + orientation ) % len( self.options )
        self.title.changeTextColorAt( self.surface, self.options[self.selected], self.unselCol, self.selCol)

    def update( self ):
        if self.isAbout == True:
            if self.aboutScreen.update() == 1:
                self.isAbout = False
            return 0
        else:
            return self.eventHandle()

    def optionPicked( self ):
        if self.selected == 0:
            return 2
        elif self.selected == 1:
            return 3
        elif self.selected == 2:
            self.isAbout = True
            return 0
        elif self.selected == 3:
            return 1
        return 0
            
    

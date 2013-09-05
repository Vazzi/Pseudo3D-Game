import pygame

class Font:
    def __init__( self ):
        self.fileName = "font.png"
        self.surface = None
        self.loadFont()

    def loadFont( self ):
        self.bitmap = pygame.image.load( self.fileName )

        self.charSize = ( 6, 8 )
        self.symbols = dict()
        symbolsString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?\"''/\\<>()[]{}"        
        for i in range( 0, len( symbolsString )):
            self.symbols[symbolsString[i]] = ( i * self.charSize[0], 0 )
        symbolsString = "abcdefghijklmnopqrstuvwxyz_ "
        for i in range( 0, len( symbolsString )):
            self.symbols[symbolsString[i]] = ( i * self.charSize[0], self.charSize[1] )
        symbolsString = "0123456789+-=*:;"
        for i in range( 0, len( symbolsString )):
            self.symbols[symbolsString[i]] = ( i * self.charSize[0], self.charSize[1] * 2 )
    
    def createTextAt( self, surface, text, y ):
        width = self.charSize[0] * len(text)
        self.surface = pygame.Surface(( width, self.charSize[1] ))
        i = 0
        for symbol in text:
            location = self.symbols[symbol]
            self.surface.blit( self.bitmap, ( self.charSize[0] * i, 0 ), ( location[0], location[1], self.charSize[0], self.charSize[1] ))
            i += 1

        x = ( surface.get_width() / 2 ) - ( self.surface.get_width() / 2 )
        surface.blit( self.surface, ( x, y ))


    def changeTextColorAt( self, surface, posY, colorFrom, colorTo ):
        colorFrom = surface.map_rgb(colorFrom)
        pixels = pygame.PixelArray( surface )
        for y in range( posY, posY + self.charSize[1] ):
            for x in range( 0, surface.get_width() ):
                if pixels[ x, y ] == colorFrom:
                       pixels[ x, y ] = colorTo
        surface = pixels.make_surface()

        

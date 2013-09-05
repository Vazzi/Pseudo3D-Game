import pygame

from MenuScreen import MenuScreen 
from GameScreen import GameScreen 

class MainWindow:

    def __init__( self, size, scale ):
        self.size = size 
        self.scaledSize = tuple( i * scale for i in size )
        self.isRunning = True
        self.game = GameScreen( size )
        self.menu = MenuScreen( size )
        self.screen = self.game

    def onInit( self ):
        result = pygame.init()
        if result[1] != 0:
            return False
        self.title = "Super Pseudo3D Game"
        pygame.display.set_caption( self.title )
        self.mainSurf = pygame.display.set_mode( self.scaledSize )
        self.surface = pygame.Surface( self.scaledSize ).convert()
        self.surface.set_colorkey(( 255,0, 255 ))

    def update( self ):
        result = self.screen.update()
        if result == 1:
            self.isRunning = False
            return False
        elif result == 2:
            if isinstance(self.screen, GameScreen ) ==  True:
                self.screen = self.menu;
            elif isinstance(self.screen, MenuScreen ) == True:
                self.screen = self.game;
        return True

    def render( self ):
        self.mainSurf.fill((0,0,0))

        pygame.transform.scale( self.screen.render(), self.scaledSize, self.surface  )
        self.mainSurf.blit( self.surface , ( 0, 0 ))

        pygame.display.flip()

    def onExecute( self ):
        if self.onInit() == False:
            print( "[DEBUG] Init fails.")
            return False

        clock = pygame.time.Clock()

        while self.isRunning:
            if self.update() == False:
                break
            self.render()

            clock.tick(60)
            pygame.display.set_caption( self.title + " FPS: " + str( int( clock.get_fps()) ))
            
        pygame.quit()



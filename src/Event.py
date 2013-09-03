import pygame 

class Event:

    def __init__( self ):
       pass
    
    def handle( self ): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False




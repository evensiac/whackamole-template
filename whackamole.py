import pygame
import random
#The window should be divided into a 20x16 grid of 32x32 squares.
#The mole image should be drawn in the top left square.
#When the user clicks on the mole's square, it should move to a different random square


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        startmole = mole_image.get_rect(topleft=(0, 0))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if startmole.collidepoint(x, y):
                        x = random.randrange(0, 640//32)*32
                        y = random.randrange(0, 512//32)*32
                        startmole.topleft = (x, y)
            screen.fill("light pink")
            clock.tick(60)
            for i in range(0,512,32):
                pygame.draw.line(screen, "Black", (0, i), (640,i))
            for v in range(0,640,32):
                pygame.draw.line(screen, "Black", (v,0), (v,512))
            screen.blit(mole_image,startmole)
            pygame.display.flip()

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

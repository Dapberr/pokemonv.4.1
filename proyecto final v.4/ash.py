import pygame
import map
import Niveles_pokemon


class Ash(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstaculos):
        super().__init__(groups)

        self.image = pygame.image.load("assets/tiles/ash.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -30)

        self.direccion = pygame.math.Vector2()
        self.velocidad = 1

        self.Obstaculos = obstaculos

    def teclado(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direccion.y = -1

        elif keys[pygame.K_DOWN]:
            self.direccion.y = 1

        else:
            self.direccion.y = 0

        if keys[pygame.K_RIGHT]:
            self.direccion.x = 1

        elif keys[pygame.K_LEFT]:
            self.direccion.x = -1

        else:
            self.direccion.x = 0

    def valormapa(self, choque):
        if choque == "L":
            pygame.init()
            self.screen = pygame.display.set_mode((1000, 600))
            pygame.display.set_caption("Laboratorio")
            


        elif choque == "C":
            pygame.init()
            self.screen = pygame.display.set_mode((1000, 600))
            pygame.display.set_caption("Centro Pokemon")


        elif choque == "1":
            pygame.init()
            self.screen = pygame.display.set_mode((600,600))
            pygame.display.set_caption("Gimnasio 1")


        elif choque == "2":
            pygame.init()
            self.screen = pygame.display.set_mode((600, 600))
            pygame.display.set_caption("Gimnasio 2")


        elif choque == "3":
            pygame.init()
            self.screen = pygame.display.set_mode((600, 600))
            pygame.display.set_caption("Gimnasio 3")


        elif choque == "4":
            pygame.init()
            self.screen = pygame.display.set_mode((600, 600))
            pygame.display.set_caption("Gimnasio 4")


        elif choque == "5":
            pygame.init()
            self.screen = pygame.display.set_mode((600, 600))
            pygame.display.set_caption("Gimnasio 5")


        elif choque == "6":
            pygame.init()
            self.screen = pygame.display.set_mode((600, 600))
            pygame.display.set_caption("Gimnasio 6")


        else:
            return(choque)

    def mover(self, velocidad):
        if self.direccion.magnitude() != 0:
            self.rect.center += self.direccion * velocidad

        self.hitbox.x += self.direccion.x * velocidad
        self.colisiones("horizontal")

        self.hitbox.y += self.direccion.y * velocidad
        self.colisiones("vertical")
        self.rect.center = self.hitbox.center

    def colisiones(self, direccion):
        if direccion == "horizontal":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direccion.x > 0:
                        self.hitbox.right = sprite.rect.left
                        print("derecha")
                        Ash_top = self.hitbox.top - 13
                        Ash_margen = Ash_top % 56
                        posy = sprite.rect.top / 56
                        posx = sprite.rect.left / 64
                        if Ash_margen > 41 : posy ++1
                        if Ash_margen > 41 or Ash_margen <15:
                            print(posy)
                            print(posx)
                            choque = (map.mapa[round(posy)][round(posx)])
                            print(self.valormapa(choque))

                    if self.direccion.x < 0:
                        self.hitbox.left = sprite.rect.right
                        print("Izquierda")
                        Ash_top = self.hitbox.top - 13
                        Ash_margen = Ash_top % 56
                        posy = sprite.rect.top / 56
                        posx = (sprite.rect.right / 64)-1
                        if Ash_margen > 41 : posy ++1
                        if Ash_margen > 41 or Ash_margen <15:
                            print(posy)
                            print(posx)
                            choque = (map.mapa[round(posy)][round(posx)])
                            print(self.valormapa(choque))

        if direccion == "vertical":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direccion.y > 0:
                        self.hitbox.bottom = sprite.rect.top
                        print("abajo")
                        Ash_left = self.hitbox.left
                        Ash_margen = Ash_left % 64
                        posy = sprite.rect.top / 56
                        posx = (sprite.rect.left / 64)
                        if Ash_margen > 49 : posy ++1
                        if Ash_margen > 49 or Ash_margen <15:
                            print(posy)
                            print(posx)
                            choque = (map.mapa[round(posy)][round(posx)])
                            print(self.valormapa(choque))

                    if self.direccion.y < 0:
                        self.hitbox.top = sprite.rect.bottom + 13
                        print("arriba")

                        Ash_left = self.hitbox.left
                        Ash_margen = Ash_left % 64
                        posy = (sprite.rect.top / 56)
                        posx = (sprite.rect.left / 64)
                        if Ash_margen > 49: posy + +1
                        if Ash_margen > 49 or Ash_margen < 15:
                            print(posy)
                            print(posx)
                            choque = (map.mapa[round(posy)][round(posx)])
                            print(self.valormapa(choque))


    def update(self):
        self.teclado()
        self.mover(self.velocidad)

import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.Clock()

# image = pygame.image.load("jump.png").convert_alpha()
pygame.display.set_caption('Tuna\'s Adventure on the Underwater Complex')

font = pygame.font.Font(None, 50)



held_right = False
held_left = False



grounds = []


class Log:
    def __init__(self):
        self.rect = pygame.Rect((800, random.randrange(400, 580)), (400, 25))
    
    def update(self):
        pygame.draw.rect(screen, "Brown", self.rect)
        self.rect.x -= 5



grounds.append(Log())

log_timer = 0


class Player:
    def __init__(self):
        self.rect = pygame.Rect((400, 0), (15, 15))
        self.y_vel = 0
        self.in_air = True
        self.alive = True

    def update(self):
        if self.alive:
            text = font.render("player", False, "Black")
            screen.blit(text, (self.rect.x - (text.get_width() / 2), self.rect.y - 50))
            # screen.blit(image, self.rect)
            pygame.draw.rect(screen,"green",self.rect)

        self.y_vel += 0.5

        self.rect.y += self.y_vel
        if self.y_vel > 10: self.y_vel = 10

        on_ground = False
        for log in grounds:
            log.update()

            if not on_ground:
                if self.rect.colliderect(log.rect):
                    self.rect.bottom = log.rect.y + 1
                    self.y_vel = 0
                    self.in_air = False
                    on_ground = True
                else:
                    self.in_air = True
            if on_ground:
                self.rect.x -= 0.5

class Cirkel:
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y), (50, 50))
    
    def update(self):

        pygame.draw.rect(screen, "Red", self.rect, border_radius=25)

        if player.alive:
            if self.rect.x > player.rect.x:
                self.rect.x -= 2
            if self.rect.x < player.rect.x:
                self.rect.x += 2

            if self.rect.y > player.rect.y:
                self.rect.y -= 2
            if self.rect.y < player.rect.y:
                self.rect.y += 2

        else:
            self.rect = self.rect = pygame.Rect((0, 0), (50, 50))

        if self.rect.colliderect(player.rect):
           player.alive = False







cirkel1 = Cirkel(0, 0)
cirkel2 = Cirkel(500, 500)


player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                held_right = True
            if event.key == pygame.K_LEFT:
                held_left = True
            if event.key == pygame.K_SPACE:
                if not player.in_air:
                    player.y_vel = -15
            if event.key == pygame.K_r:
                player.rect.x = 400
                player.rect.y = 0
                player.y_vel = 0
                player.alive = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                held_right = False
            if event.key == pygame.K_LEFT:
                held_left = False

    if held_right: player.rect.x += 5
    if held_left: player.rect.x -= 5




    screen.fill("White")
    cirkel1.update()
    cirkel2.update()

    player.update()
    

    log_timer += 1

    if log_timer > 50:
        grounds.append(Log())
        log_timer = 0




    pygame.display.flip()
    clock.tick(60)
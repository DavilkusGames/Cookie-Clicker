import pygame, random

display_w = 800
display_h = 500
game_exit = False

background = pygame.image.load("img/background.png")
main_cookie = pygame.image.load("img/cookie.png")
mini_cookie = pygame.image.load("img/mini.png")
golden_cookie = pygame.image.load("img/golden_cookie.png")
X2_cookie = pygame.image.load("img/golden_cookieX2.png")

X2_label = pygame.image.load("img/X2.png")

coords_mini = (-1,-1)
coords_golden = (-1,-1)
coords_X2 = (-1,-1)

cursor = pygame.image.load("img/cursor.png")
oven = pygame.image.load("img/oven.png")
factory = pygame.image.load("img/factory.png")
rolling_pin = pygame.image.load("img/Rolling_pin.png")

costs = [25, 123, 828, 650]

cookies = 0

cursors = 0
ovens = 0
factories = 0

HaveRollingPin = False

counter = 0

prev_count_cursor = 0
prev_count_oven = 0
prev_count_factory = 0
prev_count_factory2 = 0

IsX2 = False

pygame.init()
game_display = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption('Cookie-Clicker v0.1')
clock = pygame.time.Clock()

def process_mouse(event):
    global cookies, cursors, ovens, factories, coords_mini, coords_golden, coords_X2, IsX2, HaveRollingPin
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if main_cookie.get_rect().move((10,50)).collidepoint(pos):
            cookies+=1
        elif cursor.get_rect().move((620,38)).collidepoint(pos):
            if cookies >= costs[0]:
                if cursors < 1242:
                    cookies-=costs[0] 
                    cursors+=1
                    costs[0]+=8
        elif oven.get_rect().move((602,82)).collidepoint(pos):
            if cookies >= costs[1]:
                if ovens < 1242:
                    cookies-=costs[1] 
                    ovens+=1
                    costs[1]+=13
        elif factory.get_rect().move((570,142)).collidepoint(pos):
            if cookies >= costs[2]:
                if factories < 1242:
                    cookies-=costs[2] 
                    factories+=1
                    costs[2]+=13
        elif rolling_pin.get_rect().move((563,195)).collidepoint(pos):
            if HaveRollingPin == False:
                if cookies >= costs[3]:
                    cookies-=costs[3]
                    HaveRollingPin = True
        if mini_cookie.get_rect().move(coords_mini).collidepoint(pos):
            cookies+=8
            coords_mini = (-1,-1)
        elif golden_cookie.get_rect().move(coords_golden).collidepoint(pos):
            cookies+=13
            coords_golden = (-1,-1)
        elif X2_cookie.get_rect().move(coords_X2).collidepoint(pos):
            cookies = cookies*2
            coords_X2 = (-1,-1)
            IsX2 = True
            
def draw_text(fontsize, text, coord):
    font = pygame.font.Font("fonts/Pixel.ttf", fontsize)
    text_image = font.render(text, True, (255,255,255))
    game_display.blit(text_image, coord)

def draw_texts():
    global cookies, cursors, ovens, factories, HaveRollingPin
    
    draw_text(30, "COOKIES:" + str(cookies), (70,0))
    draw_text(25, "!CLICK IT!", (80,33))
    
    draw_text(30, "SHOP:", (650,0))
    draw_text(28, "CURSOR" + str(costs[0]) + "C", (640,38))
    draw_text(28, "OVEN" + str(costs[1]) + "C", (644,90))
    draw_text(28, "FACTORY" + str(costs[2]) + "C", (612,144))
    if HaveRollingPin == False:
        draw_text(28, "ROLLINGPIN" + str(costs[3]) + "C", (580,195))
    
    draw_text(28, str(cursors) + " PCS", (50,326))
    draw_text(28, str(ovens) + " PCS", (58,380))
    draw_text(28, str(factories) + " PCS", (58,435))

def draw_shop():
    global HaveRollingPin
    
    game_display.blit(cursor, (610,38))
    game_display.blit(oven, (602,82))
    game_display.blit(factory, (570,140))
    if HaveRollingPin == False:
        game_display.blit(rolling_pin, (543,195))

def draw_improvements():
    global HaveRollingPin
    game_display.blit(cursor, (16,326))
    game_display.blit(oven, (12,368))
    game_display.blit(factory, (12,432))
    if HaveRollingPin == True:
        game_display.blit(rolling_pin, (12,5))

def game_loop(update_time):
    global game_exit, counter, prev_count_cursor, prev_count_oven, prev_count_factory, prev_count_factory2, cookies, cursors, factories, coords_mini, coords_golden, coords_X2, IsX2, HaveRollingPin
    while not game_exit:
        for event in pygame.event.get():
            process_mouse(event)
            if event.type == pygame.QUIT:
                game_exit = True
        
        game_display.blit(background, (0,0))
        
        game_display.blit(main_cookie, (8,62))
        
        draw_shop()
        draw_improvements()
        draw_texts()
        
        if not coords_mini == (-1,-1):
            game_display.blit(mini_cookie, coords_mini)
            
        if not coords_golden == (-1,-1):
            game_display.blit(golden_cookie, coords_golden)
            
        if not coords_X2 == (-1,-1):
            game_display.blit(X2_cookie, coords_X2)
            
        if IsX2 == True:
            game_display.blit(X2_label, (120,150))
        
        counter+=1
        
        if counter >= 1000:
            counter=0
            prev_count_cursor=0
            prev_count_oven=0
            prev_count_factory=0
            prev_count_factory2=0
        if counter >= prev_count_cursor + 150:
            cookies+=cursors
            prev_count_cursor=counter
            if not cursors == 0:
                probability_mini = random.randint(0,1)
                if probability_mini == 1:
                    coords_mini = (random.randint(0,800), random.randint(0,500))
                else:
                    coords_mini = (-1,-1)
        if counter >= prev_count_oven + 30:
            cookies+=ovens
            prev_count_oven=counter
            if not ovens == 0:
                probability_golden = random.randint(0,2)
                if probability_golden == 1:
                    coords_golden = (random.randint(0,800), random.randint(0,500))
                else:
                    coords_golden = (-1,-1)         
        if counter >= prev_count_factory + 18:
            cookies+=factories
            prev_count_factory=counter
            if not factories == 0:
                if HaveRollingPin == False:
                    probability_X2 = random.randint(0,3)
                    if probability_X2 == 1:
                        coords_X2 = (random.randint(0,800), random.randint(0,500))
                    else:
                        coords_X2 = (-1,-1)
                        IsX2 = False
        if counter >= prev_count_factory2 + 30:
            prev_count_factory2=counter
            if not factories == 0:
                if HaveRollingPin == True:
                    probability_X2 = random.randint(0,3)
                    if probability_X2 == 1:
                        coords_X2 = (random.randint(0,800), random.randint(0,500))
                    else:
                        coords_X2 = (-1,-1)
                        IsX2 = False               
        pygame.display.update()
        clock.tick(update_time)

game_loop(30)
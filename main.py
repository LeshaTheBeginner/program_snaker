
import pygame
import random

class Screen:
    def __init__(self):
        pygame.init()
        pygame.font.init() 
        self.width = 600
        self.height = 600
        self.size = (self.width/16,self.height/16)
        self.rows = int(self.height/self.size[0])
        self.colums = int(self.width/self.size[1])
        self.window = pygame.display.set_mode((self.width,self.height))
        self.timer = pygame.time.Clock()

        self.comic = pygame.font.SysFont('Comic Sans MS', 30)
        self.score_text = self.comic.render("", False, (255, 0, 0))
        self.highscore_text = self.comic.render("", False, (255, 255, 0))


    
    def render(self,player_list,apple,player):
        self.window.fill((0,0,0))
        j=1
        for i in player_list:
            pygame.draw.rect(self.window,(((255/len(player_list)*j)%255),(255/1.5/len(player_list)*j)%255,255-((255/len(player_list)*j)%255)),(i[0]*self.rows,i[1]*self.colums,self.rows,self.colums))
            j+=1
        pygame.draw.rect(self.window,(0,255,0),(apple[0]*self.rows,apple[1]*self.colums,self.rows,self.colums))
        pygame.draw.rect(self.window,(255,220,0),(player[0]*self.rows,player[1]*self.colums,self.rows,self.colums))

        pygame.draw.rect(self.window,(50,50,50),(1*self.rows,32*self.colums,self.rows*self.size[0]-self.rows*2,self.colums*6))
        self.window.blit(self.score_text, (self.size[0],(self.colums-1.5)*self.size[1]-self.colums-2))
        self.window.blit(self.highscore_text, (self.size[0],(self.colums-1)*self.size[1]))
        pygame.display.flip()
        
        



class Stats:            # work in progress
    def __init__(self):
        
             
        try:
            with open("highscore.txt", "r") as highscore: 
                self.highscore = int(highscore.read())
        except:
            with open("highscore.txt","w") as highscore:
                highscore.write("0")
            self.highscore = 0
            print("Couldn't read the highscore: Is the file deleted or the inside not a number? \n Reset Highscore.")
        self.score = 0
        self.time = 0
        self.score_text = "Score: " + str(0)
        self.highscore_text = "Highscore: " + str(self.highscore)

class Snake:
    def __init__(self):
        self.size = 3
        self.xy = [(2,3),(3,3),(4,3),(5,3)]
        self.current = [5,3]
        self.direction = 2 # 0 left 1 down 2 right 3 up
        self.speed = 8
    
    def movement(self):
        # 0,0 1,0 2,0 3,0 -> 1,0 2,0 3,0 3,1 ->  2,0 3,0 3,1 3,2
        if self.direction == 0:
            self.current[0] -= 1
        elif self.direction == 1:
            self.current[1] += 1
        elif self.direction == 2:
            self.current[0] += 1
        elif self.direction == 3:
            self.current[1] -= 1
        
        self.xy.append(tuple(self.current))
        self.xy.pop(0)              # starts replacing eevery xy with current, making the snake into 1 square
    
    def eat(self):
        self.xy.insert(0,(-10000000,1000000))
        


        

class Apple:
    def __init__(self):
        self.xy = (1,2)
        self.eaten=False

    def respawn(self,rows,colums,player_list):
        self.xy = (random.randint(0,rows*2),random.randint(0,colums*2))
        while(self.xy in player_list):
            self.xy = (random.randint(0,rows*2),random.randint(0,colums*2))

class GameLoop:
    def __init__(self):
        self.apple = Apple()
        self.player = Snake()
        self.screen = Screen()
        self.stats = Stats()
    
    def EventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.player.speed = 0
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if self.player.direction != 2:
                        self.player.direction = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if self.player.direction != 0:
                        self.player.direction = 2
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.player.direction != 1:
                        self.player.direction = 3
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.player.direction != 3:
                        self.player.direction = 1

    def ifeaten(self):
        if tuple(self.player.current) == self.apple.xy:
            self.apple.respawn(int(self.screen.rows),int(self.screen.colums),self.player.xy)
            self.player.eat()
            self.stats.score_text = "Score: " + str(len(self.player.xy) - 4)
    
    def death(self):
        if self.player.xy[-1] in self.player.xy[:-1]:
            self.player.speed = 0
            if len(self.player.xy)-4 > self.stats.highscore:
                with open("highscore.txt", "w") as file:
                    file.write(str(len(self.player.xy)-4))
                    print("Your highscore was beaten!")
            else:
                print(self.stats.score, " ", self.stats.highscore)



    def tick(self):
        while self.player.speed != 0:
            self.screen.timer.tick(self.player.speed)
            self.EventHandler()
            self.player.movement()

            self.death()
            self.ifeaten()
            
            self.screen.score_text = self.screen.comic.render(self.stats.score_text, False, (255, 0, 0))
            self.screen.highscore_text = self.screen.comic.render(self.stats.highscore_text, False, (255, 255, 0))
            self.screen.render(self.player.xy,self.apple.xy,self.player.current)

        pygame.quit()

a = GameLoop()
a.tick()
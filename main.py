import pygame
import os
import random
from abc import ABC, abstractmethod

'''
1. Nama Game: just RUN!
2. Kategori Game: Endless runner, Rogue-like, Side-scrolling(Left - Right)
3. Player: 1 Player
4. Class: Dino, Obstacles, Cloud, Button
5. Objek: Player, Enemies
6. Enkapsulasi: Private Attributes
7. Pewarisan: Dari kelas Obstacles : Thorn, Spike, Cactus, Bird, T-Rex
8. Polimorfisme: Update dan init function dari kelas Obstacles
9. Abstraksi: Spawn function dari kelas Obstacles
10. GUI: Pygame
11. Deskripsi Game: just RUN! merupakan sebuah 2D Side-scrolling game (Kiri - Kanan), dengan Dino sebagai karakter utama pemain dapat memilih untuk menghindari rintangan dengan jumping, ducking, atau rolling; atau pemain juga dapat menghancurkan rintangan tersebut dengan skill seperti fireball. Game ini juga mengambil unsur dari genre Rogue-like yaitu mid-level upgrade dan permadeath dimana player dapat melakukan upgrade terhadap skillnya ditengah game namun jika player mati dalam game maka semua upgrade tersebut akan hilang dan mulai dari nol lagi.
'''
##start_loop = True
##game_loop = True

pygame.init()
screen = pygame.display.set_mode((1280,720))
window_icon = pygame.image.load("Assets/Logo/DinoIcont.png")
pygame.display.set_icon(window_icon)
pygame.display.set_caption("just RUN!")

class Button():
    def __init__(self,x,y,img):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def Place(self):
        command = False
        
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                command = True

        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False
        
        screen.blit(self.img,(self.rect.x,self.rect.y))
        return command


cactus = [pygame.image.load("Assets/Plants/Cactus1.png"),pygame.image.load("Assets/Plants/Cactus2.png")]
thorn = [pygame.image.load("Assets/Plants/Thorn1.png"),pygame.image.load("Assets/Plants/Thorn2.png")]
spike = [pygame.image.load("Assets/Plants/Spike.png"),pygame.image.load("Assets/Plants/Spike2.png")]
bird = [pygame.image.load("Assets/Bird/Bird1.png"),pygame.image.load("Assets/Bird/Bird2.png")]
t_rex = [pygame.image.load("Assets/T-Rex/T-RexRun1.png"),pygame.image.load("Assets/T-Rex/T-RexRun2.png")]
projectile_img = [pygame.image.load("Assets/Logo/FireOrb.png")]

def Upgrade(name):
    if name == "Fire Orb":
        if Fire_Orb_Stats["current_level"] == 0:
            Fire_Orb_Stats["current_level"] = 1
        elif Fire_Orb_Stats["current_level"] == 1:
            Fire_Orb_Stats["current_level"] = 2
            Fire_Orb_Stats["quantity"] += 1
        elif Fire_Orb_Stats["current_level"] == 2:
            Fire_Orb_Stats["current_level"] = 3
            Fire_Orb_Stats["damage"] += 20
        elif Fire_Orb_Stats["current_level"] == 3:
            Fire_Orb_Stats["current_level"] = 4
            Fire_Orb_Stats["quantity"] += 1
        elif Fire_Orb_Stats["current_level"] == 4:
            Fire_Orb_Stats["current_level"] = 5
            Fire_Orb_Stats["damage"] += 20
        elif Fire_Orb_Stats["current_level"] == 5:
            Fire_Orb_Stats["current_level"] = 5

Jump_Stats = {
    "current_level" : 0,
    "lvl_1_text" : ["lvl 1", "You can just jump over the obstacle."],
    "lvl_2_text" : ["lvl 2", "Jump higher by 10%."],
    "lvl_3_text" : ["lvl 3", "Jump higher by 10%."],
    "lvl_4_text" : ["lvl 4", "Jump higher by 10%."],
    "lvl_5_text" : ["lvl 5", "Jump higher by 10%."],
    "name" : "Jump",
    "damage" : 100,
    "speed" : 20,
    "quantity" : 1,
    "img" : pygame.image.load("Assets/Dino/DinoStart.png"),
    "slot_img" : pygame.image.load("Assets/Logo/JumpingSkill1.png"),
    "upgrade_img" : pygame.image.load("Assets/Logo/JumpingSkill.png"),
    "Upgrade" : Upgrade
    }
Duck_Stats = {
    "current_level" : 0,
    "lvl_1_text" : ["lvl 1", "You can duck everything !"],
    "lvl_2_text" : ["lvl 2", "b"],
    "lvl_3_text" : ["lvl 3", "c"],
    "lvl_4_text" : ["lvl 4", "d"],
    "lvl_5_text" : ["lvl 5", "e"],
    "name" : "Duck",
    "damage" : 100,
    "speed" : 20,
    "quantity" : 1,
    "img" : [pygame.image.load("Assets/Dino/DinoDuck1.png"),pygame.image.load("Assets/Dino/DinoDuck2.png")],
    "slot_img" : pygame.image.load("Assets/Logo/DuckingSkill1.png"),
    "upgrade_img" : pygame.image.load("Assets/Logo/DuckingSkill.png"),
    "Upgrade" : Upgrade
    }
Fire_Orb_Stats = {
    "current_level" : 0,
    "lvl_1_text" : ["lvl 1", "Shooting fire orb to the front."],
    "lvl_2_text" : ["lvl 2", "Fires 1 more projectile."],
    "lvl_3_text" : ["lvl 3", "Damage +20"],
    "lvl_4_text" : ["lvl 4", "Fires 1 more projectile."],
    "lvl_5_text" : ["lvl 5", "Damage +20"],
    "name" : "Fire Orb",
    "damage" : 100,
    "speed" : 20,
    "quantity" : 1,
    "img" : pygame.image.load("Assets/Logo/FireOrb.png"),
    "slot_img" : pygame.image.load("Assets/Logo/FireOrbSkill1.png"),
    "upgrade_img" : pygame.image.load("Assets/Logo/FireOrbSkill.png"),
    "Upgrade" : Upgrade
    }
Fireball_Stats = {
    "current_level" : 0,
    "lvl_1_text" : ["lvl 1", "Big fireball."],
    "lvl_2_text" : ["lvl 2", "Coldown -20%"],
    "lvl_3_text" : ["lvl 3", "Damage +20."],
    "lvl_4_text" : ["lvl 4", "Coldown -20%"],
    "lvl_5_text" : ["lvl 5", "Fires 1 more projectile."],
    "name" : "Fireball",
    "damage" : 100,
    "speed" : 20,
    "quantity" : 1,
    "img" : pygame.image.load("Assets/Logo/Fireball.png"),
    "slot_img" : pygame.image.load("Assets/Logo/FireballSkill1.png"),
    "upgrade_img" : pygame.image.load("Assets/Logo/FireballSkill.png"),
    "Upgrade" : Upgrade
    }


class Projectile:
    def __init__(self, img, player):
        self.img = img[0]
        self.damage = 10
        self.hitbox = self.img.get_rect(center=( player.hitbox.x + 87,player.hitbox.y + 30))
        self.mask = pygame.mask.from_surface(self.img)
        
    def Update(self,projectile_vel):
        self.hitbox.x += projectile_vel
##        self.hitbox.y -= projectile_vel

        for i in range (len(projectiles)-1):
            if projectiles[i].hitbox.x > 1280+self.hitbox.width:
                projectiles.pop(i)

    def Spawn(self,screen):
        screen.blit(self.img,self.hitbox)

class Fire_Orb:
    def __init__(self,player):
        self.stats = Fire_Orb_Stats
        self.img = self.stats["img"]
        self.damage = self.stats["damage"]
        self.hitbox = self.img.get_rect(center=( player.hitbox.x + 95,player.hitbox.y + 30))
        self.mask = pygame.mask.from_surface(self.img)

    def Upgrade(self,Fire_Orb_Stats):
        if self.stats["current_level"] == 0:
            Fire_Orb_Stats["current_level"] = 1
        elif self.stats["current_level"] == 1:
            Fire_Orb_Stats["current_level"] = 2
            Fire_Orb_Stats["quantity"] += 1
        elif self.stats["current_level"] == 2:
            Fire_Orb_Stats["current_level"] = 3
            Fire_Orb_Stats["damage"] += 20
        elif self.stats["current_level"] == 3:
            Fire_Orb_Stats["current_level"] = 4
            Fire_Orb_Stats["quantity"] += 1
        elif self.stats["current_level"] == 4:
            Fire_Orb_Stats["current_level"] = 5
            Fire_Orb_Stats["damage"] += 20
        elif self.stats["current_level"] == 5:
            Fire_Orb_Stats["current_level"] = 5

    def Update(self):
        self.hitbox.x += self.stats["speed"]
        for i in range(len(projectiles)-1):
            if projectiles[i].hitbox.x > 1280+self.hitbox.width:
                projectiles.pop(i)

    def Spawn(self,screen):
##        if self.count == 60/self.stats["quantity"]:
##            projectiles.append(Fire_Orb(player))
##        else :
##            self.count += 1

        screen.blit(self.img,self.hitbox)

class Jump:
    pass
class Duck:
    pass
class Fireball:
    pass

weapons = [Jump_Stats,Duck_Stats,Fire_Orb_Stats,Fireball_Stats] 

class Dino :
    x_position = 50
    y_position = 348
    y_duck_position = 380
    jump_velocity = 8
    
    def __init__(self):
        self.__run_img = [pygame.image.load("Assets/Dino/DinoRun1.png"),pygame.image.load("Assets/Dino/DinoRun2.png")]
        self.__duck_img = [pygame.image.load("Assets/Dino/DinoDuck1.png"),pygame.image.load("Assets/Dino/DinoDuck2.png")]
        self.__jump_img = [pygame.image.load("Assets/Dino/DinoStart.png")]
        self.__dead_img = [pygame.image.load("Assets/Dino/DinoDead.png")]

        self.__dino_run = True
        self.__dino_jump = False
        self.__dino_duck = False
        self.__dino_dead = False

        self.health = 100
        self.max_health =100
        self.protection = 0
        self.max_protection = 100
        self.exp = 0
        self.__step_count = 0
        self.__jump_vel = self.jump_velocity
        self._img = self.__run_img[self.__step_count]
        self.hitbox = self._img.get_rect()
        self.hitbox.x = self.x_position
        self.hitbox.y = self.y_position
        self.mask = pygame.mask.from_surface(self._img)
##        self.mask_img = self.dino_mask.to_surface()

    def Update(self,user_input):
        if self.__dino_run:
            self.Running_Dino()
        if self.__dino_jump:
            self.Jumping_Dino()
        if self.__dino_duck:
            self.Ducking_Dino()

        if self.__step_count >= 10:
            self.__step_count = 0

        if user_input[pygame.K_UP] and not self.__dino_jump:
            self.__dino_run = False
            self.__dino_jump = True
            self.__dino_duck = False
            self.__dino_dead = False
        elif user_input[pygame.K_DOWN] and not self.__dino_jump:
            self.__dino_run = False
            self.__dino_jump = False
            self.__dino_duck = True
            self.__dino_dead = False
        elif not (self.__dino_jump or user_input[pygame.K_DOWN]):
            self.__dino_run = True
            self.__dino_jump = False
            self.__dino_duck = False
            self.__dino_dead = False

    def Running_Dino(self):
        self._img = self.__run_img[self.__step_count//5]
        self.hitbox = self._img.get_rect()
        self.hitbox.x = self.x_position
        self.hitbox.y = self.y_position
        self.mask = pygame.mask.from_surface(self._img)
        self.__step_count += 1

    def Jumping_Dino(self):
        self._img = self.__jump_img[0]
        self.mask = pygame.mask.from_surface(self._img)
        if self.__dino_jump :
            self.hitbox.y -= self.__jump_vel * 4
            self.__jump_vel -= 0.8
        if self.__jump_vel < -self.jump_velocity:
            self.__dino_jump = False
            self.__jump_vel = self.jump_velocity

    def Ducking_Dino(self):
        self._img = self.__duck_img[self.__step_count//5]
        self.hitbox = self._img.get_rect()
        self.hitbox.x = self.x_position
        self.hitbox.y = self.y_duck_position
        self.mask = pygame.mask.from_surface(self._img)
        self.__step_count += 1

    def Death(self):
        if self.health <= 0 :
            self.__dino_run = False
            self.__dino_jump = False
            self.__dino_duck = False
            self.__dino_dead = True
            self._img = self.__dead_img[0]
            return self.__dino_dead
    
    def Spawn(self,screen):
        screen.blit(self._img,(self.hitbox.x, self.hitbox.y))
##        screen.blit(self.mask_img,(0,0))
        

class Obstacle:
    def __init__(self, img, obstacle_type, y_position):
        self.health = 50
        self.max_health =100
        self.protection = 0
        self.max_protection = 0
        self.img = img
        self.__obstacle_type = obstacle_type
        self.hitbox = self.img[self.__obstacle_type].get_rect()
        self.mask = pygame.mask.from_surface(self.img[obstacle_type])
        self.hitbox.x = 1280
        self.hitbox.y = y_position

    def Update(self):
        self.hitbox.x -= game_speed
        if self.hitbox.x <= -self.hitbox.width:
            enemies.pop()

    @abstractmethod
    def Spawn(self, screen):
        pass
##        screen.blit(self.img[self.__obstacle_type], self.hitbox)

    def Death(self):
        if self.health <= 0:
            enemies.pop()
            print("enemy death")

class Cactus(Obstacle):
    def __init__(self,img):
        self.__cactus_type = random.randint(0,1)
        self.damage = 5
        super().__init__(img, self.__cactus_type, 345)

    def Spawn(self, screen):
        screen.blit(self.img[self.__cactus_type], self.hitbox)

class Thorn(Obstacle):
    def __init__(self,image):
        self.__thorn_type = random.randint(0,1)
        self.damage = 10
        super().__init__(image, self.__thorn_type, 323)

    def Spawn(self, screen):
        screen.blit(self.img[self.__thorn_type], self.hitbox)

class Spike(Obstacle):
    def __init__(self,img):
        self.__spike_floor = img[0]
        self.damage = 8
        self.__floor_rect = self.__spike_floor.get_rect()
        self.__floor_rect.x = 1280
        self.__floor_rect.y = 440
        super().__init__(img,1,439)

    def Update(self):
        self.__floor_rect.x -= game_speed
        self.hitbox.x -= game_speed
        if self.__floor_rect.x <= -self.__floor_rect.width and self.hitbox.x <= -self.hitbox.width:
            enemies.pop()

    def Spawn(self, screen):
        screen.blit(self.img[1], self.hitbox)
        screen.blit(self.__spike_floor, self.__floor_rect)

class T_Rex(Obstacle):
    def __init__(self,img):
        self.img = img
        self.damage = 20
        super().__init__(img,0,340)
        self.__index = 0

    def Spawn(self,screen):
        if self.__index == 10:
            self.__index = 0
        screen.blit(self.img[self.__index//5],self.hitbox)
        self.__index += 1

class Bird(Obstacle):
    def __init__(self,img,y_position):
        self.img = img
        self.damage = 5
        super().__init__(img,0,y_position)
        self.__index = 0

    def Spawn(self,screen):
        if self.__index == 10:
            self.__index = 0
        screen.blit(self.img[self.__index//5],self.hitbox)
        self.__index += 1
            

class Cloud:
    def __init__(self, img):
        self.__x = 1280 + random.randint(500, 700)
        self.__y = random.randint(105, 200)
        self.__img = img
        self.__width = self.__img.get_width()

    def Update(self):
        self.__x -= game_speed
        if self.__x < -self.__width:
            self.__x = 1280 + random.randint(0, 10)
            self.__y = random.randint(105, 200)

    def Spawn(self, screen):
        screen.blit(self.__img,(self.__x,self.__y))

def Start_Game():
    global game_speed,x, y, enemies, projectiles, game_state, score, exp, exp_bar, current_limit, i,pxl,mins,sec,mil_sec,health
    x = 0
    y = 440
    game_speed = 20
    score = 0
    current_limit = 100
    mins = 0
    sec = 0
    mil_sec = 0
    i = 1
    j = 60
    pxl = 0
    clock = pygame.time.Clock()
    player = Dino()
    weapon_list = []
    enemies = []
    projectiles = []
    cloud = Cloud(pygame.image.load("Assets/Logo/Cloud.png"))
    cloud2 = Cloud(pygame.image.load("Assets/Logo/Cloud2.png"))

    pause_img = pygame.image.load("Assets/Logo/TopFrame_PauseButton.png")
    pause_button = Button(1244,8,pause_img)
    game_state = "Select"
    collision_immune = False
    collision_time = 0

##    bullet = pygame.Surface((10, 10))
##    bullet_mask = pygame.mask.from_surface(bullet)

    def Upgrade_Weapon():
        up_list = []
        up = 0
        finish = 0
        for i in weapon_list:
            if i["current_level"] >= 5:
                finish += 1
            else :
                up += 1

        new = (3 - up) - finish

        for a in range(up):
            up_list.append(weapon_list[a])
            
        if new != 0:
            for a in range(new):
                loop = True
                while loop:
                    add = weapons[random.randint(0,3)]
                    for i in up_list:
                        if i["name"] != add["name"]:
                            loop = False
                        else :
                            loop = True
                            break
                    
                up_list.append(add)

        upgrade_img = pygame.image.load("Assets/Logo/UpgradeMenu.png")
        up_card_img = pygame.image.load("Assets/Logo/UpgradeSlot.png")
        
        button = []
        y_pos = 60
        for i in range (len(up_list)):
            if up_list[i]["current_level"] > 0:
                button.append(Button(836,500+(i*y_pos),up_card_img))
            elif up_list[i]["current_level"] == 0:
                button.append(Button(836,500+(i*y_pos),up_card_img))
            elif up_list[i]["current_level"] >= 5:
                button.append(Button(836,500+(i*y_pos),up_card_img))

        font = pygame.font.Font('freesansbold.ttf',11)
        name1 = font.render(up_list[0]["name"],True,(255,255,255))
        lvl1  = font.render("Lvl "+str(up_list[0]["current_level"]+1),True,(255,255,255))
        desc1 = font.render(str(list(up_list[0].values())[up_list[0]["current_level"]+1][1]),True,(255,255,255))

        name2 = font.render(up_list[1]["name"],True,(255,255,255))
        lvl2  = font.render("Lvl "+str(up_list[1]["current_level"]+1),True,(255,255,255))
        desc2 = font.render(str(list(up_list[1].values())[up_list[1]["current_level"]+1][1]),True,(255,255,255))

        name3 = font.render(up_list[2]["name"],True,(255,255,255))
        lvl3  = font.render("Lvl "+str(up_list[2]["current_level"]+1),True,(255,255,255))
        desc3 = font.render(str(list(up_list[2].values())[up_list[2]["current_level"]+1][1]),True,(255,255,255))
        
        screen.blit(upgrade_img,(0,0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if button[0].Place():
                if up_list[0]["current_level"] == 0:
                    weapon_list.append(up_list[0])
                    up_list[0]["Upgrade"](up_list[0]["name"])
                elif up_list[0]["current_level"] >= 1:
                    up_list[0]["Upgrade"](up_list[0]["name"])
                elif up_list[0]["current_level"] == 5:
                    up_list[0]["Upgrade"](up_list[0]["name"])

                for i in button:
                    del i
                print(weapon_list)
                print(Fire_Orb_Stats)
                break
                
            screen.blit(up_list[0]["upgrade_img"],(847,511))
            screen.blit(name1,(889,511))
            screen.blit(lvl1,(1125,511))
            screen.blit(desc1,(889,532))
            
            if button[1].Place():
                if up_list[1]["current_level"] == 0:
                    weapon_list.append(up_list[1])
                    up_list[1]["Upgrade"](up_list[0]["name"])
                elif up_list[1]["current_level"] >= 1:
                    up_list[1]["Upgrade"](up_list[0]["name"])
                elif up_list[1]["current_level"] == 5:
                    up_list[1]["Upgrade"](up_list[0]["name"])

                for i in button:
                    del i
                break
                
            screen.blit(up_list[1]["upgrade_img"],(847,571))
            screen.blit(name2,(889,571))
            screen.blit(lvl2,(1125,571))
            screen.blit(desc2,(889,592))
            if button[2].Place():
                if up_list[2]["current_level"] == 0:
                    weapon_list.append(up_list[2])
                    up_list[2]["Upgrade"](up_list[0]["name"])
                elif up_list[2]["current_level"] >= 1:
                    up_list[2]["Upgrade"](up_list[0]["name"])
                elif up_list[2]["current_level"] == 5:
                    up_list[2]["Upgrade"](up_list[0]["name"])

                for i in button:
                    del i
                break
                
            screen.blit(up_list[2]["upgrade_img"],(847,631))
            screen.blit(name3,(889,631))
            screen.blit(lvl3,(1125,631))
            screen.blit(desc3,(889,652))

            pygame.display.update()
            

    def Status_Bar(player):
        global current_limit
        if player.exp >= current_limit :
            player.exp -= current_limit
            current_limit += (current_limit*0.1)
            exp_progress = (player.exp/current_limit)*1214
            pygame.draw.rect(screen, ("#2789cd"), pygame.Rect((12,12),(exp_progress,20)))
            game_state = "Upgrade"
            Upgrade_Weapon()
        exp_progress = (player.exp/current_limit)*1214
        pygame.draw.rect(screen, ("#2789cd"), pygame.Rect((12,12),(exp_progress,20)))

        health_bar = (player.health/player.max_health)*635
        pygame.draw.rect(screen, ("#cf0033"), pygame.Rect((65,491),(health_bar,18)))

        armor_bar = (player.protection/player.max_protection)*635
        pygame.draw.rect(screen, ("#616161"), pygame.Rect((65,513),(armor_bar,18)))

    def Score(player):
        global score, game_speed, exp,i,pxl
        score += 1
        
        if score % 100 == 0:
            player.exp += 100
        if score % 500 == 0:
            game_speed += 1

        font = pygame.font.Font('freesansbold.ttf',11)
        score_counter = font.render(str(score),True,(255,255,255))

        if len(str(score)) > i:
            i += 1
            pxl += 6
        screen.blit(score_counter,(1248-pxl,34))
        
    def Time():
        global mins, sec, mil_sec
        if mil_sec >= 30:
            mil_sec = 0
            sec += 1
            if sec >= 60:
                sec = 0
                mins += 1
        font = pygame.font.Font('freesansbold.ttf',25)
        if len(str(mins))<2:
            mins_display = font.render("0" + str(mins),True,(255,255,255))
        else:
            mins_display = font.render(str(mins),True,(255,255,255))
        if len(str(sec))<2:
            sec_display = font.render("0" + str(sec),True,(255,255,255))
        else:
            sec_display = font.render(str(sec),True,(255,255,255))

        screen.blit(mins_display,(609,58))
        screen.blit(sec_display,(643,58))
        mil_sec += 1
        
    def Game_Bg(screen):
        global game_speed,x, y
        game_bg_img = pygame.image.load("Assets/Logo/ArenaBackground3.png")
        top_menu_img = pygame.image.load("Assets/Logo/TopFrame2.png")
        bottom_menu_img = pygame.image.load("Assets/Logo/BottomFrame2.png")
        
        screen.blit(top_menu_img,(0,0))
        screen.blit(bottom_menu_img,(0,461))
        
        bg_img_width = game_bg_img.get_width()
        screen.blit(game_bg_img,(x,y))
        screen.blit(game_bg_img,(bg_img_width + x,y))
        if x <= -bg_img_width:
            screen.blit(game_bg_img,(bg_img_width + x,y))
            x=0
        x -= game_speed

    def Pause_Game():
        global game_state
        pause_menu_img = pygame.image.load("Assets/Logo/Pause_Menu.png")
        resume_img = pygame.image.load("Assets/Logo/RESUMEButton.png")
        menu_img = pygame.image.load("Assets/Logo/MENUButton.png")

        screen.blit(pause_menu_img,(0,0))
        resume_button = Button(580,304,resume_img)
        menu_button = Button(580,390,menu_img)

        while game_state == "Paused":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if resume_button.Place():
                game_state = "Run"
                del resume_button
                del menu_button
            elif menu_button.Place():
                game_state = "Run"
                del resume_button
                del menu_button
                Main_Menu()
                
            clock.tick(30)
            pygame.display.update()

    def Hit(obj1, obj2):
        if pygame.Rect.colliderect(obj1.hitbox,obj2.hitbox):
            if obj1.mask.overlap(obj2.mask,[obj2.hitbox.x-obj1.hitbox.x, obj2.hitbox.y-obj1.hitbox.y]):
                if obj1.protection <= 0:
                    obj1.health -= obj2.damage
                else :
                    if obj1.protection - obj2.damage < 0:
                        obj1.protection -= obj2.damage
                        obj1.health += obj1.protection
                        obj1.protection = 0
                    else :
                        obj1.protection -= obj2.damage
                return True

    def Result_Menu():
        result_menu_img = pygame.image.load("Assets/Logo/GameOver_Menu.png")
        play_again_img = pygame.image.load("Assets/Logo/PLAYAGAINButton.png")
        main_menu_img = pygame.image.load("Assets/Logo/MAINMENUButton.png")

        screen.blit(result_menu_img,(0,0))
        play_again_button = Button(699,442,play_again_img)
        main_menu_button = Button(461,442,main_menu_img)

        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if play_again_button.Place():
                del play_again_button
                del main_menu_button
                Start_Game()
            elif main_menu_button.Place():
                del play_again_button
                del main_menu_button
                Main_Menu()

            pygame.display.update() 

    def Skill_Selection():
        global game_state
        select_img = pygame.image.load("Assets/Logo/SkillSelectionMenu.png")
        skill1_img = pygame.image.load("Assets/Logo/JumpCard.png")
        skill2_img = pygame.image.load("Assets/Logo/DuckCard.png")
        skill3_img = pygame.image.load("Assets/Logo/FireOrbCard.png")
        skill4_img = pygame.image.load("Assets/Logo/FireballCard.png")

        skill1_button = Button(400,295,skill1_img)
        skill2_button = Button(680,295,skill2_img)
        skill3_button = Button(400,391,skill3_img)
        skill4_button = Button(680,391,skill4_img)

        if game_state == "Select":
            screen.blit(select_img,(0,0))

        while game_state == "Select":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if skill1_button.Place():
                weapon_list.append(Jump_Stats)
                weapon_list[0]["current_level"] = 1
                game_state = "Run"
                del skill1_button
                del skill2_button
                del skill3_button
                del skill4_button
            elif skill2_button.Place():
                weapon_list.append(Duck_Stats)
                weapon_list[0]["current_level"] = 1
                game_state = "Run"
                del skill1_button
                del skill2_button
                del skill3_button
                del skill4_button
            elif skill3_button.Place():
                weapon_list.append(Fire_Orb_Stats)
                weapon_list[0]["current_level"] = 1
                game_state = "Run"
                del skill1_button
                del skill2_button
                del skill3_button
                del skill4_button
            elif skill4_button.Place():
                weapon_list.append(Fireball_Stats)
                weapon_list[0]["current_level"] = 1
                game_state = "Run"
                del skill1_button
                del skill2_button
                del skill3_button
                del skill4_button

            pygame.display.update()

    def Spawn_Weapon(weapon_list):
        if weapon_list["name"] == "Fire Orb":
            projectiles.append(Fire_Orb(player))

    def Bottom_Display():
        if len(weapon_list) == 1:
            screen.blit(weapon_list[0]["slot_img"],(203,573))
        elif len(weapon_list) == 2:
            screen.blit(weapon_list[0]["slot_img"],(203,573))
            screen.blit(weapon_list[1]["slot_img"],(308,573))
        elif len(weapon_list) == 3:
            screen.blit(weapon_list[0]["slot_img"],(203,573))
            screen.blit(weapon_list[1]["slot_img"],(308,573))
            screen.blit(weapon_list[2]["slot_img"],(413,573))
    
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
        screen.fill((81,223,229))
        user_input = pygame.key.get_pressed()
        Game_Bg(screen)
        Score(player)
        Status_Bar(player)
        Time()

        cloud.Spawn(screen)
        cloud2.Spawn(screen)
        cloud.Update()
        cloud2.Update()

        Skill_Selection()

        if pause_button.Place():
            game_state = "Paused"
            Pause_Game()

        if len(enemies)==0:
            if random.randint(0,3)==0:
                    enemies.append(Cactus(cactus))
            elif random.randint(0,3)==1:
                    enemies.append(Thorn(thorn))
            elif random.randint(0,4)==2:
                    enemies.append(Spike(spike))
            elif random.randint(0,3)==2:
                    enemies.append(T_Rex(t_rex))
            elif random.randint(0,3)==3:
                if random.randint(0,2)==0:
                    enemies.append(Bird(bird,100))
                if random.randint(0,2)==1:
                    enemies.append(Bird(bird,150))
                if random.randint(0,2)==2:
                    enemies.append(Bird(bird,200))

        for enemy in enemies:
            enemy.Spawn(screen)
            enemy.Update()

        player.Spawn(screen)
        player.Update(user_input)

        if j == 60:
            Spawn_Weapon(weapon_list[0])
            j = 0
        j+=1

        for projectile in projectiles:
            projectile.Spawn(screen)
            projectile.Update()

        

        if len(enemies) >= 1:
            if pygame.time.get_ticks() - collision_time > 1000:
                collision_immune = False
            if collision_immune == False and Hit(player,enemies[0]):
                if player.Death():
                    player.Spawn(screen)
                    Result_Menu()
                print("hit")
                collision_immune = True
                collision_time = pygame.time.get_ticks()

        if len(projectiles) >= 1 and len(enemies) >= 1:
            for no in range (len(projectiles)-1):
                Hit(enemies[0],projectiles[no])
                if projectiles[no].mask.overlap(enemies[0].mask,[enemies[0].hitbox.x-projectiles[no].hitbox.x, enemies[0].hitbox.y-projectiles[no].hitbox.y]):
                    projectiles.pop(no)
            enemies[0].Death()

        Bottom_Display()
        clock.tick(30)
        pygame.display.update()    
    

def Main_Menu():
    bg_img = pygame.image.load("Assets/Logo/Background3.png")
    start_img = pygame.image.load("Assets/Logo/PLAYButton.png")
    upgrade_img = pygame.image.load("Assets/Logo/UPGRADEButton.png")
    exit_img = pygame.image.load("Assets/Logo/EXITButton.png")
    
    screen.blit(bg_img,(0,0))
    start_button = Button(584,456,start_img)
    upgrade_button= Button(584,544,upgrade_img)
    exit_button = Button(584,632,exit_img)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

     
        if start_button.Place():
            screen.fill((00,00,00))
            del start_button
            del upgrade_button
            del exit_button
            Start_Game()
        elif upgrade_button.Place():
            screen.fill((00,00,00))
            del start_button
            del upgrade_button
            del exit_button
            pass
        elif exit_button.Place():
            pygame.quit()
            
        pygame.display.update() 


Main_Menu()



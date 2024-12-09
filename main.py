from init import *

def level_wolf():
    knight.reset_stats()

    wolf = Enemy(780, 400, 300, 0, wolf_animations)
    wolf_healthbar = Healthbar((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+25, wolf.max_hp, wolf.max_hp)

    running = True
    turn = [knight, wolf]
    wait = 100
    cooldown = 0
    reward_granted = False


    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        screen.fill(COLORS['GREY'])
        draw_bg(screen, forest)
        draw_panel(screen, panel)

        knight_healthbar.draw_bar(knight.curr_hp, screen)
        knight_armor.draw_bar(knight.curr_armor, screen)
        wolf_healthbar.draw_bar(wolf.curr_hp, screen)

        breadth_first_traversal(knife, screen)
        heal.draw_skill(screen)

        knight.update()
        knight.draw_entity(screen)
        wolf.update()
        wolf.draw_entity(screen)

        if knight.alive and turn[0] is knight: 
            if curr_weapon[0][2].rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                
                if curr_weapon[0][2] is knife:          knight.attack('ATTACK 1', wolf)
                elif curr_weapon[0][2] is wooden_sword: knight.attack('ATTACK 2', wolf)
                else:                                   knight.attack('ATTACK 3', wolf)

                turn.append(turn.pop(0))

            if wooden_shield.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.defend()
                turn.append(turn.pop(0))

            if heal.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and knight.curr_hp < knight.max_hp:
                factor = randint(1,5)
                heal_amount = factor*10
                if knight.curr_hp + heal_amount <= knight.max_hp:
                    knight.curr_hp += heal_amount
                else:
                    knight.curr_hp = knight.max_hp

                turn.append(turn.pop(0))

        elif wolf.alive and turn[0] == wolf:
            cooldown += 1
            if cooldown >= wait:
                wolf.attack('ATTACK', knight)
                turn.append(turn.pop(0))
                cooldown = 0

        if knight.alive and not wolf.alive: 
            knight.progress['wolf'] = True
            if not reward_granted:
                knight.funds += knight.curr_hp
                reward_granted = True

        pygame.display.update()

def level_slime():
    knight.reset_stats()

    slime = Enemy(780, 410, 400, 0, slime_animations)
    slime_healthbar = Healthbar((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+25, slime.max_hp, slime.max_hp)

    running = True
    turn = [knight, slime]
    wait = 100
    cooldown = 0
    reward_granted = False

    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        screen.fill(COLORS['GREY'])
        draw_bg(screen, cavern)
        draw_panel(screen, panel)

        knight_healthbar.draw_bar(knight.curr_hp, screen)
        knight_armor.draw_bar(knight.curr_armor, screen)
        slime_healthbar.draw_bar(slime.curr_hp, screen)

        breadth_first_traversal(knife, screen)
        heal.draw_skill(screen)

        knight.update()
        knight.draw_entity(screen)
        slime.update()
        slime.draw_entity(screen)


        if knight.alive and turn[0] is knight: 
            if curr_weapon[0][2].rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                
                if curr_weapon[0][2] is knife:          knight.attack('ATTACK 1', slime)
                elif curr_weapon[0][2] is wooden_sword: knight.attack('ATTACK 2', slime)
                else:                                   knight.attack('ATTACK 3', slime)

                turn.append(turn.pop(0))
            

            if wooden_shield.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.defend()
                turn.append(turn.pop(0))

            if heal.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and knight.curr_hp < knight.max_hp:
                factor = randint(1,5)
                heal_amount = factor*10
                if knight.curr_hp + heal_amount <= knight.max_hp:
                    knight.curr_hp += heal_amount
                else:
                    knight.curr_hp = knight.max_hp

                turn.append(turn.pop(0))

        elif slime.alive and turn[0] == slime:
            cooldown += 1
            if cooldown >= wait:
                slime.attack('ATTACK', knight)
                turn.append(turn.pop(0))
                cooldown = 0

        if knight.alive and not slime.alive: 
            knight.progress['slime'] = True
            if not reward_granted:
                knight.funds += knight.curr_hp
                reward_granted = True

        pygame.display.update()

def level_golem():
    knight.reset_stats()

    golem = Miniboss(780, 410, 400, 100, golem_animations)
    golem_healthbar = Healthbar((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+25, golem.max_hp, golem.max_hp)
    golem_armor = Armor((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+160, golem.max_armor, golem.max_armor)
    

    running = True
    turn = [knight, golem]
    wait = 100
    cooldown = 0
    reward_granted = False

    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        screen.fill(COLORS['GREY'])
        draw_bg(screen, cavern)
        draw_panel(screen, panel)

        knight_healthbar.draw_bar(knight.curr_hp, screen)
        knight_armor.draw_bar(knight.curr_armor, screen)
        golem_healthbar.draw_bar(golem.curr_hp, screen)
        golem_armor.draw_bar(golem.curr_armor, screen)

        breadth_first_traversal(knife, screen)
        heal.draw_skill(screen)

        knight.update()
        knight.draw_entity(screen)
        golem.update()
        golem.draw_entity(screen)


        if knight.alive and turn[0] is knight: 
            if curr_weapon[0][2].rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                
                if curr_weapon[0][2] is knife:          knight.attack('ATTACK 1', golem)
                elif curr_weapon[0][2] is wooden_sword: knight.attack('ATTACK 2', golem)
                else:                                   knight.attack('ATTACK 3', golem)

                turn.append(turn.pop(0))
            

            if wooden_shield.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.defend()
                turn.append(turn.pop(0))

            if heal.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and knight.curr_hp < knight.max_hp:
                factor = randint(1,5)
                heal_amount = factor*10
                if knight.curr_hp + heal_amount <= knight.max_hp:
                    knight.curr_hp += heal_amount
                else:
                    knight.curr_hp = knight.max_hp

                turn.append(turn.pop(0))

        elif golem.alive and turn[0] == golem:
            cooldown += 1
            if cooldown >= wait:
                action = choice(golem.attacks_list)
                golem.attack(action, knight)
                turn.append(turn.pop(0))
                cooldown = 0

        if knight.alive and not golem.alive: 
            knight.progress['golem'] = True
            if not reward_granted:
                knight.funds += knight.curr_hp
                reward_granted = True

        pygame.display.update()

def level_demon():
    main_theme.fadeout(500)
    boss_theme.play(-1)

    knight.reset_stats()

    demon = Boss(800, 300, 700, 0, demon_animations)
    demon_healthbar = Healthbar((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+25, demon.max_hp, demon.max_hp)

    running = True
    turn = [knight, demon]
    wait = 100
    cooldown = 0
    reward_granted = False

    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                boss_theme.fadeout(500)
                main_theme.play(-1)
                running = False

        screen.fill(COLORS['GREY'])
        draw_bg(screen, cavern)
        draw_panel(screen, panel)

        knight_healthbar.draw_bar(knight.curr_hp, screen)
        knight_armor.draw_bar(knight.curr_armor, screen)
        demon_healthbar.draw_bar(demon.curr_hp, screen)

        breadth_first_traversal(knife, screen)
        heal.draw_skill(screen)

        knight.update()
        knight.draw_entity(screen)
        demon.update()
        demon.draw_entity(screen)


        if knight.alive and turn[0] is knight: 
            if curr_weapon[0][2].rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                
                if curr_weapon[0][2] is knife:          knight.attack('ATTACK 1', demon)
                elif curr_weapon[0][2] is wooden_sword: knight.attack('ATTACK 2', demon)
                else:                                   knight.attack('ATTACK 3', demon)

                turn.append(turn.pop(0))
            

            if wooden_shield.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.defend()
                turn.append(turn.pop(0))

            if heal.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and knight.curr_hp < knight.max_hp:
                factor = randint(1,5)
                heal_amount = factor*10
                if knight.curr_hp + heal_amount <= knight.max_hp:
                    knight.curr_hp += heal_amount
                else:
                    knight.curr_hp = knight.max_hp

                turn.append(turn.pop(0))

        elif demon.alive and turn[0] == demon:
            cooldown += 1
            if cooldown >= wait:
                action = choice(demon.attacks_list)
                demon.attack(action, knight)
                turn.append(turn.pop(0))
                cooldown = 0

        if knight.alive and not demon.alive: 
            knight.progress['demon'] = True
            if not reward_granted:
                knight.funds += knight.curr_hp
                reward_granted = True

        pygame.display.update()

def map():
    running = True

    slime_img_list = animation_parser('Assets/Enemies/Slime/IDLE.png', 4, 64, 64, 6)
    slime_img = slime_img_list[0]
    slime_rect = slime_img.get_rect()
    slime_rect.center = (SCREEN_WIDTH//3, 300)

    wolf_img_list = animation_parser('Assets/Enemies/Dark Wolf/IDLE.png', 4, 48, 32, 4)
    wolf_img = wolf_img_list[0]
    wolf_rect = wolf_img.get_rect()
    wolf_rect.center = (SCREEN_WIDTH//2, 150)

    demon_img_list = animation_parser('Assets/Enemies/Demon/IDLE.png', 4, 81, 71, 2.5)
    demon_img = demon_img_list[0]
    demon_rect = demon_img.get_rect()
    demon_rect.center = ((SCREEN_WIDTH//3)*2, 350)

    golem_img_list = animation_parser('Assets/Enemies/Golem/IDLE.png', 4, 64, 64, 4)
    golem_img = golem_img_list[0]
    golem_rect = golem_img.get_rect()
    golem_rect.center = ((SCREEN_WIDTH//3)*2, 550)


    while running:
        CLOCK.tick(FPS)
        screen.fill(COLORS['GREY'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        for level in knight.progress:
            if knight.progress[level] is True:
                edges = get_edges(level)
                for edge in edges:
                    draw_edge(screen, edge)
               

        screen.blit(slime_img, slime_rect)
        screen.blit(wolf_img, wolf_rect)
        screen.blit(demon_img, demon_rect)
        screen.blit(golem_img, golem_rect)

       
        if wolf_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            level_wolf()

        if slime_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and knight.progress['wolf']:
            level_slime()

        if demon_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and knight.progress['slime']:
            level_demon()
        
        if golem_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and knight.progress['demon']:
            level_golem()
        

        pygame.display.update()

def skills_menu():
    running = True

    while running:
        CLOCK.tick(FPS)
        screen.fill(COLORS['GREY'])

        draw_upgrades_menu(screen)
        
        draw_text(screen, f'Current funds: {knight.funds}', (SCREEN_WIDTH//4), 50)

        if weapon_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            if weapon_upgrades and knight.funds >= 50:
                curr_weapon[0][2].equipped = False
                curr_weapon[0] = weapon_upgrades.pop(0)
                curr_weapon[0][2].equipped = True

        if shield_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            if shield_upgrades and knight.funds >= 50:
                curr_shield[0][2].equipped = False
                curr_shield[0] = shield_upgrades.pop(0)
                curr_shield[0][2].equipped = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        pygame.display.update()
        
def main_menu():
    start_button = Button('Assets/UI/border 2.png', SCREEN_WIDTH//3+30, 450, 117, 59, 2.5, 'Start')
    skills = Button('Assets/UI/border 2.png', (SCREEN_WIDTH//3)*2-30, 450, 117, 59, 2.5, 'Skills')

    while True:
        CLOCK.tick(FPS)

        screen.fill(COLORS['GREY'])
        draw_menu_bg(screen, cavern)
        draw_title(screen, 'Dungeon Destroyer', 'white', SCREEN_WIDTH//2, 275)

        if start_button.draw(screen):
            map()
        if skills.draw(screen):
            skills_menu()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
            
        pygame.display.update()

if __name__ == "__main__":
    main_menu()

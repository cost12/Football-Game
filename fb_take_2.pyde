import random as r
import math

# Potential
# Effectiveness
# Performance


# To do:
    # fas blind bids
    # competitive trading
    # load to/from files
    # max 115 ovr per attribute
    # better aging for out of position attributes
    # color scheme
    # 2 years of draft picks available
    # shorter punt returns
    # lower draft overalls
    # add in transition overall - temporarily lose overall, but can gain it back by playing or being on bench behind veteran
    


def settings():
    global first_names, last_names, c
    global game1, draft1, draft_sort, season1, fa_sort, fa_price, team_sort_type, team_sort_reverse, team_schedule, ls, only_rookies
    global scroll, side_scroll, current_screen, is_first_season, auto_draft_end
    global all_teams, home_team, away_team, afc_e, afc_n, afc_s, afc_w, nfc_e, nfc_n, nfc_s, nfc_w, user_teams, user_team_number, team_phase
    global player_team, view_as
    global buttons, user_overall, scouting, user_cap
    global use_overall
    size(1920, 1000)
    only_rookies = False
    view_as = "NONE"
    team_schedule = "NONE"
    team_sort_type = 0
    team_sort_reverse = False
    fa_sort = "NONE"
    fa_price = 200000000
    team_phase = "OFFENSE"
    is_first_season = True
    current_screen = "CHOOSE DIFFICULTY"
    draft_sort = "NONE"
    scroll = 100
    side_scroll = 0
    auto_draft_end = "DONE"
    c = Constants()
    ls = League_Stats()
    user_teams = []
    user_overall = 0
    user_team_number = 1
    scouting = "TOP RED"
    user_cap = 200000000
    use_overall = True
    #                  x    y     w  h   t            d    c
    buttons = [Button(100, 120, 200, 50, "Very High", 85, "DIFFICULTY OVR"),       Button(100, 170, 200, 50, "High", 80, "DIFFICULTY OVR"),               Button(100, 220, 200, 50, "Normal", 75, "DIFFICULTY OVR"),              Button(100, 270, 200, 50, "Low", 70, "DIFFICULTY OVR"),                  Button(100, 320, 200, 50, "Very Low", 55, "DIFFICULTY OVR"),           Button(100, 370, 200, 50, "Mega Draft", 0, "DIFFICULTY OVR"),
               Button(500, 120, 200, 50, "None", "NONE", "DIFFICULTY DRAFT"),      Button(500, 170, 200, 50, "Full Red", "FULL RED", "DIFFICULTY DRAFT"), Button(500, 220, 200, 50, "Top Red", "TOP RED", "DIFFICULTY DRAFT"),    Button(500, 270, 200, 50, "Full Blue", "FULL BLUE", "DIFFICULTY DRAFT"), Button(500, 320, 200, 50, "Top Blue", "TOP BLUE", "DIFFICULTY DRAFT"),
               Button(900, 120, 200, 50, "Standard", 200000000, "DIFFICULTY CAP"), Button(900, 170, 200, 50, "Bonus", 250000000, "DIFFICULTY CAP"),       Button(900, 220, 200, 50, "Double bonus", 300000000, "DIFFICULTY CAP"), Button(900, 270, 200, 50, "None", "NONE", "DIFFICULTY CAP"), 
               Button(1300,120, 200, 50, "1 User Team", 1, "DIFFICULTY TEAMS"),    Button(1300,170, 200, 50, "2 User Teams", 2, "DIFFICULTY TEAMS"),      Button(1300,220, 200, 50, "3 User Teams", 3, "DIFFICULTY TEAMS"),      Button(1300,270, 200, 50, "4 User Teams", 4, "DIFFICULTY TEAMS"),      Button(1300,320, 200, 50, "32 User Teams", 32, "DIFFICULTY TEAMS"), 
               Button(500, 500, 200, 50, "CONTINUE", "CONTINUE", "DIFFICULTY CONTINUE"),
               Button(1600,  0, 100, 50, "SEASON",   "SEASON",   "NAVIGATION") ]
    for i in {5, 8, 11, 15}:
        buttons[i].highlight = True
    names = loadStrings("maddenNames.csv")
    first_names = []
    last_names = []
    for name in names:
        last_names.append(name[name.index(" ")  + 1:])
        first_names.append(name[0:name.index(" ")])

    pats = Team("Patriots", "New England", "NE")
    bills = Team("Bills", "Buffalo", "BUF")
    jets = Team("Jets", "New York", "NYJ")
    dolphins = Team("Dolphins", "Miami", "MIA")
    afc_e = [pats, bills, jets, dolphins]
    
    colts = Team("Colts", "Indianapolis", "IND")
    jags = Team("Jaguars", "Jacksonville", "JAX")
    titans = Team("Titans", "Tennessee", "TEN")
    texans = Team("Texans", "Houston", "HOU")
    afc_s = [colts, jags, titans, texans]
    
    ravens = Team("Ravens", "Baltimore", "BAL")
    steelers = Team("Steelers", "Pittsburgh", "PIT")
    browns = Team("Browns", "Cleveland", "CLE")
    bengals = Team("Bengals", "Cincinnati", "CIN")
    afc_n = [ravens, steelers, browns, bengals]
    
    chiefs = Team("Chiefs", "Kansas City", "KC")
    chargers = Team("Chargers", "Los Angeles", "LAC")
    raiders = Team("Raiders", "Los Vegas", "LV")
    broncos = Team("Broncos", "Denver", "DEN")
    afc_w = [chiefs, chargers, raiders, broncos]
    
    giants = Team("Giants", "New York", "NYG")
    the_team = Team("Commanders", "Washington", "WAS")
    eagles = Team("Eagles", "Philadelphia", "PHI")
    cowboys = Team("Cowboys", "Dallas", "DAL")
    nfc_e = [giants, the_team, eagles, cowboys]
    
    saints = Team("Saints", "New Orleans", "NO")
    bucs = Team("Buccaneers", "Tampa Bay", "TB")
    panthers = Team("Panthers", "Carolina", "CAR")
    falcons = Team("Falcons", "Atlanta", "ATL")
    nfc_s = [saints, bucs, panthers, falcons]
    
    packers = Team("Packers", "Green Bay", "GB")
    vikings = Team("Vikings", "Minnesota", "MIN")
    lions = Team("Lions", "Detroit", "DET")
    bears = Team("Bears", "Chicago", "CHI")
    nfc_n = [packers, vikings, bears, lions]
    
    niners = Team("49ers", "San Francisco", "SF")
    cards = Team("Cardinals", "Arizona", "ARI")
    rams = Team("Rams", "Los Angeles", "LAR")
    seahawks = Team("Seahawks", "Seattle", "SEA")
    nfc_w = [niners, cards, rams, seahawks]
    
    all_teams = [pats, bills, jets, dolphins, colts, texans, jags, titans, ravens, steelers, browns, bengals, chiefs, chargers, raiders, broncos, giants, the_team, cowboys, eagles, saints, bucs, panthers, falcons, packers, vikings, bears, lions, niners, seahawks, rams, cards]
            
def draw():
    global game1, draft1, all_teams, home_team, season1, user_teams, user_team_number, team_phase, player_team, team_sort_type, team_sort_reverse, team_schedule, ls, fa_price, fa_sort
    global buttons, auto_draft_end, scroll, side_scroll, only_rookies
    background(100)
    if current_screen == "LEAGUE STATS":
        __draw_league_stats()
    elif current_screen == "DRAFT":
        __draw_draft_screen()
    elif current_screen == "AUTO DRAFTING":
        __draw_auto_draft(draft1, auto_draft_end)
    elif current_screen == "GAME":
        game1.draw_game()
    elif current_screen == "TEAM":
        __draw_team_screen()
    elif is_team(current_screen):
        current_screen.draw_team(side_scroll, scroll, team_phase, team_sort_type, team_sort_reverse)
    elif is_player(current_screen):
        current_screen.draw_full_player(side_scroll, scroll, view_as)
    elif current_screen == "CHOOSE HOME":
        __draw_choose_home()
    elif current_screen == "CHOOSE AWAY":
        __draw_choose_away()
    elif current_screen == "SEASON":
        __draw_season_screen()
        season1.draw_season()
    elif current_screen == "CHOOSE YOUR TEAM":
        __draw_choose_team()
    elif current_screen == "CHOOSE DIFFICULTY":
        __draw_choose_diffuculty(buttons)
    elif current_screen == "FREE AGENTS":
        season1.free_agents.draw_free_agents(side_scroll, scroll, fa_sort, fa_price, only_rookies)
    elif current_screen in {"TRADE CENTER", "TRADE BLOCK", "RECENT TRADES", "PROPOSE TRADE", "MY TRADES", "TRADE OVERVIEW", "TEAM TRADEABLES"}:
        __draw_trade_center(current_screen)
    elif current_screen == "CHOOSE GAME":
        season1.draw_games_left_this_week()
    else:
        background(100)
        text(current_screen, 50, 50)
    if not (current_screen == "HOME" or current_screen == "CHOOSE YOUR TEAM" or (current_screen == "GAME" and not game1.game_over)): #or (current_screen == "DRAFT" and not draft1.is_done)
        for button in buttons:
            if button.category == "NAVIGATION":
                button.draw_button()
    all_auto = True
    for team in all_teams:
        if not team.user_type == "AUTO":
            all_auto = False
    drafting = False
    try:
        if not draft1.is_done:
            drafting = True
    except:
        pass
    if all_auto and not drafting:
        try:
            try:
                if current_screen == "DRAFT" and draft1.is_done:
                    change_screen("SEASON")
                else:
                    season1.sim_week()
            except:
                season1.sim_week()
        except:
            pass
    if current_screen in {"SEASON", "DRAFT", "LEAGUE STATS", "TRADE CENTER"}:
        get_button("BUFFER", buttons).draw_button()
        for button in buttons:
            if "CHANGE TEAM" in button.category and not button.do == "BUFFER":
                button.draw_button()

def get_button(do, buttons):
    for button in buttons:
        if button.do == do:
            return button
    return None
            
def __draw_auto_draft(draft1, until):
    textSize(35)
    background(100)
    text("Wait... Picking: Round " + str(draft1.get_round()) + ", pick: " + str(draft1.get_pick()), 500, 500)
    if (until == "DONE" and not draft1.is_done) or (until == "USER" and not draft1.current_team.user_type == "USER" and not draft1.is_done):
        make_auto_pick(draft1, True)
        background(100)
        text("Wait... Picking: Round " + str(draft1.get_round()) + ", pick: " + str(draft1.get_pick()), 500, 500)
    else:
        change_screen("DRAFT")
            
def __draw_choose_diffuculty(buttons):
    textSize(50)
    text("Choose Starting Difficulty", 10, 50, 7)
    textSize(25)
    text("Starting Overall", 40, 100, 7)
    text("Scouting", 440, 100, 7)
    text("Cap", 840, 100, 7)
    text("User Teams", 1240, 100, 7)
    for button in buttons:
        if "DIFFICULTY" in button.category:
            button.draw_button()
            
def __draw_trade_center(screen):
    global season1, all_teams
    if screen == "TRADE CENTER":
        season1.trade_center.draw_trade_center()
    elif screen == "TRADE BLOCK":
        season1.trade_center.draw_trade_block(side_scroll, scroll)
    elif screen == "PROPOSE TRADE":
        season1.trade_center.draw_propose_trade(side_scroll, scroll, all_teams)
    elif screen == "RECENT TRADES":
        season1.trade_center.draw_recent_trades(side_scroll, scroll)
    elif screen == "MY TRADES":
        season1.trade_center.draw_my_trades(side_scroll, scroll)
    elif screen == "TRADE OVERVIEW":
        season1.trade_center.draw_trade_overview(side_scroll, scroll)
    elif screen == "TEAM TRADEABLES":
        season1.trade_center.draw_team_tradeables(side_scroll, scroll)

def __draw_league_stats():
    global ls, scroll
    ls.draw_stats(10, 10 + scroll)
    ls.draw_sbs(10, 350 + scroll)
    ls.draw_leaders(300, 50 + scroll)
                        
def __draw_choose_home():
    global all_teams
    for i in range(0, len(all_teams)):
        all_teams[i].draw_team_summary(5 + (i % 6) * 200, 5 + (i / 6) * 200 + scroll)

def __draw_choose_away():
    global all_teams, home_team
    i = 0
    for team in all_teams:
        #if not (team == home_team):
        team.draw_team_summary(5 + (i % 6) * 200, 5 + (i / 6) * 200 + scroll)
        i += 1
        
def __draw_choose_team():
    global scroll, afc_e, afc_s, afc_n, afc_w, nfc_e, nfc_s, nfc_n, nfc_w, user_teams
    textSize(50)
    text("CHOOSE YOUR TEAM", 0, -50 + scroll)
    temp = []
    temp.extend(afc_e)
    temp.extend(afc_s)
    temp.extend(afc_n)
    temp.extend(afc_w)
    temp.extend(nfc_e)
    temp.extend(nfc_s)
    temp.extend(nfc_n)
    temp.extend(nfc_w)
    for i in range(0, len(temp)):
        if not temp[i] in user_teams:
            temp[i].draw_team_summary(5 + (i % 4) * 200, 5 + (i / 4) * 200 + scroll)
        
def __draw_draft_screen():
    global draft1, side_scroll, scroll, draft_sort, user_teams, user_team_number
    draft1.draw_draft(10 + side_scroll, 100 + scroll, draft_sort, user_teams[user_team_number].scouting)
    for team in draft1.teams:
        if team.user_type == "USER":
            return
    make_auto_pick(draft1, False)

                
def __draw_season_screen():
    global season1, scroll, team_schedule, user_teams, user_team_number, ls, buttons
    season1.draw_standings(10, 10 + scroll)
    season1.draw_schedule(500, 10 + scroll, team_schedule)
    fill(150)
    rect(1000, 100, 100, 100, 7)
    fill(0)
    if season1.current_week == season1.draft_week or (season1.current_week == season1.draft_end_week and not draft1.is_done):
        text("DRAFT", 1000, 100, 100, 100)
    elif not season1.ready_to_sim:
        text("ONE OR MORE TEAMS IS NOT FULL", 1000, 100, 100, 100)
    elif season1.current_week == season1.cut_week:
        text("SKIP TO REGULAR SEASON", 1000, 100, 100, 100)
    else:
        text("SIM WEEK", 1000, 100, 100, 100)
    fill(150)
    rect(1000, 250, 100, 100, 7)
    fill(0)
    textSize(30)
    if season1.current_week == season1.resign_week:
        text(str(season1.this_year) + " Resign Week", 1000, 50)
    else:
        text(str(season1.this_year) + " Week " + str(season1.current_week + 1), 1000, 50)
    textSize(15)
    text(" VIEW TEAM", 1000, 250, 100, 100)
    textSize(13)
    text("\n OVR: " + str(int(round(user_teams[user_team_number].get_team_overall()))) + "\n OFF: " + str(int(round(user_teams[user_team_number].offense))) + "\n DEF: " + str(int(round(user_teams[user_team_number].defense))), 1000, 250, 100, 100)
    upgr = 0
    inj = 0
    fa = 0
    negotiate = 0
    for player in user_teams[user_team_number].Players:
        if player.upgrade_available():
            upgr += 1
            fill(85,85,255)
            circle(1015, 336, 20)
            textSize(10)
            fill(0)
            text(upgr, 1010, 339)
        if player.injured:
            inj += 1
            fill(255, 50, 50)
            circle(1040, 336, 20)
            textSize(10)
            fill(0)
            text(inj, 1036, 339)
        if player.contract_length <= 0:
            fa += 1
            fill(255, 255, 0)
            circle(1070, 300, 20)
            textSize(10)
            fill(0)
            text(fa, 1066, 303)
        if player.will_negotiate():
            negotiate += 1
            fill(0, 150, 0)
            circle(1065, 336, 20)
            textSize(10)
            fill(0)
            text(negotiate, 1061, 339)
    textSize(15)
    fill(150)
    rect(1150, 250, 100, 100, 7)
    fill(0)
    text("FREE AGENTS", 1150, 250, 100, 100)
    fill(150)
    rect(1150, 100, 100, 100, 7)
    fill(0)
    text("OTHER TEAMS", 1150, 100, 100, 100)
    fill(150)
    rect(1000, 400, 100, 100, 7)
    fill(0)
    text("PRACTICE GAME", 1000, 400, 100, 100)
    fill(150)
    rect(1150, 400, 100, 100, 7)
    fill(0)
    text("WATCH GAME", 1150, 400, 100, 100)
    fill(150)
    rect(1150, 550, 100, 100, 7)
    fill(0)
    text("LEAGUE STATS", 1150, 550, 100, 100)
    fill(150)
    rect(1000, 550, 100, 100, 7)
    fill(0)
    text("TRADE CENTER", 1000, 550, 100, 100)
    """
    if season1.current_week > 0 and season1.current_week < season1.wildcard_week:
        ls.draw_leaders_ffp("GAME", ls.this_year, 1300, 100, 3, False)
    elif season1.current_week <= 0:
        ls.draw_leaders_ffp("SEASON", ls.this_year-1, 1300, 100, 3, False)
    elif season1.current_week >= season1.wildcard_week:
        ls.draw_leaders_ffp("SEASON", ls.this_year, 1300, 100, 3, False)
    """
                
def __draw_team_screen():
    global afc_e, afc_s, afc_n, afc_w, nfc_e, nfc_s, nfc_n, nfc_w
    temp = []
    temp.extend(afc_e)
    temp.extend(afc_s)
    temp.extend(afc_n)
    temp.extend(afc_w)
    temp.extend(nfc_e)
    temp.extend(nfc_s)
    temp.extend(nfc_n)
    temp.extend(nfc_w)
    for i in range(0, len(temp)):
        temp[i].draw_team_summary(5 + (i % 4) * 200, 5 + (i / 4) * 200 + scroll)
    
def mouseClicked():
    global game1, draft1, draft_sort, all_teams, first_draft, home_team, away_team, afc_e, afc_n, afc_s, afc_w, nfc_e, nfc_n, nfc_s, nfc_w, season1, is_first_season, user_teams, user_team_number, team_phase, player_team, team_sort_type, team_sort_reverse, team_schedule, fa_sort, fa_price, ls, user_overall, buttons, scouting, user_cap, scroll, side_scroll, view_as, only_rookies
    if  not (current_screen == "HOME" or current_screen == "CHOOSE YOUR TEAM" or (current_screen == "GAME" and not game1.game_over)):
        clicked = button_clicked(mouseX, mouseY, buttons, "NAVIGATION", "NONE")
        if not clicked == "":
            if current_screen == "GAME":
                for game in season1.schedule[season1.current_week]:
                    if game[0] == game1.away_team and game[1] == game1.home_team:
                        game.extend([game1.away_team_score, game1.home_team_score])
            elif is_player(current_screen):
                current_screen.player_mode = "NONE"
            change_screen("SEASON")
    if current_screen in {"SEASON", "DRAFT", "LEAGUE STATS", "TRADE CENTER"}:
        clicked = button_clicked(mouseX, mouseY, buttons, "CHANGE TEAMS", "EXCLUSIVE")
        if not clicked == "":
            if clicked == "BUFFER":
                return
            user_team_number = clicked
            team_schedule = user_teams[user_team_number]
            return
    if current_screen == "GAME":
        if not game1.clicked(mouseX, mouseY):
            game1.advance_play()
    elif current_screen == "DRAFT" and not draft1.is_done:
        make_user_pick(draft1, mouseX, mouseY, side_scroll, scroll)
        draft1.clicked(mouseX, mouseY, user_teams[user_team_number])
    elif current_screen == "TEAM":
        x = mouseX / 200
        y = (mouseY - scroll) / 200
        team_num = 4*y + x
        temp = []
        temp.extend(afc_e)
        temp.extend(afc_s)
        temp.extend(afc_n)
        temp.extend(afc_w)
        temp.extend(nfc_e)
        temp.extend(nfc_s)
        temp.extend(nfc_n)
        temp.extend(nfc_w)
        if team_num < len(temp) and x < 4:
            change_screen(temp[team_num])
    elif current_screen == "CHOOSE HOME":
        x = mouseX / 200
        y = (mouseY - scroll) / 200
        team_num = 6*y + x
        if team_num < len(all_teams) and x < 6:
            home_team = all_teams[team_num]
            change_screen("CHOOSE AWAY")
    elif current_screen == "CHOOSE AWAY":
        x = mouseX / 200
        y = (mouseY - scroll) / 200
        team_num = 6*y + x
        if team_num < len(all_teams) and x < 6 and y >= 0:
            #if all_teams.index(home_team) <= team_num:
            #team_num += 1
            away_team = all_teams[team_num]
            #else:
            #away_team = all_teams[team_num]
            if (not (home_team == away_team)):    
                game1 = Game(home_team, away_team, "PRE SEASON", 0)
                game1.play_game()
                change_screen("GAME")
    elif current_screen == "SEASON":
        season1.clicked(mouseX, mouseY)
        if mouseX > 1000 and mouseX < 1100 and mouseY > 100 and mouseY < 200:
            user_teams[user_team_number].ready_to_advance = True
            if not season1.current_week == season1.draft_week + 1 or draft1.is_done:
                for team in user_teams:
                    if not team.ready_to_advance or team.user_type == "AUTO":
                        return
            season1.sim_week()
            for team in user_teams:
                team.ready_to_advance = False
        
        if mouseX > 1000 and mouseX < 1100 and mouseY > 250 and mouseY < 350:
            change_screen(user_teams[user_team_number])
        if mouseX > 1150 and mouseX < 1250 and mouseY > 100 and mouseY < 200:
            change_screen("TEAM")
        if mouseX > 1000 and mouseX < 1100 and mouseY > 400 and mouseY < 500 and season1.all_teams_full():
            change_screen("CHOOSE HOME")
        if mouseX > 1150 and mouseX < 1250 and mouseY > 250 and mouseY < 350:
            change_screen("FREE AGENTS")
        if mouseX > 1150 and mouseX < 1250 and mouseY > 400 and mouseY < 500 and season1.all_teams_full():
            if season1.current_week >= 0:
                change_screen("CHOOSE GAME")
        if mouseX > 1000 and mouseX < 1100 and mouseY > 550 and mouseY < 650:
            change_screen("TRADE CENTER")
        if mouseX > 1150 and mouseX < 1250 and mouseY > 550 and mouseY < 650:
            change_screen("LEAGUE STATS")
        x = mouseX - 10
        y = mouseY - scroll - 10
        if x > 0 and x < 200:
            if y > 20 and y < 100:
                num = int(y - 20)/20
                team_schedule = season1.afc_east[num]
            elif y > 140 and y < 220:
                num = int(y - 140)/20
                team_schedule = season1.afc_south[num]
            elif y > 260 and y < 340:
                num = int(y - 260)/20
                team_schedule = season1.afc_north[num]
            elif y > 380 and y < 460:
                num = int(y - 380)/20
                team_schedule = season1.afc_west[num]
            elif y > 500 and y < 580:
                num = int(y - 580)/20
                team_schedule = season1.nfc_east[num]
            elif y > 620 and y < 700:
                num = int(y - 620)/20
                team_schedule = season1.nfc_south[num]
            elif y > 740 and y < 820:
                num = int(y - 740)/20
                team_schedule = season1.nfc_north[num]
            elif y > 860 and y < 940:
                num = int(y - 860)/20
                team_schedule = season1.nfc_west[num]
            else:
                team_schedule = "NONE"
    elif current_screen == "CHOOSE YOUR TEAM":
        x = mouseX / 200
        y = (mouseY - scroll) / 200
        team_num = 4*y + x
        temp = []
        temp.extend(afc_e)
        temp.extend(afc_s)
        temp.extend(afc_n)
        temp.extend(afc_w)
        temp.extend(nfc_e)
        temp.extend(nfc_s)
        temp.extend(nfc_n)
        temp.extend(nfc_w)
        if team_num < len(temp) and x < 4:
            mega_draft = (user_overall == 0)
            added_team = temp[team_num]
            if not added_team in user_teams:
                added_team.user_type = "USER"
                added_team.scouting = scouting
                added_team.max_cap = user_cap
                added_team.cap_left = user_cap
                user_teams.append(added_team)
            if len(user_teams) == user_team_number:
                for team in all_teams:
                    if team.user_type == "USER":
                        team.ready_to_advance = False
                        if mega_draft:
                            team.clear_team()
                            for i in range(8, 54):
                                team.draft_picks.append([i, team.abbreviation, 1966])
                        else:
                            team.set_random_team(user_overall)
                    else:
                        if mega_draft:
                            team.clear_team()
                            for i in range(8, 54):
                                team.draft_picks.append([i, team.abbreviation, 1966])
                        else:
                            team.set_random_team(75)
                all_teams.sort(key = by_team_overall, reverse = False)
                if mega_draft:
                    r.shuffle(all_teams)
                    set_draft_picks(all_teams, 53, True, 1966)
                else:
                    set_draft_picks(all_teams, 7, False, 1966)
                season1 = Season(all_teams, afc_e, afc_n, afc_s, afc_w, nfc_e, nfc_n, nfc_s, nfc_w, [afc_e, afc_n, afc_s, afc_w], [nfc_e, nfc_s, nfc_n, nfc_w], ["AFC", "NFC"], FreeAgents([Player("OL", 55)]), 1966, mega_draft)
                is_first_season = False
                for i in range(0, user_team_number):
                    buttons.append(Button(450 + (85 * i) % 1360, 900 + 35*(i/16), 85, 35, str(i+1) + ". " + user_teams[i].abbreviation, i, "CHANGE TEAMS"))
                buttons.append(Button(425, 875, min(50 + 85*user_team_number, 1385), 85 + 35*(user_team_number/16), "", "BUFFER", "CHANGE TEAMS"))
                user_team_number = 0
                ls.update_all_players(season1)
                change_screen("SEASON")
    elif current_screen == "CHOOSE DIFFICULTY":
        clicked = button_clicked(mouseX, mouseY, buttons, "DIFFICULTY OVR", "EXCLUSIVE")
        if not clicked == "":
            user_overall = clicked
        clicked = button_clicked(mouseX, mouseY, buttons, "DIFFICULTY DRAFT", "EXCLUSIVE")
        if not clicked == "":
            scouting = clicked
        clicked = button_clicked(mouseX, mouseY, buttons, "DIFFICULTY CAP", "EXCLUSIVE")
        if not clicked == "":
            user_cap = clicked
        clicked = button_clicked(mouseX, mouseY, buttons, "DIFFICULTY TEAMS", "EXCLUSIVE")
        if not clicked == "":
            user_team_number = clicked
        clicked = button_clicked(mouseX, mouseY, buttons, "DIFFICULTY CONTINUE", "NONE")
        if clicked == "CONTINUE":
            change_screen("CHOOSE YOUR TEAM")
    elif is_team(current_screen):
        if "TOGGLE" == button_clicked(mouseX, mouseY, current_screen.buttons, "ALL", "FLIP"):
            current_screen.show_overall = not current_screen.show_overall
        x = mouseX - side_scroll
        y = mouseY - scroll
        if x > 400 and x < 450 and y > -75 and y < -25:
            team_phase = "MORE"
        elif x > 450 and x < 600 and y > -75 and y < -25:
            team_phase = "STRATEGY"
        elif x > 600 and x < 750 and y > -75 and y < -25:
            team_phase = "OFFENSE"
        elif x > 750 and x < 900 and y > -75 and y < -25:
            team_phase = "DEFENSE"
        elif x > 900 and x < 1050 and y > -75 and y < -25:
            team_phase = "SPECIAL"
        elif x > 1050 and x < 1100 and y > -75 and y < -25:
            team_phase = "NUMBERS"
        elif team_phase == "MORE":
            if y > 35 and y < 60:
                if x > 5:
                    if x < 205:
                        team_sort_reverse = not team_sort_reverse
                        team_sort_type = 0
                    elif x < 255:
                        team_sort_reverse = not team_sort_reverse
                        team_sort_type = 1
                    elif x < 305:
                        team_sort_reverse = not team_sort_reverse
                        team_sort_type = 2
                    elif x < 355:
                        team_sort_reverse = not team_sort_reverse
                        team_sort_type = 3
                    elif x < 430:
                        team_sort_reverse = not team_sort_reverse
                        team_sort_type = 4
                    elif x < 555:
                        team_sort_reverse = not team_sort_reverse
                        team_sort_type = 5
                    elif x < 625:
                        team_sort_reverse = not team_sort_reverse
                        team_sort_type = 6
            elif team_phase == "MORE":
                if x > 1100 and x < 1250 and y > -25 and y < 25:
                    if user_teams[user_team_number].user_type == "AUTO":
                        user_teams[user_team_number].user_type = "USER"
                    else:
                        user_teams[user_team_number].user_type = "AUTO"
        elif team_phase == "NUMBERS":
            ls.clicked(mouseX, mouseY, "SCOPE", 50 + side_scroll)
            """if x > 5:
                current_screen.numbers_sort_order = not current_screen.numbers_sort_order
                if x < 130:
                    current_screen.numbers_table_sort = 0
                else:
                    current_screen.numbers_table_sort = (int(x) - 130) / 75 + 1"""
        elif current_screen == user_teams[user_team_number] or True:
            if x > 1100 and x < 1250 and y > -75 and y < -25:
                current_screen.best_lineup()
            elif team_phase == "STRATEGY":
                current_screen.check_for_strategy(x, y)
            else:
                scr = current_screen.check_for_clicked(x, y, team_phase)
                if is_player(scr[0]):
                    view_as = scr[1]
                    player_team = current_screen
                    change_screen(scr[0])
    elif is_player(current_screen):
        player_clicked(mouseX, mouseY, player_team, current_screen, user_teams, user_team_number, season1, side_scroll, scroll, view_as)
    elif current_screen == "FREE AGENTS":
        x = mouseX - side_scroll
        y = mouseY - scroll
        if x > 0 and x < 1350 and y > 0:
            player_num = 9 * int(y / 175) 
            player_num += int(x / 150)
            if player_num >= 0 and player_num < len(season1.free_agents.players):
                if fa_sort == "NONE" and fa_price >= 200000000 and only_rookies == False:
                    bid = min(season1.free_agents.players[player_num].min_contract(), user_teams[user_team_number].max_offer)
                    if season1.free_agents.bids[player_num][0] >= bid:
                        bid = min(season1.free_agents.bids[player_num][0] + 500000, user_teams[user_team_number].max_offer)
                    if bid > season1.free_agents.bids[player_num][0]:
                        season1.free_agents.bid_on_free_agent(season1.free_agents.players[player_num], user_teams[user_team_number], bid)
                        user_teams[user_team_number].fa_bids += bid
                        user_teams[user_team_number].fas += 1
                        user_teams[user_team_number].calculate_cap_left()
                        season1.teams_bid_on_fas()
                else:
                    count = -1
                    i = 0
                    for player in season1.free_agents.players:
                        if player.position == fa_sort and fa_price >= max(season1.free_agents.bids[i][0], player.min_contract()) and (player.years_played == 0 or not only_rookies):
                            count += 1
                            if count == player_num:
                                i = season1.free_agents.players.index(player)
                                bid = min(season1.free_agents.players[i].min_contract(), user_teams[user_team_number].max_offer)
                                if season1.free_agents.bids[i][0] >= bid:
                                    bid = min(season1.free_agents.bids[i][0] + 500000, user_teams[user_team_number].max_offer)
                                if bid > season1.free_agents.bids[i][0]:
                                    season1.free_agents.bid_on_free_agent(season1.free_agents.players[i], user_teams[user_team_number], bid)
                                    user_teams[user_team_number].fa_bids += bid
                                    user_teams[user_team_number].fas += 1
                                    user_teams[user_team_number].calculate_cap_left()
                                    season1.teams_bid_on_fas()
                        i += 1
    elif current_screen in {"TRADE CENTER", "TRADE BLOCK", "RECENT TRADES", "PROPOSE TRADE", "MY TRADES", "TRADE OVERVIEW", "TEAM TRADEABLES"}:
        if current_screen == "TRADE CENTER":
            season1.trade_center.trade_center_clicked(mouseX, mouseY)
        elif current_screen == "TRADE BLOCK":
            season1.trade_center.trade_block_clicked(side_scroll, scroll, mouseX, mouseY)
        elif current_screen == "RECENT TRADES":
            season1.trade_center.recent_trades_clicked(scroll, side_scroll, mouseX, mouseY)
        elif current_screen == "PROPOSE TRADE":
            season1.trade_center.propose_trade_clicked(side_scroll, scroll, all_teams, mouseX, mouseY)
        elif current_screen == "MY TRADES":
            season1.trade_center.my_trades_clicked(side_scroll, scroll, mouseX, mouseY)
        elif current_screen == "TRADE OVERVIEW":
            season1.trade_center.trade_overview_clicked(side_scroll, scroll, mouseX, mouseY)
        elif current_screen == "TEAM TRADEABLES":
            season1.trade_center.team_tradeables_clicked(side_scroll, scroll, mouseX, mouseY)
    elif current_screen == "CHOOSE GAME":
        if mouseX > 5 and mouseY > 50:
            x = int(mouseX - 5)/450
            y = int(mouseY - 50)/50
            game_num = x + y*3
            i = -1
            for game in season1.schedule[season1.current_week]:
                if len(game) == 2:
                    i += 1
                    if game_num == i:
                        game_type = "PRE SEASON"
                        if season1.current_week >= 0 and season1.current_week < season1.wildcard_week:
                            game_type = "REGULAR"
                        elif season1.current_week == season1.sb_week:
                            game_type = "SB"
                        elif season1.current_week == season1.pro_bowl_week:
                            game_type = "PRO BOWL"
                        elif season1.current_week >= season1.wildcard_week:
                            game_type = "PLAYOFF"
                        game1 = Game(game[1], game[0], game_type, season1.this_year)
                        game1.play_game()
                        change_screen("GAME")
    elif current_screen == "LEAGUE STATS":
        ls.clicked(mouseX, mouseY)
        
def get_team_from_name(name):
    global all_teams
    for team in all_teams:
        if team.team_name == name or team.team_location == name or team.abbreviation == name or team.name() == name:
            return team
    print str(name) + " has no team" 
    return None
        
def player_clicked(mouse_x, mouse_y, player_team, current_screen, user_teams, user_team_number, season1, side_scroll, scroll, pos):
    if mouse_x > 1300 and mouse_y > 50 and mouse_y < 100:
        current_screen.player_mode = "NONE"
        change_screen(player_team)
        return
    if not current_screen.team == user_teams[user_team_number].abbreviation:
        return
    current_screen.player_clicked(side_scroll, scroll, player_team, season1, mouse_x, mouse_y, pos)
                        
def keyPressed():
    global game1, draft1, draft_sort, home_team, away_team, fa_sort, fa_price, only_rookies
    global season1, all_teams, auto_draft_end, scroll, side_scroll
        
    if keyCode == UP:
        scroll += 50
    if keyCode == DOWN:
        scroll -= 50
    if keyCode == LEFT:
        side_scroll += 50
    if keyCode == RIGHT:
        side_scroll -= 50
    if key == " ":
        if current_screen == "GAME":
            game1.advance_play()
    if key == "s":
        if current_screen == "GAME":
            while not game1.game_over:
                game1.advance_play()
    if key == "r":
        if current_screen == "GAME" and game1.game_type == "PRE SEASON":
            game1 = Game(home_team, away_team, "PRE SEASON", 0)
            game1.play_game()
        elif current_screen == "DRAFT":
            draft_sort = "RB"
        elif current_screen == "FREE AGENTS":
            fa_sort = "RB"
    if key == "1":
        if current_screen == "FREE AGENTS":
            only_rookies = not only_rookies
    if key == "2":
        if current_screen == "GAME":
            while game1.quarter < 2:
                game1.advance_play()
    if key == "3":
        if current_screen == "GAME":
            while game1.quarter < 3:
                game1.advance_play()
    if key == "4":
        if current_screen == "GAME":
            while game1.quarter < 4:
                game1.advance_play()
    if key == "5":
        if current_screen == "GAME":
            while not (game1.quarter >= 4 and game1.seconds_left <= 120):
                game1.advance_play()
        if current_screen == "FREE AGENTS":
            fa_price = 500000
    if key == "q":
        if current_screen == "GAME" and False:
            wins = 0
            ties = 0
            losses = 0
            max_score = 0
            for x in range(0,10):
                game1 = Game(home_team, away_team, "PRE SEASON", 0)
                game1.play_game()
                while not game1.game_over:
                    game1.advance_play()
                if game1.home_team_score > game1.away_team_score:
                    wins += 1
                elif game1.home_team_score == game1.away_team_score:
                    ties += 1
                else:
                    losses += 1
                max_score = max(max(max_score, game1.home_team_score),game1.away_team_score)
            println(str(wins) + "-" + str(losses) + "-" + str(ties))
            println(max_score)
        elif current_screen == "DRAFT":
            draft_sort = "QB"
        elif current_screen == "FREE AGENTS":
            fa_sort = "QB"
    if key == "f":
        if current_screen == "GAME":
            while not (game1.play.is_change_of_possession()) and not (game1.game_over):
                game1.advance_play()
    if key == "i":
        if current_screen == "GAME":
            while not (game1.play.injury) and not (game1.game_over):
                game1.advance_play()
    if key == "a":
        if current_screen == "DRAFT":
            change_screen("AUTO DRAFTING")
            auto_draft_end = "DONE"
    if key == "w":
        if current_screen == "DRAFT":
            draft_sort = "WR"
        elif current_screen == "FREE AGENTS":
            fa_sort = "WR"
    if key == "t":
        if current_screen == "DRAFT":
            draft_sort = "TE"
        elif current_screen == "FREE AGENTS":
            fa_sort = "TE"
    if key == "o":
        if current_screen == "DRAFT":
            draft_sort = "OL"
        elif current_screen == "FREE AGENTS":
            fa_sort = "OL"
    if key == "d":
        if current_screen == "DRAFT":
            draft_sort = "DL"
        elif current_screen == "FREE AGENTS":
            fa_sort = "DL"
        elif current_screen == "GAME":
            while not game1.game_over and not game1.down == 4 and not ((game1.quarter == 2 or game1.quarter >= 4) and game1.seconds_left <= 120) and not(game1.quarter >=4 and game1.offense_score() < game1.defense_score() and game1.is_kickoff()) and not (game1.play.is_offensive_touchdown or game1.play.is_defensive_touchdown):
                game1.advance_play()
    if key == "l":
        if current_screen == "DRAFT":
            draft_sort = "LB"
        elif current_screen == "FREE AGENTS":
            fa_sort = "LB"
    if key == "b":
        if current_screen == "DRAFT":
            draft_sort = "DB"
        elif current_screen == "FREE AGENTS":
            fa_sort = "DB"
    if key == "k":
        if current_screen == "DRAFT":
            draft_sort = "K"
        elif current_screen == "FREE AGENTS":
            fa_sort = "K"
    if key == "e":
        if current_screen == "DRAFT":
            draft_sort = "RT"
        elif current_screen == "FREE AGENTS":
            fa_sort = "RT"
    if key == "n":
        if current_screen == "DRAFT":
            draft_sort = "NONE"
        elif current_screen == "FREE AGENTS":
            fa_sort = "NONE"
            fa_price = 200000000
    if key in {'=', '+'}:
        if current_screen == "FREE AGENTS":
            fa_price += 100000
    if key in {'-', '_'}:
        if current_screen == "FREE AGENTS":
            fa_price -= 100000
    if key == "p":
        make_auto_pick(draft1, False)
    
            
def change_screen(new_screen):
    global current_screen, scroll, side_scroll, ls
    current_screen = new_screen
    if new_screen == "LEAGUE STATS":
        ls.reset_buttons()
    if is_team(new_screen) or is_player(new_screen):
        scroll = 100
    else:
        scroll = 0
    side_scroll = 0
        
def divide_maybe_zero(num1, num2):
    return divide_maybe_zero_default(num1, num2, 0)
    
def divide_maybe_zero_default(num1, num2, default):
    if num2 == 0:
        return default
    else:
        return float(num1)/num2
    
def bound(c, mini = 0, maxi = 100):
    if c < mini:
        return mini
    if c > maxi:
        return maxi
    return c
        
def fix_list_chances(l):
    total_chance = 0
    unders = []
    in_range = 0
    for i in range(0, len(l)):
        if l[i] < 0:
            unders.append(i)
            l[i] = 0
        elif l[i] > 100:
            l[i] = 100
            for j in range(0, len(l)):
                if not i == j:
                    l[j] = 0
            return
        else:
            in_range += 1
            total_chance += l[i]
            
    for i in range(0, len(l)):
        if not i in unders:
            l[i] += float(100 - total_chance)/in_range
            if l[i] > 100:
                fix_list_chances(l)
                
def random_ovr_from_age(age, skew = 0):
    proj_ovr = 55
    ovr = 55
    if age <= 23:
        proj_ovr = min_max_skew(45+skew, 73+skew)
        ovr = min(random_skew(proj_ovr, 4), 80+skew)
    elif age <= 26:
        proj_ovr = min_max_skew(60+skew, 88+skew)
        ovr = min(random_skew(proj_ovr, 5), 95+skew)
    elif age <= 30:
        proj_ovr = min_max_skew(64+skew, 92+skew)
        ovr = min(random_skew(proj_ovr, 5), 99+skew)
    elif age <= 35:
        proj_ovr = min_max_skew(60+skew, 88+skew)
        ovr = min(random_skew(proj_ovr, 5), 95+skew)
    elif age <= 40:
        proj_ovr = min_max_skew(55+skew, 83+skew)
        ovr = min(random_skew(proj_ovr, 5), 90+skew)
    else:
        proj_ovr = min_max_skew(50+skew, 78+skew)
        ovr = min(random_skew(proj_ovr, 5), 85+skew)
    ovr = min(99, ovr)
    ovr = max(45, ovr)
    proj_ovr = min(99, proj_ovr)
    proj_ovr = max(45, proj_ovr)
    return (ovr, proj_ovr)
        
        
def random_starting_age():
    rand = random(0, 1)
    if rand < 0.2:
        return int(random(21, 22))
    elif rand < 0.7:
        return int(random(23, 26))
    elif rand < 0.9:
        return int(random(27, 30))
    else:
        return int(random(30, 36))
        
def make_user_pick(draft1, mouse_x, mouse_y, side_scroll, scroll):
    global user_teams, user_team_number, use_overall
    if not draft1.current_team == user_teams[user_team_number]:
        return
    x = mouse_x - 10 - side_scroll
    y = mouse_y - 100 - scroll
    if x > 0 and x < 1350 and y > 0:
        player_num = 9 * int(y / 175) 
        player_num += int(x / 150)
        if player_num >= 0 and player_num < len(draft1.players):
            if draft_sort == "NONE":
                draft1.sign_player(draft1.players[player_num])
            else:
                count = -1
                for player in draft1.players:
                    if player.position == draft_sort:
                        count += 1
                        if count == player_num:
                            draft1.sign_player(player)
            draft1.set_pick(1)
                
def make_auto_pick(draft1, auto_user):
    global use_overall
    if draft1.current_team.user_type == "BEST" and not draft1.is_done:
        #draft1.sort_by("OVERALL", 250)
        best_ovr = draft1.players[i].overall(use_overall)
        best_ind = 0
        for i in range(1, len(draft1.players)):
            ovr = draft1.players[i].overall(use_overall)
            if ovr > best_ovr:
               best_ovr = ovr
               best_ind = i
        draft1.sign_player(draft1.players[best_ind]) 
        draft1.set_pick(1)
    elif (draft1.current_team.user_type == "AUTO" or (auto_user and draft1.current_team.user_type == "USER")) and not draft1.is_done:
        #draft1.sort_by("MY VALUE", draft1.current_team, 250)
        best_value = draft1.current_team.draft_in_value(draft1.players[0], not draft1.mega_draft)
        best_ind = 0
        for i in range(1, len(draft1.players)):
            value = draft1.current_team.draft_in_value(draft1.players[i], not draft1.mega_draft)
            if value > best_value:
                best_value = value
                best_ind = i
        draft1.sign_player(draft1.players[best_ind])
        draft1.set_pick(1)

def set_draft_picks(teams_in_order, rounds, snake, this_year):
    pick_num = 0
    order = []
    for team in teams_in_order:
        order.append(team.abbreviation)
    #if first_draft:
    #    r.shuffle(order)
    for i in range(0, rounds):
        if snake and i > 0:
            order.reverse()
        for k in range(0, 32):                                   # for each pick in the round
            for team in teams_in_order:                          # find the team who has the next pick
                for pick in team.draft_picks:                    # find the next pick
                    if pick[0] == i + 1 and pick[1] == order[k] and pick[2] == this_year: 
                        pick[1] = k + 1                          # set the pick

def button_draw(buttons, category):
    for button in buttons:
        if button.category == category or category == "ALL":
            button.draw_button()

def button_clicked(mouse_x, mouse_y, buttons, category, highlight_type):
    for button in buttons:
        if button.category == category or category == "ALL":
            if button.clicked(mouse_x, mouse_y):
                if highlight_type == "EXCLUSIVE" and not button.do == "BUFFER":
                    for button2 in buttons:
                        if button2.category == category:
                            button2.highlight = False
                    button.highlight = True
                elif highlight_type == "INCLUSIVE" and not button.do == "BUFFER":
                    button.highlight = True
                elif highlight_type == "FLIP":
                    button.highlight = not button.highlight
                return button.do
    return ""

def random_skew(mean, stdev):
    num = 3.5*(random(0,1)-0.4)**3 + 0.224
    return num*(stdev/sqrt(0.043575)) + (mean - 0.315*(stdev/sqrt(0.043575)))

def reverse_skew(mean, stdev):
    num = 0.98 - (3.5*(random(0,1)-0.4)**3 + 0.224)
    return num*(stdev/sqrt(0.043575)) + (mean - 0.665*(stdev/sqrt(0.043575)))

def min_max_skew(min_val, max_val):
    stdev = (max_val - min_val)/4.694694946
    mean = min_val + 1.50900909*stdev
    return random_skew(mean, stdev)

def rand_first_name():
    global first_names
    return first_names[int(random(0,len(first_names)))]

def rand_last_name():
    global last_names
    return last_names[int(random(0,len(last_names)))]

def rand_ability_type():
    rand = int(random(0,10))
    if rand < 2:
        return "BAD"
    if rand < 8:
        return "NORMAL"
    if rand < 10:
        return "GOOD"
    
def rand_stat(ovr, avg_for_75, jump):
    return avg_for_75 + random_skew(jump*(ovr - 75), 8*jump)
    
def reverse_stat(ovr, avg_for_75, jump):
    return avg_for_75 + reverse_skew(-1*jump*(ovr-75), 8*jump)
    
def stat_to_ovr(rating, avg_for_75, jump, min_rat = "NA", max_rat = "NA"):
    ret = 75 + (rating - avg_for_75)/jump
    if not min_rat == "NA":
        ret = max(min_rat, ret)
    if not max_rat == "NA":
        ret = min(max_rat, ret)
    return ret

def reverse_stat_to_ovr(rating, avg_for_75, jump, min_rat = "NA", max_rat = "NA"):
    ret = 75 - (rating - avg_for_75)/jump
    if not min_rat == "NA":
        ret = max(min_rat, ret)
    if not max_rat == "NA":
        ret = min(max_rat, ret)
    return ret

def by_mvp_points(player, scope, this_year, record_matters):
    try:
        return player.get_mvp_points(scope, this_year, record_matters)
    except:
        return -1

def by_rating(player, scope, type, this_year = 0):
    try:
        return player.get_stat_rating(scope, type, this_year)
    except:
        return -1
    
def by_depth(player):
    try:
        return player.depth
    except:
        return -2
    
def by_contract_amount(player):
    try:
        return player.contract_amount
    except:
        return -1

def by_overall(player, pos = "NONE"):
    global use_overall
    try:
        if pos == "NONE":
            pos = player.position
        return player.get_overall(pos, use_overall)
    except:
        return -1
    
def by_team_overall(team):
    try:
        return team.get_team_overall()
    except:
        return -1
    
def by_value(player, is_projected):
    try:
        return player.get_value_proj(is_projected)
    except:
        return -1
    
def by_team_draft_value(team, player, is_projected):
    try:
        return team.draft_in_value(player, is_projected)
    except:
        return -1

def by_proj_overall(player):
    return player.projected_ovr

def by_division_record(division):
    percentage = 0
    for team in division:
        percentage += team.standings_data[4]
    return percentage
    
def by_conference_record(conf):
    percentage = 0
    for division in conf:
        for team in division:
            percentage += team.standings_data[4]
    return percentage
    
def sort_conferences(afc, nfc_):
    afc_pct = 0
    nfc_pct = 0
    for division in afc:
        for team in division:
            afc_pct += team.standings_data[4]
    for division in nfc_:
        for team in division:
            nfc_pct += team.standings_data[4]
    if afc_pct > nfc_pct:
        return [ "AFC", "NFC" ]
    else:
        return [ "NFC", "AFC" ]
      
def by_team_record(team):
    return team.standings_data[4]

def by_team_point_diff(team):
    return team.standings_data[5] - team.standings_data[6]

def by_list_index(list_, index):
    try:
        x = 0
        if not is_number(list_[index]):
            num = ""
            while list_[index][x] in "0123456789.-":
                num += list_[index][x]
                x += 1
        if x > 0:
            return float(num)
        return list_[index]
    except:
        return 0
    
def by_player_stats(player, scope, stat_type, this_year):
    return player.career_stats.get_stat(scope, stat_type, this_year)

def boost_to_ovr(boost):
    if boost == "GOOD":
        return 2
    if boost == "BAD":
        return -2
    return 0

def random_position():
    rand = random(0,39)
    if rand < 2:   
        return "QB" 
    elif rand < 5: 
        return "RB"
    elif rand < 9:   
        return "WR" 
    elif rand < 12: 
        return "TE"  
    elif rand < 18:
        return "OL"  
    elif rand < 25:
        return "DL"  
    elif rand < 30:
        return "LB"  
    elif rand < 37:
        return "DB"  
    elif rand < 38:
        return "K"  
    else:
        return "RT" 
    
def draw_table(headers, column_sizes, row_height, row_data, x, y):
    draw_table_h(headers, column_sizes, row_height, row_data, x, y, [False], False, 0)

def draw_table_h(headers, column_sizes, row_height, row_data, x, y, highlight, column_highlight, sort_column):
    stroke(0)
    fill(150)
    rect(x, y, sum(column_sizes), row_height*(len(row_data) + 1))
    #grid(column_sizes, row_height, len(row_data), x, y)
    fill(0)
    textSize(15)
    table_width = sum(column_sizes)
    if column_highlight:
        fill(200, 200, 200)
        sort_column = min(sort_column, len(column_sizes) - 1)
        rect(x + sum(column_sizes[0:sort_column]), y, column_sizes[sort_column], (len(row_data) + 1) * row_height)
    for i in range(0, len(highlight)):
        if highlight[i]:
            fill(200, 200, 0)
            rect(x, y + row_height*(i+1), table_width, row_height)
    fill(150, 150, 175)
    rect(x, y, table_width, row_height)
    fill(0)
    grid(column_sizes, row_height, len(row_data), x, y)
    add_x = 0
    for i in range(0, len(column_sizes)):
        try:
            text(" " + headers[i], x + add_x, y, column_sizes[i], row_height)
        except:
            print(i)
            print("size: " + str(len(column_sizes)))
        add_x += column_sizes[i]
    r = 0
    add_x = 0
    for row in row_data:
        r += 1
        add_x = 0
        for i in range(0, len(row)):
            if headers[i] == "PCT":
                text(" " + str(round(row[i], 3)), x + add_x, y + r*row_height, column_sizes[i], row_height)
            elif is_number(row[i]):
                try:
                    text(" " + str(int(round(row[i]))), x + add_x, y + r*row_height, column_sizes[i], row_height)
                except:
                    println(i)
                    println(str(row[0]) + ", " + str(row[1]) + ", " + str(row[2]))
            elif "don't round" in row[i]:
                #try:
                num = float(row[i][0:row[i].index("don't round")])
                #except:
                    #print "don't round"
                    #print row[i]
                text(" " + str(round(num, 1)), x + add_x, y + r*row_height, column_sizes[i], row_height)
            else:
                text(" " + row[i], x + add_x, y + r*row_height, column_sizes[i], row_height)
            add_x += column_sizes[i]
        
def grid(column_sizes, row_height, rows, x, y):
    x_add = 0
    for column in range(0, len(column_sizes)):
        line(x + x_add, y, x + x_add, y + row_height * (rows + 1))
        x_add += column_sizes[column]
    line(x + x_add, y, x + x_add, y + row_height * (rows + 1))
    for row in range(0, rows + 2):
        line(x, y + row_height*row, x + x_add, y + row_height*row)   
        
def make_career_table(stat_type, scope, this_year, player, x, y, sort_index, is_min_max, highlighting = False, column_highlight = False):
    global use_overall
    headers = ["Year", "Name", "Pos", "Ovr", "Team", "Rating"]
    column_sizes = [75, 125, 75, 75, 75, 75]
    row_height = 20
    table_rows = []
    add_to_headers = []
    stats_to_show = []
    indices_to_not_round = []
    bottom_row = []
    
    if stat_type in {"RUN", "RUSH"}:
        add_to_headers =       ["Att",     "Yds",        "Avg",            "TD",       "Long",            "Fum"]
        stats_to_show =        ["CARRIES", "RUSH YARDS", "RUSH YARDS AVG PER CARRIES", "RUSH TDS", "RUSH YARDS LONG", "RUSH FUMBLES"]
        indices_to_not_round = [8]
    elif stat_type in {"RECEIVE", "CATCH"}:
        add_to_headers =       ["Routes",     "Targets", "Catches", "Yds",             "Avg",                 "TD",            "Long",                 "Fum",              "Drops", "YAC"]
        stats_to_show =        ["ROUTES RUN", "TARGETS", "CATCHES", "RECEIVING YARDS", "RECEIVING YARDS AVG PER CATCHES", "RECEIVING TDS", "RECEIVING YARDS LONG", "RECEIVER FUMBLES", "DROPS", "YAC"]
        indices_to_not_round = [10]
    elif stat_type in {"THROW", "PASS"}:
        add_to_headers =       ["Att",           "Complete",         "%",                                  "Yds",        "Avg",            "TD",       "INT",       "Long",            "Fum",           "Sacked",       "Yds"]
        stats_to_show =        ["PASS ATTEMPTS", "PASS COMPLETIONS", "PASS COMPLETIONS PCT PER PASS ATTEMPTS", "PASS YARDS", "PASS YARDS AVG PER PASS COMPLETIONS", "PASS TDS", "PASS INTS", "PASS YARDS LONG", "POCKET FUMBLES", "TIMES SACKED", "SACKED YARDS"]
        indices_to_not_round = [8, 10]
    elif "BLOCK" in stat_type:
        type = stat_type[0:stat_type.index("BLOCK")]
        add_to_headers =       ["Att",                   "BLK",                "%"]
        stats_to_show =        [type + "BLOCK ATTEMPTS", type + "BLOCKS MADE", type + "BLOCKS MADE PCT PER " + type + "BLOCK ATTEMPTS"]
        indices_to_not_round = [8]
    elif "COVER" in stat_type:
        type = stat_type[0:stat_type.index("COVER")]
        add_to_headers =       ["Covers",        "Targets",         "Complete",                   "%",                                                      "Yds",                        "TD",                      "INT",          "Return",                   "Pick 6s",           "Tackles",               "FF",              "Safeties"]
        stats_to_show =        [type + "COVERS", type + "TARGETED", type + "COMPLETIONS ALLOWED", type + "COMPLETIONS ALLOWED PCT PER " + type + "TARGETED", type + "PASS YARDS ALLOWED", type + "PASS TDS ALLOWED", type + "PICKS", type + "PICK RETURN YARDS", type + "PICK SIXES", type + "COVER TACKLES", type + "COVER FF", type + "COVER SAFETIES" ]
        indices_to_not_round = [9]
    elif stat_type in {"BLITZ", "BLITZER"}:
        add_to_headers =       ["Blitzes", "Tackles",       "Sacks", "Yds",        "Run stop",         "Yds",                   "FF",       "Return",         "TD",           "Safeties"]
        stats_to_show =        ["BLITZES", "BLITZ TACKLES", "SACKS", "SACK YARDS", "BLITZ RUN STUFFS", "BLITZ RUN STUFF YARDS", "BLITZ FF", "BLITZ FF YARDS", "BLITZ FF TDS", "BLITZ SAFETIES"]
        indices_to_not_round = []
    elif stat_type == "XP":
        add_to_headers =       ["Att",         "Made",    "%"]
        stats_to_show =        ["XP ATTEMPTS", "XP MADE", "XP MADE PCT PER XP ATTEMPTS"]
        indices_to_not_round = [8]
    elif stat_type == "FG":
        add_to_headers =       ["Att",         "Made",    "%",                           "Long",             "Avg"]
        stats_to_show =        ["FG ATTEMPTS", "FG MADE", "FG MADE PCT PER FG ATTEMPTS", "FG DISTANCE LONG", "FG DISTANCE AVG PER FG ATTEMPTS"]
        indices_to_not_round = [8]
    elif stat_type == "PUNT":
        add_to_headers =       ["Att",   "Yds",        "Avg",            "Tb",      "Pins"]
        stats_to_show =        ["PUNTS", "PUNT YARDS", "PUNT YARDS AVG PER PUNTS", "PUNT TB", "PUNT PINS"]
        indices_to_not_round = [8]
    elif stat_type == "KICK OFF":
        add_to_headers =       ["Att",               "TB",          "TB Avg",                                "Onside",               "Success",        "Avg"]
        stats_to_show =        ["KICK OFF ATTEMPTS", "KICK OFF TB", "KICK OFF TB PCT PER KICK OFF ATTEMPTS", "ONSIDE KICK ATTEMPTS", "ONSIDE KICK SUCCESS", "ONSIDE KICK SUCCESS PCT PER ONSIDE KICK ATTEMPTS"]
        indices_to_not_round = [8, 11]
    elif stat_type == "2pt":
        add_to_headers =       ["PASS ATT",          "SUCCESS",     "%",                                          "CARRIES",     "SUCCESS",      "%",                                    "TARGETS",     "SUCCESS",     "%"]
        stats_to_show =        ["2pt PASS ATTEMPTS", "2pt PASS SUCCESS", "2pt PASS SUCCESS PCT PER 2pt PASS ATTEMPTS", "2pt CARRIES", "2pt RUSH SUCCESS", "2pt RUSH SUCCESS PCT PER 2pt CARRIES", "2pt TARGETS", "2pt CATCH SUCCESS", "2pt CATCH SUCCESS PCT PER 2pt TARGETS"]
        indices_to_not_round = [8, 11, 14]
    elif "RETURN" in stat_type:
        type = stat_type[0:stat_type.index("RETURN")]
        add_to_headers =       ["Att",            "Yds",                 "Avg",                                             "Td",                "Fumbles",               "Tb"]
        stats_to_show =        [type + "RETURNS", type + "RETURN YARDS", type + "RETURN YARDS AVG PER " + type + "RETURNS", type + "RETURN TDS", type + "RETURN FUMBLES", type + "RETURN TB"]
        indices_to_not_round = [8]
    elif stat_type == "RECORD":
        add_to_headers =       ["Played W",    "Played L",      "Played T",    "Played G",     "PCT",                  "W",    "L",      "T",    "GAMES",           "PCT",                     "SNAPS PLAYED"]
        stats_to_show =        ["PLAYED WINS", "PLAYED LOSSES", "PLAYED TIES", "GAMES PLAYED", "GAMES PLAYED WIN PCT", "WINS", "LOSSES", "TIES", "GAMES ON ROSTER", "GAMES ON ROSTER WIN PCT", "SNAPS PLAYED"]
        indices_to_not_round = []
    elif stat_type == "AWARDS":
        add_to_headers =       ["MVP",  "PRO BOWLS", "OPOY",  "DPOY",  "OROY",  "DROY"]
        stats_to_show =        ["MVPS", "PRO BOWLS", "OPOYS", "DPOYS", "OROYS", "DROYS"]
        indices_to_not_round = []
    elif stat_type == "FANTASY":
        add_to_headers =       ["FPTS", "PPR"]
        stats_to_show =        ["FANTASY POINTS", "PPR FANTASY POINTS"]
        indices_to_not_round = [6,7]
    elif not stat_type in {"MISC", "OVERALL", "RATINGS1", "RATINGS2"}:
        print("error: unknown stat_type in make_career_table - " + str(stat_type))
        
    if not stat_type in {"MISC", "OVERALL", "RATINGS1", "RATINGS2"}:
        headers.extend(add_to_headers)
        for i in range(0, len(stats_to_show)):
            column_sizes.append(75)
        bottom_row = ["CAREER", player.name(), player.position, player.overall(use_overall), player.team, str(player.get_stat_rating("CAREER", stat_type, this_year)) + "don't round"]
        for stat in stats_to_show:
            bottom_row.append(player.career_stats.get_stat("CAREER", stat, this_year))
        for j in indices_to_not_round:
            bottom_row[j] = str(bottom_row[j]) + "don't round"
        i = 0
        for a_year in range(player.draft_position[2], this_year + 1):
            table_rows.append([])
            if is_player(player):
                ovr = player.overall(use_overall)
                if not player.career_stats.get_stat(scope, "OVERALL", a_year) == 0:
                    ovr = player.career_stats.get_stat(scope, "OVERALL", a_year)
                tm = player.team
                if not player.career_stats.get_stat(scope, "TEAM", a_year) == 0:
                    tm = player.career_stats.get_stat(scope, "TEAM", a_year)
                table_rows[i] = [a_year, player.name(), player.position,  ovr,                       tm,                  str(player.get_stat_rating(scope, stat_type, a_year)) + "don't round"]
            else:
                table_rows[i] = [a_year, player.name(), "TEAM",           player.get_team_overall(), player.abbreviation, str(player.get_stat_rating(scope, stat_type, a_year)) + "don't round"]
            for stat in stats_to_show:
                table_rows[i].append(player.career_stats.get_stat(scope, stat, a_year))
            for j in indices_to_not_round:
                table_rows[i][j] = str(table_rows[i][j]) + "don't round"
            i += 1    
    elif stat_type == "MISC":
        headers.remove("Rating")
        add_to_headers = ["Age", "Seasons", "Value", "SKIPS", "Round", "Pick", "Year", "Drafted by"]
        headers.extend(add_to_headers)
        column_sizes = [125, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75]
        i = 0
        for a_year in range(player.draft_position[2], this_year + 1):
            table_rows.append([])
            if is_player(player):
                ovr = player.overall(use_overall)
                if not player.career_stats.get_stat(scope, "OVERALL", a_year) == 0:
                    ovr = player.career_stats.get_stat(scope, "OVERALL", a_year)
                tm = player.team
                if not player.career_stats.get_stat(scope, "TEAM", a_year) == 0:
                    tm = player.career_stats.get_stat(scope, "TEAM", a_year)
                table_rows[i] = [a_year, player.name(), player.position, ovr, tm, player.age, player.years_played, str(player.get_value()) + "don't round", player.skip_years, player.draft_position[0], player.draft_position[1], player.draft_position[2], player.drafted_by]
            else:
                table_rows[i] = [a_year, player.name(), "TEAM", player.get_team_overall(), player.abbreviation, str(player.average_age()) + "don't round", len(player.season_records), 0, 0, 0, 0, 0, "NONE"]
            i += 1
    elif "OVERALL" in stat_type:
        headers.remove("Rating")
        add_to_headers = [ "OFF", "DEF", "SPECIAL", "QB", "RB", "WR", "TE", "OL", "DL", "LB", "DB", "K", "RT" ]
        headers.extend(add_to_headers)
        column_sizes = [ 125, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75 ]
        i = 0
        for a_year in range(player.draft_position[2], this_year + 1):
            table_rows.append([])
            if is_player(player):
                ovr = player.overall(use_overall)
                if not player.career_stats.get_stat(scope, "OVERALL", a_year) == 0:
                    ovr = player.career_stats.get_stat(scope, "OVERALL", a_year)
                tm = player.team
                if not player.career_stats.get_stat(scope, "TEAM", a_year) == 0:
                    tm = player.career_stats.get_stat(scope, "TEAM", a_year)
                table_rows[i] = [ a_year, player.name(), player.position, ovr, tm, 0, 0, 0, player.get_overall("QB", use_overall), player.get_overall("RB", use_overall), 
                                  player.get_overall("WR", use_overall), player.get_overall("TE", use_overall), player.get_overall("OL", use_overall), player.get_overall("DL", use_overall), player.get_overall("LB", use_overall), player.get_overall("DB", use_overall), player.get_overall("K", use_overall), player.get_overall("RT", use_overall) ]
            else:
                table_rows[i] = [ a_year, player.name(), "TEAM", player.get_team_overall(), player.abbreviation, player.offense, player.defense, player.special, player.qb, player.rb, player.wr, player.te, player.ol,
                                  player.dl, player.lb, player.db, player.k_ovr, player.rt_ovr ]
            i += 1
    elif "RATINGS1" in stat_type:
        headers.remove("Rating")
        add_to_headers = ["MVP", "VP", "ALL AROUND", "AWARDS", "THROW", "RUN", "CATCH", "BLOCK", "RB", "PB"]
        headers.extend(add_to_headers)
        column_sizes = [125, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75]
        rate_types = ["ALL", "AWARDS", "THROW", "RUN", "CATCH", "BLOCK", "RUN BLOCK", "PASS BLOCK"]
        i = 0
        for a_year in range(player.draft_position[2], this_year + 1):
            table_rows.append([])
            if is_player(player):
                ovr = player.overall(use_overall)
                if not player.career_stats.get_stat(scope, "OVERALL", a_year) == 0:
                    ovr = player.career_stats.get_stat(scope, "OVERALL", a_year)
                tm = player.team
                if not player.career_stats.get_stat(scope, "TEAM", a_year) == 0:
                    tm = player.career_stats.get_stat(scope, "TEAM", a_year)
                table_rows[i] = [a_year, player.name(), player.position, ovr, tm, str(player.get_mvp_points(scope, a_year, True)) + "don't round", str(player.get_mvp_points(scope, a_year, False)) + "don't round"]
            else:
                table_rows[i] = [a_year, player.name(), "TEAM", player.get_team_overall(), player.abbreviation, "NA", "NA"]
            for rate in rate_types:
                table_rows[i].append(str(player.get_stat_rating(scope, rate, a_year)) + "don't round")
            i += 1
    elif "RATINGS2" in stat_type:
        headers.remove("Rating")
        add_to_headers = ["MVP", "VP", "ALL AROUND", "COVER", "MAN", "ZONE", "BLITZ", "XP", "FG", "PUNT", "RETURN", "KICK RT", "PUNT RT"]
        headers.extend(add_to_headers)
        column_sizes = [125, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75]
        rate_types = ["ALL", "COVER", "MAN COVER", "ZONE COVER", "BLITZ", "XP", "FG", "PUNT", "RETURN", "KICK RETURN", "PUNT RETURN"]
        i = 0
        for a_year in range(player.draft_position[2], this_year + 1):
            table_rows.append([])
            if is_player(player):
                ovr = player.overall(use_overall)
                if not player.career_stats.get_stat(scope, "OVERALL", a_year) == 0:
                    ovr = player.career_stats.get_stat(scope, "OVERALL", a_year)
                tm = player.team
                if not player.career_stats.get_stat(scope, "TEAM", a_year) == 0:
                    tm = player.career_stats.get_stat(scope, "TEAM", a_year)
                table_rows[i] = [a_year, player.name(), player.position, ovr, tm, player.get_mvp_points(scope, a_year, True), player.get_mvp_points(scope, a_year, False)]
            else:
                table_rows[i] = [a_year, player.name(), "TEAM", player.get_team_overall(), player.abbreviation, "NA", "NA"]
            for rate in rate_types:
                table_rows[i].append(str(player.get_stat_rating(scope, rate, a_year)) + "don't round")
            i += 1
    player_list_sorted = []
    team_list_sorted = []
    for row in table_rows:
        if row[1] == "TEAM":
            team_list_sorted.append(row)
        else:
            player_list_sorted.append(row)
    if not (sort_index == "NONE") and sort_index >= 0:
        if len(player_list_sorted) > 0 and sort_index < len(player_list_sorted[0]):
            player_list_sorted.sort(key = lambda l: by_list_index(l, sort_index), reverse = not is_min_max)
        if len(team_list_sorted) > 0 and sort_index < len(team_list_sorted[0]):
            team_list_sorted.sort(key = lambda l: by_list_index(l, sort_index), reverse = not is_min_max)
    table_rows = []
    table_rows.extend(player_list_sorted)
    table_rows.extend(team_list_sorted)
    table_rows.append(bottom_row)
    numbering = []
    highlight = []
    for row in table_rows:
        if row[3] == user_teams[user_team_number].abbreviation and highlighting:
            highlight.append(True)
        else:
            highlight.append(False)
    draw_table_h(headers, column_sizes, row_height, table_rows, x, y, highlight, column_highlight, sort_index)
    for i in range(1, len(table_rows) + 1):
        numbering.append([i])
    draw_table_h(["#"], [25], row_height, numbering, x - 25, y, highlight, False, sort_index)
        
def make_stats_table(stat_type, scope, this_year, players_to_include, x, y, sort_index, is_min_max, max_len):
    make_stats_table_h(stat_type, scope, this_year, players_to_include, x, y, sort_index, is_min_max, max_len, False, False)
                        
def make_stats_table_h(stat_type, scope, this_year, players_to_include, x, y, sort_index, is_min_max, max_len, highlighting, column_highlight):
    global user_teams, user_team_number, use_overall
    headers = ["Name", "Pos", "Ovr", "Team", "Rating"]
    column_sizes = [125, 75, 75, 75, 75]
    row_height = 20
    table_rows = []
    add_to_headers = []
    stats_to_show = []
    indices_to_not_round = []
    
    if stat_type in {"RUN", "RUSH"}:
        add_to_headers =       ["Att",     "Yds",        "Avg",            "TD",       "Long",            "Fum"]
        stats_to_show =        ["CARRIES", "RUSH YARDS", "RUSH YARDS AVG PER CARRIES", "RUSH TDS", "RUSH YARDS LONG", "RUSH FUMBLES"]
        indices_to_not_round = [7]
    elif stat_type in {"RECEIVE", "CATCH"}:
        add_to_headers =       ["Routes",     "Targets", "Catches", "Yds",             "Avg",                 "TD",            "Long",                 "Fum",              "Drops", "YAC"]
        stats_to_show =        ["ROUTES RUN", "TARGETS", "CATCHES", "RECEIVING YARDS", "RECEIVING YARDS AVG PER CATCHES", "RECEIVING TDS", "RECEIVING YARDS LONG", "RECEIVER FUMBLES", "DROPS", "YAC"]
        indices_to_not_round = [9]
    elif stat_type in {"THROW", "PASS"}:
        add_to_headers =       ["Att",           "Complete",         "%",                                  "Yds",        "Avg",            "TD",       "INT",       "Long",            "Fum",           "Sacked",       "Yds"]
        stats_to_show =        ["PASS ATTEMPTS", "PASS COMPLETIONS", "PASS COMPLETIONS PCT PER PASS ATTEMPTS", "PASS YARDS", "PASS YARDS AVG PER PASS COMPLETIONS", "PASS TDS", "PASS INTS", "PASS YARDS LONG", "POCKET FUMBLES", "TIMES SACKED", "SACKED YARDS"]
        indices_to_not_round = [7, 9]
    elif "BLOCK" in stat_type:
        type = stat_type[0:stat_type.index("BLOCK")]
        #if not type == "":
            #type += " "
        add_to_headers =       ["Att",                   "BLK",                "%"]
        stats_to_show =        [type + "BLOCK ATTEMPTS", type + "BLOCKS MADE", type + "BLOCKS MADE PCT PER " + type + "BLOCK ATTEMPTS"]
        indices_to_not_round = [7]
    elif "COVER" in stat_type:
        type = stat_type[0:stat_type.index("COVER")]
        #if not type == "":
            #type += " "
        add_to_headers =       ["Covers",        "Targets",         "Complete",                   "%",                                                      "Yds",                        "TD",                      "INT",          "Return",                   "Pick 6s",           "Tackles",               "FF",              "Safeties"]
        stats_to_show =        [type + "COVERS", type + "TARGETED", type + "COMPLETIONS ALLOWED", type + "COMPLETIONS ALLOWED PCT PER " + type + "TARGETED", type + "PASS YARDS ALLOWED", type + "PASS TDS ALLOWED", type + "PICKS", type + "PICK RETURN YARDS", type + "PICK SIXES", type + "COVER TACKLES", type + "COVER FF", type + "COVER SAFETIES" ]
        indices_to_not_round = [8]
    elif stat_type in {"BLITZ", "BLITZER"}:
        add_to_headers =       ["Blitzes", "Tackles",       "Sacks", "Yds",        "Run stop",         "Yds",                   "FF",       "Return",         "TD",           "Safeties"]
        stats_to_show =        ["BLITZES", "BLITZ TACKLES", "SACKS", "SACK YARDS", "BLITZ RUN STUFFS", "BLITZ RUN STUFF YARDS", "BLITZ FF", "BLITZ FF YARDS", "BLITZ FF TDS", "BLITZ SAFETIES"]
        indices_to_not_round = []
    elif stat_type == "XP":
        add_to_headers =       ["Att",         "Made",    "%"]
        stats_to_show =        ["XP ATTEMPTS", "XP MADE", "XP MADE PCT PER XP ATTEMPTS"]
        indices_to_not_round = [7]
    elif stat_type == "FG":
        add_to_headers =       ["Att",         "Made",    "%",                           "Long",             "Avg"]
        stats_to_show =        ["FG ATTEMPTS", "FG MADE", "FG MADE PCT PER FG ATTEMPTS", "FG DISTANCE LONG", "FG DISTANCE AVG PER FG ATTEMPTS"]
        indices_to_not_round = [7]
    elif stat_type == "PUNT":
        add_to_headers =       ["Att",   "Yds",        "Avg",                      "Tb",      "Pins"]
        stats_to_show =        ["PUNTS", "PUNT YARDS", "PUNT YARDS AVG PER PUNTS", "PUNT TB", "PUNT PINS"]
        indices_to_not_round = [7]
    elif stat_type == "KICK OFF":
        add_to_headers =       ["Att",               "TB",          "TB Avg",                                "Onside",               "Success",        "Avg"]
        stats_to_show =        ["KICK OFF ATTEMPTS", "KICK OFF TB", "KICK OFF TB PCT PER KICK OFF ATTEMPTS", "ONSIDE KICK ATTEMPTS", "ONSIDE KICK SUCCESS", "ONSIDE KICK SUCCESS PCT PER ONSIDE KICK ATTEMPTS"]
        indices_to_not_round = [7, 10]
    elif "RETURN" in stat_type:
        type = stat_type[0:stat_type.index("RETURN")]
        #if not type == "":
            #type += " "
        add_to_headers =       ["Att",            "Yds",                 "Avg",                                             "Td",                "Fumbles",               "Tb"]
        stats_to_show =        [type + "RETURNS", type + "RETURN YARDS", type + "RETURN YARDS AVG PER " + type + "RETURNS", type + "RETURN TDS", type + "RETURN FUMBLES", type + "RETURN TB"]
        indices_to_not_round = [7]
    elif stat_type == "2pt":
        add_to_headers =       ["PASS ATT",          "SUCCESS",     "%",                                          "CARRIES",     "SUCCESS",      "%",                                    "TARGETS",     "SUCCESS",     "%"]
        stats_to_show =        ["2pt PASS ATTEMPTS", "2pt PASS SUCCESS", "2pt PASS SUCCESS PCT PER 2pt PASS ATTEMPTS", "2pt CARRIES", "2pt RUSH SUCCESS", "2pt RUSH SUCCESS PCT PER 2pt CARRIES", "2pt TARGETS", "2pt CATCH SUCCESS", "2pt CATCH SUCCESS PCT PER 2pt TARGETS"]
        indices_to_not_round = [7, 10, 13]
    elif stat_type == "RECORD":
        add_to_headers =       ["Played W",    "Played L",      "Played T",    "Played G",     "PCT",                  "W",    "L",      "T",    "GAMES",           "PCT",                     "SNAPS PLAYED"]
        stats_to_show =        ["PLAYED WINS", "PLAYED LOSSES", "PLAYED TIES", "GAMES PLAYED", "GAMES PLAYED WIN PCT", "WINS", "LOSSES", "TIES", "GAMES ON ROSTER", "GAMES ON ROSTER WIN PCT", "SNAPS PLAYED"]
        indices_to_not_round = []
    elif stat_type == "AWARDS":
        add_to_headers =       ["MVP",  "PRO BOWLS", "OPOY",  "DPOY",  "OROY",  "DROY"]
        stats_to_show =        ["MVPS", "PRO BOWLS", "OPOYS", "DPOYS", "OROYS", "DROYS"]
        indices_to_not_round = []
    elif stat_type == "FANTASY":
        add_to_headers =       ["FPTS", "PPR"]
        stats_to_show =        ["FANTASY POINTS", "PPR FANTASY POINTS"]
        indices_to_not_round = [5,6]
    elif not stat_type in {"MISC", "OVERALL", "RATINGS1", "RATINGS2"}:
        print("error: unknown stat_type in make_stats_table - " + str(stat_type))
        
    if not stat_type in {"MISC", "OVERALL", "RATINGS1", "RATINGS2"}:
        headers.extend(add_to_headers)
        for i in range(0, len(stats_to_show)):
            column_sizes.append(75)
        i = 0
        for player in players_to_include:
            table_rows.append([])
            if is_player(player):
                ovr = player.overall(use_overall)
                if not player.career_stats.get_stat(scope, "OVERALL", this_year) == 0:
                    ovr = player.career_stats.get_stat(scope, "OVERALL", this_year)
                tm = player.team
                if not player.career_stats.get_stat(scope, "TEAM", this_year) == 0:
                    tm = player.career_stats.get_stat(scope, "TEAM", this_year)
                table_rows[i] = [player.name(), player.position, ovr,                       tm,                  str(player.get_stat_rating(scope, stat_type, this_year)) + "don't round"]
            else:
                table_rows[i] = [player.name(), "TEAM",          player.get_team_overall(), player.abbreviation, str(player.get_stat_rating(scope, stat_type, this_year)) + "don't round"]
            for stat in stats_to_show:
                table_rows[i].append(player.career_stats.get_stat(scope, stat, this_year))
            for j in indices_to_not_round:
                table_rows[i][j] = str(table_rows[i][j]) + "don't round"
            i += 1    
    elif stat_type == "MISC":
        headers.remove("Rating")
        add_to_headers = ["Age", "Seasons", "Value", "SKIPS", "Round", "Pick", "Year", "Drafted by", "Tradeable", "Salary $", "Earned $", "Loyalty"]
        headers.extend(add_to_headers)
        column_sizes = [125, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75]
        i = 0
        for player in players_to_include:
            table_rows.append([])
            if is_player(player):
                ovr = player.overall(use_overall)
                if not player.career_stats.get_stat(scope, "OVERALL", this_year) == 0:
                    ovr = player.career_stats.get_stat(scope, "OVERALL", this_year)
                tm = player.team
                if not player.career_stats.get_stat(scope, "TEAM", this_year) == 0:
                    tm = player.career_stats.get_stat(scope, "TEAM", this_year)
                table_rows[i] = [player.name(), player.position, ovr, tm, player.age, player.years_played, str(player.get_value()) + "don't round", player.skip_years, player.draft_position[0], player.draft_position[1], player.draft_position[2], player.drafted_by, player.is_tradeable(), str(round(player.contract_amount/1000000.0, 2)) + " don't round", str(round(player.career_stats.get_stat(scope, "SALARY", this_year)/1000000.0, 2)) + "don't round", player.loyalty]
            else: 
                table_rows[i] = [player.name(), "TEAM", player.get_team_overall(), player.abbreviation, str(player.average_age()) + "don't round", len(player.season_records), player.get_team_value(), 0, 0, 0, 0, "NONE", "False", 0, 0, 0]
            i += 1
    elif "OVERALL" in stat_type:
        headers.remove("Rating")
        add_to_headers = [ "OFF", "DEF", "SPECIAL", "QB", "RB", "WR", "TE", "OL", "DL", "LB", "DB", "K", "RT" ]
        headers.extend(add_to_headers)
        column_sizes = [ 125, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75 ]
        i = 0
        for player in players_to_include:
            table_rows.append([])
            if is_player(player):
                ovr = player.overall(use_overall)
                if not player.career_stats.get_stat(scope, "OVERALL", this_year) == 0:
                    ovr = player.career_stats.get_stat(scope, "OVERALL", this_year)
                tm = player.team
                if not player.career_stats.get_stat(scope, "TEAM", this_year) == 0:
                    tm = player.career_stats.get_stat(scope, "TEAM", this_year)
                table_rows[i] = [ player.name(), player.position, ovr, tm, 0, 0, 0, player.get_overall("QB", use_overall), player.get_overall("RB", use_overall), 
                                  player.get_overall("WR", use_overall), player.get_overall("TE", use_overall), player.get_overall("OL", use_overall), player.get_overall("DL", use_overall), player.get_overall("LB", use_overall), player.get_overall("DB", use_overall), player.get_overall("K", use_overall), player.get_overall("RT", use_overall) ]
            else:
                table_rows[i] = [ player.name(), "TEAM", player.get_team_overall(), player.abbreviation, player.offense, player.defense, player.special, player.qb, player.rb, player.wr, player.te, player.ol,
                                  player.dl, player.lb, player.db, player.k_ovr, player.rt_ovr ]
            i += 1
    elif "RATINGS1" in stat_type:
        headers.remove("Rating")
        add_to_headers = ["MVP", "VP", "ALL AROUND", "AWARDS", "THROW", "RUN", "CATCH", "BLOCK", "RB", "PB"]
        headers.extend(add_to_headers)
        column_sizes = [125, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75]
        rate_types = ["ALL", "AWARDS", "THROW", "RUN", "CATCH", "BLOCK", "RUN BLOCK", "PASS BLOCK"]
        i = 0
        for player in players_to_include:
            table_rows.append([])
            if is_player(player):
                ovr = player.overall(use_overall)
                if not player.career_stats.get_stat(scope, "OVERALL", this_year) == 0:
                    ovr = player.career_stats.get_stat(scope, "OVERALL", this_year)
                tm = player.team
                if not player.career_stats.get_stat(scope, "TEAM", this_year) == 0:
                    tm = player.career_stats.get_stat(scope, "TEAM", this_year)
                table_rows[i] = [player.name(), player.position, ovr, tm, str(player.get_mvp_points(scope, this_year, True)) + "don't round", str(player.get_mvp_points(scope, this_year, False)) + "don't round"]
            else:
                table_rows[i] = [player.name(), "TEAM", player.get_team_overall(), player.abbreviation, "NA", "NA"]
            for rate in rate_types:
                table_rows[i].append(str(player.get_stat_rating(scope, rate, this_year)) + "don't round")
            i += 1
    elif "RATINGS2" in stat_type:
        headers.remove("Rating")
        add_to_headers = ["MVP", "VP", "ALL AROUND", "COVER", "MAN", "ZONE", "BLITZ", "XP", "FG", "PUNT", "RETURN", "KICK RT", "PUNT RT"]
        headers.extend(add_to_headers)
        column_sizes = [125, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75]
        rate_types = ["ALL", "COVER", "MAN COVER", "ZONE COVER", "BLITZ", "XP", "FG", "PUNT", "RETURN", "KICK RETURN", "PUNT RETURN"]
        i = 0
        for player in players_to_include:
            table_rows.append([])
            if is_player(player):
                ovr = player.overall(use_overall)
                if not player.career_stats.get_stat(scope, "OVERALL", this_year) == 0:
                    ovr = player.career_stats.get_stat(scope, "OVERALL", this_year)
                tm = player.team
                if not player.career_stats.get_stat(scope, "TEAM", this_year) == 0:
                    tm = player.career_stats.get_stat(scope, "TEAM", this_year)
                table_rows[i] = [player.name(), player.position, ovr, tm, player.get_mvp_points(scope, this_year, True), player.get_mvp_points(scope, this_year, False)]
            else:
                table_rows[i] = [player.name(), "TEAM", player.get_team_overall(), player.abbreviation, "NA", "NA"]
            for rate in rate_types:
                table_rows[i].append(str(player.get_stat_rating(scope, rate, this_year)) + "don't round")
            i += 1
    player_list_sorted = []
    team_list_sorted = []
    for row in table_rows:
        if row[1] == "TEAM":
            team_list_sorted.append(row)
        else:
            player_list_sorted.append(row)
    if not (sort_index == "NONE") and sort_index >= 0:
        if len(player_list_sorted) > 0 and sort_index < len(player_list_sorted[0]):
            player_list_sorted.sort(key = lambda l: by_list_index(l, sort_index), reverse = not is_min_max)
        if len(team_list_sorted) > 0 and sort_index < len(team_list_sorted[0]):
            team_list_sorted.sort(key = lambda l: by_list_index(l, sort_index), reverse = not is_min_max)
    table_rows = []
    table_rows.extend(player_list_sorted)
    table_rows.extend(team_list_sorted)
    numbering = []
    highlight = []
    for row in table_rows[0:max_len]:
        if row[3] == user_teams[user_team_number].abbreviation and highlighting:
            highlight.append(True)
        else:
            highlight.append(False)
    if max_len > 0 and max_len < len(table_rows):
        draw_table_h(headers, column_sizes, row_height, table_rows[0:max_len], x, y, highlight, column_highlight, sort_index)
        for i in range(1, max_len + 1):
            numbering.append([i])
        draw_table_h(["#"], [25], row_height, numbering, x - 25, y, highlight, False, sort_index)
    else:
        draw_table_h(headers, column_sizes, row_height, table_rows, x, y, highlight, column_highlight, sort_index)
        for i in range(1, len(table_rows) + 1):
            numbering.append([i])
        draw_table_h(["#"], [25], row_height, numbering, x - 25, y, highlight, False, sort_index)
    
def is_number(num):
    try:
        float(num)
        return True
    except:
        return False
    
def is_player(test):
    try:
        test.injury_chance
        return True
    except:
        return False
    
def is_team(test):
    try:
        test.team_name
        return True
    except:
        return False
    
def calculate_passer_rating(att, comp, yds, td, picks):
    if att == 0:
        return 0
    a = (float(comp)/att - 0.3) * 5
    b = (float(yds)/att - 3) * 0.25
    c = (float(td)/att) * 20
    d = 2.375 - ((float(picks)/att) * 25)
    if a < 0:
        a = 0
    if a > 2.375:
        a = 2.375
    if b < 0:
        b = 0
    if b > 2.375:
        b = 2.375
    if c < 0:
        c = 0
    if c > 2.375:
        c = 2.375
    if d < 0:
        d = 0
    if d > 2.375:
        d = 2.375
    return (a + b + c + d)/6 * 100


################################################################################SEASON CLASS###########################################################################################
################################################################################SEASON CLASS###########################################################################################
################################################################################SEASON CLASS###########################################################################################
################################################################################SEASON CLASS###########################################################################################

class Season(object):
    
    def __init__(self, teams, afc_e, afc_n, afc_s, afc_w, nfc_e, nfc_n, nfc_s, nfc_w, afc_conf_ranked, nfc_conf_ranked, conf_ranked, fa, y, mega_draft):
        self.teams = teams
        self.free_agents = fa
        self.is_playoffs = False
        self.afc_east = afc_e
        self.afc_north = afc_n
        self.afc_south = afc_s
        self.afc_west = afc_w
        self.nfc_east = nfc_e
        self.nfc_north = nfc_n
        self.nfc_south = nfc_s
        self.nfc_west = nfc_w
        self.conf_ranked = conf_ranked
        self.afc_conf_ranked = afc_conf_ranked
        self.nfc_conf_ranked = nfc_conf_ranked
        self.schedule = self.make_schedule()
        self.current_week = -4
        self.afc_playoffs = []
        self.nfc_playoffs = []
        self.ready_to_sim = True
        self.done = False
        self.trade_center = TradeCenter()
        self.trade_deadline = 8
        self.this_year = y
        self.mega_draft = mega_draft
        self.afc_all_stars = Team("AFC", "ALL STARS", "AFC")
        self.nfc_all_stars = Team("NFC", "ALL STARS", "NFC")
        self.buttons = [ Button(1000, 700, 100, 100, "AFC", self.afc_all_stars, "PRO BOWL"), Button(1150, 700, 100, 100, "NFC", self.nfc_all_stars, "PRO BOWL") ]
        self.buttons[0].hide()
        self.buttons[1].hide()
        #self.games = 17
        self.resign_week = -4
        self.draft_week = -3
        self.draft_end_week = -2
        self.cut_week = -1
        self.fa_cut_week = 1
        self.wildcard_week = 18
        self.semis_week = 19
        self.conf_finals_week = 20
        self.pro_bowl_week = 21
        self.sb_week = 22
        self.season_over_week = 23
        self.num_games = 17
        
    def draw_season(self):
        for button in self.buttons:
            button.draw_button()
            
    def clicked(self, mouse_x, mouse_y):
        for button in self.buttons:
            if button.clicked(mouse_x, mouse_y):
                if button.category == "PRO BOWL":
                    change_screen(button.do)
                    
    def search_for_top_awards(self, phase, scope, award, stat, att, num, years):
        global ls
        top = ls.get_top_rated(phase, scope, award, stat, att, num, years)
        num_left = num - len(top)
        while len(top) < num and att > 0:
            att -= 5
            top.extend(ls.get_top_rated(phase, scope, award, stat, att, num_left, years))
            num_left = num - len(top)
        return top[0:min(len(top), num)]
    
    def fill_pro_bowl_teams(self):
        global ls
        #          get_top_rated(pos,        scope, stat_type, conf, min_att, num_to_return, years_in_nfl)
        mvp =   self.search_for_top_awards("ANY",     "SEASON", "MVP",  "ANY", 600, 1, "ANY")[0]
        opoys = self.search_for_top_awards("OFFENSE", "SEASON", "OPOY", "ANY", 600, 2, "ANY")
        dpoys = self.search_for_top_awards("DEFENSE", "SEASON", "DPOY", "ANY", 600, 2, "ANY")
        oroys = self.search_for_top_awards("OFFENSE", "SEASON", "OROY", "ANY", 400, 3, 0)
        droys = self.search_for_top_awards("DEFENSE", "SEASON", "DROY", "ANY", 400, 3, 0)
        
        opoy = opoys[0]
        dpoy = dpoys[0]
        oroy = oroys[0]
        droy = droys[0]
        
        if len(opoys) < 2:
            print("not enough opoys " + str(self.this_year))
        if len(dpoys) < 2:
            print("not enough dpoys " + str(self.this_year))
        if len(oroys) < 3:
            print("not enough oroys " + str(self.this_year))
        if len(droys) < 3:
            print("not enough droys " + str(self.this_year))
        
        for player in opoys:
            if not player == mvp:
                opoy = player
                break
            
        for player in dpoys:
            if not player == mvp:
                dpoy = player
                break
            
        for player in oroys:
            if not player in {mvp, opoy}:
                oroy = player
                break
            
        for player in droys:
            if not player in {mvp, dpoy}:
                droy = player
                break
        
        for team in self.teams:
            if team.abbreviation == mvp.team:
                team.add_stats(mvp, "MVPS",   1, "AWARDS", self.this_year)
            if team.abbreviation == opoy.team:
                team.add_stats(opoy, "OPOYS", 1, "AWARDS", self.this_year)
            if team.abbreviation == dpoy.team:
                team.add_stats(dpoy, "DPOYS", 1, "AWARDS", self.this_year)
            if team.abbreviation == oroy.team:
                team.add_stats(oroy, "OROYS", 1, "AWARDS", self.this_year)
            if team.abbreviation == droy.team:
                team.add_stats(droy, "DROYS", 1, "AWARDS", self.this_year)
        
        #                pos    scope     conf  att num  exp
        self.afc_all_stars.clear_team()
        self.nfc_all_stars.clear_team()
        afc_lineup = []
        #                    get_top_rated(pos,   scope, stat_type, conf, min_att, num_to_return, years_in_nfl)
        afc_lineup.extend(ls.get_top_rated("QB", "SEASON", "ALL",     "AFC", 200, 3, "ANY"))
        afc_lineup.extend(ls.get_top_rated("RB", "SEASON", "ALL",     "AFC", 90, 4, "ANY"))
        afc_lineup.extend(ls.get_top_rated("WR", "SEASON", "RECEIVE", "AFC", 60, 5, "ANY"))
        afc_lineup.extend(ls.get_top_rated("TE", "SEASON", "RECEIVE",     "AFC", 40, 4, "ANY"))
        #afc_lineup.extend(ls.get_top_rated("TE", "SEASON", "BLOCK",   "AFC", 400, 1, "ANY"))
        afc_lineup.extend(ls.get_top_rated("OL", "SEASON", "BLOCK",   "AFC", 700, 7, "ANY"))
        afc_lineup.extend(ls.get_top_rated("DL", "SEASON", "BLITZER", "AFC", 700, 8, "ANY"))
        afc_lineup.extend(ls.get_top_rated("LB", "SEASON", "ALL",     "AFC", 700, 7, "ANY"))
        afc_lineup.extend(ls.get_top_rated("DB", "SEASON", "COVER",   "AFC", 700, 8, "ANY"))
        afc_lineup.extend(ls.get_top_rated("K",  "SEASON", "ALL",     "AFC", 15, 2, "ANY"))
        #afc_lineup.extend(ls.get_top_rated("K",  "SEASON", "PUNT",    "AFC", 50, 1, "ANY"))
        afc_lineup.extend(ls.get_top_rated("RT", "SEASON", "RETURN",  "AFC", 50, 2, "ANY"))
        self.afc_all_stars.bench.extend(afc_lineup)
        self.afc_all_stars.best_lineup()
        self.afc_all_stars.Players.extend(afc_lineup)
        
        for player in afc_lineup:
            for team in self.teams:
                if team.abbreviation == player.team:
                    team.add_stats(player, "PRO BOWLS", 1, "AWARDS", self.this_year)
        
        nfc_lineup = []
        nfc_lineup.extend(ls.get_top_rated("QB", "SEASON", "ALL",     "NFC", 200, 3, "ANY"))
        nfc_lineup.extend(ls.get_top_rated("RB", "SEASON", "ALL",     "NFC", 90, 4, "ANY"))
        nfc_lineup.extend(ls.get_top_rated("WR", "SEASON", "RECEIVE", "NFC", 60, 5, "ANY"))
        nfc_lineup.extend(ls.get_top_rated("TE", "SEASON", "RECEIVE",     "NFC", 40, 4, "ANY"))
        #nfc_lineup.extend(ls.get_top_rated("TE", "SEASON", "BLOCK",   "NFC", 400, 1, "ANY"))
        nfc_lineup.extend(ls.get_top_rated("OL", "SEASON", "BLOCK",   "NFC", 700, 7, "ANY"))
        nfc_lineup.extend(ls.get_top_rated("DL", "SEASON", "BLITZER", "NFC", 700, 8, "ANY"))
        nfc_lineup.extend(ls.get_top_rated("LB", "SEASON", "ALL",     "NFC", 700, 7, "ANY"))
        nfc_lineup.extend(ls.get_top_rated("DB", "SEASON", "COVER",   "NFC", 700, 8, "ANY"))
        nfc_lineup.extend(ls.get_top_rated("K",  "SEASON", "ALL",     "NFC", 15, 2, "ANY"))
        #nfc_lineup.extend(ls.get_top_rated("K",  "SEASON", "PUNT",    "NFC", 50, 1, "ANY"))
        nfc_lineup.extend(ls.get_top_rated("RT", "SEASON", "RETURN",  "NFC", 50, 2, "ANY"))
        self.nfc_all_stars.bench.extend(nfc_lineup)
        self.nfc_all_stars.best_lineup()
        self.nfc_all_stars.Players.extend(nfc_lineup)
        
        for player in nfc_lineup:
            for team in self.teams:
                if team.abbreviation == player.team:
                    team.add_stats(player, "PRO BOWLS", 1, "AWARDS", self.this_year)
            
        self.nfc_all_stars.reset_game_stats()
        self.afc_all_stars.reset_game_stats()
        self.nfc_all_stars.best_lineup()
        self.nfc_all_stars.best_lineup()
        self.afc_all_stars.best_lineup()
        self.afc_all_stars.best_lineup()
        self.nfc_all_stars.is_all_star_team = True
        self.afc_all_stars.is_all_star_team = True
        self.buttons[0].show()
        self.buttons[1].show()

        
    def draft_pick_value(self, pick):
        pick_num = 0
        if is_number(pick[1]):
            pick_num = (pick[0] - 1) * len(self.teams) + pick[1] - 1
        else:
            index = 0
            for team in self.teams:
                index += 1
                if team.abbreviation == pick[1]:
                    break;
            pick_num = (pick[0] - 1) * len(self.teams) + index - 1
        total_picks = 7.0 * len(self.teams)
        if self.mega_draft:
            total_picks = 53 * len(self.teams) + 0.0
        offset = 0.98**pick_num
        if self.mega_draft and self.current_week < -1:
            offset = 0.995**pick_num
        best_val = 15000
        if self.mega_draft and self.current_week < -1:
            best_val = 50000
        year_diff = 0.95**(pick[2] - self.this_year)
        return best_val*offset*year_diff
        
    def make_schedule(self):
        sched = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        a = 0
        n = 0
        if self.conf_ranked[0] == "NFC":
            a = self.nfc_conf_ranked
            n = self.afc_conf_ranked
        else:
            a = self.afc_conf_ranked
            n = self.nfc_conf_ranked
        sched[0] =  [ [ n[2][0], n[2][3] ], [ a[2][1], a[1][2] ], [ a[1][0], a[0][3] ], [ n[1][2], n[2][1] ], [ a[0][1], a[0][2] ], [ n[0][3], n[0][2] ], [ n[3][2], n[1][3] ], [ a[3][0], a[2][3] ], [ a[2][2], a[3][1] ], [ a[1][3], n[3][1] ], [ n[0][1], n[0][0] ], [ n[2][2], n[3][3] ], [ n[3][0], n[1][1] ], [ a[1][1], a[0][0] ], [ a[2][0], n[1][0] ], [ a[3][2], a[3][3] ] ]
        sched[1] =  [ [ n[1][1], n[1][3] ], [ n[3][0], a[1][3] ], [ a[3][1], n[2][2] ], [ n[2][1], n[2][0] ], [ a[2][2], a[2][1] ], [ a[0][0], a[0][3] ], [ a[0][1], n[0][1] ], [ n[3][1], a[1][1] ], [ n[0][0], n[0][3] ], [ n[3][3], a[1][0] ], [ a[2][3], a[2][0] ], [ a[3][0], a[3][3] ], [ n[2][3], a[3][2] ], [ n[1][0], n[3][2] ], [ n[0][2], n[1][2] ], [ a[1][2], a[0][2] ] ]
        sched[2] =  [ [ a[2][1], a[2][3] ], [ a[1][3], a[0][1] ], [ a[0][3], n[0][0] ], [ a[3][2], n[2][0] ], [ n[1][2], a[2][2] ], [ a[1][0], a[3][0] ], [ a[3][3], n[2][1] ], [ a[0][2], a[0][0] ], [ n[2][2], n[0][2] ], [ n[1][3], n[3][3] ], [ n[0][1], n[1][1] ], [ a[2][0], a[3][1] ], [ a[1][1], n[3][0] ], [ n[1][0], n[3][1] ], [ n[3][2], a[1][2] ], [ n[2][3], n[0][3] ] ]
        sched[3] =  [ [ a[1][0], n[0][0] ], [ a[1][1], n[0][1] ], [ a[1][2], n[0][2] ], [ a[1][3], n[0][3] ], [ a[0][0], n[1][0] ], [ a[0][1], n[1][1] ], [ a[0][2], n[1][2] ], [ a[0][3], n[1][3] ], [ a[2][0], n[2][0] ], [ a[2][1], n[2][1] ], [ a[2][2], n[2][2] ], [ a[2][3], n[2][3] ], [ a[3][0], n[3][0] ], [ a[3][1], n[3][1] ], [ a[3][2], n[3][2] ], [ a[3][3], n[3][3] ] ]
        sched[4] =  [ [ n[0][2], n[2][0] ], [ a[2][1], n[1][2] ], [ a[0][0], a[0][1] ], [ a[3][0], n[2][2] ], [ a[3][3], a[2][2] ], [ a[3][1], a[0][3] ], [ n[0][3], n[0][1] ], [ a[1][2], a[1][0] ], [ n[1][3], a[2][0] ], [ n[1][1], n[3][2] ], [ n[3][1], n[3][3] ], [ n[2][1], n[2][3] ], [ a[2][3], a[3][2] ], [ n[0][0], n[1][0] ], [ a[1][3], a[1][1] ] ]
        sched[5] =  [ [ n[3][2], n[3][1] ], [ n[3][3], a[1][3] ], [ a[0][1], a[2][1] ], [ n[2][3], a[3][3] ], [ n[1][1], n[1][0] ], [ n[2][1], n[0][1] ], [ a[0][2], n[0][2] ], [ a[1][0], a[1][1] ], [ a[0][0], n[0][3] ], [ a[2][3], n[1][3] ], [ n[1][2], a[2][0] ], [ a[3][2], a[3][1] ], [ n[2][0], n[0][0] ], [ a[2][2], a[3][0] ], [ a[1][2], n[3][0] ] ]
        sched[6] =  [ [ n[0][1], a[0][0] ], [ n[1][3], n[1][1] ], [ n[3][1], a[1][2] ], [ a[2][0], a[3][0] ], [ n[0][3], a[0][3] ], [ n[0][2], n[2][1] ], [ n[1][0], a[2][3] ], [ a[1][3], a[1][0] ], [ n[3][0], n[3][2] ], [ n[1][2], n[3][3] ], [ a[2][1], a[3][2] ], [ n[0][0], a[0][2] ], [ a[1][1], a[3][1] ], [ n[2][2], n[2][0] ] ]
        sched[7] =  [ [ a[3][0], a[3][2] ], [ n[3][2], n[1][2] ], [ a[0][3], a[0][1] ], [ a[2][3], a[1][3] ], [ n[2][1], n[2][2] ], [ a[3][3], n[2][0] ], [ a[2][0], a[2][2] ], [ n[3][3], n[0][1] ], [ n[3][0], n[0][3] ], [ a[3][1], a[2][1] ], [ n[1][0], n[2][3] ], [ a[1][0], n[3][1] ], [ n[0][2], n[0][0] ], [ a[0][0], a[0][2] ] ]
        sched[8] =  [ [ n[0][3], n[2][1] ], [ n[3][1], n[1][2] ], [ n[0][2], a[0][1] ], [ a[3][1], n[2][3] ], [ n[0][1], n[2][2] ], [ n[1][1], a[2][1] ], [ a[3][2], a[2][2] ], [ a[1][3], n[3][2] ], [ n[3][3], n[1][0] ], [ a[0][2], a[2][3] ], [ n[1][3], n[3][0] ], [ a[1][2], a[0][0] ], [ a[3][3], a[2][0] ], [ n[2][0], a[3][0] ], [ a[0][3], a[1][1] ] ]
        sched[9] =  [ [ n[3][0], n[3][3] ], [ a[2][0], a[2][3] ], [ n[0][3], a[0][1] ], [ n[2][1], a[3][0] ], [ a[0][2], a[0][3] ], [ n[2][3], n[0][2] ], [ a[2][2], a[1][1] ], [ a[2][1], n[1][3] ], [ n[2][2], a[3][3] ], [ n[1][1], n[3][1] ], [ a[1][2], a[3][2] ], [ n[2][0], a[3][1] ], [ a[0][0], a[1][0] ], [ n[0][0], n[0][1] ] ]
        sched[10] = [ [ a[3][1], a[3][3] ], [ n[2][2], n[2][3] ], [ a[1][0], a[1][3] ], [ a[0][1], a[1][2] ], [ a[3][0], a[2][1] ], [ n[1][2], n[1][0] ], [ n[0][1], a[0][2] ], [ n[3][3], n[1][1] ], [ a[0][3], a[2][2] ], [ n[1][3], n[2][0] ], [ n[3][2], a[1][1] ], [ n[2][1], n[0][0] ], [ n[3][1], n[3][0] ] ]
        sched[11] = [ [ a[1][1], a[1][2] ], [ n[0][0], n[2][2] ], [ a[2][3], a[2][2] ], [ a[0][1], a[0][3] ], [ a[3][2], n[2][1] ], [ n[1][0], n[1][1] ], [ n[1][2], n[1][3] ], [ a[2][0], a[1][0] ], [ n[3][3], n[3][0] ], [ a[1][3], a[3][3] ], [ a[0][0], n[0][2] ], [ n[2][3], n[3][2] ], [ a[3][0], a[3][1] ], [ a[0][2], n[0][3] ] ]
        sched[12] = [ [ a[2][2], a[2][0] ], [ n[1][1], n[1][2] ], [ a[3][2], a[0][1] ], [ n[0][1], n[2][3] ], [ a[1][1], a[1][3] ], [ a[0][3], a[1][2] ], [ n[1][3], n[1][0] ], [ a[3][3], a[0][2] ], [ n[3][1], n[0][2] ], [ n[2][2], n[0][3] ], [ a[2][3], a[2][1] ], [ n[0][0], a[0][0] ], [ n[2][0], n[3][0] ], [ a[1][0], n[3][2] ] ]
        sched[13] = [ [ n[2][3], n[2][2] ], [ a[0][1], n[0][0] ], [ n[1][0], n[1][2] ], [ a[0][2], a[1][3] ], [ a[2][1], a[2][2] ], [ n[0][2], a[0][3] ], [ n[2][0], n[0][1] ], [ a[1][2], a[1][1] ], [ n[0][3], n[1][3] ], [ n[1][1], a[2][3] ], [ n[3][0], a[1][0] ], [ n[3][2], n[3][3] ], [ a[3][1], a[3][2] ], [ a[3][3], a[3][0] ], [ a[0][0], a[2][0] ], [ n[2][1], n[3][1] ] ]
        sched[14] = [ [ n[0][0], n[2][3] ], [ n[1][3], n[1][2] ], [ a[1][0], a[0][1] ], [ a[1][3], a[1][2] ], [ n[0][3], n[2][0] ], [ n[2][2], n[2][1] ], [ n[3][0], n[1][0] ], [ a[0][3], a[0][2] ], [ a[2][2], n[1][1] ], [ a[3][2], a[2][0] ], [ a[3][1], a[2][3] ], [ a[2][1], a[3][3] ], [ a[3][0], a[0][0] ], [ a[1][1], n[3][3] ], [ n[3][1], n[3][2] ], [ n[0][1], n[0][2] ] ]
        sched[15] = [ [ a[0][2], a[1][0] ], [ a[0][0], a[1][3] ], [ n[1][1], n[2][2] ], [ n[2][3], n[2][0] ], [ a[2][0], a[2][1] ], [ a[3][2], a[3][0] ], [ a[0][3], n[0][1] ], [ n[0][2], n[0][3] ], [ n[3][1], n[1][3] ], [ a[2][3], a[3][3] ], [ a[1][2], n[3][3] ], [ n[2][1], a[3][1] ], [ n[3][2], n[0][0] ], [ n[1][2], n[3][0] ], [ a[0][1], a[1][1] ], [ a[2][2], n[1][0] ] ]
        sched[16] = [ [ a[2][0], n[1][1] ], [ a[0][1], a[0][0] ], [ n[3][2], n[3][0] ], [ a[2][3], n[1][2] ], [ a[1][0], a[1][2] ], [ n[1][0], a[2][1] ], [ n[1][3], a[2][2] ], [ a[1][3], a[0][3] ], [ a[1][1], a[0][2] ], [ n[0][1], n[0][3] ], [ n[2][2], a[3][2] ], [ n[0][0], n[0][2] ], [ n[3][3], n[3][1] ], [ a[3][0], n[2][3] ], [ n[2][0], n[2][1] ], [ a[3][3], a[3][1] ] ]
        sched[17] = [ [ a[0][2], a[0][1] ], [ a[1][2], a[1][3] ], [ n[2][0], n[2][2] ], [ a[3][1], a[3][0] ], [ n[2][3], n[2][1] ], [ a[0][3], a[0][0] ], [ n[1][2], n[1][1] ], [ n[1][0], n[1][3] ], [ n[0][3], n[0][0] ], [ a[3][3], a[3][2] ], [ n[3][3], n[3][2] ], [ n[0][2], n[0][1] ], [ a[2][2], a[2][3] ], [ a[1][1], a[1][0] ], [ a[2][1], a[2][0] ], [ n[3][0], n[3][1] ] ]
        return sched
     
    def draw_standings(self, x, y):
        text("Week: " + str(self.current_week), x + 5, y - 20)
        draw_table(["AFC EAST",  "W", "L", "T", "PCT", "PF", "PA"], [200, 25, 25, 25, 50, 50, 50], 20, [self.afc_east[0].standings_data, self.afc_east[1].standings_data, self.afc_east[2].standings_data, self.afc_east[3].standings_data], x, y)
        draw_table(["AFC SOUTH", "W", "L", "T", "PCT", "PF", "PA"], [200, 25, 25, 25, 50, 50, 50], 20, [self.afc_south[0].standings_data, self.afc_south[1].standings_data, self.afc_south[2].standings_data, self.afc_south[3].standings_data], x, y + 120)
        draw_table(["AFC NORTH", "W", "L", "T", "PCT", "PF", "PA"], [200, 25, 25, 25, 50, 50, 50], 20, [self.afc_north[0].standings_data, self.afc_north[1].standings_data, self.afc_north[2].standings_data, self.afc_north[3].standings_data], x, y + 240)
        draw_table(["AFC WEST",  "W", "L", "T", "PCT", "PF", "PA"], [200, 25, 25, 25, 50, 50, 50], 20, [self.afc_west[0].standings_data, self.afc_west[1].standings_data, self.afc_west[2].standings_data, self.afc_west[3].standings_data], x, y + 360)
        draw_table(["NFC EAST",  "W", "L", "T", "PCT", "PF", "PA"], [200, 25, 25, 25, 50, 50, 50], 20, [self.nfc_east[0].standings_data, self.nfc_east[1].standings_data, self.nfc_east[2].standings_data, self.nfc_east[3].standings_data], x, y + 480)
        draw_table(["NFC SOUTH", "W", "L", "T", "PCT", "PF", "PA"], [200, 25, 25, 25, 50, 50, 50], 20, [self.nfc_south[0].standings_data, self.nfc_south[1].standings_data, self.nfc_south[2].standings_data, self.nfc_south[3].standings_data], x, y + 600)
        draw_table(["NFC NORTH", "W", "L", "T", "PCT", "PF", "PA"], [200, 25, 25, 25, 50, 50, 50], 20, [self.nfc_north[0].standings_data, self.nfc_north[1].standings_data, self.nfc_north[2].standings_data, self.nfc_north[3].standings_data], x, y + 720)
        draw_table(["NFC WEST", "W", "L", "T", "PCT", "PF", "PA"], [200, 25, 25, 25, 50, 50, 50], 20, [self.nfc_west[0].standings_data, self.nfc_west[1].standings_data, self.nfc_west[2].standings_data, self.nfc_west[3].standings_data], x, y + 840)
        if self.current_week > 0:
            text("Playoff picture:", x, 980 + scroll)
            draw_table(["TEAM", "W", "L", "T", "PCT", "PF", "PA"], [200, 25, 25, 25, 50, 50, 50], 20, [self.afc_playoffs[0].standings_data, self.afc_playoffs[1].standings_data, self.afc_playoffs[2].standings_data, self.afc_playoffs[3].standings_data, self.afc_playoffs[4].standings_data, self.afc_playoffs[5].standings_data, self.afc_playoffs[6].standings_data], x, y + 980)
            draw_table(["TEAM", "W", "L", "T", "PCT", "PF", "PA"], [200, 25, 25, 25, 50, 50, 50], 20, [self.nfc_playoffs[0].standings_data, self.nfc_playoffs[1].standings_data, self.nfc_playoffs[2].standings_data, self.nfc_playoffs[3].standings_data, self.nfc_playoffs[4].standings_data, self.nfc_playoffs[5].standings_data, self.nfc_playoffs[6].standings_data], x, y + 1160)
      
    def draw_games_left_this_week(self):
        global user_teams, user_team_number
        games = 0
        if self.current_week >= self.season_over_week:
            return
        for game in self.schedule[self.current_week]:
            if len(game) == 2:
                fill(150)
                if user_teams[user_team_number] in game:
                    fill(150, 150, 0)
                rect(5 + games%3 * 450, 50 + games/3 * 50, 450, 50, 7)
                fill(0)
                textSize(25)
                text(game[0].abbreviation + " at " + game[1].abbreviation, 10 + games%3 * 450, 50 + games/3 * 50, 445, 50)
                games += 1
            
    def draw_schedule(self, x, y, team):
        textSize(20)
        week_num = 1
        y_add = 10
        if team == "NONE":
            y_add -= 505 * min(self.current_week, self.num_games)
        else:
            y_add += 50
        for week in self.schedule:
            if team == "NONE":
                text("WEEK " + str(week_num) + ":", x, y + y_add)
                y_add += 40
            for game in week:
                if team == "NONE" or team == game[0] or team == game[1] or (len(game) > 2 and team == game[2]):
                    if not (len(game) == 2):
                        if not (team == "NONE") and len(game) > 2 and ( game[0] == team and game[2] > game[3] ) or ( game[1] == team and game[2] < game[3] ):
                            fill(0, 200, 0)
                        elif not (team == "NONE") and len(game) > 2 and (game[0] == team and game[2] < game[3] ) or (game[1] == team and game[2] > game[3] ):
                            fill(125, 0, 0)
                        text(str(game[2]) + " " + game[0].abbreviation, x, y + y_add)
                        text("at "  + game[1].abbreviation + " " + str(game[3]), x + 80, y + y_add)
                        fill(0)
                    else:
                        try:
                            text(game[0].abbreviation, x, y + y_add)
                            text("at "  + game[1].abbreviation, x + 80, y + y_add)
                        except:
                            text("error", x, y + y_add)
                            println(game)
                    y_add += 30
            if team == "NONE":
                y_add += 25
            week_num += 1
            
    def teams_bid_on_fas(self):
        bid = False
        for team in self.teams:
            if team.user_type == "AUTO":
                if team.add_free_agents():
                    bid = True
        if bid:
            self.teams_bid_on_fas()
                
    def teams_use_trade_block(self):
        for team in self.teams:
            if team.user_type == "AUTO":
                team.send_to_trade_block(self.trade_center)
        for team in self.teams:
            if team.user_type == "AUTO":
                team.add_from_trade_block(self.trade_center)
                
    def all_teams_full(self):
        for team in self.teams:
            if not team.full_team_yn():
                return False
        return True
                                
    def sim_week(self):
        global draft1, season1, ls, auto_draft_end
        if self.done:
            return
        if not self.trade_center.deadline_passed:
            self.teams_use_trade_block()
        autos_not_full = True
        all_autos = True
        for team in self.teams:
            if not team.user_type == "AUTO":
                all_autos = False
        tries = 0
        while autos_not_full and not (self.current_week <= self.draft_week or self.current_week > self.season_over_week) and tries < 100 and not (self.current_week == self.draft_end_week and not draft1.is_done):
            autos_not_full = False
            self.ready_to_sim = True
            for team in self.teams:
                if not team.full_team_yn():
                    self.ready_to_sim = False
                    if team.user_type == "AUTO":
                        autos_not_full = True
                        team.fill_spots()
                team.sign_53()
                team.cut_to_53()
                self.free_agents.sign_free_agents()
            tries += 1
        if tries >= 100:
            self.done = True
        if self.current_week == self.resign_week:
            for team in self.teams:
                team.sign_53()
                team.cut_to_53()
                team.week_over()
            self.current_week += 1
            self.free_agents.sort_free_agents()
            return
        self.free_agents.sort_free_agents()
        if self.ready_to_sim or (self.current_week == self.draft_week or self.current_week > self.season_over_week) and not (self.current_week == self.draft_end_week and not draft1.is_done):
            for team in self.teams:
                team.upgrade_players()
                team.week_over()
        if self.current_week >= self.cut_week and self.current_week < self.season_over_week and self.ready_to_sim and not (self.current_week == self.draft_end_week and not draft1.is_done):
            for team in self.teams:
                team.sign_53()
                team.cut_to_53()
        if self.current_week == self.cut_week and (self.ready_to_sim or not draft1.is_done):
            if draft1.is_done:
                self.current_week += 1
            else:
                draft1.set_pick(0)
                change_screen("DRAFT")
                self.ready_to_sim = False
        elif self.current_week == self.draft_end_week:
            if draft1.is_done:
                self.current_week += 1
            else:
                draft1.set_pick(0)
                if all_autos:
                    change_screen("AUTO DRAFTING")
                    auto_draft_end = "DONE"
                else:
                    change_screen("DRAFT")
                self.ready_to_sim = False
        elif self.current_week == self.draft_week:
            self.current_week += 1
            if self.mega_draft:
                draft1 = Draft(self.teams, 53, self.this_year, self.mega_draft)
            else:        
                draft1 = Draft(self.teams, 7, self.this_year, self.mega_draft)
            draft1.set_pick(1)
            if all_autos:
                change_screen("AUTO DRAFTING")
                auto_draft_end = "DONE"
            else:
                #change_screen("DRAFT")
                pass
        elif self.current_week >= self.season_over_week and self.ready_to_sim:
            self.current_week += 1
            self.free_agents.advance_season()
            self.trade_center.end_season()
            self.afc_conf_ranked.sort(key = by_division_record, reverse = True)
            self.nfc_conf_ranked.sort(key = by_division_record, reverse = True)
            self.conf_ranked = sort_conferences(self.afc_conf_ranked, self.nfc_conf_ranked)
            self.teams.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = False)
            draft_order_teams = []
            for team in self.teams:
                if not team in self.afc_playoffs and not team in self.nfc_playoffs:
                    draft_order_teams.append(team)
            for team in self.teams:
                if team in self.afc_playoffs or team in self.nfc_playoffs:
                    draft_order_teams.append(team)
            set_draft_picks(draft_order_teams, 7, False, self.this_year+1)
            if self.schedule[self.sb_week][0][2] > self.schedule[self.sb_week][0][3]:
                ls.add_sb(self.schedule[self.sb_week][0][0].team_name, self.schedule[self.sb_week][0][1].team_name, self.schedule[self.sb_week][0][2], self.schedule[self.sb_week][0][3])
            else:
                ls.add_sb(self.schedule[self.sb_week][0][1].team_name, self.schedule[self.sb_week][0][0].team_name, self.schedule[self.sb_week][0][3], self.schedule[self.sb_week][0][2])
            for team in self.teams:
                team.end_season()
            season1 = Season(self.teams, self.afc_east, self.afc_north, self.afc_south, self.afc_west, self.nfc_east, self.nfc_north, self.nfc_south, self.nfc_west, self.afc_conf_ranked, self.nfc_conf_ranked, self.conf_ranked, self.free_agents, self.this_year + 1, False)
            ls.end_year()
        elif self.ready_to_sim:
            if self.current_week >= 0 and self.current_week < self.wildcard_week:
                for team in self.teams:
                    team.end_regular_week(self.this_year)
            if self.current_week == self.fa_cut_week:
                self.free_agents.cut_free_agents(1000)
            for game in self.schedule[self.current_week]:
                if len(game) == 2:
                    new_game = 0
                    if self.current_week == self.pro_bowl_week:
                        new_game = Game(game[1], game[0], "PRO BOWL", self.this_year)
                    elif self.current_week == self.sb_week:
                        new_game = Game(game[1], game[0], "SB", self.this_year)
                    elif self.current_week >= self.wildcard_week:
                        new_game = Game(game[1], game[0], "PLAYOFF", self.this_year)
                    else:
                        new_game = Game(game[1], game[0], "REGULAR", self.this_year)
                    new_game.play_game()
                    while not new_game.game_over:
                        new_game.advance_play()
                    game.extend([new_game.away_team_score, new_game.home_team_score])
            self.current_week += 1
            self.afc_east.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
            self.afc_north.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
            self.afc_south.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
            self.afc_west.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
            self.nfc_east.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
            self.nfc_north.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
            self.nfc_south.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
            self.nfc_west.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
            if self.current_week <= self.wildcard_week:
                afc_leaders = [self.afc_east[0], self.afc_north[0], self.afc_south[0], self.afc_west[0]]
                rest = []
                rest.extend(self.afc_east[1:])
                rest.extend(self.afc_north[1:])
                rest.extend(self.afc_south[1:])
                rest.extend(self.afc_west[1:])
                rest.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
                self.afc_playoffs = []
                afc_leaders.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
                self.afc_playoffs.extend(afc_leaders)
                self.afc_playoffs.extend(rest[0:3])
                nfc_leaders = [self.nfc_east[0], self.nfc_north[0], self.nfc_south[0], self.nfc_west[0]]
                rest2 = []
                rest2.extend(self.nfc_east[1:])
                rest2.extend(self.nfc_north[1:])
                rest2.extend(self.nfc_south[1:])
                rest2.extend(self.nfc_west[1:])
                rest2.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
                self.nfc_playoffs = []
                nfc_leaders.sort(key = lambda t: (by_team_record(t), by_team_point_diff(t)), reverse = True)
                self.nfc_playoffs.extend(nfc_leaders)
                self.nfc_playoffs.extend(rest2[0:3])
            if self.current_week >= self.wildcard_week:
                self.make_playoff_brackett()
        if self.ready_to_sim or (self.current_week == self.draft_week or self.current_week > self.season_over_week):
            self.free_agents.advance_week()
            self.free_agents.sign_free_agents()
            self.free_agents.sort_free_agents()
            self.teams_bid_on_fas()
            self.trade_center.end_week()
            if self.current_week == self.trade_deadline:
                self.trade_center.deadline_passed = True
        
    def make_playoff_brackett(self):
        if self.current_week == self.wildcard_week:
            self.schedule.append([ [self.afc_playoffs[6], self.afc_playoffs[1]], [self.afc_playoffs[5], self.afc_playoffs[2]], [self.afc_playoffs[4], self.afc_playoffs[3]], [self.nfc_playoffs[6], self.nfc_playoffs[1]], [self.nfc_playoffs[5], self.nfc_playoffs[2]], [self.nfc_playoffs[4], self.nfc_playoffs[3]] ])
        elif self.current_week == self.semis_week:
            last_week_winners = []
            for i in range(0, len(self.schedule[self.wildcard_week])):
                if self.schedule[self.wildcard_week][i][2] > self.schedule[self.wildcard_week][i][3]:
                    last_week_winners.append(self.schedule[self.wildcard_week][i][0])
                else:
                    last_week_winners.append(self.schedule[self.wildcard_week][i][1])
            afc_m1 = 0
            afc_m2 = 0
            nfc_m1 = 0
            nfc_m2 = 0
            if self.afc_playoffs[6] in last_week_winners:
                afc_m1 = [self.afc_playoffs[6], self.afc_playoffs[0]]
                if self.afc_playoffs[5] in last_week_winners:
                    afc_m2 = [self.afc_playoffs[5], last_week_winners[2]]
                else:
                    afc_m2 = [last_week_winners[2], self.afc_playoffs[2]]
            else:
                if self.afc_playoffs[5] in last_week_winners:
                    afc_m1 = [self.afc_playoffs[5], self.afc_playoffs[0]]
                    afc_m2 = [last_week_winners[2], self.afc_playoffs[1]]
                else:
                    afc_m1 = [last_week_winners[2], self.afc_playoffs[0]]
                    afc_m2 = [self.afc_playoffs[2], self.afc_playoffs[1]]
            if self.nfc_playoffs[6] in last_week_winners:
                nfc_m1 = [self.nfc_playoffs[6], self.nfc_playoffs[0]]
                if self.nfc_playoffs[5] in last_week_winners:
                    nfc_m2 = [self.nfc_playoffs[5], last_week_winners[5]]
                else:
                    nfc_m2 = [last_week_winners[5], self.nfc_playoffs[2]]
            else:
                if self.nfc_playoffs[5] in last_week_winners:
                    nfc_m1 = [self.nfc_playoffs[5], self.nfc_playoffs[0]]
                    nfc_m2 = [last_week_winners[5], self.nfc_playoffs[1]]
                else:
                    nfc_m1 = [last_week_winners[5], self.nfc_playoffs[0]]
                    nfc_m2 = [self.nfc_playoffs[2], self.nfc_playoffs[1]]
            self.schedule.append([afc_m1, afc_m2, nfc_m1, nfc_m2])
        elif self.current_week == self.conf_finals_week:
            last_week_winners = []
            for i in range(0, len(self.schedule[self.semis_week])):
                if self.schedule[self.semis_week][i][2] > self.schedule[self.semis_week][i][3]:
                    last_week_winners.append(self.schedule[self.semis_week][i][0])
                else:
                    last_week_winners.append(self.schedule[self.semis_week][i][1])
            afc_m = 0
            nfc_m = 0
            if last_week_winners[0] == self.afc_playoffs[0]:
                afc_m = [last_week_winners[1], last_week_winners[0]]
            else:
                afc_m = [last_week_winners[0], last_week_winners[1]]
            if last_week_winners[2] == self.nfc_playoffs[0]:
                nfc_m = [last_week_winners[3], last_week_winners[2]]
            else:
                nfc_m = [last_week_winners[2], last_week_winners[3]]
            self.schedule.append([afc_m, nfc_m])
        elif self.current_week == self.pro_bowl_week:
            self.fill_pro_bowl_teams()
            self.schedule.append([[self.afc_all_stars, self.nfc_all_stars]])
        elif self.current_week == self.sb_week:
            last_week_winners = []
            if self.schedule[self.conf_finals_week][0][2] > self.schedule[self.conf_finals_week][0][3]:
                last_week_winners.append(self.schedule[self.conf_finals_week][0][0])
            else:
                last_week_winners.append(self.schedule[self.conf_finals_week][0][1])
            if self.schedule[self.conf_finals_week][1][2] > self.schedule[self.conf_finals_week][1][3]:
                if self.conf_ranked[0] == "NFC":
                    last_week_winners.insert(0, self.schedule[self.conf_finals_week][1][0])
                else:
                    last_week_winners.append(self.schedule[self.conf_finals_week][1][0])
            else:
                if self.conf_ranked[0] == "NFC":
                    last_week_winners.insert(0, self.schedule[self.conf_finals_week][1][1])
                else:
                    last_week_winners.append(self.schedule[self.conf_finals_week][1][1])
            self.schedule.append([last_week_winners])
            
################################################################################SEASON CLASS###########################################################################################
################################################################################SEASON CLASS###########################################################################################
################################################################################SEASON CLASS###########################################################################################
################################################################################SEASON CLASS###########################################################################################

################################################################################DRIVE CLASS###########################################################################################
################################################################################DRIVE CLASS###########################################################################################
################################################################################DRIVE CLASS###########################################################################################
################################################################################DRIVE CLASS###########################################################################################

class Drive(object):
    
    def __init__(self, team, quarter, time, yard_line):
        self.quarter_start = quarter
        self.quarter_end =   quarter
        self.time_start =    time
        self.time_end =      time
        self.yard_start =    yard_line
        self.yard_end =      yard_line
        self.plays =         0
        self.result =        "NONE"
        self.team =          team
        
    def to_string(self):
        #return str(int(self.yard_start)) + " " + str(int(self.yard_end))
        return "Q" + str(self.quarter_start) + " " + self.team_string() + " " + self.plays_string() + " plays, " + self.total_yards_string() + " yards, " + self.time_string() + ", Leads to " + self.result
    
    def time_string(self):
        seconds = self.total_time()
        string = ""
        if int(seconds) / 60 < 10:
            string = " " + str(int(seconds/60))
        else:
            string = str(int(seconds/60))
        if seconds % 60 < 10:
            string += ":0" + str(int(seconds%60))
        else:
            string += ":" + str(int(seconds%60))
        return string
        
    def total_time(self):
        if self.quarter_start == self.quarter_end:
            return self.time_start - self.time_end
        else:
            return self.time_start + 15*60.0*(self.quarter_end - self.quarter_start) - self.time_end
        
    def plays_string(self):
        if self.plays < 10:
            return " " + str(self.plays)
        return str(self.plays)
    
    def team_string(self):
        if len(self.team) == 2:
            return "(" + self.team + ") "
        return "(" + self.team + ")"
        
    def total_yards_string(self):
        yards = int(self.yard_end - self.yard_start)
        if yards < 10 and yards >= 0:
            return " " + str(yards)
        return str(yards)

################################################################################DRIVE CLASS###########################################################################################
################################################################################DRIVE CLASS###########################################################################################
################################################################################DRIVE CLASS###########################################################################################
################################################################################DRIVE CLASS###########################################################################################

################################################################################GAME CLASS###########################################################################################
################################################################################GAME CLASS###########################################################################################
################################################################################GAME CLASS###########################################################################################
################################################################################GAME CLASS###########################################################################################
    
class Game(object):
    # add buttons for choosing plays
    def __init__(self, team1, team2, game_type, this_year):
        self.this_year =                 this_year
        self.home_team =                 team1
        self.away_team =                 team2
        self.big_plays =                 ""
        self.quarter =                   1
        self.offense =                   team1
        self.defense =                   team2
        self.yard_line =                 0
        self.down =                      1
        self.to_go =                     10
        self.home_team_score =           0
        self.away_team_score =           0
        self.will_receive_first_half =   0
        self.will_receive_second_half =  0
        self.play =                      "NONE"
        self.game_over =                 False
        self.ot =                        False
        self.home_score_by_q =           [0,0,0,0,0]
        self.away_score_by_q =           [0,0,0,0,0]
        self.game_type =                 game_type
        self.seconds_left =              15*60.0
        self.two_minute_warning =        False
        self.current_drive =             0 #Drive(self.will_receive_first_half.abbreviation, self.quarter, self.seconds_left, self.yard_line)
        self.all_drives =                []
        self.buttons =                   []
        self.set_buttons()
        
    def is_kickoff(self):
        if self.play.is_extra_point or self.play.field_goal_result == "MADE":
            return True
        return False
        
    def offense_score(self):
        if self.home_team == self.offense:
            return self.home_team_score
        return self.away_team_score
    
    def defense_score(self):
        if self.home_team == self.defense:
            return self.home_team_score
        return self.away_team_score
        
    def draw_buttons(self, type = "PLAY"):
        global user_teams
        for button in self.buttons:
            button.hide()
        for button in self.buttons:
            if type == "KICK OFF" and self.offense in user_teams:
                if button.category in {"OFF CONTROL", "KICK OFF CHOICE"}:
                    button.show()
            else:
                if button.category in {"OFF CONTROL", "OFF PLAY TYPE"} and self.offense in user_teams:
                    button.show()
                elif button.category in {"DEF CONTROL", "DEF PLAY TYPE", "DEF BLITZERS", "DEF PLAY FORM"} and self.defense in user_teams:
                    button.show()
                elif button.category in {"OFF PLAY FORM"} and get_button("PASS", self.buttons).highlight and self.offense in user_teams:
                    button.show()
                elif button.category in {"OFF PLAY FORM", "OFF PLAY RB"} and get_button("RUN", self.buttons).highlight and self.offense in user_teams:
                    button.show()
            if type == "PAT" and self.offense in user_teams:
                if button.category in {"PAT CHOICE"}:
                    button.show()
        for button in self.buttons:
            button.draw_button()
                    
    def reset_buttons(self):
        for button in self.buttons:
            if button.do in {"OFF AUTO", "DEF AUTO"}:
                button.highlight = True
            elif button.do in {"OFF USER", "DEF USER"}:
                button.highlight = False
            
    def clicked(self, mouse_x, mouse_y):
        category = ""
        b = None
        for button in self.buttons:
            if button.clicked(mouse_x, mouse_y):
                category = button.category
                button.highlight = not button.highlight
                b = button
        for button in self.buttons:
            if button.category == category and not button == b:
                button.highlight = False
        return not (button == None)
        
    def set_buttons(self):
        self.buttons.append(Button(1325, 85, 100, 35, "AUTO", "OFF AUTO", "OFF CONTROL"))
        self.buttons.append(Button(1425, 85, 100, 35, "USER", "OFF USER", "OFF CONTROL"))
        self.buttons.append(Button(1325, 120, 100, 35, "PASS", "PASS", "OFF PLAY TYPE"))
        self.buttons.append(Button(1325, 155, 100, 35, "RUN",  "RUN",  "OFF PLAY TYPE"))
        self.buttons.append(Button(1325, 190, 100, 35, "PUNT", "PUNT", "OFF PLAY TYPE"))
        self.buttons.append(Button(1325, 225, 100, 35, "FG",   "FG",   "OFF PLAY TYPE"))
        self.buttons.append(Button(1325, 260, 100, 35, "i",          "i",          "OFF PLAY FORM"))
        self.buttons.append(Button(1325, 295, 150, 35, "GOAL LINE",  "goal line",  "OFF PLAY FORM"))
        self.buttons.append(Button(1325, 330, 150, 35, "SINGLEBACK", "singleback", "OFF PLAY FORM"))
        self.buttons.append(Button(1325, 365, 100, 35, "SPREAD",     "spread",     "OFF PLAY FORM"))
        self.buttons.append(Button(1325, 400, 100, 35, "RB1", "RB1", "OFF PLAY RB"))
        self.buttons.append(Button(1325, 435, 100, 35, "RB2", "RB2", "OFF PLAY RB"))
        
        self.buttons.append(Button(1325, 470, 100, 35, "1pt", "1pt", "PAT CHOICE"))
        self.buttons.append(Button(1325, 505, 100, 35, "2pt", "2pt", "PAT CHOICE"))
        
        self.buttons.append(Button(1325, 120, 100, 35, "TB", "TOUCHBACK", "KICK OFF CHOICE"))
        self.buttons.append(Button(1325, 155, 100, 35, "SHORT", "RETURN", "KICK OFF CHOICE"))
        self.buttons.append(Button(1325, 190, 100 ,35, "ONSIDE", "ONSIDE", "KICK OFF CHOICE"))
        
        self.buttons.append(Button(1550, 85, 100, 35, "AUTO", "DEF AUTO", "DEF CONTROL"))
        self.buttons.append(Button(1650, 85, 100, 35, "USER", "DEF USER", "DEF CONTROL"))
        self.buttons.append(Button(1550, 120, 100, 35, "MAN",  "MAN",  "DEF PLAY TYPE"))
        self.buttons.append(Button(1550, 155, 100, 35, "ZONE", "ZONE", "DEF PLAY TYPE"))
        self.buttons.append(Button(1550, 190, 150, 35, "GOAL LINE", "goal line", "DEF PLAY FORM"))
        self.buttons.append(Button(1550, 225, 100, 35, "3-4",       "3-4",       "DEF PLAY FORM"))
        self.buttons.append(Button(1550, 260, 100, 35, "4-3",       "4-3",       "DEF PLAY FORM"))
        self.buttons.append(Button(1550, 295, 100, 35, "NICKEL",    "nickel",    "DEF PLAY FORM"))
        self.buttons.append(Button(1550, 330, 100, 35, "DIME",      "dime",      "DEF PLAY FORM"))
        self.buttons.append(Button(1550, 365, 100, 35, "QUARTER",   "quarter",   "DEF PLAY FORM"))
        self.buttons.append(Button(1550, 400, 150, 35, "0 BLITZERS", 0, "DEF BLITZERS"))
        self.buttons.append(Button(1550, 435, 150, 35, "1 BLITZER",  1, "DEF BLITZERS"))
        self.buttons.append(Button(1550, 470, 150, 35, "2 BLITZERS", 2, "DEF BLITZERS"))
        self.buttons.append(Button(1550, 505, 150, 35, "3 BLITZERS", 3, "DEF BLITZERS"))
        
        for i in (0, 2, 6, 10, 12, 14, 17, 19, 21, 27):
            self.buttons[i].highlight = True
        
    def time_string(self):
        space = " "
        if int(self.seconds_left/60) < 10:
            space = "  "
        if int(self.seconds_left%60) < 10:
            return "Q" + str(int(self.quarter)) + space + str(int(self.seconds_left/60)) + ":0" + str(int(self.seconds_left%60)) + " "
        return "Q" + str(int(self.quarter)) + space + str(int(self.seconds_left/60)) + ":" + str(int(self.seconds_left%60)) + " "
    
    def field_position_string(self):
        if self.yard_line > 50:
            return "opp " + str(int(100 - self.yard_line)) + " yard line"
        else:
            return "own " + str(int(self.yard_line)) + " yard line"
    
    def play_game(self):
        self.offense.reset_game_stats()
        self.defense.reset_game_stats()
        self.coin_toss()
        self.offense = self.will_receive_second_half
        self.defense = self.will_receive_first_half
        self.start_quarter(1)
        self.kickoff()
        self.current_drive = Drive(self.offense.abbreviation, self.quarter, self.seconds_left, self.yard_line)
        self.all_drives.append(self.current_drive)
        self.check_for_score()
        self.check_for_turnover()
        self.check_for_change_of_possession()
        self.play.do_the_stats_thing(self.game_type, self.this_year)
        self.running_clock = False
        
    def run_clock(self, seconds, in_play = False):
        if not in_play and not self.running_clock:
            return
        if self.quarter in {2,4} and not self.two_minute_warning and self.seconds_left - seconds <= 120:
            self.two_minute_warning = True
            self.running_clock = False
            if self.seconds_left > 120 and not in_play:
                self.seconds_left = 120
            elif in_play:
                self.seconds_left -= seconds
        else:
            self.seconds_left -= seconds
            if self.seconds_left < 1:
                self.seconds_left = 0
                        
    def advance_play(self):
        if self.play.injury:
            self.offense.best_lineup()
            self.defense.best_lineup()
        if not self.game_over:
            if (self.play.is_offensive_touchdown or self.play.is_defensive_touchdown) and not self.play.is_extra_point:
                self.attempt_extra_point()
            elif self.seconds_left <= 0:
                self.start_quarter(self.quarter + 1)
            elif self.is_kickoff() or self.play.is_offensive_safety or self.play.is_defensive_safety:
                self.kickoff()
                self.check_for_score()
                #self.check_for_turnover()
                self.check_for_change_of_possession()
            else:
                self.do_a_play()
                self.check_for_score()
                #self.check_punt_and_missed_fg()
                self.check_made_fg()
                #self.check_for_turnover()
                self.check_for_change_of_possession()
                self.update_down_and_distance(self.play.play_gain)
                if self.running_clock:
                    self.run_clock(random(25, 39))
        if not self.game_over:
            self.reset_buttons()
            self.play.do_the_stats_thing(self.game_type, self.this_year)
        
    def update_standings_data(self):
        if not self.game_over:
            return
        self.all_drives[len(self.all_drives)-1].result = "END GAME"
        self.home_team.update_standings_data("PF", self.home_team_score, self.game_type, self.this_year)
        self.home_team.update_standings_data("PA", self.away_team_score, self.game_type, self.this_year)
        self.away_team.update_standings_data("PF", self.away_team_score, self.game_type, self.this_year)
        self.away_team.update_standings_data("PA", self.home_team_score, self.game_type, self.this_year)
        if self.home_team_score > self.away_team_score:
            self.home_team.update_standings_data("WIN", 1, self.game_type, self.this_year)
            self.away_team.update_standings_data("LOSS", 1, self.game_type, self.this_year)
            self.home_team.add_stats("ALL", "WINS", 1, self.game_type, self.this_year)
            self.away_team.add_stats("ALL", "LOSSES", 1, self.game_type, self.this_year)
        elif self.home_team_score < self.away_team_score:
            self.home_team.update_standings_data("LOSS", 1, self.game_type, self.this_year)
            self.away_team.update_standings_data("WIN", 1, self.game_type, self.this_year)
            self.home_team.add_stats("ALL", "LOSSES", 1, self.game_type, self.this_year)
            self.away_team.add_stats("ALL", "WINS", 1, self.game_type, self.this_year)
        else:
            self.home_team.update_standings_data("TIE", 1, self.game_type, self.this_year)
            self.away_team.update_standings_data("TIE", 1, self.game_type, self.this_year)
            self.home_team.add_stats("ALL", "TIES", 1, self.game_type, self.this_year)
            self.away_team.add_stats("ALL", "TIES", 1, self.game_type, self.this_year)
        
    def draw_game(self):
        global scroll, c
        backwards = False
        if self.home_team == self.defense:
            backwards = True
        fill(0,200,0)
        rect(100,100,1200, 530) #field
        stroke(0)
        strokeWeight(5)
        line(200, 102, 200, 628) #end zone
        line(1200, 102, 1200, 628) # middle
        line(700, 102, 700, 628) #end zone
        strokeWeight(1)
        for x in range(0,99):
            line(210 + 10*x, 100, 210 + 10*x, 110) #small marks
            line(210 + 10*x, 630, 210 + 10*x, 620) #small marks
            line(210 + 10*x, 335, 210 + 10*x, 325) #hash marks
            line(210 + 10*x, 395, 210 + 10*x, 405) #hash marks
            if x % 5 == 4:
                line(210 + 10*x, 100, 210 + 10*x, 630) #cross field lines
            if x % 10 == 9:
                num = 0
                if x < 50:
                    num = x + 1
                else:
                    num = 100 - (x + 1)
                fill(0)
                textSize(20)
                if num == 50:
                    text("5 0", 195 + 10*x, 125) #numbers
                    text("5 0", 195 + 10*x, 620) #numbers
                else:
                    text(num, 198 + 10*x, 125) #numbers
                    text(num, 198 + 10*x, 620) #numbers
                textSize(10)
        stroke(255,255,0)
        strokeWeight(5)
        line(100, 335, 100, 395) #field goal
        line(1300, 335, 1300, 395) #field goal
        strokeWeight(1)
        stroke(0)
        fill(0)
        if backwards:
            rect(1400 - (205 + 10*min(self.yard_line, 105)), 360, 10,10) #ball
        else:
            rect(195 + 10*min(self.yard_line, 105), 360, 10,10) #ball
        strokeWeight(2)
        stroke(0,0,200)
        if self.yard_line > 0 and self.yard_line < 100:
            if backwards:
                line(1400 - (200 + 10*self.yard_line), 100, 1400 - (200 + 10*self.yard_line), 630) #line of scrimmage
            else:
                line(200 + 10*self.yard_line, 100, 200 + 10*self.yard_line, 630) #line of scrimmage
        stroke(200,200,0)
        if self.yard_line + self.to_go > 0 and self.yard_line + self.to_go < 100:
            if backwards:
                line(1400 - (200 + 10*(self.yard_line + self.to_go)), 100, 1400 - (200 + 10*(self.yard_line + self.to_go)), 630) #first down
            else:
                line(200 + 10*(self.yard_line + self.to_go), 100, 200 + 10*(self.yard_line + self.to_go), 630) #first down
        x = 175
        y = 365
        textSize(60)
        pushMatrix()
        translate(x,y)
        rotate(-HALF_PI)
        translate(-x,-y)
        textAlign(CENTER)
        text(self.home_team.team_location.upper(), x,y) #left end zone
        textAlign(LEFT)
        popMatrix()
        x2 = 1225
        y2 = 365
        textSize(60)
        pushMatrix()
        translate(x2,y2)
        rotate(HALF_PI)
        translate(-x2,-y2)
        textAlign(CENTER)
        text(self.home_team.team_name.upper(), x2,y2) #right end zone
        textAlign(LEFT)
        popMatrix()
        textSize(10)
        strokeWeight(1)
        textSize(25)
        text(self.home_team.abbreviation + ": " + str(self.home_team_score) + "   " + self.away_team.abbreviation + ": " + str(self.away_team_score),50,50)
        text(str(int(round(self.home_team.get_team_overall()))) + " OVR  vs " + str(int(round(self.away_team.get_team_overall()))) + " OVR", 50, 75)
        yd_line = self.yard_line
        if yd_line > 50:
            yd_line = 100 - yd_line
        to_go = int(round(self.to_go))
        if to_go == 0:
            to_go = "INCHES"
        if self.to_go + self.yard_line >= 100:
            to_go = "GOAL"
        down_and_dist = str(self.down) + " & " + str(to_go) + " at the " + str(int(round(yd_line)))
        if self.play.is_defensive_touchdown or self.play.is_offensive_touchdown:
            down_and_dist = "TOUCHDOWN"
        elif self.play.is_kick_off:
            down_and_dist = "KICK OFF"
        elif self.play.is_extra_point:
            down_and_dist = "PAT"
        text(down_and_dist + "       Q" + str(self.quarter) + "    Time: " + str(self.time_string()), 700, 50)
        textSize(15)
        text(self.offense.name() + " have the ball", 100, 675)
        text(self.current_drive.to_string(), 50, 900)
        if not (self.play == "NONE"):
            self.play.draw_play(50, 700)
        if self.play.is_score():
            score = "FIELD GOAL!"
            if self.play.is_defensive_touchdown or self.play.is_offensive_touchdown:
                score = "TOUCHDOWN!"
            elif self.play.is_defensive_safety or self.play.is_offensive_touchdown:
                score = "SAFETY!"
            textSize(75)
            fill(255,255,0)
            text(score, 430, 375)
            fill(0)
            textSize(10)
        textSize(15)
        stats_to_show = []
        start_x = 0
        start_y = 0
        if self.game_over:
            background(100)
            draw_table(["Team", "1", "2", "3", "4", "OT", "FINAL"], [125, 50, 50, 50, 50, 50, 50], 20, [[self.home_team.abbreviation, self.home_score_by_q[0], self.home_score_by_q[1], self.home_score_by_q[2], self.home_score_by_q[3], self.home_score_by_q[4], self.home_team_score], [self.away_team.abbreviation, self.away_score_by_q[0], self.away_score_by_q[1], self.away_score_by_q[2], self.away_score_by_q[3], self.away_score_by_q[4], self.away_team_score]], 300, 5 + scroll)
            
            start_x = 100
            start_y = 100
            stats_to_show = ["THROW", "RECEIVE", "RUN", "BLOCK", "COVER", "BLITZ", "XP", "FG", "PUNT", "KICK OFF", "RETURN", "2pt"]
            #text(self.big_plays, 1300, 220 + scroll)
            y = 0
            for drive in self.all_drives:
                if drive.result == "NONE":
                    self.all_drives.remove(drive)
                else:
                    text(drive.to_string(), 1300, 220 + scroll + y)
                    y += 20
        elif self.play.will_punt or self.play.is_kick_off:
            start_x = 500
            start_y = 635
            stats_to_show = ["PUNT", "RETURN"]
        elif self.play.play_type in {"EXTRA POINT", "FIELD GOAL"}:
            start_x = 500
            start_y = 635
            stats_to_show = ["XP", "FG"]
        elif self.play.pass_run == "PASS":
            start_x = 500
            start_y = 635
            stats_to_show = ["THROW", "RECEIVE"]
        elif self.play.pass_run == "RUN":
            start_x = 500
            start_y = 635
            stats_to_show = ["RUN", "BLITZ"]
        if not self.game_over and not self.play.is_score() and not self.is_kickoff():
            self.draw_buttons()
        elif not self.game_over and self.is_kickoff():
            self.draw_buttons("KICK OFF")
        elif not self.game_over and self.play.is_offensive_touchdown or self.play.is_defensive_touchdown:
            self.draw_buttons("PAT")
            
        prev_players = 0
        for stat in stats_to_show:
            players = []
            for player in self.home_team.Players:
                if player.has_stats(stat, "GAME"):
                    players.append(player)
            for player in self.away_team.Players:
                if player.has_stats(stat, "GAME"):
                    players.append(player)
            players.sort(key = lambda p: by_rating(p, "GAME", stat), reverse = True)
            players.append(self.home_team)
            players.append(self.away_team)
            make_stats_table(stat, "GAME", 0, players, start_x, start_y + prev_players*20 + scroll, -1, False, -1)
            prev_players += len(players) + 2
    
    
    def update_down_and_distance(self, gain):
        if self.play.is_change_of_possession():
            self.down = 1
            self.to_go = 10
        elif self.play.is_score():
            self.down = 1
            self.to_go = 10
        elif gain < self.to_go:
            self.down += 1
            self.to_go -= gain
        elif gain > self.to_go:
            self.down = 1
            self.to_go = 10
        if self.to_go + self.yard_line > 100:
            self.to_go = 100.0 - self.yard_line
            
    def add_score(self, points, team):
        if team == self.home_team:
            self.home_team_score += points
            if self.ot:
                self.home_score_by_q[4] += points
            else:
                self.home_score_by_q[self.quarter - 1] += points
        else:
            self.away_team_score += points
            if self.ot:
                self.away_score_by_q[4] += points
            else:
                self.away_score_by_q[self.quarter - 1] += points
            
    def check_made_fg(self):
        if self.play.will_kick_field_goal and self.play.field_goal_result == "MADE":
            self.add_score(3, self.offense)
            self.current_drive.result = "FG MADE (" + str(int(117-self.yard_line)) + " yards)"
            #self.all_drives.append(self.current_drive)
            #print "added in check for made fg"
            self.yard_line = 35
            self.down = 1
            self.to_go = 10
            
    def check_for_change_of_possession(self):
        if self.play.is_change_of_possession():
            temp = self.offense
            self.offense = self.defense
            self.defense = temp
            
            if not self.play.change_of_possession_type() == "KICK OFF":
                self.current_drive.result = self.play.change_of_possession_type()
                #self.all_drives.append(self.current_drive)
                #print "added in check for change of possesion"
                
            if not self.play.is_touchback and not self.play.is_kick_off:
                self.yard_line = 100 - self.yard_line
                
            self.current_drive = Drive(self.offense.abbreviation, self.quarter, self.seconds_left, self.yard_line)
            self.all_drives.append(self.current_drive)
            
    def check_punt_and_missed_fg(self):
        pass
        
    def coin_toss(self):
        rand = int(random(0,2))
        if rand == 0:
            self.will_receive_first_half = self.home_team
            self.will_receive_second_half = self.away_team
        else:
            self.will_receive_first_half = self.away_team
            self.will_receive_second_half = self.home_team
    
    def kickoff(self):
        offense_score = 0
        defense_score = 0
        if self.offense == self.home_team:
            offense_score = self.home_team_score
            defense_score = self.away_team_score
        else:
            offense_score = self.away_team_score
            defense_score = self.home_team_score
        self.yard_line = 35
        onside = self.quarter >= 4 and self.seconds_left <= 150.0 and offense_score < defense_score
        self.play = Play(self.offense, self.defense, self.down, self.to_go, 0, self.quarter, self.seconds_left, offense_score, defense_score, True, onside, 0, self.game_type)
        k = "AUTO"
        if get_button("OFF USER", self.buttons).highlight:
            self.play.is_onside_kick = get_button("ONSIDE", self.buttons).highlight
            for button in self.buttons:
                if button.category == "KICK OFF CHOICE" and not button.do == "ONSIDE" and button.highlight:
                    k = button.do
        self.yard_line = self.play.play_result(kick = k)
        self.check_touchback()
        if not self.play.is_touchback:
            self.run_clock(self.play.play_time, True)
        self.running_clock = self.play.is_running_clock
        self.current_drive = Drive(self.offense.abbreviation, self.quarter, self.seconds_left, self.yard_line)
        self.all_drives.append(self.current_drive)
        
    def do_a_play(self):
        offense_score = 0
        defense_score = 0
        if self.offense == self.home_team:
            offense_score = self.home_team_score
            defense_score = self.away_team_score
        else:
            offense_score = self.away_team_score
            defense_score = self.home_team_score
        self.play = Play(self.offense, self.defense, self.down, self.to_go, self.yard_line, self.quarter, self.seconds_left, offense_score, defense_score, False, False, 0, self.game_type)
        off_form = "AUTO"
        def_form = "AUTO"
        p_r = "AUTO"
        m_z = "AUTO"
        nb = "AUTO"
        rb = "AUTO"
        if get_button("OFF USER", self.buttons).highlight:
            for button in self.buttons:
                if button.highlight:
                    if button.category == "OFF PLAY FORM":
                        off_form = button.do
                    elif button.category == "OFF PLAY TYPE":
                        if button.do == "PUNT":
                            self.play.will_punt = True
                            self.play.will_kick_field_goal = False
                        elif button.do == "FG":
                            self.play.will_punt = False
                            self.play.will_kick_field_goal = True
                        else:
                            self.play.will_punt = False
                            self.play.will_kick_field_goal = False
                            p_r = button.do
                    elif button.category == "OFF PLAY RB":
                        if button.do == "RB1":
                            rb = self.offense.rb1
                        else:
                            rb = self.offense.rb2
        if get_button("DEF USER", self.buttons).highlight:
            for button in self.buttons:
                if button.highlight:
                    if button.category == "DEF PLAY FORM":
                        def_form = button.do
                    elif button.category == "DEF PLAY TYPE":
                        m_z = button.do
                    elif button.category == "DEF BLITZERS":
                        nb = button.do
        self.play.play_result(off_form, def_form, p_r, m_z, nb, rb)
        self.running_clock = self.play.is_running_clock
        self.yard_line += self.play.play_gain
        self.check_touchback()
        self.run_clock(self.play.play_time, True)
        if not self.play.is_change_of_possession():
            self.current_drive.yard_end = self.yard_line
        self.current_drive.quarter_end = self.quarter
        self.current_drive.time_end = self.seconds_left
        self.current_drive.plays += 1
        return self.play.play_gain
    
    def check_touchback(self):
        if self.play.is_touchback:
            if self.play.is_kick_off:
                self.yard_line = 25
            else:
                self.yard_line = 20
        
    def start_quarter(self, quarter):
        if quarter > 4 and not self.home_team_score == self.away_team_score:
            self.game_over = True
            self.update_standings_data()
            return
        if quarter > 5:
            if not self.game_type in {"PLAYOFF", "SB"}:
                self.game_over = True
                self.update_standings_data()
                return
        self.two_minute_warning = False
        self.quarter = quarter
        self.seconds_left = 15*60.0
        if self.quarter == 3 or self.quarter > 4:
            if self.quarter > 4:
                self.seconds_left = 10*60.0
                self.ot = True
                self.coin_toss()
            self.offense = self.will_receive_first_half
            self.defense = self.will_receive_second_half
            self.kickoff()
            self.check_for_score()
            self.check_for_turnover()
            self.down = 1
            self.to_go = 10
            self.current_drive.result = "END HALF"
            #self.all_drives.append(self.current_drive)
            #print "added in start quarter"
            self.current_drive = Drive(self.offense.abbreviation, quarter, self.seconds_left, self.yard_line)
            self.all_drives.append(self.current_drive)
            
    def check_for_score(self):
        if self.play.is_offensive_touchdown:
            self.yard_line = 85
            self.to_go = 10
            self.down = 1
            self.add_score(6, self.offense)
            self.current_drive.result = "TOUCHDOWN (" + str(int(self.play.play_gain)) + " yards)"
        elif self.play.is_defensive_touchdown:
            self.yard_line = 15
            self.to_go = 10
            self.down = 1
            self.add_score(6, self.defense)
            self.current_drive.result = "DEF TOUCHDOWN (" + str(int(self.play.play_gain)) + " yards)"
        elif self.play.is_defensive_safety:
            self.yard_line = 20
            self.to_go = 10
            self.down = 1
            self.add_score(2, self.defense)
            self.current_drive.result = "SAFETY (" + str(int(self.play.play_gain)) + " yards)"
        elif self.play.is_offensive_safety:
            self.yard_line = 20
            self.to_go = 10
            self.down = 1
            self.add_score(2, self.offense)
            self.current_drive.result = "OFF SAFETY (" + str(int(self.play.play_gain)) + " yards)"
        #self.all_drives.append(self.current_drive)
        #print "added in check for score"
    
    def check_for_turnover(self):
        pass
        #if self.play.is_turnover():
            
    def attempt_extra_point(self):
        offense_score = self.offense_score()
        defense_score = self.defense_score()
        pat_amount = 1
        self.yard_line = 85
        if defense_score - offense_score in {-5, -1, 2, 5, 10, 18} and self.quarter >= 3:
            pat_amount = 2
            self.yard_line = 98
        self.play = Play(self.offense, self.defense, self.down, self.to_go, self.yard_line, self.quarter, self.seconds_left, offense_score, defense_score, False, False, pat_amount, self.game_type)
        off_form = "AUTO"
        def_form = "AUTO"
        p_r = "AUTO"
        m_z = "AUTO"
        nb = "AUTO"
        rb = "AUTO"
        if get_button("OFF USER", self.buttons).highlight:
            if get_button("2pt", self.buttons).highlight:
                pat_amount = 2
            if get_button("1pt", self.buttons).highlight:
                pat_amount = 1
            if pat_amount == 2:
                for button in self.buttons:
                    if button.highlight:
                        if button.category == "OFF PLAY FORM":
                            off_form = button.do
                        elif button.category == "OFF PLAY TYPE":
                            if button.do == "PUNT":
                                p_r = "PASS"
                            elif button.do == "FG":
                                p_r = "PASS"
                            else:
                                self.play.will_punt = False
                                self.play.will_kick_field_goal = False
                                p_r = button.do
                        elif button.category == "OFF PLAY RB":
                            if button.do == "RB1":
                                rb = self.offense.rb1
                            else:
                                rb = self.offense.rb2
                if get_button("DEF USER", self.buttons).highlight:
                    for button in self.buttons:
                        if button.highlight:
                            if button.category == "DEF PLAY FORM":
                                def_form = button.do
                            elif button.category == "DEF PLAY TYPE":
                                m_z = button.do
                            elif button.category == "DEF BLITZERS":
                                nb = button.do
        self.play.is_extra_point = pat_amount
        self.play.play_result(off_form, def_form, p_r, m_z, nb, rb)
        self.running_clock = self.play.is_running_clock
        if self.play.field_goal_result == "MADE" or self.play.is_offensive_safety:
            self.add_score(1, self.offense)
        elif self.play.is_offensive_touchdown:
            self.add_score(2, self.offense)
        elif self.play.is_defensive_safety:
            self.add_score(1, self.defense)
        elif self.play.is_defensive_touchdown:
            self.add_score(2, self.defense)
        self.yard_line = 35
    
    
################################################################################GAME CLASS###########################################################################################
################################################################*****###########GAME CLASS###########################################################################################
################################################################################GAME CLASS###########################################################################################
################################################################################GAME CLASS###########################################################################################
    
################################################################################PLAY CLASS###########################################################################################
################################################################################PLAY CLASS###########################################################################################
################################################################################PLAY CLASS###########################################################################################
################################################################################PLAY CLASS###########################################################################################

class Play(object):
    
    def __init__(self, offense, defense, down, to_go, yard_line, quarter, seconds_left, offense_score, defense_score, is_kick_off, is_onside_kick, is_extra_point, game_type):
        self.offense =                 offense
        self.defense =                 defense
        self.is_kick_off =             is_kick_off
        self.is_onside_kick =          is_onside_kick
        self.is_extra_point =          is_extra_point
        if is_kick_off or is_extra_point:
            self.will_punt = False
            self.will_kick_field_goal = False
        else:
            self.will_kick_field_goal =    self.should_kick_field_goal(down, to_go, yard_line, quarter, seconds_left, offense_score, defense_score)
            self.will_punt =               self.should_punt(down, to_go, yard_line, quarter, seconds_left, offense_score, defense_score)
        self.off_form =                "NONE"
        self.def_form =                "NONE"
        self.pass_run =                "NONE"
        self.man_zone =                "NONE"
        self.num_blitzers =            "NONE"
        self.receivers =               "NONE"
        self.blockers =                "NONE"
        self.coverage =                "NONE"
        self.blitzers =                "NONE"
        self.pass_dist =               "NONE"
        self.pass_result =             "NONE"
        self.target =                  "NONE"
        self.target_defender =         "NONE"
        self.run_dist =                "NONE"
        self.yac =                     "NONE"
        self.run_result =              "NONE"
        self.run_dist =                "NONE"
        self.rusher =                  "NONE"
        self.def_return =              "NONE"
        self.forced_turnover =         "NONE"
        self.scramble_result =         "NONE"
        self.scramble_dist =           "NONE"
        self.field_goal_dist =         "NONE"
        self.field_goal_result =       "NONE"
        self.punt_dist =               "NONE"
        self.punt_result =             "NONE"
        self.punt_return =             "NONE"
        self.yard_line =               yard_line
        self.kick_off_result =         "NONE"
        self.kick_off_return =         "NONE"
        self.yards_lost =              "NONE"
        self.tackler =                 "NONE"
        self.dropped =                 False
        self.is_offensive_touchdown =  False
        self.is_defensive_touchdown =  False
        self.is_defensive_safety =     False
        self.is_offensive_safety =     False
        self.is_touchback =            False
        self.is_fumble =               False
        self.injury =                  False
        self.injured =                 "NONE"
        self.game_type =               game_type
        self.play_type =               "NONE"
        self.is_running_clock =        False
        self.play_time =               0.0
        self.play_gain =               0.0
        self.to_go_start =             to_go
        self.down_start =              down
        self.user_controlled =         False
        
    def is_score(self):
        return self.is_offensive_touchdown or self.is_defensive_touchdown or self.is_defensive_safety or self.is_offensive_safety or (self.will_kick_field_goal and self.field_goal_result == "MADE")
    
    def is_turnover(self):
        return self.is_fumble or self.pass_result == "INT" or self.run_result == "FUMBLE" or self.scramble_result == "FUMBLE" or self.kick_off_result == "ONSIDE KICK SUCCESS"
    
    def is_change_of_possession(self): # ^ is xor
        if self.is_extra_point:
            return False
        return ((self.is_turnover() ^ self.will_punt) ^ self.is_kick_off) or (self.will_kick_field_goal and self.field_goal_result == "MISS") or (self.to_go_start > self.play_gain and self.down_start >= 4 and not self.will_kick_field_goal and not self.is_offensive_touchdown)
      
    def change_of_possession_type(self):
        if not self.is_change_of_possession():
            return "NONE"
        if self.is_fumble or self.run_result == "FUMBLE" or self.scramble_result == "FUMBLE":
            return "FUMBLE"
        elif self.pass_result == "INT":
            return "INT"
        elif self.will_punt:
            return "PUNT"
        elif self.is_kick_off:
            return "KICK OFF"
        elif self.will_kick_field_goal and self.field_goal_result == "MISS":
            return "FG MISSED"
        elif self.to_go_start > self.play_gain and self.down_start >= 4 and not self.will_kick_field_goal and not self.is_offensive_touchdown:
            return "DOWNS"
            
    def draw_play(self,x,y):
        text("Play type: " + self.play_type, x, y)
        words = ""
        if self.play_type == "KICK OFF":
            if self.kick_off_result == "TOUCHBACK":
                words += self.offense.k.name() + " kicked it for a touchback"
            elif self.is_onside_kick:
                if self.is_turnover():
                    words += self.offense.k.name() + " did a successful onside kick"
                else:
                    words += self.offense.k.name() + " tried an unsuccessful onside kick"
            else:
                words += self.offense.k.name() + " kicked it to " + self.defense.rt.name() + " who returned it for " + str(int(round(self.kick_off_return))) + " yards"
        if self.play_type == "EXTRA POINT":
            if self.field_goal_result == "MISS":
                words += self.offense.k.name() + " missed the extra point"
            else:
                words += self.offense.k.name() + " made the extra point"
        if self.play_type in {"2pt PASS", "2pt SCRAMBLE", "2pt RUN"}:
            if self.is_offensive_touchdown:
                words += "2pt Success"
            else:
                words += "2pt Failure"
            if self.play_type == "2pt PASS":
                words += " " + self.offense.qb1.name() + " to " + self.target.name()
            elif self.play_type == "2pt SCRAMBLE":
                words += " " + self.offense.qb1.name() + " runs it"
            else:
                words += " " + self.rusher.name() + " runs it"
        if self.play_type == "PUNT":
            if self.punt_result == "PIN":
                words += self.offense.k.first_name + " " + self.offense.k.last_name + " pinned the " + self.defense.abbreviation + " inside the 5"
            elif self.punt_result == "TOUCHBACK":
                words += self.offense.k.first_name + " " + self.offense.k.last_name + " kicked it for a touchback"
            else:
                words += self.offense.k.first_name + " " + self.offense.k.last_name + " punted it " + str(int(round(self.punt_dist))) + " yards and " + self.defense.rt.first_name + " " + self.defense.rt.last_name + " returned it " + str(int(round(self.punt_return))) + " yards"
        if self.play_type == "FIELD GOAL":
            if self.field_goal_result == "MISS":
                words += self.offense.k.first_name + " " + self.offense.k.last_name + " missed the field goal"
            else:
                words += self.offense.k.first_name + " " + self.offense.k.last_name + " made the field goal"
        if self.play_type in {"PASS", "SCRAMBLE"}:
            if self.pass_result == "SACK":
                words += self.offense.qb1.first_name + " " + self.offense.qb1.last_name + " was sacked for a loss of " + str(int(round(self.yards_lost))) + " yards"
            elif self.pass_result == "SCRAMBLE":
                if self.scramble_result == "GAIN":
                    words += self.offense.qb1.first_name + " " + self.offense.qb1.last_name + " scrambled for " + str(int(round(self.scramble_dist))) + " yards"
                elif self.scramble_result == "LOSS":
                    words += self.offense.qb1.first_name + " " + self.offense.qb1.last_name + " scrambled, but was tackled for a loss of " + str(int(round(-1*self.yards_lost))) + " yards"
                else:
                    words += self.offense.qb1.first_name + " " + self.offense.qb1.last_name + " tried to scramble, but fumbled, " + self.forced_turnover.first_name + " " + self.forced_turnover.last_name + " recovered it and returned it for " + str(int(round(self.def_return))) + " yards"
            elif self.pass_result == "INCOMPLETE":
                words += self.offense.qb1.first_name + " " + self.offense.qb1.last_name + " was looking for " + self.target.first_name + " " + self.target.last_name + " " + str(int(round(self.pass_dist))) + " yards downfield, but the pass fell incomplete"
            elif self.pass_result == "COMPLETE":
                words += self.offense.qb1.first_name + " " + self.offense.qb1.last_name + " found " + self.target.first_name + " " + self.target.last_name + " " + str(int(round(self.pass_dist))) + " yards downfield for a " + str(int(round(self.pass_dist + self.yac))) + " yard gain" 
            elif self.pass_result == "INT":
                words += self.offense.qb1.first_name + " " + self.offense.qb1.last_name + " was looking for " + self.target.first_name + " " + self.target.last_name + " " + str(int(round(self.pass_dist))) + " yards downfield, but " + self.forced_turnover.first_name + " " + self.forced_turnover.last_name + " stepped in for an interception"
        if self.play_type == "RUN":
            if self.run_result == "LOSS":
                words += self.rusher.first_name + " " + self.rusher.last_name + " was stopped in the backfield for a loss of " + str(int(round(self.yards_lost))) + " yards"
            elif self.run_result == "GAIN":
                words += self.rusher.first_name + " " + self.rusher.last_name + " ran for " + str(int(round(self.run_dist))) + " yards"
            elif self.run_result == "FUMBLE":
                words += self.rusher.first_name + " " + self.rusher.last_name + " fumbled, " + self.forced_turnover.first_name + " " + self.forced_turnover.last_name + " scooped it up and returned it " + str(int(round(self.def_return))) + " yards"
        if not (self.tackler == "NONE"):
            try:
                words += " " + self.tackler.first_name + " " + self.tackler.last_name + " was in on the tackle"
            except:
                println(self.tackler)
                println(self.pass_run)
                println(self.man_zone)
                println(self.num_blitzers)
                println("")
        if self.is_fumble:
            words += " FUMBLE!"
        if self.injury:
            words += " injury on the play: " + self.injured.first_name + " " + self.injured.last_name + " " + self.injured.position
        words += "\nTime: " + str(int(round(self.play_time))) + "s"
        words += "\nOff: " + self.off_form + " " + self.pass_run
        words += "\nDef: " + self.def_form + " " + self.man_zone + " " + str(self.num_blitzers) + " blitzers"
        text(words, x, y + 5, 400, 300)
        
    def play_result(self, off_form = "AUTO", def_form = "AUTO", p_r = "AUTO", m_z = "AUTO", nb = "AUTO", rb = "AUTO", kick = "AUTO"):
        global c
        play_gain = 0
        if not (self.will_punt or self.will_kick_field_goal or self.is_kick_off or self.is_extra_point == 1):
            if off_form == "AUTO":
                self.off_form = self.get_off_formation()
            else:
                self.off_form = off_form
            if def_form == "AUTO":
                self.def_form = self.get_def_formation()
            else:
                self.def_form = def_form
            if p_r == "AUTO":
                self.pass_run = self.get_pass_run()
            else:
                self.pass_run = p_r
            if m_z == "AUTO":
                self.man_zone = self.get_man_zone()
            else:
                self.man_zone = m_z
            if nb == "AUTO":
                self.num_blitzers = self.get_num_blitzers()
            else:
                self.num_blitzers = nb
            self.receivers = self.get_receivers(self.off_form, self.pass_run)
            self.blockers = self.get_blockers(self.off_form, self.pass_run, rb)
            self.coverage = self.get_coverage(self.def_form, self.num_blitzers)
            self.blitzers = self.get_blitzers(self.def_form, self.num_blitzers)
        
        if not self.game_type in {"PRE SEASON", "PRO BOWL"}:
            self.create_injuries()
        if self.pass_run == "PASS" and self.is_extra_point in {0,2}:
            if self.is_extra_point == 2:
                self.play_type = "2pt PASS"
            else:
                self.play_type = "PASS"
            self.target = self.get_target()
            self.pass_dist = self.get_pass_distance()
            self.pass_result = self.get_pass_result()
            if self.pass_result == "COMPLETE":
                self.yac = self.get_yac()
                self.tackler = self.get_tackler("COVERAGE")
                if self.yard_line + self.pass_dist + self.yac > 100 or self.yard_line + self.pass_dist > 100:
                    self.is_offensive_touchdown = True
                    self.is_running_clock = False
                    if self.yard_line + self.pass_dist > 100:
                        self.pass_dist = 100 - self.yard_line
                        self.yac = 0
                    else:
                        self.yac = 100 - (self.yard_line + self.pass_dist)
                elif self.check_for_fumble(self.target):
                    self.def_return = self.get_def_return()
                    self.is_running_clock = False
                    cur_yd_line = self.yard_line + self.pass_dist + self.yac - self.def_return 
                    if cur_yd_line > 100:
                        self.is_offensive_safety = True
                        self.def_return = -1 * (100 - (self.yard_line + self.pass_dist + self.yac))
                    if cur_yd_line < 0:
                        self.is_defensive_touchdown = True
                        self.def_return = self.yard_line + self.pass_dist + self.yac
                    play_gain = self.pass_dist + self.yac - self.def_return
                elif self.yard_line + self.pass_dist + self.yac < 0:
                    self.is_defensive_safety = True
                    self.is_running_clock = False
                elif not self.is_extra_point:
                        self.is_running_clock = True # unless oob
                play_gain = self.pass_dist + self.yac
            elif self.pass_result == "INCOMPLETE":
                self.is_running_clock = False
                play_gain = 0
            elif self.pass_result == "SACK":
                if not self.is_extra_point:
                    self.is_running_clock = True
                self.yards_lost = random(4, 13)
                self.tackler = self.get_tackler("BLITZER")
                if self.check_for_fumble(self.offense.qb1):
                    self.is_running_clock = False
                    self.def_return = self.get_def_return()
                    cur_yd_line = self.yard_line - self.yards_lost - self.def_return
                    if cur_yd_line < 0:
                        self.is_defensive_touchdown = True
                        self.def_return = self.yard_line - self.yards_lost
                    elif cur_yd_line > 100:
                        self.is_offensive_safety = True
                        self.def_return = -1 * (100 - (self.yard_line - self.yards_lost))
                    play_gain = (-1 * self.yards_lost) - self.def_return
                if self.yard_line - self.yards_lost < 0:
                    self.is_running_clock = False
                    self.is_defensive_safety = True
                    self.yards_lost = self.yard_line
                play_gain = -1 * self.yards_lost
            elif self.pass_result == "INT":
                self.is_running_clock = False
                self.def_return = self.get_def_return()
                if self.yard_line + self.pass_dist - self.def_return < 0:
                    self.is_defensive_touchdown = True
                    self.def_return = self.yard_line
                elif self.yard_line + self.pass_dist - self.def_return > 100:
                    if self.yard_line + self.pass_dist > 100:
                        self.is_touchback = True
                        self.def_return = 0
                    else:
                        self.is_offensive_safety = True
                        self.def_return = -1 * (100 - (self.yard_line + self.pass_dist))
                play_gain = self.pass_dist - self.def_return
            elif self.pass_result == "SCRAMBLE":
                if self.is_extra_point == 2:
                    self.play_type = "2pt SCRAMBLE"
                else:
                    self.play_type = "SCRAMBLE"
                self.scramble_result = self.get_scramble_result()
                if self.scramble_result == "GAIN":
                    if not self.is_extra_point:
                        self.is_running_clock = True
                    self.scramble_dist = self.get_scramble_dist()
                    self.tackler = self.get_tackler("BLITZER")
                    if self.yard_line + self.scramble_dist > 100:
                        self.is_running_clock = False
                        self.is_offensive_touchdown = True
                        self.scramble_dist = 100 - self.yard_line
                    elif self.yard_line + self.scramble_dist < 0:
                        self.is_running_clock = False
                        self.is_defensive_safety = True
                        self.scramble_dist = -1*self.yard_line
                    play_gain = self.scramble_dist
                elif self.scramble_result == "LOSS":
                    if not self.is_extra_point:
                        self.is_running_clock = True
                    self.yards_lost = random(1, 10)
                    self.tackler = self.get_tackler("BLITZER")
                    if self.yard_line - self.yards_lost < 0:
                        self.is_running_clock = False
                        self.is_defensive_safety = True
                        self.yards_lost = self.yard_line
                    play_gain = -1 * self.yards_lost
                elif self.scramble_result == "FUMBLE":
                    self.is_running_clock = False
                    self.def_return = self.get_def_return()
                    if self.yard_line - self.def_return < 0:
                        self.is_defensive_touchdown = True
                        self.def_return = self.yard_line
                    elif self.yard_line - self.def_return > 100:
                        self.is_offensive_safety = True
                        self.def_return = -1 * (100 - self.yard_line)
                    play_gain = -1*self.def_return
        elif self.pass_run == "RUN" and self.is_extra_point in {0,2}:
            if self.is_extra_point == 2:
                self.play_type = "2pt RUN"
            else:
                self.play_type = "RUN"
            self.run_result = self.get_run_result()
            if self.run_result == "GAIN":
                if not self.is_extra_point:
                    self.is_running_clock = True
                self.run_dist = self.get_run_dist()
                self.tackler = self.get_tackler("BLITZER")
                if self.yard_line + self.run_dist > 100:
                    self.is_running_clock = False
                    self.is_offensive_touchdown = True
                    self.run_dist = 100 - self.yard_line
                elif self.yard_line + self.run_dist < 0:
                    self.is_running_clock = False
                    self.is_defensive_safety = True
                    self.run_dist = -1 * self.yard_line
                play_gain = self.run_dist
            elif self.run_result == "LOSS":
                if not self.is_extra_point:
                    self.is_running_clock = True
                self.yards_lost = random(1, 7)
                self.tackler = self.get_tackler("BLITZER")
                if self.yard_line - self.yards_lost < 0:
                    self.is_running_clock = False
                    self.is_defensive_safety = True
                    self.yards_lost = self.yard_line
                play_gain = -1 * self.yards_lost
            elif self.run_result == "FUMBLE":
                self.is_running_clock = False
                self.def_return = self.get_def_return()
                if self.yard_line - self.def_return < 0:
                    self.is_defensive_touchdown = True
                    self.def_return = self.yard_line
                elif self.yard_line - self.def_return > 100:
                    self.is_offensive_safety = True
                    self.def_return = -1 * (100 - self.yard_line)
                play_gain = -1*self.def_return
        elif self.will_punt:
            self.play_type = "PUNT"
            self.is_running_clock = False
            self.punt_dist = self.get_punt_dist()
            self.punt_result = self.get_punt_result()
            if self.punt_result == "PIN":
                self.punt_dist = 100 - self.yard_line - random(1,5)
                play_gain = self.punt_dist
            if self.punt_result == "TOUCHBACK":
                self.punt_dist = 101 - self.yard_line
                self.is_touchback = True
                play_gain = 100 - self.yard_line - 20
            if self.punt_result == "RETURN":
                self.punt_return = self.get_punt_return()
                self.tackler = self.get_tackler("SPECIAL TEAMS")
                if self.yard_line + self.punt_dist - self.punt_return > 100:
                    self.is_offensive_safety = True
                    self.punt_return = -1 * (100 - (self.yard_line + self.punt_dist))
                elif self.yard_line + self.punt_dist - self.punt_return < 0:
                    self.is_defensive_touchdown = True
                    self.punt_return = self.yard_line + self.punt_dist
                elif self.check_for_fumble(self.defense.rt):
                    self.def_return = self.get_def_return()
                    cur_yd_line = self.yard_line + self.punt_dist  + self.def_return - self.punt_return
                    if cur_yd_line > 100:
                        self.is_offensive_touchdown = True
                    elif cur_yd_line < 0:
                        self.is_defensive_safety = True
                    play_gain = self.punt_dist + self.def_return - self.punt_return
                play_gain = self.punt_dist - self.punt_return
        elif self.will_kick_field_goal:
            self.is_running_clock = False
            self.play_type = "FIELD GOAL"
            self.field_goal_dist = (100 - self.yard_line) + 17
            self.field_goal_result = self.get_field_goal_result()
            if self.field_goal_result == "MISS":
                play_gain = -7
            else:
                play_gain = 0
        elif self.is_kick_off:
            self.is_running_clock = False
            self.play_type = "KICK OFF"
            if kick == "AUTO":
                self.kick_off_result = self.get_kick_off_result()
            else:
                self.kick_off_result = kick
            if self.kick_off_result == "RETURN":
                self.kick_off_return = self.get_kick_off_return()
                self.tackler = self.get_tackler("SPECIAL TEAMS")
                start_return = random(0,10)
                if start_return + self.kick_off_return > 100:
                    self.is_defensive_touchdown = True
                    self.kick_off_return = 100 - start_return
                elif start_return + self.kick_off_return < 0:
                    self.is_offensive_safety = True
                    self.kick_off_return = -1 * start_return
                elif self.check_for_fumble(self.defense.rt):
                    self.def_return = self.get_def_return()
                    cur_yd_line = start_return  - self.def_return + self.kick_off_return
                    if cur_yd_line < 0:
                        self.is_offensive_touchdown = True
                    elif cur_yd_line > 100:
                        self.is_defensive_safety = True
                    play_gain = start_return + self.kick_off_return - self.def_return
                play_gain = start_return + self.kick_off_return
            elif self.kick_off_result == "TOUCHBACK":
                self.is_touchback = True
                play_gain = 25
            elif self.kick_off_result == "ONSIDE KICK SUCCESS":
                play_gain = random(50, 55)
            elif self.kick_off_result == "ONSIDE KICK FAIL":
                play_gain = random(45, 58)
        elif self.is_extra_point == 1:
            self.is_running_clock = False
            self.play_type = "EXTRA POINT"
            self.field_goal_dist = 32
            self.field_goal_result = self.get_field_goal_result()
            play_gain = 0
        if self.to_go_start > play_gain and self.down_start >= 4:
            self.is_running_clock = False
        self.play_time = c.clock_runoff(self.play_type, play_gain)
        self.play_gain = play_gain
        return play_gain
        
    def do_the_stats_thing(self, game_type, this_year):
        if self.pass_run in ["PASS", "RUN"]:
            for player in self.blockers:
                self.offense.add_stats(player, "SNAPS PLAYED", 1, game_type, this_year)
            for player in self.receivers:
                self.offense.add_stats(player, "SNAPS PLAYED", 1, game_type, this_year)
            for player in self.coverage:
                self.defense.add_stats(player, "SNAPS PLAYED", 1, game_type, this_year)
            for player in self.blitzers:
                self.defense.add_stats(player, "SNAPS PLAYED", 1, game_type, this_year)
            self.offense.add_stats(self.offense.qb1, "SNAPS PLAYED", 1, game_type, this_year)
            if self.pass_run == "PASS":
                for cov in self.coverage:
                    self.defense.add_stats(cov, self.man_zone + " COVERS", 1, game_type, this_year)
            for blitzer in self.blitzers:
                self.defense.add_stats(blitzer, "BLITZES", 1, game_type, this_year)
            for blocker in self.blockers:
                self.offense.add_stats(blocker, self.pass_run + " BLOCK ATTEMPTS", 1, game_type, this_year)
                if not (self.pass_result == "SACK" or self.run_result == "LOSS" or self.scramble_result == "LOSS"):
                    self.offense.add_stats(blocker, self.pass_run + " BLOCKS MADE", 1, game_type, this_year)
                #elif self.pass_result == "SACK" or self.scramble_result == "LOSS":
                    #self.offense.add_stats(blocker, "SACKS ALLOWED", 1, game_type, this_year)
                #else:
                    #self.offense.add_stats(blocker, "RUN STUFFS ALLOWED", 1, game_type, this_year)
        else:
            self.offense.add_stats(self.offense.k, "SNAPS PLAYED", 1, game_type, this_year)
            self.defense.add_stats(self.defense.rt, "SNAPS PLAYED", 1, game_type, this_year)
        if self.pass_run == "PASS" and not self.is_extra_point:
            for rec in self.receivers:
                self.offense.add_stats(rec, "ROUTES RUN", 1, game_type, this_year)
            if self.pass_result == "COMPLETE":
                self.offense.add_stats(self.offense.qb1, "PASS ATTEMPTS", 1, game_type, this_year)
                self.offense.add_stats(self.offense.qb1, "PASS COMPLETIONS", 1, game_type, this_year)
                self.offense.add_stats(self.offense.qb1, "PASS YARDS", self.pass_dist + self.yac, game_type, this_year)
                self.offense.add_stats(self.target, "CATCHES", 1, game_type, this_year)
                self.offense.add_stats(self.target, "RECEIVING YARDS", self.pass_dist + self.yac, game_type, this_year)
                self.offense.add_stats(self.target, "YAC", self.yac, game_type, this_year)
                self.offense.add_stats(self.target, "TARGETS", 1, game_type, this_year)
                self.defense.add_stats(self.tackler, self.man_zone + " COVER TACKLES", 1, game_type, this_year)
                if self.man_zone == "MAN" and not (self.target_defender == "NONE"):
                    self.defense.add_stats(self.target_defender, self.man_zone + " TARGETED", 1, game_type, this_year)
                    self.defense.add_stats(self.target_defender, self.man_zone + " COMPLETIONS ALLOWED", 1, game_type, this_year)
                    self.defense.add_stats(self.target_defender, self.man_zone + " PASS YARDS ALLOWED", self.pass_dist + self.yac, game_type, this_year)
                else:
                    self.defense.add_stats("NONE", self.man_zone + " TARGETED", 1, game_type, this_year)
                    self.defense.add_stats("NONE", self.man_zone + " COMPLETIONS ALLOWED", 1, game_type, this_year)
                    self.defense.add_stats("NONE", self.man_zone + " PASS YARDS ALLOWED", self.pass_dist + self.yac, game_type, this_year)
                if self.is_offensive_touchdown:
                    self.offense.add_stats(self.offense.qb1, "PASS TDS", 1, game_type, this_year)
                    self.offense.add_stats(self.target, "RECEIVING TDS", 1, game_type, this_year)
                    if self.man_zone == "MAN" and not (self.target_defender == "NONE"):
                        self.defense.add_stats(self.target_defender, self.man_zone + " PASS TDS ALLOWED", 1, game_type, this_year)
                    else:
                        self.defense.add_stats("NONE", self.man_zone + " PASS TDS ALLOWED", 1, game_type, this_year)
                if self.is_defensive_safety:
                    self.defense.add_stats(self.tackler, self.man_zone + " COVER SAFETIES", 1, game_type, this_year)
                if self.is_fumble:
                    self.offense.add_stats(self.target, "RECEIVER FUMBLES", 1, game_type, this_year)
                    self.defense.add_stats(self.tackler, self.man_zone + " COVER FF", 1, game_type, this_year)
                    self.defense.add_stats(self.tackler, self.man_zone + " COVER FF RETURN YARDS", self.def_return, game_type, this_year)
                    if self.is_defensive_touchdown:
                        self.defense.add_stats(self.tackler, self.man_zone + " COVER FF TDS", 1, game_type, this_year)
            elif self.pass_result == "INCOMPLETE":
                self.offense.add_stats(self.offense.qb1, "PASS ATTEMPTS", 1, game_type, this_year)
                self.offense.add_stats(self.target, "TARGETS", 1, game_type, this_year)
                if self.dropped:
                    self.offense.add_stats(self.target, "DROPS", 1, game_type, this_year)
                if self.man_zone == "MAN" and not (self.target_defender == "NONE"):
                    self.defense.add_stats(self.target_defender, self.man_zone + " TARGETED", 1, game_type, this_year)
                else:
                    self.defense.add_stats("NONE", self.man_zone + " TARGETED", 1, game_type, this_year)
            elif self.pass_result == "INT":
                self.offense.add_stats(self.offense.qb1, "PASS ATTEMPTS", 1, game_type, this_year)
                self.offense.add_stats(self.offense.qb1, "PASS INTS", 1, game_type, this_year)
                self.offense.add_stats(self.target, "TARGETS", 1, game_type, this_year)
                self.defense.add_stats(self.forced_turnover, self.man_zone + " PICKS", 1, game_type, this_year)
                self.defense.add_stats(self.forced_turnover, self.man_zone + " PICK RETURN YARDS", self.def_return, game_type, this_year)
                if self.man_zone == "MAN" and not (self.target_defender == "NONE"):
                    self.defense.add_stats(self.target_defender, self.man_zone + " TARGETED", 1, game_type, this_year)
                else:
                    self.defense.add_stats("NONE", self.man_zone + " TARGETED", 1, game_type, this_year)
                if self.is_defensive_touchdown:
                    self.defense.add_stats(self.forced_turnover, self.man_zone + " PICK SIXES", 1, game_type, this_year)
            elif self.pass_result == "SACK":
                self.offense.add_stats(self.offense.qb1, "TIMES SACKED", 1, game_type, this_year)
                self.offense.add_stats(self.offense.qb1, "SACKED YARDS", self.yards_lost, game_type, this_year)
                self.defense.add_stats(self.tackler, "BLITZ TACKLES", 1, game_type, this_year)
                self.defense.add_stats(self.tackler, "SACKS", 1, game_type, this_year)
                self.defense.add_stats(self.tackler, "SACK YARDS", self.yards_lost, game_type, this_year)
                if self.is_defensive_safety:
                    self.defense.add_stats(self.tackler, "BLITZ SAFETIES", 1, game_type, this_year)
                if self.is_fumble:
                    self.offense.add_stats(self.offense.qb1, "POCKET FUMBLES", 1, game_type, this_year)
                    self.defense.add_stats(self.tackler, "BLITZ FF", 1, game_type, this_year)
                    self.defense.add_stats(self.tackler, "BLITZ FF RETURN YARDS", self.def_return, game_type, this_year)
                    if self.is_defensive_touchdown:
                        self.defense.add_stats(self.tackler, "BLITZ FF TDS", 1, game_type, this_year)
            elif self.pass_result == "SCRAMBLE":
                if self.scramble_result == "LOSS":
                    self.offense.add_stats(self.offense.qb1, "TIMES SACKED", 1, game_type, this_year)
                    self.offense.add_stats(self.offense.qb1, "SACKED YARDS", self.yards_lost, game_type, this_year)
                    self.defense.add_stats(self.tackler, "BLITZ TACKLES", 1, game_type, this_year)
                    self.defense.add_stats(self.tackler, "SACKS", 1, game_type, this_year)
                    self.defense.add_stats(self.tackler, "SACK YARDS", self.yards_lost, game_type, this_year)
                    if self.is_defensive_safety:
                        self.defense.add_stats(self.tackler, "BLITZ SAFETIES", 1, game_type, this_year)
                elif self.scramble_result == "GAIN":
                    """if self.scramble_dist < 0:
                        self.offense.add_stats(self.offense.qb1, "TIMES SACKED", 1, game_type, this_year)
                        self.offense.add_stats(self.offense.qb1, "SACKED YARDS", -1*self.scramble_dist, game_type, this_year)
                        self.defense.add_stats(self.tackler, "BLITZ TACKLES", 1, game_type, this_year)
                        self.defense.add_stats(self.tackler, "SACKS", 1, game_type, this_year)
                        self.defense.add_stats(self.tackler, "SACK YARDS", -1*self.scramble_dist, game_type, this_year)
                        if self.is_defensive_safety:
                            self.defense.add_stats(self.tackler, "BLITZ SAFETIES", 1, game_type, this_year)
                    else:"""
                    self.offense.add_stats(self.offense.qb1, "CARRIES", 1, game_type, this_year)
                    self.offense.add_stats(self.offense.qb1, "RUSH YARDS", self.scramble_dist, game_type, this_year)
                    if self.tackler in self.blitzers:
                        self.defense.add_stats(self.tackler, "BLITZ TACKLES", 1, game_type, this_year)
                    else:
                        self.defense.add_stats(self.tackler, self.man_zone + " COVER TACKLES", 1, game_type, this_year)
                    if self.is_offensive_touchdown:
                        self.offense.add_stats(self.offense.qb1, "RUSH TDS", 1, game_type, this_year)
                elif self.scramble_result == "FUMBLE":
                    self.offense.add_stats(self.offense.qb1, "RUSH FUMBLES", 1, game_type, this_year)
                    if self.tackler in self.blitzers:
                        self.defense.add_stats(self.forced_turnover, "BLITZ FF", 1, game_type, this_year)
                        self.defense.add_stats(self.forced_turnover, "BLITZ FF RETURN YARDS", self.def_return, game_type, this_year)
                    else:
                        self.defense.add_stats(self.forced_turnover, self.man_zone + " COVER FF", 1, game_type, this_year)
                        self.defense.add_stats(self.forced_turnover, self.man_zone + " COVER FF RETURN YARDS", self.def_return, game_type, this_year)
                    if self.is_defensive_touchdown:
                        if self.tackler in self.blitzers:
                            self.defense.add_stats(self.forced_turnover, "BLITZ FF TDS", 1, game_type, this_year)
                        else:
                            self.defense.add_stats(self.forced_turnover, self.man_zone + " COVER FF TDS", 1, game_type, this_year)
        elif self.pass_run == "RUN" and not self.is_extra_point:
            for cov in self.coverage:
                self.defense.add_stats(cov, "RUN COVERS", 1, game_type, this_year)
            if self.run_result == "GAIN":
                self.offense.add_stats(self.rusher, "CARRIES", 1, game_type, this_year)
                self.offense.add_stats(self.rusher, "RUSH YARDS", self.run_dist, game_type, this_year)
                if self.tackler in self.blitzers:
                    self.defense.add_stats(self.tackler, "BLITZ TACKLES", 1, game_type, this_year)
                else:
                    self.defense.add_stats(self.tackler, "RUN COVER TACKLES", 1, game_type, this_year)
                if self.is_offensive_touchdown:
                    self.offense.add_stats(self.rusher, "RUSH TDS", 1, game_type, this_year)
                if self.run_dist < 0:
                    if self.tackler in self.blitzers:
                        self.defense.add_stats(self.tackler, "BLITZ RUN STUFFS", 1, game_type, this_year)
                        self.defense.add_stats(self.tackler, "BLITZ RUN STUFF YARDS", -1*self.run_dist, game_type, this_year)
                    else:
                        self.defense.add_stats(self.tackler, "RUN COVER RUN STUFFS", 1, game_type, this_year)
                        self.defense.add_stats(self.tackler, "RUN COVER RUN STUFF YARDS", -1*self.run_dist, game_type, this_year)
                    if self.is_defensive_safety:
                        if self.tackler in self.blitzers:
                            self.defense.add_stats(self.tackler, "BLITZ SAFETIES", 1, game_type, this_year)
                        else:
                            self.defense.add_stats(self.tackler, "RUN COVER SAFETIES", 1, game_type, this_year)
            elif self.run_result == "LOSS":
                self.offense.add_stats(self.rusher, "CARRIES", 1, game_type, this_year)
                self.offense.add_stats(self.rusher, "RUSH YARDS", -1*self.yards_lost, game_type, this_year)
                self.defense.add_stats(self.tackler, "BLITZ TACKLES", 1, game_type, this_year)
                self.defense.add_stats(self.tackler, "BLITZ RUN STUFFS", 1, game_type, this_year)
                self.defense.add_stats(self.tackler, "BLITZ RUN STUFF YARDS", self.yards_lost, game_type, this_year)
                if self.is_defensive_safety:
                    self.defense.add_stats(self.tackler, "BLITZ SAFETIES", 1, game_type, this_year)
            elif self.run_result == "FUMBLE":
                self.offense.add_stats(self.rusher, "CARRIES", 1, game_type, this_year)
                self.offense.add_stats(self.rusher, "RUSH FUMBLES", 1, game_type, this_year)
                self.defense.add_stats(self.forced_turnover, "BLITZ FF", 1, game_type, this_year)
                self.defense.add_stats(self.forced_turnover, "BLITZ FF RETURN YARDS", self.def_return, game_type, this_year)
                if self.is_defensive_touchdown:
                    self.defense.add_stats(self.forced_turnover, "BLITZ FF TDS", 1, game_type, this_year)
        elif self.is_extra_point:
            if self.is_extra_point == 1:
                self.offense.add_stats(self.offense.k, "XP ATTEMPTS", 1, game_type, this_year)
                if self.field_goal_result == "MADE":
                    self.offense.add_stats(self.offense.k, "XP MADE", 1, game_type, this_year)
            elif self.is_extra_point == 2:
                if self.play_type == "2pt PASS":
                    if self.pass_result in {"INT", "INCOMPLETE", "COMPLETE"}:
                        self.offense.add_stats(self.offense.qb1, "2pt PASS ATTEMPTS", 1, game_type, this_year)
                        self.offense.add_stats(self.target, "2pt TARGETS", 1, game_type, this_year)
                    if self.pass_result == "COMPLETE" and self.is_offensive_touchdown:
                        self.offense.add_stats(self.offense.qb1, "2pt PASS SUCCESS", 1, game_type, this_year)
                        self.offense.add_stats(self.target, "2pt CATCH SUCCESS", 1, game_type, this_year)
                elif self.play_type == "2pt SCRAMBLE":
                    self.offense.add_stats(self.offense.qb1, "2pt CARRIES", 1, game_type, this_year)
                    if self.is_offensive_touchdown:
                        self.offense.add_stats(self.offense.qb1, "2pt RUSH SUCCESS", 1, game_type, this_year)
                elif self.play_type == "2pt RUN":
                    self.offense.add_stats(self.rusher, "2pt CARRIES", 1, game_type, this_year)
                    if self.is_offensive_touchdown:
                        self.offense.add_stats(self.rusher, "2pt RUSH SUCCESS", 1, game_type, this_year)
        elif self.is_kick_off:
            # add punt and kick defense stats somewhere/everywhere
            if self.kick_off_result == "TOUCHBACK":
                self.offense.add_stats(self.offense.k, "KICK OFF ATTEMPTS", 1, game_type, this_year)
                self.offense.add_stats(self.offense.k, "KICK OFF TB", 1, game_type, this_year)
                self.defense.add_stats(self.defense.rt, "KICK RETURN TB", 1, game_type, this_year)
            elif self.kick_off_result == "RETURN":
                self.offense.add_stats(self.offense.k, "KICK OFF ATTEMPTS", 1, game_type, this_year)
                self.offense.add_stats(self.tackler, "KICK TACKLES", 1, game_type, this_year)
                self.defense.add_stats(self.defense.rt, "KICK RETURNS", 1, game_type, this_year)
                self.defense.add_stats(self.defense.rt, "KICK RETURN YARDS", self.kick_off_return, game_type, this_year)
                if self.is_defensive_touchdown:
                    self.defense.add_stats(self.defense.rt, "KICK RETURN TDS", 1, game_type, this_year)
                elif self.is_offensive_safety:
                    self.offense.add_stats(self.tackler, "KICK SAFETIES", 1, game_type, this_year)
                if self.is_fumble:
                    self.defense.add_stats(self.defense.rt, "KICK RETURN FUMBLES", 1, game_type, this_year)
                    self.offense.add_stats(self.tackler, "KICK FF", 1, game_type, this_year)
                    self.offense.add_stats(self.tackler, "KICK FF RETURN YARDS", self.def_return, game_type, this_year)
                    if self.is_offensive_touchdown:
                        self.offense.add_stats(self.tackler, "KICK FF TDS", 1, game_type, this_year)
            elif self.kick_off_result == "ONSIDE KICK SUCCESS":
                self.offense.add_stats(self.offense.k, "ONSIDE KICK ATTEMPTS", 1, game_type, this_year)
                self.offense.add_stats(self.offense.k, "ONSIDE KICK SUCCESS", 1, game_type, this_year)
            elif self.kick_off_result == "ONSIDE KICK FAIL":
                self.offense.add_stats(self.offense.k, "ONSIDE KICK ATTEMPTS", 1, game_type, this_year)
        elif self.will_punt:
            self.offense.add_stats(self.offense.k, "PUNTS", 1, game_type, this_year)
            if self.punt_result == "PIN":
                self.offense.add_stats(self.offense.k, "PUNT PINS", 1, game_type, this_year)
                self.offense.add_stats(self.offense.k, "PUNT YARDS", self.punt_dist, game_type, this_year)
            elif self.punt_result == "TOUCHBACK":
                self.offense.add_stats(self.offense.k, "PUNT TB", 1, game_type, this_year)
                self.offense.add_stats(self.offense.k, "PUNT YARDS", self.punt_dist, game_type, this_year)
                self.defense.add_stats(self.defense.rt, "PUNT RETURN TB", 1, game_type, this_year)
            elif self.punt_result == "RETURN":
                self.offense.add_stats(self.offense.k, "PUNT YARDS", self.punt_dist, game_type, this_year)
                self.offense.add_stats(self.tackler, "PUNT TACKLES", 1, game_type, this_year)
                self.defense.add_stats(self.defense.rt, "PUNT RETURNS", 1, game_type, this_year)
                self.defense.add_stats(self.defense.rt, "PUNT RETURN YARDS", self.punt_return, game_type, this_year)
                if self.is_defensive_touchdown:
                    self.defense.add_stats(self.defense.rt, "PUNT RETURN TDS", 1, game_type, this_year)
                elif self.is_offensive_safety:
                    self.offense.add_stats(self.tackler, "PUNT SAFETIES", 1, game_type, this_year)
                if self.is_fumble:
                    self.defense.add_stats(self.defense.rt, "PUNT RETURN FUMBLES", 1, game_type, this_year)
                    self.offense.add_stats(self.tackler, "PUNT FF", 1, game_type, this_year)
                    self.offense.add_stats(self.tackler, "PUNT FF RETURN YARDS", self.def_return, game_type, this_year)
                    if self.is_offensive_touchdown:
                        self.offense.add_stats(self.tackler, "PUNT FF TDS", 1, game_type, this_year)
        elif self.will_kick_field_goal:
            self.offense.add_stats(self.offense.k, "FG ATTEMPTS", 1, game_type, this_year)
            if self.field_goal_result == "MADE":
                self.offense.add_stats(self.offense.k, "FG MADE", 1, game_type, this_year)
                self.offense.add_stats(self.offense.k, "FG DISTANCE", self.field_goal_dist, game_type, this_year)
        
    def get_blitzers(self, formation, num_blitzers):
        blitzers = [self.defense.dl1, self.defense.dl2, self.defense.dl3]
        other_players = []
        if formation == "goal line":
            blitzers.append(self.defense.dl4)
            blitzers.append(self.defense.dl5)
            blitzers.append(self.defense.dl6)
            other_players = [self.defense.lb4, self.defense.lb3, self.defense.lb2, self.defense.lb1, self.defense.db2, self.defense.db1]
        elif formation == "3-4":
            other_players = [self.defense.lb4, self.defense.lb3, self.defense.lb2, self.defense.lb1, self.defense.db4, self.defense.db3, self.defense.db2, self.defense.db1]
        elif formation == "4-3":
            blitzers.append(self.defense.dl4)
            other_players = [self.defense.lb3, self.defense.lb2, self.defense.lb1, self.defense.db4, self.defense.db3, self.defense.db2, self.defense.db1]
        elif formation == "nickel":
            blitzers.append(self.defense.dl4)
            other_players = [self.defense.lb2, self.defense.lb1, self.defense.db5, self.defense.db4, self.defense.db3, self.defense.db2, self.defense.db1]
        elif formation == "dime":
            blitzers.append(self.defense.dl4)
            other_players = [self.defense.lb1, self.defense.db6, self.defense.db5, self.defense.db4, self.defense.db3, self.defense.db2, self.defense.db1]
        elif formation == "quarter":
            other_players = [self.defense.lb2, self.defense.lb1, self.defense.db6, self.defense.db5, self.defense.db4, self.defense.db3, self.defense.db2, self.defense.db1]
        for i in range(0,num_blitzers):
            blitzers.append(other_players[i])
        return blitzers
        
    def get_coverage(self, formation, blitzers):
        coverage = [self.defense.db1, self.defense.db2]
        if formation == "goal line":
            coverage.append(self.defense.lb1)
            coverage.append(self.defense.lb2)
            coverage.append(self.defense.lb3)
            coverage.append(self.defense.lb4)
        elif formation == "3-4":
            coverage.append(self.defense.db3)
            coverage.append(self.defense.db4)
            coverage.append(self.defense.lb1)
            coverage.append(self.defense.lb2)
            coverage.append(self.defense.lb3)
            coverage.append(self.defense.lb4)
        elif formation == "4-3":
            coverage.append(self.defense.db3)
            coverage.append(self.defense.db4)
            coverage.append(self.defense.lb1)
            coverage.append(self.defense.lb2)
            coverage.append(self.defense.lb3)
        elif formation == "nickel":
            coverage.append(self.defense.db3)
            coverage.append(self.defense.db4)
            coverage.append(self.defense.db5)
            coverage.append(self.defense.lb1)
            coverage.append(self.defense.lb2)
        elif formation == "dime":
            coverage.append(self.defense.db3)
            coverage.append(self.defense.db4)
            coverage.append(self.defense.db5)
            coverage.append(self.defense.db6)
            coverage.append(self.defense.lb1)
        elif formation == "quarter":
            coverage.append(self.defense.db3)
            coverage.append(self.defense.db4)
            coverage.append(self.defense.db5)
            coverage.append(self.defense.db6)
            coverage.append(self.defense.lb1)
            coverage.append(self.defense.lb2)
        for i in range(0,blitzers):
            coverage.remove(coverage[len(coverage) - 1])
        return coverage
        
    def get_blockers(self, formation, pass_run, rb = "AUTO"):
        blockers = [self.offense.ol1, self.offense.ol2, self.offense.ol3, self.offense.ol4, self.offense.ol5]
        if formation == "goal line":
            blockers.append(self.offense.te2)
            if pass_run == "RUN":
                if not rb == "AUTO":
                    self.rusher = rb
                elif random(0,100) < self.offense.rb1_chance:
                    self.rusher = self.offense.rb1
                else:
                    self.rusher = self.offense.rb2
                blockers.append(self.offense.te1)
                if self.rusher == self.offense.rb1:
                    blockers.append(self.offense.rb2)
                else:
                    blockers.append(self.offense.rb1)
        elif formation == "i":
            blockers.append(self.offense.te1)
            if pass_run == "RUN":
                if not rb == "AUTO":
                    self.rusher = rb
                elif random(0,100) < self.offense.rb1_chance:
                    self.rusher = self.offense.rb1
                else:
                    self.rusher = self.offense.rb2
                if self.rusher == self.offense.rb1:
                    blockers.append(self.offense.rb2)
                else:
                    blockers.append(self.offense.rb1)
        elif formation == "singleback" and pass_run == "RUN":
            if not rb == "AUTO":
                self.rusher = rb
            elif random(0,100) < self.offense.rb1_chance:
                self.rusher = self.offense.rb1
            else:
                self.rusher = self.offense.rb2
            blockers.append(self.offense.te1)
        elif formation == "spread" and pass_run == "RUN":
            if not rb == "AUTO":
                self.rusher = rb
            elif random(0,100) < self.offense.rb1_chance:
                self.rusher = self.offense.rb1
            else:
                self.rusher = self.offense.rb2
            blockers.append(self.offense.te1)
        return blockers
            
        
    def get_receivers(self, formation, pass_run):
        receivers = [self.offense.wr1]
        if formation == "goal line":
            receivers.append(self.offense.rb1)
            if pass_run == "PASS":
                receivers.append(self.offense.te1)
                receivers.append(self.offense.rb2)
        elif formation == "i":
            receivers.append(self.offense.wr2)
            receivers.append(self.offense.rb1)
            if pass_run == "PASS":
                receivers.append(self.offense.rb2)
        elif formation == "singleback":
            receivers.append(self.offense.wr2)
            receivers.append(self.offense.wr3)
            receivers.append(self.offense.rb1)
            if pass_run == "PASS":
                receivers.append(self.offense.te1)
        elif formation == "spread":
            receivers.append(self.offense.wr2)
            receivers.append(self.offense.wr3)
            receivers.append(self.offense.rb1)
            if pass_run == "PASS":
                receivers.append(self.offense.te1)
        return receivers
            
        
    def get_off_formation(self):
        global c
        play = self.offense.offense_formation_chance
        rand = random(0,100)
        if rand < play[c.goal_line]:
            return "goal line"
        elif rand < play[c.i] + play[c.goal_line]:
            return "i"
        elif rand < play[c.singleback] + play[c.i] + play[c.goal_line]:
            return "singleback"
            #elif rand < play[c.spread] + play[c.singleback] + play[c.i] + play[c.goal_line]:
        else:
            return "spread"
            
        
    def get_def_formation(self):
        global c
        play = self.defense.defense_formation_chance
        rand = random(0,100)
        if rand < play[c.goal_line]:
            return "goal line"
        elif rand < play[c.three_four] + play[c.goal_line]:
            return "3-4"
        elif rand < play[c.four_three] + play[c.three_four] + play[c.goal_line]:
            return "4-3"
        elif rand < play[c.nickel] + play[c.four_three] + play[c.three_four] + play[c.goal_line]:
            return "nickel"
        elif rand < play[c.dime] + play[c.nickel] + play[c.four_three] + play[c.three_four] + play[c.goal_line]:
            return "dime"
            #elif rand < play[c.quarter] + play[c.dime] + play[c.nickel] + play[c.four_three] + play[c.three_four] + play[c.goal_line]:
        else:
            return "quarter"
        
    def get_pass_run(self):
        rand = random(0,100)
        if rand < self.offense.pass_chance:
            return "PASS"
        return "RUN"
        
    def get_man_zone(self):
        rand = random(0,100)
        if rand < self.defense.man_chance:
            return "MAN"
        return "ZONE"
        
    def get_num_blitzers(self):
        rand = random(0,100)
        blitzers = self.defense.blitzers_chance
        if rand < blitzers[0]:
            return 0
        elif rand < blitzers[1] + blitzers[0]:
            return 1
        elif rand < blitzers[2] + blitzers[1] + blitzers[0]:
            return 2
        elif rand < blitzers[3] + blitzers[2] + blitzers[1] + blitzers[0]:
            return 3
        
    def get_pass_result(self):
        global c
        scr_chance = self.offense.scramble_chance
        if random(0,100) < scr_chance:
            return "SCRAMBLE"
        sack_chance = self.get_sack_chance()
        if random(0,100) < sack_chance:
            return "SACK"
        if self.man_zone == "ZONE":
            int_chance = 0
            catch_chance = 0
            for cov in self.coverage:
                int_chance += cov.int_catch_chance
                catch_chance += cov.complete_chance_allowed
            int_chance /= len(self.coverage)
            catch_chance /= len(self.coverage)
            int_boost = 0
            catch_boost = 0
            if self.pass_dist > 10:
                if self.offense.qb1.dist_effect_int == "GOOD":
                    int_boost = random(-0.5,0.5)*c.int_jump*(self.pass_dist - 10)/5
                if self.offense.qb1.dist_effect_int == "NORMAL":
                    int_boost = random(0.5,2.5)*c.int_jump*(self.pass_dist - 10)/5
                if self.offense.qb1.dist_effect_int == "BAD":
                    int_boost = random(2.5,5)*c.int_jump*(self.pass_dist - 10)/5
                if self.offense.qb1.dist_effect_complete == "GOOD":
                    catch_boost = random(-0.5, 0.5)*c.complete_jump*(self.pass_dist - 10)/5
                if self.offense.qb1.dist_effect_complete == "NORMAL":
                    catch_boost = random(-2.5,-0.5)*c.complete_jump*(self.pass_dist - 10)/5
                if self.offense.qb1.dist_effect_complete == "BAD":
                    catch_boost = random(-5,-2.5)*c.complete_jump*(self.pass_dist - 10)/5
            int_chance = (int_chance + self.offense.qb1.int_chance)/2 + int_boost
            if self.target.catch_boost == "GOOD":
                catch_boost += random(0,2)
            catch_chance = (catch_chance + self.offense.qb1.complete_chance)/2 + catch_boost
            rand = random(0,100)
            if rand < int_chance:
                self.forced_turnover = self.get_interceptor()
                return "INT"
            elif rand < int_chance + catch_chance:
                drop_chance = self.target.drop_chance
                drop_boost = 0
                if self.target.dist_effect_drop == "GOOD":
                    drop_boost = random(-0.5,0.5)*c.complete_jump*(self.pass_dist - 10)/5
                if self.target.dist_effect_drop == "NORMAL":
                    drop_boost = random(0.5,2.5)*c.complete_jump*(self.pass_dist - 10)/5
                if self.target.dist_effect_drop == "GOOD":
                    drop_boost = random(2.5,5)*c.complete_jump*(self.pass_dist - 10)/5
                if random(0,100) < drop_chance + drop_boost:
                    self.dropped = True
                    return "INCOMPLETE"
                return "COMPLETE"
            else:
                return "INCOMPLETE"
        elif self.man_zone == "MAN":
            int_chance = 0
            catch_chance = 0
            self.target_defender = self.get_defender()
            if len(self.coverage) > len(self.receivers):
                i = len(self.receivers)
                for x in range(i, len(self.coverage)):
                    int_chance += self.coverage[x].int_catch_chance
                    catch_chance += 1 - self.coverage[x].complete_chance_allowed
            if self.target_defender == "NONE":
                int_chance = 0
                catch_chance = 100
            else:
                int_chance /= 2*len(self.receivers)
                int_chance += self.target_defender.int_catch_chance
                catch_chance /= 2*len(self.receivers)
                catch_chance = self.target_defender.complete_chance_allowed - catch_chance
            int_boost = 0
            catch_boost = 0
            if self.pass_dist > 10:
                if self.offense.qb1.dist_effect_int == "GOOD":
                    int_boost = random(-0.5,0.5)*c.int_jump*(self.pass_dist - 10)/5
                if self.offense.qb1.dist_effect_int == "NORMAL":
                    int_boost = random(0.5,2.5)*c.int_jump*(self.pass_dist - 10)/5
                if self.offense.qb1.dist_effect_int == "BAD":
                    int_boost = random(2.5,5)*c.int_jump*(self.pass_dist - 10)/5
                if self.offense.qb1.dist_effect_complete == "GOOD":
                    catch_boost = random(-0.5,0.5)*c.complete_jump*(self.pass_dist - 10)/5
                if self.offense.qb1.dist_effect_complete == "NORMAL":
                    catch_boost = random(-2.5,-0.5)*c.complete_jump*(self.pass_dist - 10)/5
                if self.offense.qb1.dist_effect_complete == "BAD":
                    catch_boost = random(-5,-2.5)*c.complete_jump*(self.pass_dist - 10)/5
            int_chance = (int_chance + self.offense.qb1.int_chance)/2 + int_boost
            if self.target.catch_boost == "GOOD":
                catch_boost += random(0,2)
            catch_chance = (catch_chance + self.offense.qb1.complete_chance)/2 + catch_boost
            rand = random(0,100)
            if rand < int_chance:
                self.forced_turnover = self.get_interceptor()
                return "INT"
            elif rand < int_chance + catch_chance:
                drop_chance = self.target.drop_chance
                drop_boost = 0
                if self.target.dist_effect_drop == "GOOD":
                    drop_boost = random(-0.5,0.5)*c.complete_jump*(self.pass_dist - 10)/5
                if self.target.dist_effect_drop == "NORMAL":
                    drop_boost = random(0.5,2.5)*c.complete_jump*(self.pass_dist - 10)/5
                if self.target.dist_effect_drop == "GOOD":
                    drop_boost = random(2.5,5)*c.complete_jump*(self.pass_dist - 10)/5
                if random(0,100) < drop_chance + drop_boost:
                    self.dropped = True
                    return "INCOMPLETE"
                return "COMPLETE"
            else:
                return "INCOMPLETE"
        
    def get_yac(self):
        if self.man_zone == "MAN":
            if self.target_defender == "NONE":
                mean = self.target.YAC + 10
                stdev = self.target.stdev_YAC
            else:
                mean = (self.target.YAC + self.target_defender.YAC_allowed)/2
                stdev = (self.target.stdev_YAC + self.target_defender.stdev_YAC_allowed)/2
            return max(random_skew(mean, stdev), -1)
        else:
            mean = 0
            for cov in self.coverage:
                mean += cov.YAC_allowed
            mean /= len(self.coverage)
            mean = (mean + self.target.YAC)/2
            return max(random_skew(mean, self.target.stdev_YAC), -1)
        
    def get_pass_distance(self):
        if self.man_zone == "MAN":
            if self.get_defender() == "NONE":
                mean = (self.target.target_dist + self.offense.qb1.air_yds_throw)/2
                stdev = (self.target.stdev_target_dist + self.offense.qb1.stdev_air_yds_throw)/2
            else:
                mean = (self.get_defender().air_yds_allowed + self.target.target_dist + self.offense.qb1.air_yds_throw)/3
                stdev = (self.get_defender().stdev_air_yds_allowed + self.target.stdev_target_dist + self.offense.qb1.stdev_air_yds_throw)/3
        else:
            def_mean = 0
            def_std = 0
            for defender in self.coverage:
                def_mean += defender.air_yds_allowed
                def_std += defender.stdev_air_yds_allowed
            def_mean /= len(self.coverage)
            def_std /= len(self.coverage)
            mean = (def_mean + self.target.target_dist + self.offense.qb1.air_yds_throw)/3
            stdev = (def_std + self.target.stdev_target_dist + self.offense.qb1.stdev_air_yds_throw)/3
        return max(random_skew(mean, stdev), -1)
        
    def get_run_result(self):
        # loss, fumble, gain
        fum = self.rusher.fumble_chance
        def_fum = 0
        def_gain_chance = 0
        for blitzer in self.blitzers:
            def_fum += blitzer.ff_chance
            def_gain_chance += blitzer.blocked_chance
        def_fum /= len(self.blitzers)
        def_gain_chance /= len(self.blitzers)
        fum = (fum + def_fum)/2
        gain_chance = 0
        for blocker in self.blockers:
            gain_chance += blocker.block_chance
        gain_chance /= len(self.blockers)
        gain_chance = (gain_chance + def_gain_chance)/2 + len(self.blockers) - (5/4)*len(self.blitzers)
        rand = random(0,100)
        if rand < fum:
            self.forced_turnover = self.get_fum_forcer()
            return "FUMBLE"
        elif rand < fum + gain_chance:
            return "GAIN"
        else:
            return "LOSS"
        
    def get_run_dist(self):
        mean = self.rusher.run_dist
        stdev = self.rusher.stdev_run_dist
        def_mean = 0
        for cov in self.coverage:
            def_mean += cov.run_dist_allowed
        for blitzer in self.blitzers:
            def_mean += blitzer.run_dist_allowed
        def_mean /= 11
        mean = (mean + def_mean)/2
        return max(random_skew(mean, stdev), -1)
        
    def get_target(self):
        global c
        # for the pass
        wrs = 0
        tes = 0
        rbs = 0
        for receiver in self.receivers:
            if receiver.position == "WR":
                wrs += 1
            if receiver.position == "TE":
                tes += 1
            if receiver.position == "RB":
                rbs += 1
        catch_sum = 0
        if wrs >= 1:
            catch_sum += self.offense.fave_targets[c.wr1]
        if wrs >= 2:
            catch_sum += self.offense.fave_targets[c.wr2]
        if wrs >= 3:
            catch_sum += self.offense.fave_targets[c.wr3]
        if tes >= 1:
            catch_sum += self.offense.fave_targets[c.te1]
        if tes >= 2:
            catch_sum += self.offense.fave_targets[c.te2]
        if rbs >= 1:
            catch_sum += self.offense.fave_targets[c.rb1]
        if rbs >= 2:
            catch_sum += self.offense.fave_targets[c.rb2]
        rand = random(0,catch_sum)
        catch_sum = 0
        if wrs >= 1:
            catch_sum += self.offense.fave_targets[c.wr1]
            if rand < catch_sum:
                return self.offense.wr1
        if wrs >= 2:
            catch_sum += self.offense.fave_targets[c.wr2]
            if rand < catch_sum:
                return self.offense.wr2
        if wrs >= 3:
            catch_sum += self.offense.fave_targets[c.wr3]
            if rand < catch_sum:
                return self.offense.wr3
        if tes >= 1:
            catch_sum += self.offense.fave_targets[c.te1]
            if rand < catch_sum:
                return self.offense.te1
        if tes >= 2:
            catch_sum += self.offense.fave_targets[c.te2]
            if rand < catch_sum:
                return self.offense.te2
        if rbs >= 1:
            catch_sum += self.offense.fave_targets[c.rb1]
            if rand < catch_sum:
                return self.offense.rb1
        if rbs >= 2:
            catch_sum += self.offense.fave_targets[c.rb2]
            if rand < catch_sum:
                return self.offense.rb2
    
    def get_def_return(self):
        mean = self.forced_turnover.def_return_dist
        stdev = self.forced_turnover.stdev_def_return_dist
        return max(random_skew(mean, stdev), -1)
        
    def get_fum_forcer(self):
        fum = 0
        forcer = self.blitzers[0]
        for cov in self.coverage:
            fum += cov.ff_chance
        for blitzer in self.blitzers:
            fum += blitzer.ff_chance
        rand = random(0,fum)
        fum = 0
        for cov in self.coverage:
            fum += cov.ff_chance
            if rand < fum:
                return cov
        for blitzer in self.blitzers:
            fum += blitzer.ff_chance
            if rand < fum:
                return blitzer
        return forcer
            
    def get_sack_chance(self):
        off_chance = 0
        def_chance = 0
        for blocker in self.blockers:
            off_chance += blocker.sack_allowed_chance
        off_chance /= len(self.blockers)
        for blitzer in self.blitzers:
            def_chance += blitzer.sack_chance
        def_chance /= len(self.blockers)
        sack_chance = (off_chance + def_chance)/2 + (len(self.blitzers) - len(self.blockers)) + (self.pass_dist - 5)*0.1
        return sack_chance
    
    def get_defender(self):
        i = 0
        while self.receivers[i] != self.target:
            i += 1
        if len(self.coverage) > i:
            return self.coverage[i]
        return "NONE"
    
    def get_scramble_result(self):
        # gain, loss, fumble
        sack = self.get_sack_chance()*0.9
        fum = 0
        for blitzer in self.blitzers:
            fum += blitzer.ff_chance
        fum /= len(self.blitzers)
        fum = (fum + self.offense.qb1.fumble_chance)/2
        rand = random(0,100)
        if rand < sack:
            return "LOSS"
        elif rand < sack + fum:
            self.forced_turnover = self.get_fum_forcer()
            return "FUMBLE"
        else:
            return "GAIN"
        
    def get_scramble_dist(self):
        mean = self.offense.qb1.run_dist
        stdev = self.offense.qb1.stdev_run_dist
        return max(random_skew(mean, stdev), -1)
        
    def get_interceptor(self):
        interceptor = self.coverage[0]
        if self.man_zone == "MAN":
            if self.target_defender == "NONE":
                return self.coverage[0]
            return self.target_defender
        if self.man_zone == "ZONE":
            int_chance = 0
            for cov in self.coverage:
                int_chance += cov.int_catch_chance
            rand = random(0, int_chance)
            int_chance = 0
            for cov in self.coverage:
                int_chance += cov.int_catch_chance
                if rand < int_chance:
                    return cov
        return interceptor
                
    def should_punt(self, down, to_go, yard_line, quarter, seconds_left, offense_score, defense_score):
        if down == 4:
            if self.will_kick_field_goal:
                return False
            if to_go < self.offense.fourth_down_attempt_dist:
                if random(0,100) < self.offense.fourth_down_attempt_chance:
                    return False
            if offense_score < defense_score and quarter >= 4 and seconds_left < 180:
                return False
            return True
        return False
        
    def should_kick_field_goal(self, down, to_go, yard_line, quarter, seconds_left, offense_score, defense_score):
        if 100 - yard_line + 17 < self.offense.k.fg_range:
            if (quarter == 2 or (quarter >= 4 and offense_score + 3 >= defense_score))and seconds_left <= 30:
                return True
            if down == 4:
                if to_go < self.offense.fourth_down_attempt_dist:
                    if random(0,100) < self.offense.fourth_down_attempt_chance:
                        return False
                if quarter >= 4 and offense_score + 3 < defense_score and seconds_left < 180:
                    return False
                return True
        return False
    
    def get_punt_dist(self):
        return random_skew(self.offense.k.punt_dist, self.offense.k.stdev_punt_dist)
        
    def get_punt_result(self):
        if 100 - self.yard_line - self.punt_dist < 10:
            if random(0,100) < self.offense.k.pin_chance:
                return "PIN"
            else:
                return "TOUCHBACK"
        elif self.yard_line + self.punt_dist < 100:
            return "RETURN"
        return "TOUCHBACK"
        
    def get_punt_return(self):
        rand = random(0,1)
        if rand < 0.2:
            return 0
        elif rand < 0.7:
            return random(0,10)
        else:
            return max(random_skew(self.defense.rt.kick_return_dist/2, self.defense.rt.stdev_kick_return_dist), -1)
        
    def get_field_goal_result(self):
        if self.offense.k.fg_range < self.field_goal_dist:
            return "MISS"
        if random(0,100) < self.offense.k.fg_made_chance - 0.5*(self.field_goal_dist - 33):
            return "MADE"
        return "MISS"
    
    def get_kick_off_result(self):
        if self.is_onside_kick:
            if random(0, 100) < self.offense.k.onside_kick_chance:
                return "ONSIDE KICK SUCCESS"
            return "ONSIDE KICK FAIL"
        tb_chance = (self.offense.k.touchback_forced_chance + self.defense.rt.touchback_chance)/2
        if random(0,100) < tb_chance:
            return "TOUCHBACK"
        return "RETURN"
        
    def get_kick_off_return(self):
        return max(random_skew(self.defense.rt.kick_return_dist, self.defense.rt.stdev_kick_return_dist), -1)
    
    def get_tackler(self, job):
        backup = self.blitzers[0]
        tackle = 0
        rand = 0
        if job == "BLITZER":
            if self.pass_run == "PASS":
                tackle = 0
                for blitzer in self.blitzers:
                    tackle += blitzer.sack_chance
                rand = random(0, tackle)
                tackle = 0
                for blitzer in self.blitzers:
                    tackle += blitzer.sack_chance
                    if rand < tackle:
                        return blitzer
            else:
                tackle = 0
                for blitzer in self.blitzers:
                    if blitzer.run_dist_allowed <= 1:
                        tackle += 1
                    else:
                        tackle += 1/blitzer.run_dist_allowed
                rand = random(0, tackle)
                tackle = 0
                for blitzer in self.blitzers:
                    if blitzer.run_dist_allowed <= 1:
                        tackle += 1
                    else:
                        tackle += 1/blitzer.run_dist_allowed
                    if rand < tackle:
                        return blitzer
        elif job == "COVERAGE":
            if self.pass_run == "PASS" and self.man_zone == "MAN" and not (self.target_defender == "NONE"):
                if self.target_defender.YAC_allowed <= 1:
                    tackle += 1
                else:
                    tackle = 1/self.target_defender.YAC_allowed
                for cov in self.coverage:
                    if cov.YAC_allowed <= 1:
                        tackle += 1/10.0
                    else:
                        tackle += (1/cov.YAC_allowed)/10
                rand = random(0,tackle)
                if self.target_defender.YAC_allowed <= 1:
                    tackle += 1
                else:
                    tackle = 1/self.target_defender.YAC_allowed
                if rand < tackle:
                    return self.target_defender
                for cov in self.coverage:
                    if cov.YAC_allowed <= 1:
                        tackle += 1/10.0
                    else:
                        tackle += (1/cov.YAC_allowed)/10
                    if rand < tackle:
                        return cov
            else:
                tackle = 0
                for cov in self.coverage:
                    if cov.YAC_allowed <= 1:
                        tackle += 1
                    else:
                        tackle += 1/cov.YAC_allowed
                rand = random(0,tackle)
                tackle = 0
                for cov in self.coverage:
                    if cov.YAC_allowed <= 1:
                        tackle += 1
                    else:
                        tackle += 1/cov.YAC_allowed
                    if rand < tackle:
                        return cov
        elif job == "SPECIAL TEAMS":
            tackle = 0
            if self.offense.db1.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.db1.YAC_allowed
            if self.offense.db2.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.db2.YAC_allowed
            if self.offense.db3.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.db3.YAC_allowed
            if self.offense.db4.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.db4.YAC_allowed
            if self.offense.lb1.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.lb1.YAC_allowed
            if self.offense.lb2.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.lb2.YAC_allowed
            rand = random(0, tackle)
            tackle = 0
            if self.offense.db1.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.db1.YAC_allowed
            if rand < tackle:
                return self.offense.db1
            if self.offense.db2.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.db2.YAC_allowed
            if rand < tackle:
                return self.offense.db2
            if self.offense.db3.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.db3.YAC_allowed
            if rand < tackle:
                return self.offense.db3
            if self.offense.db4.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.db4.YAC_allowed
            if rand < tackle:
                return self.offense.db4
            if self.offense.lb1.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.lb1.YAC_allowed
            if rand < tackle:
                return self.offense.lb1
            if self.offense.lb2.YAC_allowed <= 1:
                tackle += 1
            else:
                tackle += 1/self.offense.lb2.YAC_allowed
            if rand < tackle:
                return self.offense.lb2
        println("oof error " + job)
        return backup
    
    def check_for_fumble(self, ballcarrier):
        fum_chance = (self.tackler.ff_chance + ballcarrier.fumble_chance)/2
        if random(0,100) < fum_chance:
            self.is_fumble = True
            self.forced_turnover = self.tackler
            return True
        
    def create_injuries(self):
        players = []
        if self.pass_run == "PASS" or self.pass_run == "RUN":
            players = [self.offense.qb1]
            players.extend(self.blockers)
            players.extend(self.receivers)
            players.extend(self.blitzers)
            players.extend(self.coverage)
        elif self.is_kick_off or self.will_punt:
            players = [self.offense.k, self.defense.rt]
        else:
            players = [self.offense.k]
        for player in players:
            try:
                if random(0,100) < player.injury_chance:
                    self.injury = True
                    self.injured = player
                    player.get_injured()
            except:
                pass

################################################################################PLAY CLASS###########################################################################################
################################################################################PLAY CLASS###########################################################################################
################################################################################PLAY CLASS###########################################################################################
################################################################################PLAY CLASS###########################################################################################

################################################################################STATS CLASS###########################################################################################
################################################################################STATS CLASS###########################################################################################
################################################################################STATS CLASS###########################################################################################
################################################################################STATS CLASS###########################################################################################

class Stats(object):
    
    def __init__(self):
        self.stats = {}
        self.pos_ratings = {}        
        
    def get_mvp_points(self, scope, this_year, position, record_matters = True):
        global c
        points = self.get_stat_rating(scope, "ALL", this_year)
        #points *= c.position_value(position)
        if record_matters:
            points *= c.position_value(position)
            points *= (1 + self.get_stat(scope, "GAMES PLAYED WIN PCT", this_year))/2.0
        return points
    
    
    
    def get_fantasy_points(self, scope, this_year, ppr = False):
        points = 0
        points +=  0.1*self.get_stat(scope, "RECEIVING YARDS", this_year)
        points +=    6*self.get_stat(scope, "RECEIVING TDS", this_year)
        points +=   -2*self.get_stat(scope, "RECEIVER FUMBLES", this_year)
        if ppr:
            points +=  self.get_stat(scope, "CATCHES", this_year)
        points +=  0.1*self.get_stat(scope, "RUSH YARDS", this_year)
        points +=    6*self.get_stat(scope, "RUSH TDS", this_year)
        points +=   -2*self.get_stat(scope, "RUSH FUMBLES", this_year)
        points += 0.04*self.get_stat(scope, "PASS YARDS", this_year)
        points +=    4*self.get_stat(scope, "PASS TDS", this_year)
        points +=   -2*self.get_stat(scope, "PASS INTS", this_year)
        points +=   -2*self.get_stat(scope, "POCKET FUMBLES", this_year)
        points +=    6*self.get_stat(scope, "RETURN TDS", this_year)
        points +=    1*self.get_stat(scope, "XP MADE", this_year)
        points +=  0.1*self.get_stat(scope, "FG DISTANCE", this_year)
        points +=   -1*(self.get_stat(scope, "FG ATTEMPTS", this_year) - self.get_stat(scope, "FG MADE", this_year))
        return points
        
    def get_stat_rating(self, scope, stat, this_year):
        global c
        min_rat = 15
        max_rat = 115
        if stat in {"QB","WR","RB","TE","OL","DL","LB","DB","K","RT"}:
            if not (stat in self.pos_ratings.keys()):
                self.pos_ratings[stat] = {this_year : [False, 0, 0]}
            if not (this_year in self.pos_ratings[stat].keys()):
                self.pos_ratings[stat][this_year] = [False,0,0]
            if self.pos_ratings[stat][this_year][0]:
                return self.pos_ratings[stat][this_year][1], self.pos_ratings[stat][this_year][2]
            stats = []
            if stat == "QB":
                stats.append("PASS")
                stats.append("RUN")
            elif stat == "RB":
                stats.append("RUN")
                stats.append("CATCH")
            elif stat == "WR":
                stats.append("CATCH")
            elif stat == "TE":
                stats.append("BLOCK")
                stats.append("CATCH")
            elif stat == "OL":
                stats.append("BLOCK")
            elif stat == "DL":
                stats.append("BLITZER")
            elif stat == "LB":
                stats.append("BLITZER")
                stats.append("COVER")
            elif stat == "DB":
                stats.append("COVER")
            elif stat == "K":
                stats.append("XP")
                stats.append("FG")
            elif stat == "RT":
                stats.append("RETURN")
            rat = 0
            att = 0
            for astat in stats:
                weight = 1.0
                if astat == "BLOCK":
                    weight = 0.1
                umb_att = self.get_umbrella_attempts(astat)
                add_att = self.get_stat(scope, umb_att, this_year) * weight
                rat += add_att * self.get_stat_rating("CAREER", astat,0)
                att += add_att
            if len(stats) == 0:
                print(pos)
            final_rating = divide_maybe_zero(rat,att)
            self.pos_ratings[stat][this_year][1] = final_rating
            self.pos_ratings[stat][this_year][2] = att
            self.pos_ratings[stat][this_year][0] = True
            return final_rating, att
        if stat == "ALL":
            rat = 0
            att = 0
            for a_stat in ["PASS", "RUN", "CATCH", "BLOCK", "COVER", "BLITZ", "XP", "FG", "RETURN", "KICK OFF", "2pt"]:
                umbrella_attempts = self.get_umbrella_attempts(a_stat)
                temp_rat = self.get_stat_rating(scope, a_stat, this_year)
                rat += temp_rat * self.get_stat(scope, umbrella_attempts, this_year)
                att += self.get_stat(scope, umbrella_attempts, this_year)
            rat = divide_maybe_zero(rat, att)
            return rat
        elif stat == "AWARDS":
            mvp = 10 * self.get_stat(scope, "MVPS",  this_year)
            opoy = 5 * self.get_stat(scope, "OPOYS", this_year)
            dpoy = 5 * self.get_stat(scope, "DPOYS", this_year)
            oroy = 5 * self.get_stat(scope, "OROYS", this_year)
            droy = 5 * self.get_stat(scope, "DROYS", this_year)
            prob = 1 * self.get_stat(scope, "PRO BOWLS", this_year)
            return mvp + opoy + dpoy + oroy + droy + prob
        elif stat == "FANTASY":
            return divide_maybe_zero(self.get_fantasy_points(scope, this_year), self.get_stat(scope, "GAMES PLAYED", this_year))
        elif stat in {"PASS", "THROW"}:
            if self.get_stat(scope, "PASS ATTEMPTS", this_year) == 0:
                return 0
            interception = reverse_stat_to_ovr(100*float(self.get_stat(scope, "PASS INTS PER PASS ATTEMPTS", this_year)), c.int_avg, c.int_jump, min_rat, max_rat)
            comp =                 stat_to_ovr(100*float(self.get_stat(scope, "PASS COMPLETIONS PER PASS ATTEMPTS", this_year)), c.complete_avg, c.complete_jump, min_rat, max_rat)
            sack =         reverse_stat_to_ovr(100*float(self.get_stat(scope, "TIMES SACKED PER DROP BACKS", this_year)), c.sack_avg, c.sack_jump, min_rat, max_rat)
            yards = 0
            if self.get_stat(scope, "PASS COMPLETIONS", this_year) > 0:
                yards =            stat_to_ovr(    float(self.get_stat(scope, "PASS YARDS PER PASS COMPLETIONS", this_year)), c.air_yds_avg + c.YAC_avg, sqrt(c.air_yds_jump**2 + c.YAC_jump**2), min_rat, max_rat)
            fumble = 100
            if self.get_stat(scope, "TIMES SACKED", this_year) > 0:
                fumble =  reverse_stat_to_ovr(100*float(self.get_stat(scope, "POCKET FUMBLES PER TIMES SACKED", this_year)), c.fumble_avg, c.fumble_jump, min_rat, max_rat)
            td =                  stat_to_ovr(100*float(self.get_stat(scope, "PASS TDS PER PASS ATTEMPTS", this_year)), c.td_avg, c.td_jump, min_rat, max_rat)
            rat = float(interception + comp + yards + td + 0.2*fumble + 0.2*sack)/4.4
            return rat
        elif stat in {"RUSH", "RUN"}:
            fumble = 0
            run = 0
            td = 0
            if self.get_stat(scope, "CARRIES", this_year) > 0:
                fumble = reverse_stat_to_ovr(100*float(self.get_stat(scope, "RUSH FUMBLES PER CARRIES", this_year)), c.fumble_avg, c.fumble_jump, min_rat, max_rat)
                run =            stat_to_ovr(    float(self.get_stat(scope, "RUSH YARDS PER CARRIES", this_year)), c.run_avg, c.run_jump, min_rat, max_rat)
                td =             stat_to_ovr(100*float(self.get_stat(scope, "RUSH TDS PER CARRIES", this_year)), c.td_avg, c.td_jump, min_rat, max_rat)
            rat = (1.8*run + 0.9*td + fumble)/3.7
            return rat
        elif stat in {"RECEIVE", "CATCH"}:
            fumble = 100
            if self.get_stat(scope, "CATCHES", this_year) > 0:
                fumble = reverse_stat_to_ovr(100*float(self.get_stat(scope, "RECEIVER FUMBLES PER CATCHES", this_year)), c.fumble_avg, c.fumble_jump, min_rat, max_rat)
            drop = 100
            complete = 0
            td = 0
            if self.get_stat(scope, "TARGETS", this_year) > 0:
                drop = reverse_stat_to_ovr(100*float(self.get_stat(scope, "DROPS PER TARGETS", this_year)), c.drop_avg, c.drop_jump, min_rat, max_rat)
                complete =     stat_to_ovr(100*float(self.get_stat(scope, "CATCHES PER TARGETS", this_year)), c.complete_avg, c.complete_jump, min_rat, max_rat)
                td =           stat_to_ovr(100*float(self.get_stat(scope, "RECEIVING TDS PER TARGETS", this_year)), c.td_avg, c.td_jump, min_rat, max_rat)
            else:
                return 0
            distance = 0
            yac = 0
            if self.get_stat(scope, "CATCHES", this_year) > 0:
                distance = stat_to_ovr(float(self.get_stat(scope, "YBC PER CATCHES", this_year)), c.air_yds_avg, 1.25*c.air_yds_jump, min_rat, max_rat)
                yac =      stat_to_ovr(float(self.get_stat(scope, "YAC PER CATCHES", this_year)), c.YAC_avg, c.YAC_jump, min_rat, max_rat)
            rat = (drop + 1.1*distance + 1.1*yac + 0.9*td + complete + 0.8*fumble)/5.9
            return rat
        elif "BLOCK" in stat:
            type = stat[0:stat.index("BLOCK")]
            #if not type == "":
                #type += " "
            block = 0
            sack = 100
            if self.get_stat(scope, type + "BLOCK ATTEMPTS", this_year) > 0:
                block = stat_to_ovr(100*float(self.get_stat(scope, type + "BLOCKS MADE PER " + type + "BLOCK ATTEMPTS", this_year)), c.block_chance_avg, c.block_jump, min_rat, max_rat)
            #if self.get_stat(scope, "PASS BLOCK ATTEMPTS", this_year) > 0:
                #sack =  stat_to_ovr(100*float(self.get_stat(scope, "PASS BLOCKS MADE PER PASS BLOCK ATTEMPTS", this_year)), c.block_chance_avg, c.sack_jump)
            #rat = (block + sack)/2.0
            rat = block
            return rat
        elif " COVER" in stat:
            type_of_cover = stat[0:stat.index(" COVER")]
            pick = 0
            complete = 100
            pass_td = 100
            int_td = 0
            tackle = 0
            if self.get_stat(scope, type_of_cover + " TARGETED", this_year) > 0:
                pick =             stat_to_ovr(100*float(self.get_stat(scope, type_of_cover + " PICKS PER " + type_of_cover + " TARGETED", this_year)),               c.int_avg,           c.int_jump,           50,      140)
                complete = reverse_stat_to_ovr(100*float(self.get_stat(scope, type_of_cover + " COMPLETIONS ALLOWED PER " + type_of_cover + " TARGETED", this_year)), c.complete_avg,      c.complete_jump,      min_rat, max_rat)
                pass_td =  reverse_stat_to_ovr(100*float(self.get_stat(scope, type_of_cover + " PASS TDS ALLOWED PER " + type_of_cover + " TARGETED", this_year)),    c.td_avg,            c.td_jump,            min_rat, max_rat)
                tackle =           stat_to_ovr(100*float(self.get_stat(scope, type_of_cover + " COVER TACKLES PER" + type_of_cover + " COVERS", this_year)),          c.rating_tackle_avg, c.rating_tackle_jump, 55,      max_rat)
                int_td =                       500*float(self.get_stat(scope, type_of_cover + " PICK SIXES PER" + type_of_cover + " TARGETED", this_year))
            safety = 0
            ff_td = 0
            ff = 0
            pass_yds = 100
            if self.get_stat(scope, type_of_cover + " COMPLETIONS ALLOWED", this_year) > 0:
                ff =               stat_to_ovr(100*float(self.get_stat(scope, type_of_cover + " COVER FF PER " + type_of_cover + " COMPLETIONS ALLOWED", this_year)), c.fumble_avg, c.fumble_jump, 50, max_rat)
                pass_yds = reverse_stat_to_ovr(    float(self.get_stat(scope, type_of_cover + " PASS YARDS ALLOWED PER " + type_of_cover + " COMPLETIONS ALLOWED", this_year)), c.air_yds_avg + c.YAC_avg, sqrt(c.air_yds_jump**2 + c.YAC_jump**2), min_rat, max_rat)
                ff_td =                        250*float(self.get_stat(scope, type_of_cover + " COVER FF TDS PER " + type_of_cover + " COMPLETIONS ALLOWED", this_year))
                safety =                       250*float(self.get_stat(scope, type_of_cover + " COVER SAFETIES PER " + type_of_cover + " COMPLETIONS ALLOWED", this_year))
            rat = (pass_td + 1.1*max(pick, complete) + 0.9*min(pick, complete) + 1.1*pass_yds + 0.5*ff + 0.3*tackle)/4.9 + int_td + ff_td + safety
            if type_of_cover == "ZONE" and self.get_stat(scope, type_of_cover + " COVERS", this_year) > 0 and not self.get_stat(scope, type_of_cover + " TARGETED", this_year) > 0:
                pick =   stat_to_ovr(100*float(self.get_stat(scope, type_of_cover + " PICKS PER " + type_of_cover + " COVERS", this_year)), c.int_avg/7.0, c.int_jump, 50, 140)
                tackle = stat_to_ovr(100*float(self.get_stat(scope, type_of_cover + " COVER TACKLES PER" + type_of_cover + " COVERS", this_year)), c.rating_tackle_avg, c.rating_tackle_jump, 50, max_rat)
                int_td = 500*float(self.get_stat(scope, type_of_cover + " PICK SIXES PER" + type_of_cover + " COVERS", this_year))
                ff =     stat_to_ovr(100*float(self.get_stat(scope, type_of_cover + " COVER FF PER " + type_of_cover + " COVERS", this_year)), c.fumble_avg, c.fumble_jump, 50, max_rat)
                ff_td =  250*float(self.get_stat(scope, type_of_cover + " COVER FF TDS PER " + type_of_cover + " COVERS", this_year))
                rat = (pick + ff + tackle) / 2.8 + int_td + ff_td + 3
            return rat
        elif stat == "COVER":
            #return (self.get_stat(scope, "MAN COVERS", this_year)*self.get_stat_rating(scope, "MAN COVER", this_year) + self.get_stat(scope, "ZONE COVERS", this_year)*self.get_stat_rating(scope, "ZONE COVER", this_year) + self.get_stat(scope, "RUN COVERS", this_year)*self.get_stat_rating(scope, "RUN COVER", this_year))/self.get_stat(scope, "COVERS", this_year)
            return divide_maybe_zero((self.get_stat(scope, "MAN COVERS", this_year)*self.get_stat_rating(scope, "MAN COVER", this_year) + self.get_stat(scope, "ZONE COVERS", this_year)*self.get_stat_rating(scope, "ZONE COVER", this_year)), (self.get_stat(scope, "MAN COVERS", this_year) + self.get_stat(scope, "ZONE COVERS", this_year)))
            #return self.get_stat_rating(scope, "MAN COVER", this_year)
        elif stat in {"BLITZ", "BLITZER"}:
            tackle = 0
            safety = 0
            ff_td = 0
            ff = 0
            sack = 0
            run_stop = 0
            if self.get_stat(scope, "BLITZES", this_year) > 0:
                tackle =   stat_to_ovr(100*float(self.get_stat(scope, "BLITZ TACKLES PER BLITZES", this_year)), c.rating_tackle_avg, c.rating_tackle_jump, min_rat, max_rat)
                safety =               500*float(self.get_stat(scope, "BLITZ SAFETIES PER BLITZES", this_year))
                ff_td =                500*float(self.get_stat(scope, "BLITZ FF TDS PER BLITZES", this_year))
                ff =       stat_to_ovr(100*float(self.get_stat(scope, "BLITZ FF PER BLITZES", this_year)), c.fumble_avg, c.fumble_jump, 50, max_rat)
                sack =     stat_to_ovr(100*float(self.get_stat(scope, "SACKS PER BLITZES", this_year)), c.rating_sack_avg, c.sack_jump, min_rat, max_rat)
                run_stop = stat_to_ovr(100*float(self.get_stat(scope, "BLITZ RUN STUFFS PER BLITZES", this_year)), c.rating_sack_avg, c.sack_jump, min_rat, max_rat)
            rat = (0.8*ff + sack + run_stop + tackle)/3.8 + safety + ff_td
            return rat
        elif stat == "XP":
            if self.get_stat(scope, "XP ATTEMPTS", this_year) > 0:
                return stat_to_ovr(100*float(self.get_stat(scope, "XP MADE PER XP ATTEMPTS", this_year)), c.fg_chance_avg, 2*c.fg_chance_jump, min_rat, max_rat)
            else:
                return 0
        elif stat == "FG":
            if self.get_stat(scope, "FG ATTEMPTS", this_year) > 0:
                pct =      stat_to_ovr(float(self.get_stat(scope, "FG MADE PCT PER FG ATTEMPTS", this_year)), c.fg_chance_avg, 2*c.fg_chance_jump, min_rat, max_rat)
                distance = stat_to_ovr(float(self.get_stat(scope, "FG DISTANCE AVG PER FG ATTEMPTS", this_year)), c.rating_fg_range_avg, 2*c.fg_range_jump, min_rat, max_rat)
                rat = (pct + 0.75*distance)/1.75
                return rat
            else:
                return 0
        elif stat == "PUNT":
            if self.get_stat(scope, "PUNTS", this_year) > 0:
                #tb =   stat_to_ovr(100*float(self.punt_stats[scope][c.punt_tb])/self.punt_stats[scope][c.punts], c.touchback_avg, c.touchback_jump)
                yards = stat_to_ovr(    float(self.get_stat(scope, "PUNT YARDS PER PUNTS", this_year)), c.rating_punt_avg, 2*c.punt_jump, min_rat, max_rat)
                pin =   stat_to_ovr(100*float(self.get_stat(scope, "PUNT PINS PER PUNTS", this_year)), c.rating_pin_avg, 2*c.pin_jump, min_rat, max_rat)
                #rat = (tb + yards + pin)/3.0
                rat = (1.2*yards + pin)/2.2
                return rat
            else:
                return 0
        elif stat == "KICK OFF":
            if self.get_stat(scope, "KICK OFF ATTEMPTS", this_year) > 0:
                tb =         stat_to_ovr(100*float(self.get_stat(scope, "KICK OFF TB PCT PER KICK OFF ATTEMPTS", this_year)), c.touchback_avg, c.touchback_jump, min_rat, max_rat)
                onside = 50
                if self.get_stat(scope, "ONSIDE KICK ATTEMPTS", this_year) > 0:
                    onside = stat_to_ovr(100*float(self.get_stat(scope, "ONSIDE KICK SUCCESS PCT PER ONSIDE KICK ATTEMPTS", this_year)), c.onside_avg, c.onside_jump, min_rat, max_rat)
                return (tb + onside) / 2.0
            else:
                return 0
        elif " RETURN" in stat:
            type_of_return = stat[0:stat.index(" RETURN")]
            ret_mult = 1
            if type_of_return == "KICK":
                ret_mult = 2
            if self.get_stat(scope, type_of_return + " RETURNS", this_year) > 0:
                #tb = stat_to_ovr(100*float(self.return_stats[scope][c.punt_tb])/self.return_stats[scope][c.punts], c.touchback_avg, c.touchback_jump)
                yards =          stat_to_ovr(    float(self.get_stat(scope, type_of_return + " RETURN YARDS PER " + type_of_return + " RETURNS", this_year)), ret_mult*c.rating_return_avg, 3*c.return_jump, min_rat, max_rat)
                fumble = reverse_stat_to_ovr(100*float(self.get_stat(scope, type_of_return + " RETURN FUMBLES PER " + type_of_return + " RETURNS", this_year)), c.fumble_avg, c.fumble_jump, min_rat, max_rat)
                td =                          10*float(self.get_stat(scope, type_of_return + " RETURN TDS PER " + type_of_return + " RETURN", this_year)) 
                #rat = (tb + yards + fumble)/3.0 + td
                rat = (yards + 0.8*fumble)/1.8 + td
                return rat
            else:
                return 0
        elif stat == "RETURN":
            return divide_maybe_zero((self.get_stat(scope, "PUNT RETURNS", this_year)*self.get_stat_rating(scope, "PUNT RETURN", this_year) + self.get_stat(scope, "KICK RETURNS", this_year)*self.get_stat_rating(scope, "KICK RETURN", this_year)),self.get_stat(scope, "RETURNS", this_year))
        elif stat == "2pt":
            return 100*divide_maybe_zero( self.get_stat(scope, "2pt PASS SUCCESS", this_year)+self.get_stat(scope, "2pt RUSH SUCCESS", this_year)+self.get_stat(scope, "2pt CATCH SUCCESS", this_year), self.get_stat(scope, "2pt PASS ATTEMPTS", this_year)+self.get_stat(scope, "2pt CARRIES", this_year)+self.get_stat(scope, "2pt TARGETS", this_year) )
        elif stat == "RECORD":
            return 100.0*self.get_stat(scope, "GAMES PLAYED WIN PCT", this_year)
        else:
            print("error: unknown stat in get_stat_rating - " + str(stat))
        
    def add_stat(self, stat_name, stat_amount, game_type, this_year):
        # Formats:
            # GAME STAT             * clears each game
            
            # SEASON  (YEAR) STAT   * stays forever
            # PLAYOFF (YEAR) STAT   * stays forever
            
            # REGULAR  CAREER STAT  * stays forever
            # PLAYOFF  CAREER STAT  * stays forever
            # SB       CAREER STAT  * stays forever
            # PRO BOWL CAREER STAT  * stays forever
            
            # CAREER HIGH STAT      * stays forever
            # SEASON HIGH STAT      * stays forever
            
        # STAT types:
            # TEAM
            # OVERALL
            # SALARY
            
            # PASS COMPLETIONS
            # PASS ATTEMPTS
            # PASS YARDS
            # PASS YARDS LONG
            # PASS TDS
            # PASS INTS
            # POCKET FUMBLES
            # TIMES SACKED
            # SACKED YARDS
            
            # ROUTES RUN
            # TARGETS
            # CATCHES
            # RECEIVING YARDS
            # RECEIVING YARDS LONG
            # RECEIVING TDS
            # YAC
            # RECEIVER FUMBLES
            # DROPS
            
            # CARRIES
            # RUSH YARDS
            # RUSH YARDS LONG
            # RUSH TDS
            # RUSH FUMBLES
            
            # (PASS/RUN) BLOCK ATTEMPTS
            # (PASS/RUN) BLOCKS MADE
            
            # BLITZES
            # SACKS
            # SACK YARDS
            # BLITZ RUN STUFFS
            # BLITZ RUN STUFF YARDS
            # BLITZ FF
            # BLITZ FF TDS
            # BLITZ FF RETURN YARDS
            # BLITZ TACKLES
            # BLITZ SAFETIES
            
            # RUN COVERS
            # RUN COVER TACKLES
            # RUN COVER RUN STUFFS
            # RUN COVER RUN STUFF YARDS
            # RUN COVER FF
            # RUN COVER FF TDS
            # RUN COVER FF RETURN YARDS
            # RUN COVER SAFETIES
            
            # (MAN/ZONE) COVERS
            # (MAN/ZONE) TARGETED
            # (MAN/ZONE) COMPLETIONS ALLOWED
            # (MAN/ZONE) YARDS ALLOWED
            # (MAN/ZONE) YAC ALLOWED
            # (MAN/ZONE) PASS TDS ALLOWED
            # (MAN/ZONE) PICKS
            # (MAN/ZONE) PICK SIXES
            # (MAN/ZONE) PICK RETURN YARDS
            # (MAN/ZONE) TACKLES
            # (MAN/ZONE) FF
            # (MAN/ZONE) FF TDS
            # (MAN/ZONE) FF RETURN YARDS
            # (MAN/ZONE) SAFETIES
            
            # XP ATTEMPTS
            # XP MADE
            
            # FG ATTEMPTS
            # FG MADE
            # FG DISTANCE
            # FG DISTANCE LONG
            
            # PUNTS
            # PUNT YARDS
            # PUNT YARDS LONG
            # PUNT TB
            # PUNT PINS
            # KICK OFFS
            # KICK OFF TB
            
            # (PUNT/KICK) RETURNS
            # (PUNT/KICK) RETURN TB
            # (PUNT/KICK) RETURNS
            # (PUNT/KICK) RETURN YARDS
            # (PUNT/KICK) RETURN YARDS LONG
            # (PUNT/KICK) RETURN FUMBLE
            # (PUNT/KICK) RETURN TDS
            
            ## GAMES STARTED
            ## STARTER WINS
            ## STARTER LOSSES
            ## STARTER TIES
            
            # GAMES PLAYED
            # PLAYED WINS
            # PLAYED LOSSES
            # PLAYED TIES
            
            # GAMES ON ROSTER
            # WINS
            # LOSSES
            # TIES
            
            # SNAPS PLAYED
            
        # TEAMS ONLY:
            # RUSH YARDS ALLOWED
            # RUSH TDS ALLOWED
            
        scopes = ["GAME"]
        if game_type == "PRO BOWL":
            scopes = ["GAME", "PRO BOWL CAREER"]
        elif game_type == "SB":
            scopes = ["GAME", "SB CAREER"]
        elif game_type == "PLAYOFF":
            scopes = ["GAME", "PLAYOFF " + str(this_year), "PLAYOFF CAREER"]
        elif game_type == "REGULAR":
            scopes = ["GAME", "SEASON " + str(this_year), "REGULAR CAREER"]
        elif game_type == "PRE SEASON":
            scopes = ["GAME"]
        elif game_type == "AWARDS":
            scopes = ["SEASON " + str(this_year), "REGULAR CAREER"]
        else:
            print("error: unknown game type in add_stat - " + str(game_type))
            
        for scope in scopes:
            if stat_name in {"TEAM", "OVERALL"}:
                if stat_name == "OVERALL":
                    if not (scope + " " + stat_name) in self.stats or stat_amount > self.stats[scope + " " + stat_name]:
                        self.stats[scope + " " + stat_name] = stat_amount
                else:
                    self.stats[scope + " " + stat_name] = stat_amount
            else:
                self.stats[scope + " " + stat_name] = self.stats.get(scope + " " + stat_name, 0) + stat_amount
            if stat_name in {"WINS", "LOSSES", "TIES"}:
                self.stats[scope + " GAMES ON ROSTER"] = self.stats.get(scope + " GAMES ON ROSTER", 0) + stat_amount
                if self.stats.get("GAME SNAPS PLAYED", 0) > 0:
                    self.stats[scope + " GAMES PLAYED"] = self.stats.get(scope + " GAMES PLAYED", 0) + stat_amount
                    self.stats[scope + " PLAYED " + stat_name] = self.stats.get(scope + " PLAYED " + stat_name, 0) + stat_amount
            else:
                for pos in self.pos_ratings.keys():
                    if this_year in self.pos_ratings[pos].keys():
                        self.pos_ratings[pos][this_year][0] = False
                    else:
                        self.pos_ratings[pos][this_year] = [False,0,0]
            if stat_name in {"PASS YARDS", "RECEIVING YARDS", "RUSH YARDS", "PUNT YARDS", "FG DISTANCE", "PUNT RETURN YARDS", "KICK RETURN YARDS"}:
                for s in [scope, "CAREER HIGH", "SEASON HIGH"]:
                    try:
                        if stat_amount > self.stats[s + " " + str(stat_name) + " LONG"]:
                            self.stats[s + " " + str(stat_name) + " LONG"] = stat_amount
                    except:
                        self.stats[s + " " + str(stat_name) + " LONG"] = stat_amount
            if scope == "GAME":
                self.stats["CAREER HIGH " + stat_name] = max(self.stats.get("CAREER HIGH " + stat_name, -100), self.stats[scope + " " + stat_name])
            elif scope == "SEASON " + str(this_year):
                self.stats["SEASON HIGH " + stat_name] = max(self.stats.get("SEASON HIGH " + stat_name, -100), self.stats[scope + " " + stat_name])
                
                
    def has_stats(self, scope, type, this_year = 0):
        return self.has_stats_min_att(type, scope, this_year, 1, True)
        
    def has_stats_min_att(self, scope, type, this_year, min_att, is_umbrella):
        if is_umbrella:
            if type in {"AWARDS", "MVP", "PRO BOWL", "OPOY", "DPOY", "OROY", "DROY"}:
                sum = 0
                for award in {"MVPS", "PRO BOWLS", "OPOYS", "DPOYS", "OROYS", "DROYS", "DROY"}:
                    sum += self.get_stat(scope, award, this_year)
                return sum >= min_att
            #elif type == "ALL":
            #    sum = 0
            #    for type in ["PASS", "CATCH", "RUN", "BLOCK", "BLITZ", "COVER", "XP", "FG", "RETURN"]:
            #        att_name = self.get_umbrella_attempts(type)
            #        sum += self.get_stat(scope, att_name, this_year)
            #    return sum >= min_att
            elif "RATING" in type:
                return self.get_stat(scope, "SNAPS PLAYED", this_year) >= min_att
            else:
                att_name = self.get_umbrella_attempts(type)
                return self.get_stat(scope, att_name, this_year) >= min_att
        else:
            return self.get_stat(scope, type, this_year) >= min_att
        
    def set_stat(self, stat_name, stat_amount):
        self.stats[stat_name] = stat_amount
        
    #def calculate_stat(self, stat_name):
    #   pass
        
    #def get_stat_in_scope(self, scope, stat_name):
    #    return self.get_stat(str(scope) + " " + str(stat_name))
    
    def get_stat_umbrella_name(self, stat):
        if stat in {"RUSH YARDS AVG"}:
            return "RUSH"
        elif stat in {"RECEIVING YARDS AVG"}:
            return "RECEIVE"
        elif stat in {"PASS COMPLETIONS PCT", "PASS YARDS AVG"}:
            return "PASS"
        elif stat in {"BLOCK ATTEMPTS", "BLOCKS MADE"}:
            return "BLOCK"
        elif stat in {"PASS COMPLETIONS PCT ALLOWED", "COVERS", "TARGETED", "COMPLETIONS ALLOWED", "PASS YARDS ALLOWED", "PASS TDS ALLOWED", "PICKS", "PICK SIXES", "PICK RETURN YARDS", "COVER TACKLES", "COVER FF", "COVER FF TDS", "COVER FF RETURN YARDS", "COVER SAFETIES"}:
            return "COVER"
        elif stat in {"XP MADE PCT"}:
            return "XP"
        elif stat in {"FG MADE PCT"}:
            return "FG"
        elif stat in {"PUNT YARDS AVG"}:
            return "PUNT"
        elif stat in {"ONSIDE KICK SUCCESS PCT PER ONSIDE KICK ATTEMPTS", "KICK OFF TB PCT PER KICK OFF ATTEMPTS"}:
            return "KICK OFF"
        elif stat in {"RETURN YARDS AVG", "RETURNS", "RETURN YARDS", "RETURN TDS", "RETURN FUMBLES", "RETURN TB", "RETURNS"}:
            return "RETURN"
        elif stat in {"2pt PASS SUCCESS", "2pt RUSH SUCCESS", "2pt CATCH SUCCESS", "2pt PASS ATTEMPTS", "2pt CARRIES", "2pt TARGETS", "2pt PASS SUCCESS PCT PER 2pt PASS ATTEMPTS", "2pt RUSH SUCCESS PCT PER 2pt CARRIES", "2pt CATCH SUCCESS PCT PER 2pt TARGETS"}:
            return "2pt"
        elif stat in {"WINS", "LOSSES", "TIES", "WIN", "LOSS", "TIE"}:
            return "RECORD"
        else:
            print("error: unkown stat in get_stat_umbrella_attempts - " + str(stat))
            return ""
    
    def get_umbrella_attempts(self, name):
        if name in {"RUSH", "RUN"}:
            return "CARRIES"
        elif name in {"RECEIVE", "CATCH"}:
            return "TARGETS"
        elif name == "THROW":
            return "PASS ATTEMPTS"
        elif name in {"PASS", "BLOCK", "XP", "FG", "KICK OFF"} or "BLOCK" in name:
            return str(name) + " ATTEMPTS"
        elif name in {"COVER", "PUNT", "RETURN"} or "COVER" in name or "RETURN" in name:
            return str(name) + "S"
        elif name in {"RETURNS", "2pt"}:
            return name
        elif name in {"BLITZ", "BLITZER"}:
            return "BLITZES"
        elif name == "RECORD":
            return "GAMES ON ROSTER"
        elif name == "ALL" or "FANTASY":
            return "SNAPS PLAYED"
        elif name == "OVERALL":
            return "OVERALL"
        elif name == "MISC":
            return "MISC"
        else:
            print ("error: unknown name in get_umbrella_attempts - " + str(name))
            return ""
        
    def get_umbrella_similar_stats(self, name):
        if name == "COVER":
            return ["MAN ", "ZONE ", "RUN "]
        elif name == "RETURN":
            return ["KICK ", "PUNT "]
        elif name == "RECORD":
            return [""]
        elif name == "BLOCK":
            return ["PASS ", "RUN "]
        else:
            print("error: unknown name in get_umbrella_similar_stats - " + str(name))
            return [""]
        
        
    def get_stat(self, scope, stat_name, this_year):
        if scope == "YEAR":
            if not " PER " in stat_name:
                if stat_name == "OVERALL":
                    return max(self.get_stat("SEASON", stat_name, this_year), self.get_stat("PLAYOFF", stat_name, this_year))
                elif stat_name == "TEAM":
                    pl_team = self.get_stat("PLAYOFF", stat_name, this_year)
                    if pl_team == 0:
                        return self.get_stat("SEASON", stat_name, this_year)
                    else:
                        return pl_team
                else:
                    return (self.get_stat("SEASON", stat_name, this_year) + self.get_stat("PLAYOFF", stat_name, this_year))
        elif scope == "CAREER":
            if not " PER " in stat_name and not " WIN PCT" in stat_name:
                if " LONG" in stat_name:
                    return self.get_stat("CAREER HIGH", stat_name, this_year)
                elif stat_name == "OVERALL":
                    return max(self.get_stat("REGULAR CAREER", stat_name, this_year), self.get_stat("PLAYOFF CAREER", stat_name, this_year), self.get_stat("SB CAREER", stat_name, this_year))
                elif stat_name == "TEAM":
                    return 0
                else:
                    return (self.get_stat("REGULAR CAREER", stat_name, this_year) + self.get_stat("PLAYOFF CAREER", stat_name, this_year) + self.get_stat("SB CAREER", stat_name, this_year))
        elif scope in {"SEASON", "PLAYOFF"}:
            scope = scope + " " + str(this_year)
        combination_stat_names = {"BLOCK ATTEMPTS", "BLOCKS MADE", "COVERS", "TARGETED", "COMPLETIONS ALLOWED", "PASS YARDS ALLOWED", "PASS TDS ALLOWED", "PICKS", "PICK SIXES", "PICK RETURN YARDS", "COVER TACKLES", "COVER FF", "COVER FF TDS", "COVER FF RETURN YARDS", "COVER SAFETIES", "RETURNS", "RETURN YARDS", "RETURN TDS", "RETURN FUMBLES", "RETURN TB"}
        compound_stat_names = {"DROP BACKS", "TURNOVERS", "TAKEAWAYS", "ALL PURPOSE YARDS", "TDS"} # add here and get_stat_parts
        
        if stat_name == "YBC":
            return self.get_stat(scope, "RECEIVING YARDS", this_year) - self.get_stat(scope, "YAC", this_year)
        elif " AVG PER " in stat_name or (" PER " in stat_name and not "PCT PER " in stat_name):
            if " AVG PER " in stat_name:
                stat1 = stat_name[0:stat_name.index(" AVG PER ")]
                stat2 = stat_name[stat_name.index(" AVG PER ") + 9:]
                return divide_maybe_zero(self.get_stat(scope, stat1, this_year), self.get_stat(scope, stat2, this_year))
            else:
                stat1 = stat_name[0:stat_name.index(" PER ")]
                stat2 = stat_name[stat_name.index(" PER ") + 5:]
                return divide_maybe_zero(self.get_stat(scope, stat1, this_year), self.get_stat(scope, stat2, this_year))
        elif " PCT PER " in stat_name:
            stat1 = stat_name[0:stat_name.index(" PCT PER ")]
            stat2 = stat_name[stat_name.index(" PCT PER ") + 9:]
            return 100*divide_maybe_zero(self.get_stat(scope, stat1, this_year), self.get_stat(scope, stat2, this_year))
        elif " WIN PCT" in stat_name:
            if stat_name[0:stat_name.index(" WIN PCT")] == "GAMES PLAYED":
                return divide_maybe_zero(self.get_stat(scope, "PLAYED WINS", this_year) + self.get_stat(scope, "PLAYED TIES", this_year) / 2.0, self.get_stat(scope, "GAMES PLAYED", this_year))
            elif stat_name[0:stat_name.index(" WIN PCT")] == "GAMES ON ROSTER":
                return divide_maybe_zero(self.get_stat(scope, "WINS", this_year) + self.get_stat(scope, "TIES", this_year) / 2.0, self.get_stat(scope, "GAMES ON ROSTER", this_year))
            else:
                print("error: unknown game type in get_stat - " + str(stat_name))
        elif stat_name in combination_stat_names:
            umbrella =     self.get_stat_umbrella_name(stat_name)
            try_at_front = self.get_umbrella_similar_stats(umbrella)
            stat_value =   0
            for word in try_at_front:
                stat_value += self.get_stat(scope, str(word) + str(stat_name), this_year)
            return stat_value
        elif stat_name in compound_stat_names:
            pieces = self.get_stat_parts(stat_name)
            stat_value = 0
            for piece in pieces:
                stat_value += self.get_stat(scope, piece, this_year)
            return stat_value
        elif "FANTASY" in stat_name:
            if "PPR" in stat_name:
                return self.get_fantasy_points(scope, this_year, True)
            return self.get_fantasy_points(scope, this_year)
        else:
            return self.stats.get(str(scope) + " " + str(stat_name), 0)
        
    def get_stat_parts(self, stat):
        if stat == "DROP BACKS":
            return ["TIMES SACKED", "PASS ATTEMPTS"]
        elif stat == "TURNOVERS":
            return ["PASS INTS", "POCKET FUMBLES", "RECEIVER FUMBLES", "RUSH FUMBLES"]
        elif stat == "ALL PURPOSE YARDS":
            return ["RECEIVING YARDS", "RUSH YARDS"]
        elif stat == "TAKEAWAYS":
            return ["RUN COVER FF", "BLITZ FF", "MAN FF", "ZONE FF", "ZONE PICKS", "MAN PICKS"]
        elif stat == "TDS":
            return ["RECEIVING TDS", "RUSH TDS", "BLITZ FF TDS", "RUN COVER FF TDS", "MAN PICK SIXES", "ZONE PICK SIXES", "MAN COVER FF TDS", "ZONE COVER FF TDS"]
        
    def reset_game_stats(self):
        for a_key in self.stats.keys():
            if "GAME " in a_key:
                del self.stats[a_key]

################################################################################STATS CLASS###########################################################################################
################################################################################STATS CLASS###########################################################################################
################################################################################STATS CLASS###########################################################################################
################################################################################STATS CLASS###########################################################################################



################################################################################PLAYER CLASS###########################################################################################
################################################################################PLAYER CLASS###########################################################################################
################################################################################PLAYER CLASS###########################################################################################
################################################################################PLAYER CLASS###########################################################################################

class Player(object):
    def __init__(self, pos, ovr, proj_ovr = "NONE"):
        global c
        if proj_ovr == "NONE":
            proj_ovr = ovr
        self.first_name =                 rand_first_name()
        self.last_name =                  rand_last_name()
        self.drafted_by =                 "Undrafed"
        self.draft_position =             [0,0,1966]
        self.position =                   pos
        self.age =                        int(random(20,24))
        self.age_type =                   rand_ability_type()
        self.skip_years =                 0
        self.start_age =                  self.age
        self.years_played =               0
        self.retired =                    False
        self.xp =                         0
        self.upgrade_type =               rand_ability_type()
        self.team =                       "ROOKIE"
        self.projected_ovr =              proj_ovr
        self.adjust_ovr =                 0
        self.contract_amount =            0
        self.contract_length =            0
        self.depth =                      0
        self.is_first_year_of_contract =  False
        self.confidence =                 0.5
        self.loyalty =                    min_max_skew(10,50)
        self.stamina =                    random_skew(75, 4)
        self.fatigue =                    0
        self.injured =                    False 
        self.injury_length =              0
        self.injury_amount =              0
        self.injury_chance =              random(c.injury_chance_avg - 15 * c.injury_jump, c.injury_chance_avg + 15 * c.injury_jump)
        self.block_chance =               rand_stat(ovr, c.block_chance_avg, c.block_jump) 
        self.sack_allowed_chance =        reverse_stat(ovr, c.sack_avg, c.sack_jump)
        self.int_chance =                 reverse_stat(ovr, c.int_avg, c.int_jump)
        self.dist_effect_int =            rand_ability_type()
        self.complete_chance =            rand_stat(ovr, c.complete_avg, c.complete_jump)
        self.dist_effect_complete =       rand_ability_type()
        self.air_yds_throw =              rand_stat(ovr, c.air_yds_avg, c.air_yds_jump)
        self.stdev_air_yds_throw =        random(5,15)
        self.fumble_chance =              reverse_stat(ovr, c.fumble_avg, c.fumble_jump)
        self.drop_chance =                reverse_stat(ovr, c.drop_avg, c.drop_jump)
        self.dist_effect_drop =           rand_ability_type()
        self.target_dist =                rand_stat(ovr, c.air_yds_avg, c.air_yds_jump)
        self.stdev_target_dist =          random(5,15)
        self.YAC =                        rand_stat(ovr, c.YAC_avg, c.YAC_jump)
        self.stdev_YAC =                  random(5,15)
        self.run_dist =                   rand_stat(ovr, c.run_avg, c.run_jump)
        self.stdev_run_dist =             random(4,10)
        self.catch_boost =                rand_ability_type()
        self.air_yds_allowed =            reverse_stat(ovr, c.air_yds_avg, c.air_yds_jump)
        self.stdev_air_yds_allowed =      random(5,15)
        self.int_catch_chance =           rand_stat(ovr, c.int_avg, c.int_jump)
        self.def_return_dist =            rand_stat(ovr, c.YAC_avg, c.YAC_jump)
        self.stdev_def_return_dist =      random(5,15)
        self.complete_chance_allowed =    reverse_stat(ovr, c.complete_avg, c.complete_jump)
        self.YAC_allowed =                reverse_stat(ovr, c.YAC_avg, c.YAC_jump)
        self.stdev_YAC_allowed =          random(5,15)
        self.sack_chance =                rand_stat(ovr, c.sack_avg, c.sack_jump)
        self.blocked_chance =             reverse_stat(ovr, c.block_chance_avg, c.block_jump)
        self.run_dist_allowed =           reverse_stat(ovr, c.run_avg, c.run_jump)
        self.stdev_run_dist_allowed =     random(4,10)
        self.ff_chance =                  rand_stat(ovr, c.fumble_avg, c.fumble_jump)
        self.fg_range =                   rand_stat(ovr, c.fg_range_avg, c.fg_range_jump)
        self.fg_made_chance =             rand_stat(ovr, c.fg_chance_avg, c.fg_chance_jump)
        self.punt_dist =                  rand_stat(ovr, c.punt_avg, c.punt_jump)
        self.stdev_punt_dist =            random(5,10)
        self.kick_return_allowed =        reverse_stat(ovr, c.return_avg, c.return_jump)
        self.stdev_kick_return_allowed =  random(6,20)
        self.touchback_forced_chance =    rand_stat(ovr, c.touchback_avg, c.touchback_jump)
        self.onside_kick_chance =         rand_stat(ovr, c.onside_avg, c.onside_jump)
        self.pin_chance =                 rand_stat(ovr, c.pin_avg, c.pin_jump)
        self.kick_return_dist =           rand_stat(ovr, c.return_avg, c.return_jump)
        self.stdev_kick_return_dist =     random(6,20)
        self.touchback_chance =           reverse_stat(ovr, c.touchback_avg, c.touchback_jump)
        self.career_stats =               Stats()
        #self.record_stats =               [[c.wins, c.losses - 1, c.ties - 2, c.seasons - 3, c.superbowls - 4], [c.wins, c.losses - 1, c.ties - 2, c.seasons - 3, c.superbowls - 4], [c.wins, c.losses - 1, c.ties - 2, c.seasons - 3, c.superbowls - 4], [c.wins, c.losses - 1, c.ties - 2, c.seasons - 3, c.superbowls - 4] ]
        if pos == "QB":
            self.adjust_ovr_for_qb()
        elif pos == "RB":
            self.adjust_ovr_for_rb()
        elif pos == "WR":
            self.adjust_ovr_for_wr()
        elif pos == "TE":
            self.adjust_ovr_for_te()
        elif pos == "OL":
            self.adjust_ovr_for_ol()
        elif pos == "DL":
            self.adjust_ovr_for_dl()
        elif pos == "LB":
            self.adjust_ovr_for_lb()
        elif pos == "DB":
            self.adjust_ovr_for_db()
        elif pos == "K":
            self.adjust_ovr_for_k()
        elif pos == "RT":
            self.adjust_ovr_for_rt()
        self.fix_chances(ovr)
        self.player_mode = "NONE"
        self.in_trade_block = False
        self.buttons = [ Button(200, 200, 100, 100, "START", "START", "DEPTH"),
                         Button(200, 300, 100, 100, "BENCH", "BENCH", "DEPTH"),
                         Button(200, 400, 100, 100, "GOOD",  "GOOD",  "OPINION"),
                         Button(200, 500, 100, 100, "BAD",   "BAD",   "OPINION"),
                        
                         Button(350, 200, 100, 100, "Trade Block",     "TRADE",     "TRADE"),
                         Button(350, 300, 100, 100, "Sign",      "SIGN",      "CONTRACT"),
                         Button(350, 400, 100, 100, "Negotiate", "NEGOTIATE", "CONTRACT"),
                        #Button(350, 500, 100, 100, "Upgrade",   "UPGRADE",   "UPGRADE"),
                         Button(350, 500,  50,  50, "Cut",       "CUT",       "CONTRACT")]
        
        self.get_button("SIGN").highlight = True
            
    def get_button(self, do):
        for button in self.buttons:
            if button.do == do:
                return button
                  
    def player_clicked(self, side_scroll, scroll, player_team, season1, mouse_x, mouse_y, pos = "NONE"):
        clicked = ""
        for button in self.buttons:
            if button.clicked(mouse_x, mouse_y):
                clicked = button.do
                if button.category == "OPINION":
                    button.highlight = not button.highlight
                break
        if clicked == "START":
            if self.depth > 0:
                self.depth = 0
            else:
                self.depth = 1
        elif clicked == "BENCH":
            if self.depth < 0:
                self.depth = 0
            else:
                self.depth = -1
        elif clicked == "CUT":
            self.player_mode = "NONE"
            player_team.cut_player(self)
            change_screen(player_team)
        elif clicked == "NEGOTIATE":
            if self.will_negotiate() and get_team_from_name(self.team).negotiations > 0:
                self.negotiate()
                get_team_from_name(self.team).negotiations -= 1
        elif clicked == "SIGN" and self.contract_length <= 0:
            player_team.sign_player(self, int(random(3,6)), self.expected_contract())
        elif clicked == "UPGRADE" and self.upgrade_available():
            self.player_mode = "UPGRADE"
        elif clicked == "TRADE" and self.is_tradeable():
            if self.in_trade_block:
                season1.trade_center.remove_from_trade_block(self)
                self.in_trade_block = False
            else:
                season1.trade_center.add_to_trade_block(self)
                self.in_trade_block = True
        elif self.player_mode == "UPGRADE":
            skill = self.check_skill_clicked(mouse_x-side_scroll, mouse_y-scroll, pos)
            if not (skill == "NONE"):
                self.upgrade_player(skill, 1, self.upgrade_type, True)
                self.player_mode = "NONE"
        
    def draw_buttons(self, side_scroll, scroll):
        if self.depth > 0:
            self.get_button("START").highlight = True
            self.get_button("BENCH").highlight = False
        elif self.depth == 0:
            self.get_button("START").highlight = False
            self.get_button("BENCH").highlight = False
        else:
            self.get_button("START").highlight = False
            self.get_button("BENCH").highlight = True
        for button in self.buttons:
            button.x_off = side_scroll
            button.y_off = scroll
            if button.do == "UPGRADE" and self.upgrade_available():
                if self.player_mode == "UPGRADE":
                    button.t = "Choose a skill"
                else:
                    button.t = "UPGRADE"
                button.draw_button()
            elif button.do == "NEGOTIATE" and self.will_negotiate() and get_team_from_name(self.team).negotiations > 0:
                button.draw_button()
            elif button.do in {"CUT"} or button.category in {"OPINION", "DEPTH"} or (button.do == "SIGN" and self.contract_length <= 0):
                button.draw_button()
            elif button.do == "TRADE" and self.is_tradeable():
                if self.in_trade_block:
                    button.t = "Remove from trade block"
                else:
                    button.t = "TRADE"
                button.draw_button()
    
    def set_age(self, age):
        self.age = age
        self.start_age = age
        
    def adjust_to_team(self):
        if self.adjust_ovr > 0:
            max_boost = min(3,self.adjust_ovr*0.5)
            rand_boost = random(0, max_boost)
            self.change_overall(rand_boost)
            self.adjust_ovr = self.adjust_ovr - rand_boost
        
    def get_mvp_points(self, scope, this_year, record_matters):
        return self.career_stats.get_mvp_points(scope, this_year, self.position, record_matters)
            
    def is_tradeable(self):
        if not self.injured and self.contract_length > 0 and not self.is_first_year_of_contract:
            return True
        return False
        
    def draw_stats_line(self, x, y, widths, c_height, stat_types):
        pass
        
    def name(self):
        return self.first_name + " " + self.last_name
        
    def get_value(self):
        return self.get_value_proj(False)
        
    def get_value_proj(self, is_projected):
        global c, use_overall
        #overall, age, age type, contract length, contract amount, position
        ovr = 1
        overall = self.overall(use_overall)
        if is_projected:
            overall = self.projected_ovr
        if overall > 60:
            ovr = (overall - 59)**3
        else:
            ovr = 1/(61 - overall)**3
        age = 1.2*0.938**(self.age - 20)
        if self.age_range() == "MED":
            age *= 0.8
        elif self.age_range() == "OLD":
            age *= 0.6
        elif self.age_range() == "RETIRING":
            age *= 0.1
        contract = 1
        if self.contract_length > 0:
            contract = (self.expected_contract() / self.contract_amount + (10 - self.contract_length) ) / (11 - self.contract_length)
            contract += (self.contract_length - 2)/10.0
            contract = min(contract, 2)
        position = c.position_value(self.position)
        return ovr*age*contract*position
        
    def end_week(self):
        global c, season1, use_overall
        type = "REGULAR"
        if season1.current_week <= 0:
            type = "PRE SEASON"
        elif season1.current_week == season1.pro_bowl_week:
            type = "PRO BOWL"
        elif season1.current_week == season1.sb_week:
            type = "SB"
        elif season1.current_week >= season1.wildcard_week:
            type = "PLAYOFF"
        new_fat = max(0,self.fatigue-5)
        self.change_overall(self.fatigue-new_fat)
        self.fatigue = new_fat
        self.career_stats.add_stat("OVERALL", self.overall(use_overall), type, season1.this_year)
        self.career_stats.add_stat("TEAM", self.team, type, season1.this_year)
        if self.age_range() == "YOUNG" and not self.team == "FREE AGENT":
            self.xp += 30 * c.position_xp_multiplier(self.position)
            self.adjust_to_team()
        if self.injured:
            self.injury_length -= 1
            if self.injury_length <= 0:
                self.injury_length = 0
                self.injured = False
                self.change_overall(self.injury_amount)
                self.injury_amount = 0
                self.depth = 0
            
    def get_injured(self):
        self.depth = -1
        self.injured = True
        self.injury_length += int(min_max_skew(1, 16))
        self.change_overall(self.injury_amount)
        self.injury_amount += min_max_skew(5, 30)
        self.change_overall(self.injury_amount * -1)
        
    def upgrade_available(self):
        global use_overall
        if self.overall(use_overall) + self.injury_amount >= 99:
            return False
        return self.xp >= self.xp_for_upgrade()
        
    def xp_for_upgrade(self):
        global use_overall
        ovr = self.overall(use_overall) + self.injury_amount
        if ovr > 85:
            return 500 + (ovr - 55)**2.2
        elif ovr > 55:
            return 500 + 0.75 * (ovr - 55)**2
        else:
            return 500
        
    def change_overall(self, amount):
        if amount + self.overall(True) > 99:
            amount = 99 - self.overall(True)
        self.upgrade_player("injury", amount, "NORMAL", False)
        self.upgrade_player("block chance", amount, "NORMAL", False)
        self.upgrade_player("sack allowed chance", amount, "NORMAL", False)
        self.upgrade_player("int throw", amount, "NORMAL", False)
        self.upgrade_player("complete chance", amount, "NORMAL", False)
        self.upgrade_player("air yds throw", amount, "NORMAL", False)
        self.upgrade_player("fumble chance", amount, "NORMAL", False)
        self.upgrade_player("drop chance", amount, "NORMAL", False)
        self.upgrade_player("target dist", amount, "NORMAL", False)
        self.upgrade_player("yac", amount, "NORMAL", False)
        self.upgrade_player("run dist", amount, "NORMAL", False)
        self.upgrade_player("air yds allowed", amount, "NORMAL", False)
        self.upgrade_player("int catch chance", amount, "NORMAL", False)
        self.upgrade_player("complete chance allowed", amount, "NORMAL", False)
        self.upgrade_player("yac allowed", amount, "NORMAL", False)
        self.upgrade_player("sack chance", amount, "NORMAL", False)
        self.upgrade_player("blocked chance", amount, "NORMAL", False)
        self.upgrade_player("run dist allowed", amount, "NORMAL", False)
        self.upgrade_player("ff chance", amount, "NORMAL", False)
        self.upgrade_player("fg range", amount, "NORMAL", False)
        self.upgrade_player("fg made chance", amount, "NORMAL", False)
        self.upgrade_player("punt dist", amount, "NORMAL", False)
        self.upgrade_player("kick return dist", amount, "NORMAL", False)
        self.upgrade_player("tb forced chance", amount, "NORMAL", False)
        self.upgrade_player("pin chance", amount, "NORMAL", False)
        self.upgrade_player("kick return dist", amount, "NORMAL", False)
        self.upgrade_player("tb chance", amount, "NORMAL", False)
        self.upgrade_player("onside kick", amount, "NORMAL", False)
    
    def end_season(self):
        global season1, use_overall
        if not self.team in {"ROOKIE", "FREE AGENT"}:
            self.add_loyalty(random(0, 4))
        self.in_trade_block = False
        skips = season1.this_year - self.draft_position[2] + self.start_age - self.age
        self.age += skips + 1
        self.years_played += skips + 1
        self.skip_years += skips
        self.is_first_year_of_contract = False
        self.change_overall(self.fatigue)
        self.fatigue = 0
        if self.contract_length > 0:
            self.contract_length -= 1
        else:
            self.cut_player()
        self.injury_length -= 5
        if self.injury_length <= 0:
            self.injury_length = 0
            self.injured = False
            self.change_overall(self.injury_amount)
            self.injury_amount = 0
            self.depth = 0
        self.age_overall()
        if random(0,1) < self.boom_chance():
            max_inc = 99 - self.injury_amount - self.get_overall(self.position, use_overall)
            self.change_overall(random(min(4, max_inc), min(max_inc, 10)))
        if random(0,1) < self.retire_chance():
            self.retire()
            
    def boom_chance(self):
        age_range = self.age_range()
        if self.team == "FREE AGENT":
            return 0.0001
        elif age_range == "YOUNG":
            return 0.0010
        elif age_range == "MED":
            return 0.0005
        elif age_range == "OLD":
            return 0.0001
        else:
            return 0
    
    def retire_chance(self):
        global use_overall
        age_range = self.age_range()
        if age_range == "RETIRING":
            return 1.0
        if self.years_played == 0:
            return 0
        chance = 0.0
        ovr = self.overall(use_overall)
        if age_range == "YOUNG":
            if ovr < 60:
                chance += 0.4
            if self.team == "FREE AGENT":
                chance += 0.6
        elif age_range == "MED":
            chance += 0.05
            if ovr < 60:
                chance += 0.65
            elif ovr < 70:
                chance += 0.35
            elif ovr < 80:
                chance += 0.15
            if self.team == "FREE AGENT":
                chance += 0.65
            if self.injured:
                chance += 0.3
        elif age_range == "OLD":
            chance += 0.3
            if ovr < 60:
                chance += 0.75
            elif ovr < 70:
                chance += 0.6
            elif ovr < 80:
                chance += 0.35
            elif ovr < 85:
                chance += 0.25
            if self.team == "FREE AGENT":
                chance += 0.72
            if self.injured:
                chance += 0.4
        else:
            print("error: unkown age_range: " + age_range)
        if ovr > 90:
            chance -= 0.2
        if chance < 0:
            chance = 0
        if chance > 1:
            chance = 1
        return chance
            
    def retire(self):
        global season1, c
        self.retired = True
        self.team = "RETIRED"
        self.cut_player()
                
    def age_range(self):
        if self.age_type == "BAD":
            med = 26
            old = 30
            retiring = 35
        elif self.age_type == "NORMAL":
            med = 29
            old = 34
            retiring = 40
        elif self.age_type == "GOOD":
            med = 33
            old = 38
            retiring = 45
        else:
            println("error: unknown age_type: " + self.age_type)
        if self.age < med:
            return "YOUNG"
        elif self.age < old:
            return "MED"
        elif self.age < retiring:
            return "OLD"
        elif retiring <= self.age:
            return "RETIRING"
        else:
            println("error: age not in range: " + str(self.age))
            
    def age_overall(self):
        global use_overall
        age_range = self.age_range()
        if age_range == "YOUNG":
            amount = random(0.1, 1.75)
        elif age_range == "MED":
            amount = random(-6.1, -2.1)
        elif age_range == "OLD":
            amount = random(-10.5, -5.2)
        else:
            amount = -2
        self.upgrade_player("injury", amount, "NORMAL", False)
        if self.position == "QB":
            self.upgrade_player("int throw", amount - 0.5, "NORMAL", False)
            self.upgrade_player("complete chance", amount, "NORMAL", False)
            self.upgrade_player("air yds throw", amount, "NORMAL", False)
            self.upgrade_player("fumble chance", amount, "NORMAL", False)
            self.upgrade_player("run dist", amount - 1.0, "NORMAL", False)
        elif self.position == "RB":
            self.upgrade_player("fumble chance", amount - 0.5, "NORMAL", False)
            self.upgrade_player("block chance", amount * 0.5, "NORMAL", False)
            self.upgrade_player("sack allowed chance", amount * 0.5, "NORMAL", False)
            self.upgrade_player("drop chance", amount * 0.9, "NORMAL", False)
            self.upgrade_player("target dist", amount - 0.5, "NORMAL", False)
            self.upgrade_player("yac", amount * 0.95, "NORMAL", False)
            self.upgrade_player("run dist", amount, "NORMAL", False)
        elif self.position == "WR":
            self.upgrade_player("drop chance", amount, "NORMAL", False)
            self.upgrade_player("target dist", amount, "NORMAL", False)
            self.upgrade_player("yac", amount, "NORMAL", False)
            self.upgrade_player("fumble chance", amount - 0.5, "NORMAL", False)
            self.upgrade_player("kick return dist", amount, "NORMAL", False)
            self.upgrade_player("tb chance", amount, "NORMAL", False)
        elif self.position == "TE":
            self.upgrade_player("fumble chance", amount - 0.5, "NORMAL", False)
            self.upgrade_player("block chance", amount * 0.9, "NORMAL", False)
            self.upgrade_player("sack allowed chance", amount * 0.9, "NORMAL", False)
            self.upgrade_player("drop chance", amount * 0.9, "NORMAL", False)
            self.upgrade_player("target dist", amount, "NORMAL", False)
            self.upgrade_player("yac", amount, "NORMAL", False)
        elif self.position == "OL":
            self.upgrade_player("block chance", amount, "NORMAL", False)
            self.upgrade_player("sack allowed chance", amount, "NORMAL", False)
        elif self.position == "DL":
            self.upgrade_player("sack chance", amount, "NORMAL", False)
            self.upgrade_player("blocked chance", amount, "NORMAL", False)
            self.upgrade_player("run dist allowed", amount, "NORMAL", False)
            self.upgrade_player("ff chance", amount, "NORMAL", False)
        elif self.position == "LB":
            self.upgrade_player("sack chance", amount * 0.9, "NORMAL", False)
            self.upgrade_player("blocked chance", amount * 0.9, "NORMAL", False)
            self.upgrade_player("run dist allowed", amount * 0.9, "NORMAL", False)
            self.upgrade_player("ff chance", amount, "NORMAL", False)
            self.upgrade_player("air yds allowed", amount * 0.9, "NORMAL", False)
            self.upgrade_player("int catch chance", amount - 0.5, "NORMAL", False)
            self.upgrade_player("complete chance allowed", amount, "NORMAL", False)
            self.upgrade_player("yac allowed", amount, "NORMAL", False)
        elif self.position == "DB":
            self.upgrade_player("sack chance", amount * 0.7, "NORMAL", False)
            self.upgrade_player("blocked chance", amount * 0.7, "NORMAL", False)
            self.upgrade_player("run dist allowed", amount * 0.7, "NORMAL", False)
            self.upgrade_player("ff chance", amount - 0.5, "NORMAL", False)
            self.upgrade_player("air yds allowed", amount, "NORMAL", False)
            self.upgrade_player("int catch chance", amount, "NORMAL", False)
            self.upgrade_player("complete chance allowed", amount, "NORMAL", False)
            self.upgrade_player("yac allowed", amount, "NORMAL", False)
        elif self.position == "K":
            self.upgrade_player("fg range", amount - 0.5, "NORMAL", False)
            self.upgrade_player("fg made chance", amount, "NORMAL", False)
            self.upgrade_player("punt dist", amount - 0.5, "NORMAL", False)
            self.upgrade_player("kick return allowed", amount, "NORMAL", False)
            self.upgrade_player("tb forced chance", amount, "NORMAL", False)
            self.upgrade_player("pin chance", amount, "NORMAL", False)
            self.upgrade_player("onside kick", amount, "NORMAL", False)
        elif self.position == "RT":
            self.upgrade_player("kick return dist", amount, "NORMAL", False)
            self.upgrade_player("tb chance", amount, "NORMAL", False)
        if self.overall(True) >= 98.5:
            self.change_overall(98 - self.overall(True))
        if self.overall(use_overall) >= 98.5:
            self.change_overall(98 - self.overall(use_overall))
    
    def has_stats(self, type, scope, this_year = 0):
        return self.has_stats_min_att(type, scope, this_year, 1)
        
    def has_stats_min_att(self, type, scope, this_year, min_att):
        return self.career_stats.has_stats_min_att(scope, type, this_year, min_att, True)
    
    def check_skill_clicked(self, x, y, pos = "NONE"):
        x -= 20 # yikes
        if pos == "NONE":
            pos = self.position
        if x > 5 and x < 85:
            if y > 220:
                if y < 240:
                    #return "injury"
                    return "NONE"
                elif y < 260:
                    if pos == "QB":
                        return "int throw"
                    elif pos == "RB" or pos == "TE" or pos == "OL":
                        return "block chance"
                    elif pos == "WR":
                        return "fumble chance"
                    elif pos == "K":
                        return "fg range"
                    elif pos == "RT":
                        return "kick return dist"
                elif y < 280:
                    if pos == "QB":
                        return "complete chance"
                    elif pos in ["RB", "TE", "OL"]:
                        return "sack allowed chance"
                    elif pos == "WR":
                        return "drop chance"
                    elif pos == "K":
                        return "fg made chance"
                elif y < 300:
                    if pos == "QB":
                        return "air yds throw"
                    elif pos in ["RB", "TE"]:
                        return "fumble chance"
                    elif pos == "WR":
                        return "target dist"
                    elif pos in ["DL", "LB", "DB"]:
                        return "sack chance"
                    elif pos == "K":
                        return "punt dist"
                    elif pos == "RT":
                        return "tb chance"
                elif y < 320:
                    if pos in ["RB", "TE"]:
                        return "drop chance"
                    elif pos in ["DL", "LB", "DB"]:
                        return "blocked chance"
                    elif pos == "RT":
                        return "fumble chance"
                elif y < 340:
                    if pos in ["RB", "TE"]:
                        return "target dist"
                    elif pos == "WR":
                        return "yac"
                    elif pos in ["DL", "LB", "DB"]:
                        return "run dist allowed"
                    elif pos == "K":
                        return "kick return allowed"
                elif y < 360:
                    if pos == "QB":
                        return "fumble chance"
                elif y < 380:
                    if pos == "QB":
                        return "run dist"
                    elif pos in ["RB", "TE"]:
                        return "yac"
                    elif pos in ["DL", "LB", "DB"]:
                        return "ff chance"
                    elif pos == "K":
                        return "tb forced chance"
                elif y < 400:
                    if pos in ["LB", "DB"]:
                        return "air yds allowed"
                    elif pos == "K":
                        return "pin chance"
                elif y < 420:
                    if pos == "RB":
                        return "run dist"
                    elif pos == "K":
                        return "onside kick"
                elif y < 440:
                    if pos in ["LB", "DB"]:
                        return "int catch chance"
                elif y < 460:
                    if pos in ["LB", "DB"]:
                        return "complete chance allowed"
                elif y < 480:
                    if pos in ["LB", "DB"]:
                        return "yac allowed"
        return "NONE"
        
    def draw_full_player(self, x, y, pos = "NONE"):
        global c, ls, use_overall
        if pos == "NONE":
            pos = self.position
        fill(150)
        rect(1300, 50, 66, 50, 7)
        fill(0)
        text("Team", 1300, 50, 66, 50)
        textSize(50)
        text(self.first_name + " " + self.last_name + " " + self.position, x + 5, y - 50)
        text(str(int(round(self.get_overall(pos, use_overall)))) + " OVR", x + 5, y)
        textSize(25)
        text("(proj: " + str(int(round(self.projected_ovr))) + " ovr)", x + 205, y)
        text("Team: " + self.team + " Drafted by: " + self.drafted_by + "(" + str(self.draft_position[0]) + ", " + str(self.draft_position[1]) + ", " + str(self.draft_position[2]) + ")", x + 5, y + 30)
        text("Age: " + str(self.age) + " years, played for " + str(self.years_played) + " years", x + 5, y + 60)
        if self.contract_length == 0:
            text("Expected contract: " + str(round(self.expected_contract()/1000000.0, 2)) + " million", x + 5, y + 90)
            text("Contract: " + str(self.contract_length) + " years, $" + str(round(self.contract_amount/1000000.0, 2)) + " million", x + 500, y + 90)
        else:
            text("Contract: " + str(self.contract_length) + " years, $" + str(round(self.contract_amount/1000000.0, 2)) + " million", x + 5, y + 90)
        text("XP: " + str(int(round(self.xp))) + " Skips: " + str(self.skip_years), x + 5, y + 120)
        text("XP to next level: " + str(int(round(self.xp_for_upgrade()))), x + 5, y + 150)
        if self.injured:
            text("Injured for " + str(self.injury_length) + " weeks (-" + str(int(self.injury_amount)) + " ovr), fatigue: " + str(round(self.fatigue,2)), x + 5, y + 180)
        else:
            text("Healthy, fatigue: " + str(round(self.fatigue,2)), x + 5, y + 180)
        text("Value: " + str(int(self.get_value())), x + 5, y + 205)
        textSize(15)
        table_data = [["INJ", str(round(self.injury_chance, 4)) + "%", str(int(round(reverse_stat_to_ovr(self.injury_chance, c.injury_chance_avg, c.injury_jump)))) + " OVR"],
                      ["STA", "NA", str(int(round(self.stamina, 0))) + " OVR"]]
        if pos == "QB":
            if use_overall:
                table_data.extend([  ["INT",       str(round(self.int_chance, 2)) + "%",             str(int(round(reverse_stat_to_ovr(self.int_chance, c.int_avg, c.int_jump)))) + " OVR"],
                                     ["COMP",      str(round(self.complete_chance, 2)) + "%",        str(int(round(stat_to_ovr(self.complete_chance, c.complete_avg, c.complete_jump)))) + " OVR"],
                                     ["AIR YDS",   str(round(self.air_yds_throw, 2)) + " yards",     str(int(round(stat_to_ovr(self.air_yds_throw, c.air_yds_avg, c.air_yds_jump)))) + " OVR"],
                                     ["STDEV",     str(self.stdev_air_yds_throw) + "don't round",    "NA"],
                                     ["FUM",       str(round(self.fumble_chance, 2)) + "%",          str(int(round(reverse_stat_to_ovr(self.fumble_chance, c.fumble_avg, c.fumble_jump)))) + " OVR"],
                                     ["RUN",       str(round(self.run_dist, 2)) + " yards",          str(int(round(stat_to_ovr(self.run_dist, c.run_avg, c.run_jump)))) + " OVR"], 
                                     ["STDEV",     str(round(self.stdev_run_dist, 2)) + "don't round", "NA"] ])
            else:
                table_data.extend([  ["INT","?","?"],
                                     ["COMP","?","?"],
                                     ["AIR YDS","?","?"],
                                     ["STDEV","?","?"],
                                     ["FUM","?","?"],
                                     ["RUN","?","?"],
                                     ["STDEV","?","?"]   ])                            
        elif pos == "RB":
            if use_overall:
                table_data.extend([  ["BLK",       str(round(self.block_chance, 2)) + "%",           str(int(round(stat_to_ovr(self.block_chance, c.block_chance_avg, c.block_jump)))) + " OVR"],
                                    ["SACK",      str(round(self.sack_allowed_chance, 2)) + "%",    str(int(round(reverse_stat_to_ovr(self.sack_allowed_chance, c.sack_avg, c.sack_jump)))) + " OVR"],
                                    ["FUM",       str(round(self.fumble_chance, 2)) + "%",          str(int(round(reverse_stat_to_ovr(self.fumble_chance, c.fumble_avg, c.fumble_jump)))) + " OVR"],
                                    ["DROP",      str(round(self.drop_chance, 2)) + "%",            str(int(round(reverse_stat_to_ovr(self.drop_chance, c.drop_avg, c.drop_jump)))) + " OVR"],
                                    ["ADOT",      str(round(self.target_dist, 2)) + " yards",       str(int(round(stat_to_ovr(self.target_dist, c.air_yds_avg, c.air_yds_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_target_dist, 2)) + "don't round", "NA"],
                                    ["YAC",       str(round(self.YAC, 2)) + " yards",               str(int(round(stat_to_ovr(self.YAC, c.YAC_avg, c.YAC_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_YAC, 2)) + "don't round",         "NA"],
                                    ["RUN",       str(round(self.run_dist, 2)) + " yards",          str(int(round(stat_to_ovr(self.run_dist, c.run_avg, c.run_jump)))) + " OVR"], 
                                    ["STDEV",     str(round(self.stdev_run_dist, 2)) + "don't round", "NA"] ])    
            else:
                table_data.extend([  ["BLK","?","?"],
                                     ["SACK","?","?"],
                                     ["FUM","?","?"],
                                     ["DROP","?","?"],
                                     ["ADOT","?","?"],
                                     ["STDEV","?","?"],
                                     ["YAC","?","?"],
                                     ["STDEV","?","?"],
                                     ["RUN","?","?"],
                                     ["STDEV","?","?"]   ])  
        elif pos == "WR":
            if use_overall:
                table_data.extend([  ["FUM",       str(round(self.fumble_chance, 2)) + "%",          str(int(round(reverse_stat_to_ovr(self.fumble_chance, c.fumble_avg, c.fumble_jump)))) + " OVR"],
                                    ["DROP",      str(round(self.drop_chance, 2)) + "%",            str(int(round(reverse_stat_to_ovr(self.drop_chance, c.drop_avg, c.drop_jump)))) + " OVR"],
                                    ["ADOT",      str(round(self.target_dist, 2)) + " yards",       str(int(round(stat_to_ovr(self.target_dist, c.air_yds_avg, c.air_yds_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_target_dist, 2)) + "don't round", "NA"],
                                    ["YAC",       str(round(self.YAC, 2)) + " yards",               str(int(round(stat_to_ovr(self.YAC, c.YAC_avg, c.YAC_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_YAC, 2)) + "don't round",         "NA"] ])
            else:
                table_data.extend([  ["FUM","?","?"],
                                     ["DROP","?","?"],
                                     ["ADOT","?","?"],
                                     ["STDEV","?","?"],
                                     ["YAC","?","?"],
                                     ["STDEV","?","?"]  ]) 
        elif pos == "TE":
            if use_overall:
                table_data.extend([  ["BLK",       str(round(self.block_chance, 2)) + "%",           str(int(round(stat_to_ovr(self.block_chance, c.block_chance_avg, c.block_jump)))) + " OVR"],
                                    ["SACK",      str(round(self.sack_allowed_chance, 2)) + "%",    str(int(round(reverse_stat_to_ovr(self.sack_allowed_chance, c.sack_avg, c.sack_jump)))) + " OVR"],
                                    ["FUM",       str(round(self.fumble_chance, 2)) + "%",          str(int(round(reverse_stat_to_ovr(self.fumble_chance, c.fumble_avg, c.fumble_jump)))) + " OVR"],
                                    ["DROP",      str(round(self.drop_chance, 2)) + "%",            str(int(round(reverse_stat_to_ovr(self.drop_chance, c.drop_avg, c.drop_jump)))) + " OVR"],
                                    ["ADOT",      str(round(self.target_dist, 2)) + " yards",       str(int(round(stat_to_ovr(self.target_dist, c.air_yds_avg, c.air_yds_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_target_dist, 2)) + "don't round", "NA"],
                                    ["YAC",       str(round(self.YAC, 2)) + " yards",               str(int(round(stat_to_ovr(self.YAC, c.YAC_avg, c.YAC_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_YAC, 2)) + "don't round",         "NA"] ])
            else:
                table_data.extend([  ["BLK","?","?"],
                                     ["SACK","?","?"],
                                     ["FUM","?","?"],
                                     ["DROP","?","?"],
                                     ["ADOT","?","?"],
                                     ["STDEV","?","?"],
                                     ["YAC","?","?"],
                                     ["STDEV","?","?"]  ]) 
        elif pos == "OL":
            if use_overall:
                table_data.extend([  ["BLK",       str(round(self.block_chance, 2)) + "%",           str(int(round(stat_to_ovr(self.block_chance, c.block_chance_avg, c.block_jump)))) + " OVR"],
                                     ["SACK",      str(round(self.sack_allowed_chance, 2)) + "%",    str(int(round(reverse_stat_to_ovr(self.sack_allowed_chance, c.sack_avg, c.sack_jump)))) + " OVR"] ])
            else:
                table_data.extend([  ["BLK","?","?"],
                                     ["SACK","?","?"]  ]) 
        elif pos == "DL":
            if use_overall:
                table_data.extend([  ["RET",       str(round(self.def_return_dist, 2)) + " yards",   "NA"],
                                    ["STDEV",     str(round(self.stdev_def_return_dist, 2)) + "don't round", "NA"],
                                    ["SACK",      str(round(self.sack_chance, 2)) + "%",            str(int(round(stat_to_ovr(self.sack_chance, c.sack_avg, c.sack_jump)))) + " OVR"],
                                    ["BLK",       str(round(self.blocked_chance, 2)) + "%",         str(int(round(reverse_stat_to_ovr(self.blocked_chance, c.block_chance_avg, c.block_jump)))) + " OVR"],
                                    ["RUN",       str(round(self.run_dist_allowed, 2)) + " yards",  str(int(round(reverse_stat_to_ovr(self.run_dist_allowed, c.run_avg, c.run_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_run_dist_allowed, 2)) + "don't round", "NA"],
                                    ["FF",        str(round(self.ff_chance, 2)) + "%",              str(int(round(stat_to_ovr(self.ff_chance, c.fumble_avg, c.fumble_jump)))) + " OVR"] ])
            else:
                table_data.extend([  ["RET","?","?"],
                                     ["STDEV","?","?"],
                                     ["SACK","?","?"],
                                     ["BLK","?","?"],
                                     ["RUN","?","?"],
                                     ["STDEV","?","?"],
                                     ["FF","?","?"]     ]) 
        elif pos == "LB":
            if use_overall:
                table_data.extend([  ["RET",       str(round(self.def_return_dist, 2)) + " yards",   "NA"],
                                    ["STDEV",     str(round(self.stdev_def_return_dist, 2)) + "don't round", "NA"],
                                    ["SACK",      str(round(self.sack_chance, 2)) + "%",            str(int(round(stat_to_ovr(self.sack_chance, c.sack_avg, c.sack_jump)))) + " OVR"],
                                    ["BLK",       str(round(self.blocked_chance, 2)) + "%",         str(int(round(reverse_stat_to_ovr(self.blocked_chance, c.block_chance_avg, c.block_jump)))) + " OVR"],
                                    ["RUN",       str(round(self.run_dist_allowed, 2)) + " yards",  str(int(round(reverse_stat_to_ovr(self.run_dist_allowed, c.run_avg, c.run_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_run_dist_allowed, 2)) + "don't round", "NA"],
                                    ["FF",        str(round(self.ff_chance, 2)) + "%",              str(int(round(stat_to_ovr(self.ff_chance, c.fumble_avg, c.fumble_jump)))) + " OVR"],
                                    ["PASS",      str(round(self.air_yds_allowed, 2)) + " yards",   str(int(round(reverse_stat_to_ovr(self.air_yds_allowed, c.air_yds_avg, c.air_yds_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_air_yds_allowed, 2)) + "don't round", "NA"],
                                    ["INT",       str(round(self.int_catch_chance, 2)) + "%",       str(int(round(stat_to_ovr(self.int_catch_chance, c.int_avg, c.int_jump)))) + " OVR"],
                                    ["COMP",      str(round(self.complete_chance_allowed, 2)) + "%", str(int(round(reverse_stat_to_ovr(self.complete_chance_allowed, c.complete_avg, c.complete_jump)))) + " OVR"],
                                    ["YAC",       str(round(self.YAC_allowed, 2)) + " yards",       str(int(round(reverse_stat_to_ovr(self.YAC_allowed, c.YAC_avg, c.YAC_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_YAC_allowed, 2)) + "don't round",     "NA"] ])
            else:
                table_data.extend([  ["RET","?","?"],
                                     ["STDEV","?","?"],
                                     ["SACK","?","?"],
                                     ["BLK","?","?"],
                                     ["RUN","?","?"],
                                     ["STDEV","?","?"],
                                     ["FF","?","?"],
                                     ["PASS","?","?"],
                                     ["STDEV","?","?"],
                                     ["INT","?","?"],
                                     ["COMP","?","?"],
                                     ["YAC","?","?"],
                                     ["STDEV","?","?"]   ])
        elif pos == "DB":
            if use_overall:
                table_data.extend([  ["RET",       str(round(self.def_return_dist, 2)) + " yards",   "NA"],
                                    ["STDEV",     str(round(self.stdev_def_return_dist, 2)) + "don't round", "NA"],
                                    ["SACK",      str(round(self.sack_chance, 2)) + "%",            str(int(round(stat_to_ovr(self.sack_chance, c.sack_avg, c.sack_jump)))) + " OVR"],
                                    ["BLK",       str(round(self.blocked_chance, 2)) + "%",         str(int(round(reverse_stat_to_ovr(self.blocked_chance, c.block_chance_avg, c.block_jump)))) + " OVR"],
                                    ["RUN",       str(round(self.run_dist_allowed, 2)) + " yards",  str(int(round(reverse_stat_to_ovr(self.run_dist_allowed, c.run_avg, c.run_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_run_dist_allowed, 2)) + "don't round", "NA"],
                                    ["FF",        str(round(self.ff_chance, 2)) + "%",              str(int(round(stat_to_ovr(self.ff_chance, c.fumble_avg, c.fumble_jump)))) + " OVR"],
                                    ["PASS",      str(round(self.air_yds_allowed, 2)) + " yards",   str(int(round(reverse_stat_to_ovr(self.air_yds_allowed, c.air_yds_avg, c.air_yds_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_air_yds_allowed, 2)) + "don't round", "NA"],
                                    ["INT",       str(round(self.int_catch_chance, 2)) + "%",       str(int(round(stat_to_ovr(self.int_catch_chance, c.int_avg, c.int_jump)))) + " OVR"],
                                    ["COMP",      str(round(self.complete_chance_allowed, 2)) + "%", str(int(round(reverse_stat_to_ovr(self.complete_chance_allowed, c.complete_avg, c.complete_jump)))) + " OVR"],
                                    ["YAC",       str(round(self.YAC_allowed, 2)) + " yards",       str(int(round(reverse_stat_to_ovr(self.YAC_allowed, c.YAC_avg, c.YAC_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_YAC_allowed, 2)) + "don't round",     "NA"] ])
            else:
                table_data.extend([  ["RET","?","?"],
                                     ["STDEV","?","?"],
                                     ["SACK","?","?"],
                                     ["BLK","?","?"],
                                     ["RUN","?","?"],
                                     ["STDEV","?","?"],
                                     ["FF","?","?"],
                                     ["PASS","?","?"],
                                     ["STDEV","?","?"],
                                     ["INT","?","?"],
                                     ["COMP","?","?"],
                                     ["YAC","?","?"],
                                     ["STDEV","?","?"]   ])
        elif pos == "K":
            if use_overall:
                table_data.extend([  ["RANGE",     str(int(round(self.fg_range))) + " yards",        str(int(round(stat_to_ovr(self.fg_range, c.fg_range_avg, c.fg_range_jump)))) + " OVR"],
                                    ["PCT",       str(round(self.fg_made_chance, 2)) + "%",         str(int(round(stat_to_ovr(self.fg_made_chance, c.fg_chance_avg, c.fg_chance_jump)))) + " OVR"],
                                    ["PUNT",      str(round(self.punt_dist, 2)) + " yards",         str(int(round(stat_to_ovr(self.punt_dist, c.punt_avg, c.punt_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_punt_dist, 2)) + "don't round", "NA"],
                                    ["RET",       str(round(self.kick_return_allowed, 2)) + " yards", str(int(round(reverse_stat_to_ovr(self.kick_return_allowed, c.return_avg, c.return_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_kick_return_allowed, 2)) + "don't round", "NA"],
                                    ["TB",        str(round(self.touchback_forced_chance, 2)) + "%", str(int(round(stat_to_ovr(self.touchback_forced_chance, c.touchback_avg, c.touchback_jump)))) + " OVR"],
                                    ["PIN",       str(round(self.pin_chance, 2)) + "%",            str(int(round(stat_to_ovr(self.pin_chance, c.pin_avg, c.pin_jump)))) + " OVR"],
                                    ["ONSIDE",    str(round(self.onside_kick_chance, 2)) + "%",    str(int(round(stat_to_ovr(self.onside_kick_chance, c.onside_avg, c.onside_jump)))) + " OVR"] ])
            else:
                table_data.extend([  ["RANGE","?","?"],
                                     ["PCT","?","?"],
                                     ["PUNT","?","?"],
                                     ["STDEV","?","?"],
                                     ["RET","?","?"],
                                     ["STDEV","?","?"],
                                     ["TB","?","?"],
                                     ["PIN","?","?"],
                                     ["ONSIDE","?","?"]  ])
        elif pos == "RT":
            if use_overall:
                table_data.extend([  ["RET",       str(round(self.kick_return_dist, 2)) + " yards",  str(int(round(stat_to_ovr(self.kick_return_dist, c.return_avg, c.return_jump)))) + " OVR"],
                                    ["STDEV",     str(round(self.stdev_kick_return_dist, 2)) + "don't round", "NA"],
                                    ["TB",        str(round(self.touchback_chance, 2)) + "%", str(int(round(reverse_stat_to_ovr(self.touchback_chance, c.touchback_avg, c.touchback_jump)))) + " OVR"],
                                    ["FUM",       str(round(self.fumble_chance, 2)) + "%",          str(int(round(reverse_stat_to_ovr(self.fumble_chance, c.fumble_avg, c.fumble_jump)))) + " OVR"] ])
            else:
                table_data.extend([  ["RET","?","?"],
                                     ["STDEV","?","?"],
                                     ["TB","?","?"],
                                     ["FUM","?","?"]   ])
        table_data.append( ["LOYALTY", "NA", self.loyalty] )
        draw_table(["Trait", "Value", "OVR"], [80, 100, 50], 20, table_data, x + 5, y + 225)
        x += 100
        ls.draw_player_stats(self, x + 475, y - 5)
        self.draw_buttons(x, y)
        
                    
    def draw_player(self, x, y, real_ovr, sf, pos = "NONE", use_ovr = "NONE"):
        if pos == "NONE":
            pos = self.position
        self.draw_player_scouting(x, y, real_ovr, sf, "NONE", pos, use_ovr)
    
    def draw_player_scouting(self, x, y, real_ovr, sf, scouting, pos = "NONE", use_ovr = "NONE"):
        global use_overall
        if use_ovr == "NONE":
            use_ovr = use_overall
        fill(150)
        if pos == "NONE":
            pos = self.position
        ovr = 0
        if real_ovr:
            ovr = self.get_overall(pos, use_ovr)
        else:
            ovr = self.projected_ovr
        if ovr < 60:
            fill(150, 75, 50)
        elif ovr < 70:
            fill(200, 200, 200)
        elif ovr < 80:
            fill(150, 150, 25)
        elif ovr < 90:
            fill(200,100,100)
        elif ovr < 100:
            fill(100,100,200)
        if not real_ovr and ovr + 10 < self.overall(use_ovr) and scouting in {"TOP BLUE", "FULL BLUE"}:
            fill(100,100,255)
        elif not real_ovr and ovr + 5 < self.overall(use_ovr) and scouting in {"TOP BLUE", "FULL BLUE", "TOP RED", "FULL RED"}:
            fill(255,100,100)
        elif not real_ovr and ovr - 10 > self.overall(use_ovr) and scouting in {"FULL BLUE"}:
            fill(100,100,255)
        elif not real_ovr and ovr - 5 > self.overall(use_ovr) and scouting in {"FULL RED", "FULL BLUE"}:
            fill(255,100,100)
        rect(x,y, 140*sf, 165*sf, 7*sf)
        fill(0)
        textSize(20*sf)
        text(self.name(), x + 5*sf, y + 5*sf, 135*sf, 50*sf)
        info = "\n"
        if self.years_played == 0:
            info += "R"
        if self.depth > 0:
            info += "Start"
        elif self.depth < 0:
            info += "Bench"
        if self.get_button("GOOD").highlight:
            info += "+"
        if self.get_button("BAD").highlight:
            info += "-"
        textSize(15*sf)
        text(info, x + 10*sf, y + 10*sf, 135*sf, 50*sf)
        words = ""
        if self.injured:
            words += "Inj: " + str(self.injury_length) + " games\n"
        if self.contract_length > 0:
            words += "$" + str(round(self.contract_amount/1000000.0, 2)) + " mil"
        #if not real_ovr:
            #words += str(int(round(self.get_value_proj(True))))
        elif real_ovr:
            words += "Min: $" + str(round(self.min_contract()/1000000.0, 2)) + " mil"
        if real_ovr == True:
            text("POSITION: " + str(self.position) + "\nOVR: " + str(int(round(self.get_overall(pos, use_ovr)))) + "\nAGE: " + str(self.age) + "\n" + words, x + 15*sf, y + 60*sf, 135*sf, 100*sf)
        else:
            text("POSITION: " + str(self.position) + "\nPROJ OVR: " + str(int(round(self.projected_ovr))) + "\nAGE: " + str(self.age) + "\n" + words, x + 15*sf, y + 60*sf, 135*sf, 100*sf)
        if self.upgrade_available():
            fill(85,85,255)
            circle(x + 20*sf, y + 150*sf, 20*sf)
        if self.contract_length <= 0:
            fill(255, 255, 0)
            circle(x + 120*sf, y + 150*sf, 20*sf)
        elif self.contract_length == 1:
            fill(200, 0, 200)
            circle(x + 120*sf, y + 150*sf, 20*sf)
        if self.injured:
            fill(255, 85, 85)
            circle(x + 70*sf, y + 150*sf, 20*sf)
        if self.will_negotiate():
            fill(0, 200, 0)
            circle(x + 120*sf, y + 40*sf, 15*sf)
    
    def upgrade_player(self, type, amount, upgrade_type, use_xp):
        global c, use_overall
        cost = self.xp_for_upgrade()
        ovr = self.overall(use_overall)
        if ((self.upgrade_available() and use_xp) or not use_xp) and (amount < 0 or ovr < 99):
            if use_xp and not type == "injury":
                self.xp -= cost
            up_amount = 1
            if upgrade_type == "BAD":
                up_amount = 0.5
            if upgrade_type == "GOOD":
                up_amount = 2
            up_amount *= amount
            if ovr > 98 and up_amount > 1:
                up_amount = 1
            if type == "injury":
                if not use_xp:
                    self.injury_chance -= c.injury_jump*up_amount
                if self.injury_chance <= 0.0001:
                    self.injury_chance = 0.0001
            elif type == "block chance":
                self.block_chance += c.block_jump*up_amount
            elif type == "sack allowed chance":        
                self.sack_allowed_chance -= c.sack_jump*up_amount
            elif type == "int throw":
                self.int_chance -= c.int_jump*up_amount
            elif type == "complete chance":
                self.complete_chance += c.complete_jump*up_amount
            elif type == "air yds throw":
                self.air_yds_throw += c.air_yds_jump*up_amount
            elif type == "fumble chance":
                self.fumble_chance -= c.fumble_jump*up_amount
            elif type == "drop chance":
                if self.drop_chance <= 0.01:
                    self.xp += cost
                else:
                    self.drop_chance -= c.drop_jump*up_amount
                if self.drop_chance <= 0.01:
                    self.drop_chance = 0.01
            elif type == "target dist":
                self.target_dist += c.air_yds_jump*up_amount
            elif type == "yac":
                self.YAC += c.YAC_jump*up_amount
            elif type == "run dist":
                self.run_dist += c.run_jump*up_amount
            elif type == "air yds allowed":
                self.air_yds_allowed -= c.air_yds_jump*up_amount
            elif type == "int catch chance":
                self.int_catch_chance += c.int_jump*up_amount
            elif type == "complete chance allowed":
                self.complete_chance_allowed -= c.complete_jump*up_amount
            elif type == "yac allowed":
                self.YAC_allowed -= c.YAC_jump*up_amount
            elif type == "sack chance":
                self.sack_chance += c.sack_jump*up_amount
            elif type == "blocked chance":
                self.blocked_chance -= c.block_jump*up_amount
            elif type == "run dist allowed":
                self.run_dist_allowed -= c.run_jump*up_amount
            elif type == "ff chance":
                self.ff_chance += c.fumble_jump*up_amount
            elif type == "fg range":
                if self.fg_range > 64:
                    self.xp += cost
                else:
                    self.fg_range += c.fg_range_jump*up_amount
            elif type == "fg made chance":
                self.fg_made_chance += c.fg_chance_jump*up_amount
            elif type == "punt dist":
                if self.punt_dist > 69:
                    self.xp+= cost
                else:
                    self.punt_dist += c.punt_jump*up_amount
            elif type == "kick return allowed":
                self.kick_return_allowed -= c.return_jump*up_amount
            elif type == "tb forced chance":
                self.touchback_forced_chance += c.touchback_jump*up_amount
            elif type == "pin chance":
                self.pin_chance += c.pin_jump*up_amount
            elif type == "kick return dist":
                self.kick_return_dist += c.return_jump*up_amount
            elif type == "tb chance":
                self.touchback_chance -= c.touchback_jump*up_amount
            elif type == "onside kick":
                self.onside_kick_chance += c.onside_jump*up_amount
            else:
                println("ERROR in upgrade player: " + type)
        
    def overall(self, using_ovr):
        return self.get_overall(self.position, using_ovr)
    
    def get_overall(self, pos, using_ovr):
        global c, season1
        if not using_ovr:
            try:
                season1.this_year
            except:
                return 40
            att3 = 1
            if self.years_played < 2:
                att3 = 100
            ovr1, att1 = self.get_stat_rating("YEAR", pos, season1.this_year)
            ovr2, att2 = self.get_stat_rating("YEAR", pos, season1.this_year-1)
            ovr3 = self.projected_ovr
            return divide_maybe_zero_default(ovr1*att1+ovr2*att2+ovr3*att3,att1+att2+att3,40)
        ovr = 0
        if pos == "QB":
            interception = reverse_stat_to_ovr(self.int_chance, c.int_avg, c.int_jump)
            comp = stat_to_ovr(self.complete_chance, c.complete_avg, c.complete_jump)
            yards = stat_to_ovr(self.air_yds_throw, c.air_yds_avg, c.air_yds_jump)
            run = stat_to_ovr(self.run_dist, c.run_avg, c.run_jump)
            fumble = reverse_stat_to_ovr(self.fumble_chance, c.fumble_avg, c.fumble_jump)
            boost = boost_to_ovr(self.dist_effect_complete) + boost_to_ovr(self.dist_effect_complete)
            ovr = ((interception + comp + yards)/3 * (100 - 2)/100) + ((99*run + fumble)/100 * 2)/100 + boost
        if pos == "WR":
            fumble = reverse_stat_to_ovr(self.fumble_chance, c.fumble_avg, c.fumble_jump)
            drop = reverse_stat_to_ovr(self.drop_chance, c.drop_avg, c.drop_jump)
            distance = stat_to_ovr(self.target_dist, c.air_yds_avg, c.air_yds_jump)
            yac = stat_to_ovr(self.YAC, c.YAC_avg, c.YAC_jump)
            boost = boost_to_ovr(self.dist_effect_drop) + boost_to_ovr(self.catch_boost)
            ovr = (3*(drop + distance + yac) + fumble)/10
        if pos == "RB":
            block = stat_to_ovr(self.block_chance, c.block_chance_avg, c.block_jump)
            sack = reverse_stat_to_ovr(self.sack_allowed_chance, c.sack_avg, c.sack_jump)
            fumble = reverse_stat_to_ovr(self.fumble_chance, c.fumble_avg, c.fumble_jump)
            drop = reverse_stat_to_ovr(self.drop_chance, c.drop_avg, c.drop_jump)
            target = stat_to_ovr(self.target_dist, c.air_yds_avg, c.air_yds_jump)
            yac = stat_to_ovr(self.YAC, c.YAC_avg, c.YAC_jump)
            run = stat_to_ovr(self.run_dist, c.run_avg, c.run_jump)
            boost = boost_to_ovr(self.dist_effect_drop) + boost_to_ovr(self.catch_boost)
            ovr = 0.1*(block + sack)/1.9 + 0.55*(run + fumble)/2 + 0.35*(drop + target + yac)/2.98
        if pos == "OL":
            block = stat_to_ovr(self.block_chance, c.block_chance_avg, c.block_jump)
            sack = reverse_stat_to_ovr(self.sack_allowed_chance, c.sack_avg, c.sack_jump)
            ovr = (block + sack)/2
        if pos == "TE":
            block = stat_to_ovr(self.block_chance, c.block_chance_avg, c.block_jump)
            sack = reverse_stat_to_ovr(self.sack_allowed_chance, c.sack_avg, c.sack_jump)
            fumble = reverse_stat_to_ovr(self.fumble_chance, c.fumble_avg, c.fumble_jump)
            drop = reverse_stat_to_ovr(self.drop_chance, c.drop_avg, c.drop_jump)
            target = stat_to_ovr(self.target_dist, c.air_yds_avg, c.air_yds_jump)
            yac = stat_to_ovr(self.YAC, c.YAC_avg, c.YAC_jump)
            boost = boost_to_ovr(self.dist_effect_drop) + boost_to_ovr(self.catch_boost)
            ovr = 0.59*(drop + target + yac)/3 + 0.01*fumble + 0.4*(block + sack)/2
        if pos == "DL":
            pick = stat_to_ovr(self.int_catch_chance, c.int_avg, c.int_jump)
            sack = stat_to_ovr(self.sack_chance, c.sack_avg, c.sack_jump)
            blocked = reverse_stat_to_ovr(self.blocked_chance, c.block_chance_avg, c.block_jump)
            run = reverse_stat_to_ovr(self.run_dist_allowed, c.run_avg, c.run_jump)
            ff = stat_to_ovr(self.ff_chance, c.fumble_avg, c.fumble_jump)
            ovr = 0.9*(sack + blocked + run)/3 + 0.1*ff + 0.01*pick
        if pos == "LB":
            pick = stat_to_ovr(self.int_catch_chance, c.int_avg, c.int_jump)
            sack = stat_to_ovr(self.sack_chance, c.sack_avg, c.sack_jump)
            blocked = reverse_stat_to_ovr(self.blocked_chance, c.block_chance_avg, c.block_jump)
            run = reverse_stat_to_ovr(self.run_dist_allowed, c.run_avg, c.run_jump)
            ff = stat_to_ovr(self.ff_chance, c.fumble_avg, c.fumble_jump)
            pass_yds = reverse_stat_to_ovr(self.air_yds_allowed, c.air_yds_avg, c.air_yds_jump)
            complete = reverse_stat_to_ovr(self.complete_chance_allowed, c.complete_avg, c.complete_jump)
            yac = reverse_stat_to_ovr(self.YAC_allowed, c.YAC_avg, c.YAC_jump)
            ovr = 0.46*(pass_yds + pick + complete + yac)/3.97 + 0.53*(sack + blocked + run)/2.98 + 0.01*ff
        if pos == "DB":
            pick = stat_to_ovr(self.int_catch_chance, c.int_avg, c.int_jump)
            sack = stat_to_ovr(self.sack_chance, c.sack_avg, c.sack_jump)
            blocked = reverse_stat_to_ovr(self.blocked_chance, c.block_chance_avg, c.block_jump)
            run = reverse_stat_to_ovr(self.run_dist_allowed, c.run_avg, c.run_jump)
            ff = stat_to_ovr(self.ff_chance, c.fumble_avg, c.fumble_jump)
            pass_yds = reverse_stat_to_ovr(self.air_yds_allowed, c.air_yds_avg, c.air_yds_jump)
            complete = reverse_stat_to_ovr(self.complete_chance_allowed, c.complete_avg, c.complete_jump)
            yac = reverse_stat_to_ovr(self.YAC_allowed, c.YAC_avg, c.YAC_jump)
            ovr = 0.85*(pass_yds + pick + complete + yac)/4 + 0.04*(sack + blocked)/1.95 + 0.01*ff + 0.1*run
        if pos == "K":
            rang = stat_to_ovr(self.fg_range, c.fg_range_avg, c.fg_range_jump)
            made = stat_to_ovr(self.fg_made_chance, c.fg_chance_avg, c.fg_chance_jump)
            punt = stat_to_ovr(self.punt_dist, c.punt_avg, c.punt_jump)
            ret = reverse_stat_to_ovr(self.kick_return_allowed, c.return_avg, c.return_jump)
            tb = stat_to_ovr(self.touchback_forced_chance, c.touchback_avg, c.touchback_jump)
            pin = stat_to_ovr(self.pin_chance, c.pin_avg, c.pin_jump)
            onside = stat_to_ovr(self.onside_kick_chance, c.onside_avg, c.onside_jump)
            ovr = 0.6*(rang + made + pin)/3 + 0.3*(punt + ret)/2 + 0.05*tb + 0.05*onside
        if pos == "RT":
            ret = stat_to_ovr(self.kick_return_dist, c.return_avg, c.return_jump)
            tb = reverse_stat_to_ovr(self.touchback_chance, c.touchback_avg, c.touchback_jump)
            fumble = reverse_stat_to_ovr(self.fumble_chance, c.fumble_avg, c.fumble_jump)
            ovr = (9*ret + tb + 5*fumble)/15
        return ovr
    
    def get_stat_rating(self, scope, stat, this_year = 0):
        return self.career_stats.get_stat_rating(scope, stat, this_year)
    
    def add_loyalty(self, amount):
        self.loyalty += amount
        if self.loyalty > 99:
            self.loyalty = 99
        elif self.loyalty < 0:
            self.loyalty = 0
                
    def sign_player(self, new_team, contract_len, money_year):
        self.depth = 0
        self.team = new_team
        self.contract_amount = money_year
        self.contract_length = contract_len
        self.is_first_year_of_contract = True
        self.add_loyalty(random(1, contract_len))
    
    def cut_player(self):
        global season1
        if not self.team == "FREE AGENT":
            self.loyalty = min_max_skew(10, 50)
            self.depth = 0
            self.contract_amount = 0
            self.contract_length = 0
            if not self.retired:
                self.team = "FREE AGENT"
                season1.free_agents.add_free_agents([self])
        
    def trade_player(self, new_team):
        self.depth = 0
        self.team = new_team
        self.loyalty = min_max_skew(10, 50)
        
    def get_rating(self):
        pass
        
    def change_position(self, pos):
        self.position = pos
        
    def negotiate(self):
        if self.will_negotiate():
            expected = self.expected_contract()
            earnings = self.career_stats.get_stat("CAREER", "SALARY", 0)
            e_prob = 1 - 9999999.0/earnings
            l_prob = self.loyalty / 100.0
            p_prob = max(0, self.contract_amount / expected - 1)
            rand = random(0, 1)
            if rand < e_prob*l_prob or rand < l_prob**2 or rand < l_prob*p_prob:
                if self.contract_amount > expected:
                    self.contract_amount = expected
                else:
                    self.contract_amount = random(self.min_contract(), self.contract_amount)
                get_team_from_name(self.team).calculate_cap_left()
        
    def will_negotiate(self):
        if self.loyalty < 50 or self.contract_length <= 0:
            return False
        earnings = self.career_stats.get_stat("CAREER", "SALARY", 0)
        if earnings < 10000000:
            return False
        if self.contract_amount <= self.min_contract() + 10000:
            return False
        return True
        
    def expected_contract(self):
        global c, use_overall
        base = 100000 + 100000*self.years_played
        ovr = max(55, self.get_overall(self.position, use_overall))
        bonus = (ovr - 55)**2 * 10000
        multiplier = c.contract_multiplier(self.position)
        if self.years_played == 0:
            multiplier *= 0.5
        return base + bonus*multiplier
    
    def min_contract(self):
        return max(self.confidence*self.expected_contract(), 100000 + 100000*self.years_played)
        
    def adjust_ovr_for_qb(self):
        self.block_chance *= 0.6
        self.sack_allowed_chance *= 1.5
        self.fumble_chance *= 2
        self.drop_chance *= 2
        self.YAC *= 0.25
        self.run_dist *= min_max_skew(0.75, 1.2)
        self.air_yds_allowed *= 2
        self.int_catch_chance *= 0.25
        self.def_return_dist *= 0.2
        self.complete_chance_allowed *= 2
        self.YAC_allowed *= 2
        self.sack_chance *= 0.2
        self.blocked_chance *= 2
        self.run_dist_allowed *= 2
        self.ff_chance *= 0.2
        self.fg_range *= 0.2
        self.fg_made_chance *= 0.2
        self.punt_dist *= min_max_skew(0.2, 0.8)
        self.touchback_forced_chance *= 0.4
        self.pin_chance *= 0.1
        self.kick_return_dist *= 0.2
        self.onside_kick_chance *= 0.2
            
    def adjust_ovr_for_rb(self):
        global c
        self.block_chance -= 7*c.block_jump
        self.sack_allowed_chance += 7*c.block_jump
        self.int_chance *= 5
        self.complete_chance *= 0.5
        self.air_yds_throw *= 0.25
        self.drop_chance += random(2, 8)*c.drop_jump
        self.target_dist -= random(3, 10)*c.air_yds_jump
        self.air_yds_allowed *= 1.5
        self.int_catch_chance *= 0.9
        self.complete_chance_allowed *= 1.2
        self.YAC_allowed *= 1.2
        self.sack_chance *= 0.75
        self.blocked_chance *= 1.25
        self.run_dist_allowed *= 1.4
        self.ff_chance *= 1.5
        self.fg_range *= 0.1
        self.fg_made_chance *= 0.1
        self.punt_dist *= 0.1
        self.touchback_forced_chance *= 0.1
        self.pin_chance *= 0.1
        self.onside_kick_chance *= 0.1 
        
    def adjust_ovr_for_wr(self):
        self.block_chance *= 0.75
        self.sack_allowed_chance /= 0.75
        self.int_chance *= 2
        self.complete_chance *= 0.85
        self.air_yds_throw *= 0.9
        self.target_dist *= 1.1
        self.run_dist *= 0.9
        self.air_yds_allowed *= 1.2
        self.complete_chance_allowed *= 1.3
        self.sack_chance *= 0.5
        self.blocked_chance *= 1.25
        self.run_dist_allowed *= 1.5
        self.ff_chance *= 1.5
        self.fg_range *= 0.1
        self.fg_made_chance *= 0.1
        self.punt_dist *= 0.5
        self.touchback_forced_chance *= 0.4
        self.pin_chance *= 0.1
        self.onside_kick_chance *= 0.1
        
    def adjust_ovr_for_te(self):
        global c
        self.block_chance -= 3*c.block_jump
        self.sack_allowed_chance += 3*c.block_jump
        self.int_chance *= 5 
        self.complete_chance *= 0.5
        self.air_yds_throw *= 0.5
        self.YAC -= 3*c.YAC_jump
        self.run_dist *= 0.75
        self.stdev_run_dist *= 0.5
        self.air_yds_allowed *= 2
        self.def_return_dist *= 0.8
        self.complete_chance_allowed *= 1.4
        self.sack_chance *= 0.8
        self.blocked_chance /= 0.8
        self.run_dist_allowed *= 1.2
        self.ff_chance *= 1.2
        self.fg_range *= 0.1
        self.fg_made_chance *= 0.1
        self.punt_dist *= 0.2
        self.touchback_forced_chance *= 0.3
        self.pin_chance *= 0.1
        self.kick_return_dist *= 0.8
        self.onside_kick_chance *= 0.1
        
    def adjust_ovr_for_ol(self):
        self.int_chance *= 7
        self.complete_chance *= 0.2
        self.air_yds_throw *= 0.3
        self.fumble_chance *= 3
        self.drop_chance *= 5
        self.target_dist *= 0.75
        self.YAC *= 0.4
        self.run_dist *= 0.3
        self.stdev_run_dist *= 0.3
        self.air_yds_allowed *= 2
        self.int_catch_chance *= 0.2
        self.def_return_dist *= 0.3
        self.complete_chance_allowed *= 2
        self.YAC_allowed *= 3
        self.sack_chance *= 0.75
        self.blocked_chance /= 0.75
        self.ff_chance *= 2
        self.fg_range *= 0.01
        self.fg_made_chance *= 0.01
        self.punt_dist *= 0.1
        self.touchback_forced_chance *= 0.1
        self.pin_chance *= 0.01
        self.kick_return_dist *= 0.2
        self.onside_kick_chance *= 0.1
        
    def adjust_ovr_for_dl(self):
        self.block_chance *= 0.8
        self.sack_allowed_chance /= 0.8
        self.int_chance *= 5
        self.complete_chance *= 0.4 
        self.air_yds_throw *= 0.5
        self.fumble_chance *= 3
        self.drop_chance *= 5
        self.target_dist *= 0.5
        self.YAC *= 0.5
        self.run_dist *= 0.2
        self.air_yds_allowed *= 1.2
        self.int_catch_chance *= 0.1
        self.def_return_dist *= 0.4
        self.complete_chance_allowed *= 1.2
        self.YAC_allowed *= 1.3
        self.fg_range *= 0.1
        self.fg_made_chance *= 0.1
        self.punt_dist *= 0.3
        self.touchback_forced_chance *= 0.2
        self.pin_chance *= 0.1
        self.kick_return_dist *= 0.2
        self.onside_kick_chance *= 0.1
        
    def adjust_ovr_for_lb(self):
        global c
        self.block_chance *= 0.6
        self.sack_allowed_chance /= 0.6
        self.int_chance *= 3
        self.complete_chance *= 0.25
        self.air_yds_throw *= 0.75
        self.fumble_chance *= 2
        self.drop_chance *= 5
        self.target_dist *= 0.7 
        self.YAC *= 0.5 
        self.run_dist *= 0.25
        self.complete_chance_allowed += 6*c.complete_jump
        self.YAC_allowed += 3*c.YAC_jump
        self.sack_chance -= 2*c.sack_jump
        self.blocked_chance += 2*c.block_jump
        self.run_dist_allowed += c.run_jump
        self.fg_range *= 0.1
        self.fg_made_chance *= 0.1
        self.punt_dist *= 0.2
        self.touchback_forced_chance *= 0.3
        self.pin_chance *= 0.1
        self.kick_return_dist *= 0.4
        self.onside_kick_chance *= 0.1
        
    def adjust_ovr_for_db(self):
        global c
        self.block_chance *= 0.4
        self.sack_allowed_chance /= 0.4
        self.int_chance *= 3 
        self.complete_chance *= 0.4
        self.air_yds_throw *= 0.8
        self.drop_chance *= 2
        self.run_dist *= 0.5
        self.sack_chance -= 4*c.sack_jump
        self.blocked_chance += 4*c.block_jump
        self.run_dist_allowed += 4*c.run_jump
        self.ff_chance += 4*c.fumble_jump
        self.fg_range *= 0.1
        self.fg_made_chance *=0.1 
        self.punt_dist *= 0.4
        self.touchback_forced_chance *= 0.4
        self.pin_chance *= 0.1
        self.onside_kick_chance *= 0.1
        
    def adjust_ovr_for_k(self):
        self.block_chance *= 0.2
        self.sack_allowed_chance /= 0.2
        self.int_chance *= 3
        self.complete_chance *= 0.75
        self.air_yds_throw *= 0.8
        self.fumble_chance *= 4
        self.drop_chance *= 5
        self.target_dist *= 0.75
        self.YAC *= 0.4
        self.run_dist *= 0.2
        self.air_yds_allowed *= 4
        self.int_catch_chance *= 0.2
        self.def_return_dist *= 0.4
        self.complete_chance_allowed *= 2
        self.YAC_allowed *= 2 
        self.sack_chance *=0.2
        self.blocked_chance /= 0.2
        self.run_dist_allowed *= 0.2
        self.ff_chance *= 0.1
        self.kick_return_dist *= 0.2
        if self.fg_range < 33:
            self.fg_range = 33
        if self.punt_dist < 35:
            self.punt_dist = 35
        
    def adjust_ovr_for_rt(self):
        self.block_chance *= 0.2
        self.sack_allowed_chance /= 0.2
        self.int_chance *= 4
        self.complete_chance *= 0.2
        self.air_yds_throw *= 0.3
        self.drop_chance *= 1.05
        self.target_dist *= 0.9
        self.YAC *= 1.05
        self.run_dist *= 0.8
        self.air_yds_allowed *= 2
        self.int_catch_chance *= 0.9
        self.def_return_dist *= 1.05
        self.complete_chance_allowed *= 1.25
        self.YAC_allowed *= 1.15
        self.sack_chance *= 0.3
        self.blocked_chance /= 0.3
        self.run_dist_allowed *= 1.5
        self.ff_chance *= 0.2
        self.fg_range *= 0.1
        self.fg_made_chance *= 0.1
        self.punt_dist *= 0.3
        self.pin_chance *= 0.1
        self.kick_return_dist *= 1.07
            
    
    def fix_chances(self, ovr):
        """
        if self.block_chance <= 0:
            self.block_chance = 1
        elif self.block_chance >= 100:
            self.block_chance = 99
        if self.sack_allowed_chance <= 0:
            self.sack_allowed_chance = 1
        elif self.sack_allowed_chance >= 100:
            self.sack_allowed_chanc = 99
        if self.injury_chance <= 0:
            self.injury_chance = 0.001
        elif self.injury_chance >= 100:
            self.injury_chance = 99
        if self.int_chance <= 0:
            self.int_chance = 0.01
        if self.complete_chance <= 0:
            self.complete_chance = 1
        if self.int_chance + self.complete_chance >= 100:
            self.complete_chance = (self.complete_chance / (self.int_chance + self.complete_chance))*99.0
            self.int_chance = (self.int_chance / (self.int_chance + self.complete_chance))*99.0
        if self.fumble_chance <= 0:
            self.fumble_chance = 0.01
        elif self.fumble_chance >= 100:
            self.fumble_chance = 0.99
        """
        if self.drop_chance <= 0:
            self.drop_chance = 0.1
        """
        elif self.drop_chance >= 100:
            self.drop_chance = 99
        if self.int_catch_chance <= 0:
            self.int_catch_chance = 0.1
        if self.complete_chance_allowed <= 0:
            self.complete_chance_allowed = 1
        if self.complete_chance_allowed + self.int_catch_chance >= 100:
            self.complete_chance_allowed = (self.complete_chance_allowed / (self.complete_chance_allowed + self.int_catch_chance))*99.0
            self.int_catch_chance = (self.int_catch_chance / (self.complete_chance_allowed + self.int_catch_chance))*99.0
        if self.sack_chance <= 0:
            self.sack_chance = 1
        elif self.sack_chance >= 100:
            self.sack_chance = 99
        if self.blocked_chance <= 0:
            self.blocked_chance = 1
        elif self.blocked_chance >= 100:
            self.blocked_chance = 99
        if self.ff_chance <= 0:
            self.ff_chance = 0.01
        elif self.ff_chance >= 100:
            self.ff_chance = 99
        if self.fg_range > 65:
            self.fg_range = 65
        if self.fg_made_chance <= 0:
            self.fg_made_chance = 1
        elif self.fg_made_chance >= 100:
            self.fg_made_chance = 99
        if self.touchback_forced_chance <= 0:
            self.touchback_forced_chance = 1
        elif self.touchback_forced_chance >= 100:
            self.touchback_forced_chance = 99
        if self.pin_chance <= 0:
            self.pin_chance = 0.1
        elif self.pin_chance >= 100:
            self.pin_chance = 99
        if self.touchback_chance <= 0:
            self.touchback_chance = 1
        elif self.touchback_chance >= 100:
            self.touchback_chance = 99
        if self.punt_dist > 70:
            self.punt_dist = 70
        """
        if not self.overall(True) == ovr:
            self.change_overall( ovr - self.overall(True) )
    
    def add_stats(self, type, amount, game_type, this_year):
        global c, ls
        self.career_stats.add_stat(type, amount, game_type, this_year)
        
        xp_boost =            c.stat_xp(type) * amount
        game_multiplier =     c.game_xp_multiplier(game_type)
        position_multiplier = c.position_xp_multiplier(self.position)
        total_xp =            max(0, xp_boost * position_multiplier * game_multiplier)
        
        self.xp += total_xp
        ls.add_xp(self.position, total_xp)
        fat = c.fatigue_calc(total_xp, self.position, self.stamina)
        self.fatigue += fat
        self.change_overall(-fat)
        ls.add_fatigue(self.position, fat)
            
    def reset_game_stats(self):
        self.career_stats.reset_game_stats()
    
    """def reset_season_stats(self):
        self.run_stats[1] = [0]*5
        self.receive_stats[1] = [0]*9
        self.throw_stats[1] = [0]*9
        self.block_stats[1] = [0]*2
        self.cover_stats[1] = [0]*13
        self.blitzer_stats[1] = [0]*10
        self.xp_stats[1] = [0]*2
        self.fg_stats[1] = [0]*4
        self.punt_stats[1] = [0]*4
        self.return_stats[1] = [0]*5"""
    

################################################################################PLAYER CLASS###########################################################################################
################################################################################PLAYER CLASS###########################################################################################
################################################################################PLAYER CLASS###########################################################################################
################################################################################PLAYER CLASS###########################################################################################


################################################################################TEAM CLASS###########################################################################################
################################################################################TEAM CLASS###########################################################################################
################################################################################TEAM CLASS###########################################################################################
################################################################################TEAM CLASS###########################################################################################

class Team(object):
    
    def __init__(self, name, place, abbrv):
        global use_overall
        self.is_all_star_team =        False
        #self.all_stars_selected =      0
        self.show_overall =            use_overall
        self.team_name =               name
        self.team_location =           place
        self.abbreviation =            abbrv
        self.ready_to_advance =        True
        self.xp =                      0
        #self.cash =                    0
        self.max_cap =                 200000000
        self.cap_left =                200000000
        #self.stadium_level =           0
        #self.fans =                    0
        self.scouting =                "NONE"
        self.negotiations =            10
        self.resignings =              3
        self.fa_bids =                 0
        self.fas =                     0
        self.fa_pos =                  []
        self.draft_picks =             [[1, abbrv, 1966], [2, abbrv, 1966], [3, abbrv, 1966], [4, abbrv, 1966], [5, abbrv, 1966], [6, abbrv, 1966], [7, abbrv, 1966], [1, abbrv, 1967], [2, abbrv, 1967], [3, abbrv, 1967], [4, abbrv, 1967], [5, abbrv, 1967], [6, abbrv, 1967], [7, abbrv, 1967]]
        self.user_type =              "AUTO"
        self.qb1 =                     Player("QB", 20)
        self.qb2 =                     Player("QB", 20)
        self.rb1 =                     Player("RB", 20)
        self.rb2 =                     Player("RB", 20)
        self.rb3 =                     Player("RB", 20)
        self.wr1 =                     Player("WR", 20)
        self.wr2 =                     Player("WR", 20)
        self.wr3 =                     Player("WR", 20)
        self.wr4 =                     Player("WR", 20)
        self.te1 =                     Player("TE", 20)
        self.te2 =                     Player("TE", 20)
        self.te3 =                     Player("TE", 20)
        self.ol1 =                     Player("OL", 20)
        self.ol2 =                     Player("OL", 20)
        self.ol3 =                     Player("OL", 20)
        self.ol4 =                     Player("OL", 20)
        self.ol5 =                     Player("OL", 20)
        self.ol6 =                     Player("OL", 20)
        self.dl1 =                     Player("DL", 20)
        self.dl2 =                     Player("DL", 20)
        self.dl3 =                     Player("DL", 20)
        self.dl4 =                     Player("DL", 20)
        self.dl5 =                     Player("DL", 20)
        self.dl6 =                     Player("DL", 20)
        self.dl7 =                     Player("DL", 20)
        self.lb1 =                     Player("LB", 20)
        self.lb2 =                     Player("LB", 20)
        self.lb3 =                     Player("LB", 20)
        self.lb4 =                     Player("LB", 20)
        self.lb5 =                     Player("LB", 20)
        self.db1 =                     Player("DB", 20)
        self.db2 =                     Player("DB", 20)
        self.db3 =                     Player("DB", 20)
        self.db4 =                     Player("DB", 20)
        self.db5 =                     Player("DB", 20)
        self.db6 =                     Player("DB", 20)
        self.db7 =                     Player("DB", 20)
        self.k =                       Player("K", 20)
        self.rt =                      Player("RT", 20)
        # all the starters
        self.line_up =                 [self.qb1, self.qb2, self.rb1, self.rb2, self.rb3, self.wr1, self.wr2, self.wr3, self.wr4, self.te1, self.te2, self.te3, self.ol1, self.ol2, self.ol3, self.ol4, self.ol5, self.ol6, self.dl1, self.dl2, self.dl3, self.dl4, self.dl5, self.dl6, self.dl7, self.lb1, self.lb2, self.lb3, self.lb4, self.lb5, self.db1, self.db2, self.db3, self.db4, self.db5, self.db6, self.db7, self.k, self.rt]
        # players on the bench
        self.bench =                   []
        # all players on the team
        self.Players =                 []
        self.max_offer =               0
        self._calculate_max_offer()
        self.qb =                      0
        self.rb =                      0
        self.wr =                      0
        self.te =                      0
        self.ol =                      0
        self.dl =                      0
        self.lb =                      0
        self.db =                      0
        self.k_ovr =                   0
        self.rt_ovr =                  0
        self.offense =                 0
        self.defense =                 0
        self.special =                 0
        self.biggest_needs =           [0,0,0,0,0,0,0,0,0,0]
        self.career_stats =            Stats()
        #self.record_stats =            [[c.wins, c.losses - 1, c.ties - 2, c.seasons - 3, c.superbowls - 4], [c.wins, c.losses - 1, c.ties - 2, c.seasons - 3, c.superbowls - 4], [c.wins, c.losses - 1, c.ties - 2, c.seasons - 3, c.superbowls - 4], [c.wins, c.losses - 1, c.ties - 2, c.seasons - 3, c.superbowls - 4] ]
        self.standings_data =          [self.name(), 0,0,0,0.000,0,0]
        self.season_records =          []
        self.div_finish =              []
        self.pass_chance =                 random(58, 67)
        self.man_chance =                  random(30,70)
        self.offense_formation_chance =    [25, 25, 25, 25]
        self.defense_formation_chance =    [17, 17, 17, 17, 16, 16]
        self.blitzers_chance =             [50, 25, 20, 5]
        self.plays_per_game =              random(115, 140)
        self.fourth_down_attempt_chance =  random(0,25)
        self.fourth_down_attempt_dist =    random(0,3)
        self.fave_targets =                [16, 19, 25, 17, 0, 8, 15]
        self.scramble_chance =             2
        self.rb1_chance =                  70
        self.numbers_scope =               "GAME"
        self.numbers_table_sort =          0
        self.numbers_sort_order =          False
        self.o_form =                      "i"
        self.d_form =                      "3-4"
        self.buttons =                     []
        self.set_buttons()
        
        
    def set_buttons(self):
        global use_overall
        x = 1100
        y = 75
        self.buttons.append( Button(x, y, 5, 5, "TOGGLE", "TOGGLE", "TEAM VIEW") )
        self.buttons[0].highlight = use_overall
        
    def get_stat_rating(self, scope, stat, this_year = 0):
        return self.career_stats.get_stat_rating(scope, stat, this_year)
        
    def cap_used(self):
        used = 0
        for player in self.Players:
            used += player.contract_amount
        return used
    
    def draft_in_value(self, player, is_projected):
        mul = 1.0
        if player.position in self.full_positions():
            mul = 0.5
        return mul*self.trade_in_value_proj(player, is_projected)
    
    def trade_in_value(self, player):
        return self.trade_in_value_proj(player, False)
        
    def trade_in_value_proj(self, player, is_projected):
        ovr = self.get_team_overall()
        if player.position == "QB":
            diff = self.qb - ovr
        elif player.position == "RB":
            diff = self.rb - ovr
        elif player.position == "WR":
            diff = self.wr - ovr
        elif player.position == "TE":
            diff = self.te - ovr
        elif player.position == "OL":
            diff = self.ol - ovr
        elif player.position == "DL":
            diff = self.dl - ovr
        elif player.position == "LB":
            diff = self.lb - ovr
        elif player.position == "DB":
            diff = self.db - ovr
        elif player.position == "K":
            diff = self.k_ovr - ovr
        elif player.position == "RT":
            diff = self.rt_ovr - ovr
        return player.get_value_proj(is_projected) * min((1 - diff/100.0)**3, 1.25)
        
    def trade_out_value(self, player):
        ovr = self.get_team_overall()
        if player.position == "QB":
            diff = self.qb - ovr
        elif player.position == "RB":
            diff = self.rb - ovr
        elif player.position == "WR":
            diff = self.wr - ovr
        elif player.position == "TE":
            diff = self.te - ovr
        elif player.position == "OL":
            diff = self.ol - ovr
        elif player.position == "DL":
            diff = self.dl - ovr
        elif player.position == "LB":
            diff = self.lb - ovr
        elif player.position == "DB":
            diff = self.db - ovr
        elif player.position == "K":
            diff = self.k_ovr - ovr
        elif player.position == "RT":
            diff = self.rt_ovr - ovr
        return player.get_value() * min((diff/100.0 - 1), 0.93)
        
    def average_age(self):
        if len(self.Players) == 0:
            return 0
        age = 0.0
        for player in self.Players:
            age += player.age
        age /= len(self.Players)
        return age
    
    def get_team_value(self):
        val = 0
        for player in self.Players:
            val += player.get_value()
        return val

    def name(self):
        return self.team_location + " " + self.team_name
        
    def draw_team_formations(self, formation, x, y, flip):
        multy = 1
        if not flip:
            multy = -1
        textSize(20)
        if formation in ["goal line o", "i", "singleback", "spread"]:
            text("WR1", x, y)
            text("OL\nOL\nOL\nOL\nOL", x, y + 80)
            if formation == "goal line o":
                text("QB", x - 30 * multy, y + 140)
                text("RB2", x - 70 * multy, y + 140)
                text("RB1", x - 110 * multy, y + 140)
                text("TE1", x - 20 * multy, y + 60)
                text("TE2", x - 20 * multy, y + 220)
            elif formation == "i":
                text("QB", x - 30 * multy, y + 140)
                text("RB2", x - 70 * multy, y + 140)
                text("RB1", x - 110 * multy, y + 140)
                text("TE1", x - 20 * multy, y + 60)
                text("WR2", x, y + 250)
            elif formation == "singleback":
                text("QB", x - 70 * multy, y + 140)
                text("WR3", x - 20 * multy, y + 230)
                text("RB1", x - 70 * multy, y + 160)
                text("TE1", x - 20 * multy, y + 60)
                text("WR2", x, y + 250)
            elif formation == "spread":
                text("QB", x - 70 * multy, y + 140)
                text("WR3", x - 20 * multy, y + 230)
                text("RB1", x - 70 * multy, y + 160)
                text("TE1", x - 20 * multy, y + 60)
                text("WR2", x, y + 250)
        elif formation in ["goal line d", "3-4", "4-3", "nickel", "dime", "quarter"]:
            text("DB", x, y)
            text("DB", x, y + 250)
            if formation == "goal line d":
                text("DL\nDL\nDL\nDL\nDL", x, y + 80)
                text("LB\nLB\nLB\nLB", x + 40 * multy, y + 90)
            elif formation == "3-4":
                text("DL\nDL\nDL", x, y + 110)
                text("LB\nLB\nLB\nLB", x + 40 * multy, y + 90)
                text("DB", x + 60 * multy, y + 20)
                text("DB", x + 60 * multy, y + 230)
            elif formation == "4-3":
                text("DL\nDL\nDL\nDL", x, y + 90)
                text("LB\nLB\nLB", x + 40 * multy, y + 110)
                text("DB", x + 60 * multy, y + 20)
                text("DB", x + 60 * multy, y + 230)
            elif formation == "nickel":
                text("DL\nDL\nDL\nDL", x, y + 90)
                text("LB\nLB", x + 40 * multy, y + 130)
                text("DB", x + 60 * multy, y + 20)
                text("DB", x + 60 * multy, y + 230)
                text("DB", x, y + 230)
            elif formation == "dime":
                text("DL\nDL\nDL\nDL", x, y + 90)
                text("LB", x + 40 * multy, y + 140)
                text("DB", x + 60 * multy, y + 20)
                text("DB", x + 60 * multy, y + 230)
                text("DB", x, y + 230)
                text("DB", x, y + 60)
            elif formation == "quarter":
                text("DL\nDL\nDL", x, y + 110)
                text("LB\nLB", x + 40 * multy, y + 130)
                text("DB", x + 60 * multy, y + 20)
                text("DB", x + 60 * multy, y + 230)
                text("DB", x, y + 230)
                text("DB", x, y + 60)
        
    def draw_team_summary(self, x, y):
        ovr = self.get_team_overall()
        if not self.full_team_yn():
            fill(150)
        elif ovr < 65:
            r = 175 + 5 * (ovr - 50)
            fill(max(r, 150), 20, 20)
        elif ovr < 80:
            rg = 105 + 10 * (ovr - 65)
            fill(rg, rg, 0)
        elif ovr < 90:
            g = 255 - 10 * (ovr - 80)
            fill(0, g, 0)
        elif ovr < 100:
            b = 255 - 10 * (ovr - 90)
            fill(0, 0, b)
        rect(x, y, 195, 195, 7)
        fill(0)
        textSize(25)
        text(self.name(), x + 5, y + 5, 185, 80)
        textSize(15)
        text("OVR: " + str(int(round(ovr))), x + 5, y + 95)
        text("OFF OVR: " + str(int(round(self.offense))), x + 5, y + 115)
        text("DEF OVR: " + str(int(round(self.defense))), x + 5, y + 135)
        if is_number(self.cap_left):
            text("Cap: $" + str(round(self.cap_left/1000000.0, 2)) + " million", x + 5, y + 155)
        text("Players: " + str(len(self.Players)), x + 5, y + 175)
            
    def __draw_player(self, player, x, y, real_ovr, scal, pos = "NONE"):
        try:
            player.draw_player(x, y, real_ovr, scal, pos, self.show_overall)
        except:
            text("EMPTY", x, y)
            
    def get_clicked(self, x, y, team_phase, mouse_x, mouse_y):
        if team_phase == "TRADE":
            x_off = mouse_x - x
            y_off = mouse_y - y
            x_across = int(x_off / 150)
            y_down = int(y_off / 175)
            if y_down >= 0 and y_down < 10:
                positions = ["QB", "RB", "WR", "TE", "OL", "DL", "LB", "DB", "K", "RT"]
                position = positions[y_down]
                at_pos = []
                for player in self.Players:
                    if player.position == position and player.is_tradeable():
                        at_pos.append(player)
                if x_across >= 0 and x_across < len(at_pos):
                    return at_pos[x_across]
            else:
                y_down = int(y_off - 10*175 - 10)/40
                if y_down >= 0 and y_down < len(self.draft_picks):
                    return self.draft_picks[y_down]
        return "NONE"            
    
    def draw_team(self, x, y, team, sort_type, sort_reverse):
        global c, season1, user_teams, use_overall
        textSize(25)
        text(self.name() + ": " + str(int(round(self.get_team_overall()))) + " OVR", x, y - 65)
        fill(150)
        rect(x + 400, y - 75, 50, 50, 7)
        fill(0)
        text("$", x + 400, y - 75, 50, 50)
        fill(150)
        rect(x + 450, y - 75, 150, 50, 7)
        fill(0)
        text("STRATEGY", x + 450, y - 75, 150, 50)
        fill(150)
        rect(x + 600, y - 75, 150, 50, 7)
        fill(0)
        text("OFFENSE", x + 600, y - 75, 150, 50)
        fill(150)
        rect(x + 750, y - 75, 150, 50, 7)
        fill(0)
        text("DEFENSE", x + 750, y - 75, 150, 50)
        fill(150)
        rect(x + 900, y - 75, 150, 50, 7)
        fill(0)
        text("SPECIAL", x + 900, y - 75, 150, 50)
        fill(150)
        rect(x + 1050, y - 75, 50, 50, 7)
        fill(0)
        text("#s", x + 1050, y - 75, 50, 50)
        fill(150)
        rect(x + 1100, y - 75, 150, 50, 7)
        fill(0)
        text("BEST LINEUP", x + 1100, y - 75, 150, 50)
        textSize(25)
        button_draw(self.buttons, "ALL")
        if team == "TRADE":
            x_val = x
            y_val = y
            for position in ["QB", "RB", "WR", "TE", "OL", "DL", "LB", "DB", "K", "RT"]:
                for player in self.Players:
                    if player.position == position and player.is_tradeable():
                        player.draw_player(x_val, y_val, True, 1, use_ovr = self.show_overall)
                        x_val += 150
                y_val += 175
                x_val = x
            y_val += 40
            for pick in self.draft_picks:
                textSize(30)
                text("Round " + str(pick[0]) + ", pick " + str(pick[1]) + ", " + str(pick[2]), x_val, y_val)
                y_val += 40
        elif team == "MORE":
            fill(150)
            rect(x + 1100, y - 25, 150, 50, 7)
            fill(0)
            if self.user_type == "AUTO":
                text("USER", x + 1100, y - 25, 150, 50)
            else:
                text("AUTO", x + 1100, y - 25, 150, 50)
            textSize(20)
            text("QB: " + str(int(self.qb)), x + 1100, y + 50)
            text("RB: " + str(int(self.rb)), x + 1100, y + 75)
            text("WR: " + str(int(self.wr)), x + 1100, y + 100)
            text("TE: " + str(int(self.te)), x + 1100, y + 125)
            text("OL: " + str(int(self.ol)), x + 1100, y + 150)
            text("DL: " + str(int(self.dl)), x + 1100, y + 175)
            text("LB: " + str(int(self.lb)), x + 1100, y + 200)
            text("DB: " + str(int(self.db)), x + 1100, y + 225)
            text("K:  " + str(int(self.k_ovr)), x + 1100, y + 250)
            text("RT: " + str(int(self.rt_ovr)), x + 1100, y + 275)
            text("Draft picks: ", x + 1100, y + 325)
            self.draft_picks.sort(key = lambda l: (by_list_index(l,2), -season1.draft_pick_value(l)), reverse = False)
            offset = 0
            for pick in self.draft_picks:
                text("     Round " + str(pick[0]) + ", pick " + str(pick[1]) + ", " + str(pick[2]) + ", value: " + str(int(season1.draft_pick_value(pick))), x + 1100, y + 350 + 25*offset)
                offset += 1
            if is_number(self.cap_left):
                text("Cap remaining: " + str(round(self.cap_left/1000000.0, 2)) + " million", x + 5, y - 25)
            else:
                text("Cap used: " + str(round(self.cap_used()/1000000, 2)) + " million", x + 5, y - 25)
            text("FA Bidding: " + str(round(self.fa_bids/1000000.0, 2)) + " million, " + str(self.fas) + " players", x + 500, y + 5)
            text("XP: " + str(int(self.xp)), x + 5, y + 5)
            if is_number(self.max_offer):
                text("Max Offer: " + str(round(self.max_offer/1000000.0, 2)) + " million", x + 125, y + 5)
            else:
                text("Max Offer: NA", x + 125, y + 5)
            text("Players: " + str(len(self.Players)) + " Age: " + str(round(self.average_age(), 2)) + " Negotiations: " + str(self.negotiations) + " Resigns: " + str(self.resignings), x + 5, y + 30)
            table_info = []
            text("SB:       " + str(self.career_stats.get_stat("SB CAREER", "WINS", season1.this_year))      + "-" + str(self.career_stats.get_stat("SB CAREER", "LOSSES", season1.this_year)),      675, 50 + scroll)
            text("Playoffs: " + str(self.career_stats.get_stat("PLAYOFF CAREER", "WINS", season1.this_year)) + "-" + str(self.career_stats.get_stat("PLAYOFF CAREER", "LOSSES", season1.this_year)), 675, 75 + scroll)
            text("Regular:  " + str(self.career_stats.get_stat("REGULAR CAREER", "WINS", season1.this_year)) + "-" + str(self.career_stats.get_stat("REGULAR CAREER", "LOSSES", season1.this_year)) + "-" + str(self.career_stats.get_stat("REGULAR CAREER", "TIES", season1.this_year)), 675, 100 + scroll)
            text("Total:    " + str(self.career_stats.get_stat("CAREER", "WINS", season1.this_year))         + "-" + str(self.career_stats.get_stat("CAREER", "LOSSES", season1.this_year))         + "-" + str(self.career_stats.get_stat("CAREER", "TIES", season1.this_year)),         675, 125 + scroll)
            i = 1
            a_year = 1966 + len(self.season_records)
            for record in reversed(self.season_records):
                a_year -= 1
                i += 1
                text(str(a_year) + ":  " + str(record[0]) + "-" + str(record[1]) + "-" + str(record[2]), 675, 150 + 25*i + scroll)
            text("Now:       " + str(self.standings_data[1]) + "-" + str(self.standings_data[2]) + "-" + str(self.standings_data[3]), 675, 150 + 25 + scroll)
            for player in self.Players:
                table_info.append([player.first_name + " " + player.last_name, player.position, player.get_overall(player.position, use_overall), player.age, player.contract_length, str(round(player.contract_amount/1000000.0, 2)) + " million", player.get_value()])
            table_info.sort(key = lambda l: by_list_index(l, sort_type), reverse = not sort_reverse)
            draw_table_h(["Name", "POS", "OVR", "Age", "Length", "$", "Value"], [200, 50, 50, 50, 75, 125, 75], 25, table_info, x + 5, y + 35, [], True, sort_type)
        elif team == "STRATEGY":
            self.draw_team_formations(self.o_form, 1000, 150, True)
            self.draw_team_formations(self.d_form, 1050, 150, True)
            textSize(25)
            text("Pass: " + str(round(self.pass_chance, 2)) + "%", x + 5, y)
            text("Offense formation:", x + 5, y + 35)
            text("Goal line: " +     str(round(self.offense_formation_chance[0], 2)) + "%", x + 25, y + 70)
            text("I formation: " +   str(round(self.offense_formation_chance[1], 2)) + "%", x + 25, y + 105)
            text("Singleback: " +    str(round(self.offense_formation_chance[2], 2)) + "%", x + 25, y + 140)
            text("Spread: " +        str(round(self.offense_formation_chance[3], 2)) + "%", x + 25, y + 175)
            text("Fourth dist: " +   str(round(self.fourth_down_attempt_dist, 2)), x + 5, y + 210)
            text("Fourth chance: " + str(round(self.fourth_down_attempt_chance, 2)) + "%", x + 5, y + 245)
            text("Targets:", x + 5, y + 280)
            try:
                text(self.wr1.first_name + ": " + str(round(self.fave_targets[0],                                                                                     2)) + "%", x + 25, y + 315)
                text(self.wr2.first_name + ": " + str(round(self.fave_targets[1]*(1-self.offense_formation_chance[0]/100.0),                                          2)) + "%", x + 25, y + 350)
                text(self.wr3.first_name + ": " + str(round(self.fave_targets[2]*(  self.offense_formation_chance[2]/100.0 + self.offense_formation_chance[3]/100.0), 2)) + "%", x + 25, y + 385)
                text(self.te1.first_name + ": " + str(round(self.fave_targets[3]*(1-self.offense_formation_chance[1]/100.0),                                          2)) + "%", x + 25, y + 420)
                text(self.te2.first_name + ": " + str(round(self.fave_targets[4]* 0,                                                                                  2)) + "%", x + 25, y + 455)
                text(self.rb1.first_name + ": " + str(round(self.fave_targets[5],                                                                                     2)) + "%", x + 25, y + 490)
                text(self.rb2.first_name + ": " + str(round(self.fave_targets[6]*(  self.offense_formation_chance[0]/100.0 + self.offense_formation_chance[1]/100.0), 2)) + "%", x + 25, y + 525)
                text("Scramble: " + str(round(self.scramble_chance, 2)) + "%", x + 5, y + 560)
            except:
                text("fill team", x + 25, y + 415)
            
            text("Plays: " + str(int(self.plays_per_game)), x + 500, y)
            text("Man: " + str(round(self.man_chance, 2)) + "%", x + 500, y + 35)
            text("Defense formation:", x + 500, y + 70)
            text("Goal line: " + str(round(self.defense_formation_chance[0], 2)) + "%", x + 525, y + 105)
            text("3-4: " +       str(round(self.defense_formation_chance[1], 2)) + "%", x + 525, y + 140)
            text("4-3: " +       str(round(self.defense_formation_chance[2], 2)) + "%", x + 525, y + 175)
            text("Nickel: " +    str(round(self.defense_formation_chance[3], 2)) + "%", x + 525, y + 210)
            text("Dime: " +      str(round(self.defense_formation_chance[4], 2)) + "%", x + 525, y + 245)
            text("Quarter: " +   str(round(self.defense_formation_chance[5], 2)) + "%", x + 525, y + 280)
            text("Blitzers:", x + 500, y + 315)
            text("0: " + str(round(self.blitzers_chance[0], 2)) + "%", x + 525, y + 350)
            text("1: " + str(round(self.blitzers_chance[1], 2)) + "%", x + 525, y + 385)
            text("2: " + str(round(self.blitzers_chance[2], 2)) + "%", x + 525, y + 420)
            text("3: " + str(round(self.blitzers_chance[3], 2)) + "%", x + 525, y + 455)
            text("Rusher:", x + 500, y + 490)
            try:
                text(self.rb1.first_name + ": " + str(round(self.rb1_chance, 2)) + "%", x + 525, y + 525)
            except:
                text("NO RB", x + 525, y + 525)
            try:
                text(self.rb2.first_name + ": " + str(round(100 - self.rb1_chance, 2)) + "%", x + 525, y + 560)
            except:
                text("NO RB", x + 525, y + 560)
            for i in range(0, 34):
                if not i in {1, 8, 19, 26, 31}:
                    x2 = 275
                    y2 = (i % 17) * 35 - 20
                    if i >= 17:
                        x2 = 740
                    fill(150)
                    rect(x + x2, y + y2, 25, 25, 7)
                    rect(x + x2 + 30, y + y2, 25, 25, 7)
                    fill(0)
                    textSize(20)
                    text(" +", x + x2, y + y2, 25, 25)
                    text(" -", x + x2 + 30, y + y2, 25, 25)
        elif team == "NUMBERS":
            ls.draw_team_stats(self, x + 50, y)
        elif team == "OFFENSE":
            text("Offense: " + str(int(round(self.offense))) + " OVR", x, y - 25)
            self.__draw_player(self.qb1, x + 650, y + 175, True, 0.75)
            self.__draw_player(self.rb1, x + 525, y + 250, True, 0.75)
            self.__draw_player(self.rb2, x + 775, y + 250, True, 0.75)
            self.__draw_player(self.wr1, x + 10, y, True, 0.75)
            self.__draw_player(self.wr2, x + 1200, y, True, 0.75)
            self.__draw_player(self.wr3, x + 200, y + 75, True, 0.75)
            self.__draw_player(self.te1, x + 1025, y + 75, True, 0.75)
            self.__draw_player(self.ol1, x + 400, y, True, 0.75)
            self.__draw_player(self.ol2, x + 525, y, True, 0.75)
            self.__draw_player(self.ol3, x + 650, y, True, 0.75)
            self.__draw_player(self.ol4, x + 775, y, True, 0.75)
            self.__draw_player(self.ol5, x + 900, y, True, 0.75)
            textSize(25)
            fill(0)
            text("SUBS:", x, y + 375)
            self.__draw_player(self.qb2, x, y + 400, True, 0.75)
            self.__draw_player(self.rb3, x + 125, y + 400, True, 0.75)
            self.__draw_player(self.wr4, x + 250, y + 400, True, 0.75)
            self.__draw_player(self.te2, x + 375, y + 400, True, 0.75)
            self.__draw_player(self.te3, x + 500, y + 400, True, 0.75)
            self.__draw_player(self.ol6, x + 625, y + 400, True, 0.75)
            textSize(25)
            i = 0
            for player in self.bench:
                try:
                    pos = player.position
                    if pos == "QB" or pos == "RB" or pos == "WR" or pos == "TE" or pos == "OL":
                        self.__draw_player(player, x + (125 * i), y + 530, True, 0.75)
                        i += 1
                except:
                    self.bench.remove(player)
        elif team == "DEFENSE":
            textSize(25)
            text("Defense: " + str(int(round(self.defense))) + " OVR", x, y - 25)
            self.__draw_player(self.dl1, x + 475, y + 200, True, 0.75)
            self.__draw_player(self.dl2, x + 600, y + 200, True, 0.75)
            self.__draw_player(self.dl3, x + 725, y + 200, True, 0.75)
            self.__draw_player(self.dl4, x + 850, y + 200, True, 0.75)
            self.__draw_player(self.lb1, x + 500, y + 50, True, 0.75)
            self.__draw_player(self.lb2, x + 650, y + 50, True, 0.75)
            self.__draw_player(self.lb3, x + 800, y + 50, True, 0.75)
            self.__draw_player(self.db1, x + 100, y + 200, True, 0.75)
            self.__draw_player(self.db2, x + 1150, y + 200, True, 0.75)
            self.__draw_player(self.db3, x + 250, y, True, 0.75)
            self.__draw_player(self.db4, x + 1000, y, True, 0.75)
            textSize(25)
            fill(0)
            text("SUBS:", x, y + 375)
            self.__draw_player(self.dl5, x, y + 400, True, 0.75)
            self.__draw_player(self.dl6, x + 125, y + 400, True, 0.75)
            self.__draw_player(self.dl7, x + 250, y + 400, True, 0.75)
            self.__draw_player(self.lb4, x + 375, y + 400, True, 0.75)
            self.__draw_player(self.lb5, x + 500, y + 400, True, 0.75)
            self.__draw_player(self.db5, x + 625, y + 400, True, 0.75)
            self.__draw_player(self.db6, x + 750, y + 400, True, 0.75)
            self.__draw_player(self.db7, x + 875, y + 400, True, 0.75)
            textSize(25)
            i = 0
            for player in self.bench:
                try:
                    pos = player.position
                    if pos == "DL" or pos == "LB" or pos == "DB":
                        self.__draw_player(player, x + (125 * i), y + 530, True, 0.75)
                        i += 1
                except:
                    self.bench.remove(player)
                
        elif team == "SPECIAL":
            textSize(25)
            text("Special: " + str(int(round(self.special))) + " OVR", x, y - 25)
            self.__draw_player(self.k, x + 550, y + 100, True, 0.75)
            self.__draw_player(self.rt, x + 700, y + 100, True, 0.75, "RT")
            textSize(25)
            fill(0)
            text("SUBS:", x, y + 375)
            i = 0
            st_available = []
            st_available.extend(self.bench)
            for player in [self.wr1, self.wr2, self.wr3, self.wr4]:
                st_available.append(player)
            if self.rt in st_available:
                st_available.remove(self.rt)
            for player in st_available:
                try:
                    pos = player.position
                    if pos == "K":
                        self.__draw_player(player, x + (125 * i), y + 530, True, 0.75)
                        i += 1
                    elif pos in {"RT", "WR"}:
                        self.__draw_player(player, x + (125 * i), y + 530, True, 0.75, "RT")
                        i += 1
                except:
                    if player in self.bench:
                        self.bench.remove(player)
                    
    def check_for_strategy(self, x, y):
        global user_teams, user_team_number
        if not self.abbreviation == user_teams[user_team_number].abbreviation:
            return
        index = -1
        add_sub = 0
        for i in range(0, 34):
            if not i in {1, 8, 19, 26, 31}:
                x2 = 275
                y2 = (i % 17) * 35 - 20
                if i >= 17:
                    x2 = 740
                if x > x2 and x < x2 + 25 and y > y2 and y < y2 + 25:
                    index = i
                    add_sub = 1
                elif x > x2 + 30 and x < x2 + 55 and y > y2 and y < y2 + 25:
                    index = i
                    add_sub = -1
        if index == -1:
            return
        elif index == 0:
            self.pass_chance += 0.5 * add_sub
        elif index == 2:
            self.o_form = "goal line o"
            self.offense_formation_chance[0] += 0.5 * add_sub
            self.offense_formation_chance[1] -= 0.5/3 * add_sub
            self.offense_formation_chance[2] -= 0.5/3 * add_sub
            self.offense_formation_chance[3] -= 0.5/3 * add_sub
        elif index == 3:
            self.o_form = "i"
            self.offense_formation_chance[1] += 0.5 * add_sub
            self.offense_formation_chance[0] -= 0.5/3 * add_sub
            self.offense_formation_chance[2] -= 0.5/3 * add_sub
            self.offense_formation_chance[3] -= 0.5/3 * add_sub
        elif index == 4:
            self.o_form = "singleback"
            self.offense_formation_chance[2] += 0.5 * add_sub
            self.offense_formation_chance[0] -= 0.5/3 * add_sub
            self.offense_formation_chance[1] -= 0.5/3 * add_sub
            self.offense_formation_chance[3] -= 0.5/3 * add_sub
        elif index == 5:
            self.o_form = "spread"
            self.offense_formation_chance[3] += 0.5 * add_sub
            self.offense_formation_chance[0] -= 0.5/3 * add_sub
            self.offense_formation_chance[1] -= 0.5/3 * add_sub
            self.offense_formation_chance[2] -= 0.5/3 * add_sub
        elif index == 6:
            self.fourth_down_attempt_dist += 0.5 * add_sub
        elif index == 7:
            self.fourth_down_attempt_chance += 0.5 * add_sub
        elif index == 9:
            self.fave_targets[0] += 0.5 * add_sub
            self.fave_targets[1] -= 0.5/6 * add_sub   
            self.fave_targets[2] -= 0.5/6 * add_sub 
            self.fave_targets[3] -= 0.5/6 * add_sub 
            self.fave_targets[4] -= 0.5/6 * add_sub 
            self.fave_targets[5] -= 0.5/6 * add_sub 
            self.fave_targets[6] -= 0.5/6 * add_sub
        elif index == 10:
            self.fave_targets[1] += 0.5 * add_sub
            self.fave_targets[0] -= 0.5/6 * add_sub   
            self.fave_targets[2] -= 0.5/6 * add_sub 
            self.fave_targets[3] -= 0.5/6 * add_sub 
            self.fave_targets[4] -= 0.5/6 * add_sub 
            self.fave_targets[5] -= 0.5/6 * add_sub 
            self.fave_targets[6] -= 0.5/6 * add_sub
        elif index == 11:
            self.fave_targets[2] += 0.5 * add_sub
            self.fave_targets[0] -= 0.5/6 * add_sub   
            self.fave_targets[1] -= 0.5/6 * add_sub 
            self.fave_targets[3] -= 0.5/6 * add_sub 
            self.fave_targets[4] -= 0.5/6 * add_sub 
            self.fave_targets[5] -= 0.5/6 * add_sub 
            self.fave_targets[6] -= 0.5/6 * add_sub
        elif index == 12:
            self.fave_targets[3] += 0.5 * add_sub
            self.fave_targets[0] -= 0.5/6 * add_sub   
            self.fave_targets[1] -= 0.5/6 * add_sub 
            self.fave_targets[2] -= 0.5/6 * add_sub 
            self.fave_targets[4] -= 0.5/6 * add_sub 
            self.fave_targets[5] -= 0.5/6 * add_sub 
            self.fave_targets[6] -= 0.5/6 * add_sub
        elif index == 13:
            self.fave_targets[4] += 0.5 * add_sub
            self.fave_targets[0] -= 0.5/6 * add_sub   
            self.fave_targets[1] -= 0.5/6 * add_sub 
            self.fave_targets[2] -= 0.5/6 * add_sub 
            self.fave_targets[3] -= 0.5/6 * add_sub 
            self.fave_targets[5] -= 0.5/6 * add_sub 
            self.fave_targets[6] -= 0.5/6 * add_sub
        elif index ==14:
            self.fave_targets[5] += 0.5 * add_sub
            self.fave_targets[0] -= 0.5/6 * add_sub   
            self.fave_targets[1] -= 0.5/6 * add_sub 
            self.fave_targets[2] -= 0.5/6 * add_sub 
            self.fave_targets[3] -= 0.5/6 * add_sub 
            self.fave_targets[4] -= 0.5/6 * add_sub 
            self.fave_targets[6] -= 0.5/6 * add_sub
        elif index == 15:
            self.fave_targets[6] += 0.5 * add_sub
            self.fave_targets[0] -= 0.5/6 * add_sub   
            self.fave_targets[1] -= 0.5/6 * add_sub 
            self.fave_targets[2] -= 0.5/6 * add_sub 
            self.fave_targets[3] -= 0.5/6 * add_sub 
            self.fave_targets[4] -= 0.5/6 * add_sub 
            self.fave_targets[5] -= 0.5/6 * add_sub
        elif index == 16:
            self.scramble_chance += 0.5 * add_sub
        elif index == 17:
            self.plays_per_game += 0.5 * add_sub
        elif index == 18:
            self.man_chance += 0.5 * add_sub
        elif index == 20:
            self.d_form = "goal line d"
            self.defense_formation_chance[0] += 0.5 * add_sub
            self.defense_formation_chance[1] -= 0.5/5 * add_sub
            self.defense_formation_chance[2] -= 0.5/5 * add_sub
            self.defense_formation_chance[3] -= 0.5/5 * add_sub
            self.defense_formation_chance[4] -= 0.5/5 * add_sub
            self.defense_formation_chance[5] -= 0.5/5 * add_sub
        elif index == 21:
            self.d_form = "3-4"
            self.defense_formation_chance[1] += 0.5 * add_sub
            self.defense_formation_chance[0] -= 0.5/5 * add_sub
            self.defense_formation_chance[2] -= 0.5/5 * add_sub
            self.defense_formation_chance[3] -= 0.5/5 * add_sub
            self.defense_formation_chance[4] -= 0.5/5 * add_sub
            self.defense_formation_chance[5] -= 0.5/5 * add_sub
        elif index == 22:
            self.d_form = "4-3"
            self.defense_formation_chance[2] += 0.5 * add_sub
            self.defense_formation_chance[0] -= 0.5/5 * add_sub
            self.defense_formation_chance[1] -= 0.5/5 * add_sub
            self.defense_formation_chance[3] -= 0.5/5 * add_sub
            self.defense_formation_chance[4] -= 0.5/5 * add_sub
            self.defense_formation_chance[5] -= 0.5/5 * add_sub
        elif index == 23:
            self.d_form = "nickel"
            self.defense_formation_chance[3] += 0.5 * add_sub
            self.defense_formation_chance[0] -= 0.5/5 * add_sub
            self.defense_formation_chance[1] -= 0.5/5 * add_sub
            self.defense_formation_chance[2] -= 0.5/5 * add_sub
            self.defense_formation_chance[4] -= 0.5/5 * add_sub
            self.defense_formation_chance[5] -= 0.5/5 * add_sub
        elif index == 24:
            self.d_form = "dime"
            self.defense_formation_chance[4] += 0.5 * add_sub
            self.defense_formation_chance[0] -= 0.5/5 * add_sub
            self.defense_formation_chance[1] -= 0.5/5 * add_sub
            self.defense_formation_chance[2] -= 0.5/5 * add_sub
            self.defense_formation_chance[3] -= 0.5/5 * add_sub
            self.defense_formation_chance[5] -= 0.5/5 * add_sub
        elif index == 25:
            self.d_form = "quarter"
            self.defense_formation_chance[5] += 0.5 * add_sub
            self.defense_formation_chance[0] -= 0.5/5 * add_sub
            self.defense_formation_chance[1] -= 0.5/5 * add_sub
            self.defense_formation_chance[2] -= 0.5/5 * add_sub
            self.defense_formation_chance[3] -= 0.5/5 * add_sub
            self.defense_formation_chance[4] -= 0.5/5 * add_sub
        elif index == 27:
            self.blitzers_chance[0] += 0.5 * add_sub
            self.blitzers_chance[1] -= 0.5/3 * add_sub
            self.blitzers_chance[2] -= 0.5/3 * add_sub
            self.blitzers_chance[3] -= 0.5/3 * add_sub
        elif index == 28:
            self.blitzers_chance[1] += 0.5 * add_sub
            self.blitzers_chance[0] -= 0.5/3 * add_sub
            self.blitzers_chance[2] -= 0.5/3 * add_sub
            self.blitzers_chance[3] -= 0.5/3 * add_sub
        elif index == 29:
            self.blitzers_chance[2] += 0.5 * add_sub
            self.blitzers_chance[0] -= 0.5/3 * add_sub
            self.blitzers_chance[1] -= 0.5/3 * add_sub
            self.blitzers_chance[3] -= 0.5/3 * add_sub
        elif index == 30:
            self.blitzers_chance[3] += 0.5 * add_sub
            self.blitzers_chance[0] -= 0.5/3 * add_sub
            self.blitzers_chance[1] -= 0.5/3 * add_sub
            self.blitzers_chance[2] -= 0.5/3 * add_sub
        elif index == 32:
            self.rb1_chance += 0.5 * add_sub
        elif index == 33:
            self.rb1_chance -= 0.5 * add_sub
            
        for l in [self.offense_formation_chance, self.fave_targets, self.defense_formation_chance, self.blitzers_chance]:
            fix_list_chances(l)
        self.rb1_chance = bound(self.rb1_chance)
        self.man_chance = bound(self.man_chance)
        self.scramble_chance = bound(self.scramble_chance)
        self.fourth_down_attempt_chance = bound(self.fourth_down_attempt_chance)
        self.fourth_down_attempt_dist = bound(self.fourth_down_attempt_dist)
        self.pass_chance = bound(self.pass_chance)

        
    def _check_player(self, x, y, p_x, p_y):
        if x > p_x and x < p_x + 140*0.75 and y > p_y and y < p_y + 165*0.75:
            return True
        return False
    
    def check_for_clicked(self, x, y, team_phase):
        if team_phase == "OFFENSE":
            if self._check_player(x, y, 650, 175):
                return (self.qb1, "QB")
            elif self._check_player(x, y, 525, 250):
                return (self.rb1, "RB")
            elif self._check_player(x, y, 775, 250):
                return (self.rb2, "RB")
            elif self._check_player(x, y, 10, 0):
                return (self.wr1, "WR")
            elif self._check_player(x, y, 1200, 0):
                return (self.wr2, "WR")
            elif self._check_player(x, y, 200, 75):
                return (self.wr3, "WR")
            elif self._check_player(x, y, 1025, 75):
                return (self.te1, "TE")
            elif self._check_player(x, y, 400, 0):
                return (self.ol1, "OL")
            elif self._check_player(x, y, 525, 0):
                return (self.ol2, "OL")
            elif self._check_player(x, y, 650, 0):
                return (self.ol3, "OL")
            elif self._check_player(x, y, 775, 0):
                return (self.ol4, "OL")
            elif self._check_player(x, y, 900, 0):
                return (self.ol5, "OL")
            elif self._check_player(x, y, 0, 400):
                return (self.qb2, "QB")
            elif self._check_player(x, y, 125, 400):
                return (self.rb3, "RB")
            elif self._check_player(x, y, 250, 400):
                return (self.wr4, "WR")
            elif self._check_player(x, y, 375, 400):
                return (self.te2, "TE")
            elif self._check_player(x, y, 500, 400):
                return (self.te3, "TE")
            elif self._check_player(x, y, 625, 400):
                return (self.ol6, "OL")
            else:
                i = 0
                for player in self.bench:
                    pos = player.position
                    if pos in {"QB", "RB", "WR", "TE", "OL"}:
                        if self._check_player(x, y, 125 * i, 530):
                            return (player, "NONE")
                        i += 1
        elif team_phase == "DEFENSE":
            if self._check_player(x, y, 475, 200):
                return (self.dl1, "DL")
            elif self._check_player(x, y, 600, 250):
                return (self.dl2, "DL")
            elif self._check_player(x, y, 725, 250):
                return (self.dl3, "DL")
            elif self._check_player(x, y, 850, 250):
                return (self.dl4, "DL")
            elif self._check_player(x, y, 500, 50):
                return (self.lb1, "LB")
            elif self._check_player(x, y, 650, 50):
                return (self.lb2, "LB")
            elif self._check_player(x, y, 800, 50):
                return (self.lb3, "LB")
            elif self._check_player(x, y, 100, 200):
                return (self.db1, "DB")
            elif self._check_player(x, y, 1150, 200):
                return (self.db2, "DB")
            elif self._check_player(x, y, 250, 0):
                return (self.db3, "DB")
            elif self._check_player(x, y, 1000, 0):
                return (self.db4, "DB")
            elif self._check_player(x, y, 0, 400):
                return (self.dl5, "DL")
            elif self._check_player(x, y, 125, 400):
                return (self.dl6, "DL")
            elif self._check_player(x, y, 250, 400):
                return (self.dl7, "DL")
            elif self._check_player(x, y, 375, 400):
                return (self.lb4, "LB")
            elif self._check_player(x, y, 500, 400):
                return (self.lb5, "LB")
            elif self._check_player(x, y, 625, 400):
                return (self.db5, "DB")
            elif self._check_player(x, y, 750, 400):
                return (self.db6, "DB")
            elif self._check_player(x, y, 875, 400):
                return (self.db7, "DB")
            else:
                i = 0
                for player in self.bench:
                    pos = player.position
                    if pos == "DL" or pos == "LB" or pos == "DB":
                        if self._check_player(x, y, 125*i, 530):
                            return (player, "NONE")
                        i += 1
        elif team_phase == "SPECIAL":
            if self._check_player(x, y, 550, 100):
                return (self.k, "K")
            elif self._check_player(x, y, 700, 100):
                return (self.rt, "RT")
            else:
                i = 0
                st_available = []
                st_available.extend(self.bench)
                for player in [self.wr1, self.wr2, self.wr3, self.wr4]:
                    st_available.append(player)
                if self.rt in st_available:
                    st_available.remove(self.rt)
                for player in st_available:
                    try:
                        pos = player.position
                    except:
                        continue
                    if pos in {"K", "RT", "WR"}:
                        if self._check_player(x, y, 125*i, 530):
                            return (player, "NONE")
                        i += 1
        return "NONE"

    def reset_game_stats(self):
        for player in self.Players:
            player.reset_game_stats()
        self.career_stats.reset_game_stats()
        
    """def reset_season_stats(self):
        for player in self.Players:
            player.reset_season_stats()
        self.run_stats[1] = [0]*5
        self.receive_stats[1] = [0]*9
        self.throw_stats[1] = [0]*9
        self.block_stats[1] = [0]*2
        self.cover_stats[1] = [0]*13
        self.blitzer_stats[1] = [0]*10
        self.xp_stats[1] = [0]*2
        self.fg_stats[1] = [0]*4
        self.punt_stats[1] = [0]*4
        self.return_stats[1] = [0]*5"""
        
    def add_stats(self, player, type, amount, game_type, this_year):
        global c
        if player == "ALL":
            for player in self.Players:
                player.add_stats(type, amount, game_type, this_year)
        elif player == "NONE":
            pass
        else:
            try:
                player.add_stats(type, amount, game_type, this_year)
            except:
                println("error")
                println(player.name())
                println(type)
                println(amount)
                print(game_type)
                print(this_year)
                println("")
                rect(0,0,500,500)
                
        self.career_stats.add_stat(type, amount, game_type, this_year)
        
        xp_boost =        c.stat_xp(type) * amount
        game_multiplier = c.game_xp_multiplier(game_type)
        total_xp =        max(0, xp_boost * game_multiplier)
        self.xp +=        total_xp
            
    def update_standings_data(self, type, amount, game_type, this_year):
        if type == "WIN":
            self.add_stats("ALL", type, amount, game_type, this_year)
            if game_type == "REGULAR":
                self.standings_data[1] += amount
        elif type == "LOSS":
            self.add_stats("ALL", type, amount, game_type, this_year)
            if game_type == "REGULAR":
                self.standings_data[2] += amount
        elif type == "TIE":
            self.add_stats("ALL", type, amount, game_type, this_year)
            if game_type == "REGULAR":
                self.standings_data[3] += amount
        elif type == "PF":
            if game_type == "REGULAR":
                self.standings_data[5] += amount
        elif type == "PA":
            if game_type == "REGULAR":
                self.standings_data[6] += amount
        if self.standings_data[1] == 0:
            self.standings_data[4] = 0.000
        else:
            self.standings_data[4] = (float(self.standings_data[1]) + self.standings_data[3]/2.0) / (self.standings_data[1] + self.standings_data[2] + self.standings_data[3])

    def upgrade_players(self):
        for player in self.Players:
            while player.upgrade_available():
                trait = 0
                options = []
                if player.position == "QB":
                    options = ["injury", "int throw", "complete chance", "air yds throw", "fumble chance"]
                    trait = options[int(random(0,5))]
                elif player.position == "RB":
                    options = ["injury", "block chance", "sack allowed chance", "fumble chance", "drop chance", "target dist", "yac", "run dist"]
                    trait = options[int(random(0,8))]
                elif player.position == "WR":
                    options = ["injury", "fumble chance", "drop chance", "target dist", "yac"]
                    trait = options[int(random(0,5))]
                elif player.position == "TE":
                    options = ["injury", "block chance", "sack allowed chance", "fumble chance", "drop chance", "target dist", "yac"]
                    trait = options[int(random(0,7))]
                elif player.position == "OL":
                    options = ["injury", "block chance", "sack allowed chance"]
                    trait = options[int(random(0,3))]
                elif player.position == "DL":
                    options = ["injury", "sack chance", "blocked chance", "run dist allowed", "ff chance"]
                    trait = options[int(random(0,5))]
                elif player.position == "LB" or player.position == "DB":
                    options = ["injury", "sack chance", "blocked chance", "run dist allowed", "ff chance", "air yds allowed", "int catch chance", "complete chance allowed", "yac allowed"]
                    trait = options[int(random(0, 9))]
                elif player.position == "K":
                    options = ["injury", "fg range", "fg made chance", "punt dist", "kick return dist", "tb forced chance", "pin chance"]
                    trait = options[int(random(0,7))]
                elif player.position == "RT":
                    options = ["injury", "kick return dist", "tb chance"]
                    trait = options[int(random(0, 3))]
                player.upgrade_player(trait, 1, player.upgrade_type, True)
    
    def end_season(self):
        global season1
        self.negotiations = 10
        self.resignings = 3
        self.season_records.append( [self.standings_data[1], self.standings_data[2], self.standings_data[3]] )
        self.standings_data = [self.name(), 0,0,0,0.000,0,0]
        #self.reset_season_stats()
        for player in self.Players:
            player.end_season()
            if player.retired:
                self.cut_player(player)
        self.add_stats("ALL", "SEASON", 1, "REGULAR", season1.this_year)
        self.calculate_cap_left()
    
    def week_over(self):
        self.fa_pos = []
        self.calculate_cap_left()
        for player in self.Players:
            player.end_week()
            
    def end_regular_week(self, this_year):
        for player in self.Players:
            player.add_stats("SALARY", player.contract_amount/18.0, "REGULAR", this_year)
    
    def sync_line_up(self):
        self.line_up = [self.qb1, self.qb2, self.rb1, self.rb2, self.rb3, self.wr1, self.wr2, self.wr3, self.wr4, self.te1, self.te2, self.te3, self.ol1, self.ol2, self.ol3, self.ol4, self.ol5, self.ol6, self.dl1, self.dl2, self.dl3, self.dl4, self.dl5, self.dl6, self.dl7, self.lb1, self.lb2, self.lb3, self.lb4, self.lb5, self.db1, self.db2, self.db3, self.db4, self.db5, self.db6, self.db7, self.k, self.rt]    

    def sync_starters(self):
        self.qb1 = self.line_up[0]
        self.qb2 = self.line_up[1]
        self.rb1 = self.line_up[2]
        self.rb2 = self.line_up[3]
        self.rb3 = self.line_up[4]
        self.wr1 = self.line_up[5]
        self.wr2 = self.line_up[6]
        self.wr3 = self.line_up[7]
        self.wr4 = self.line_up[8]
        self.te1 = self.line_up[9]
        self.te2 = self.line_up[10]
        self.te3 = self.line_up[11]
        self.ol1 = self.line_up[12]
        self.ol2 = self.line_up[13]
        self.ol3 = self.line_up[14]
        self.ol4 = self.line_up[15]
        self.ol5 = self.line_up[16]
        self.ol6 = self.line_up[17]
        self.dl1 = self.line_up[18]
        self.dl2 = self.line_up[19]
        self.dl3 = self.line_up[20]
        self.dl4 = self.line_up[21]
        self.dl5 = self.line_up[22]
        self.dl6 = self.line_up[23]
        self.dl7 = self.line_up[24]
        self.lb1 = self.line_up[25]
        self.lb2 = self.line_up[26]
        self.lb3 = self.line_up[27]
        self.lb4 = self.line_up[28]
        self.lb5 = self.line_up[29]
        self.db1 = self.line_up[30]
        self.db2 = self.line_up[31]
        self.db3 = self.line_up[32]
        self.db4 = self.line_up[33]
        self.db5 = self.line_up[34]
        self.db6 = self.line_up[35]
        self.db7 = self.line_up[36]
        self.k =   self.line_up[37]
        self.rt =  self.line_up[38]
        
        
    def best_lineup(self):
        qb_order = [self.qb1, self.qb2]
        for player in self.bench:
            try:
                if player.position == "QB":
                    qb_order.append(player)
                    self.bench.remove(player)
            except:
                self.bench.remove(player)
        qb_order.sort(key = lambda p: (by_depth(p), by_overall(p)), reverse = True)
        rb_order = [self.rb1, self.rb2, self.rb3]
        for player in self.bench:
            try:
                if player.position == "RB":
                    rb_order.append(player)
                    self.bench.remove(player)
            except:
                self.bench.remove(player)
        rb_order.sort(key = lambda p: (by_depth(p), by_overall(p)), reverse = True)
        wr_order = [self.wr1, self.wr2, self.wr3, self.wr4]
        for player in self.bench:
            try:
                if player.position == "WR":
                    wr_order.append(player)
                    self.bench.remove(player)
            except:
                self.bench.remove(player)
        wr_order.sort(key = lambda p: (by_depth(p), by_overall(p)), reverse = True)
        te_order = [self.te1, self.te2, self.te3]
        for player in self.bench:
            try:
                if player.position == "TE":
                    te_order.append(player)
                    self.bench.remove(player)
            except:
                self.bench.remove(player)
        te_order.sort(key = lambda p: (by_depth(p), by_overall(p)), reverse = True)
        ol_order = [self.ol1, self.ol2, self.ol3, self.ol4, self.ol5, self.ol6]
        for player in self.bench:
            try:
                if player.position == "OL":
                    ol_order.append(player)
                    self.bench.remove(player)
            except:
                self.bench.remove(player)
        ol_order.sort(key = lambda p: (by_depth(p), by_overall(p)), reverse = True)
        dl_order = [self.dl1, self.dl2, self.dl3, self.dl4, self.dl5, self.dl6, self.dl7]
        for player in self.bench:
            try:
                if player.position == "DL":
                    dl_order.append(player)
                    self.bench.remove(player)
            except:
                self.bench.remove(player)
        dl_order.sort(key = lambda p: (by_depth(p), by_overall(p)), reverse = True)
        lb_order = [self.lb1, self.lb2, self.lb3, self.lb4, self.lb5]
        for player in self.bench:
            try:
                if player.position == "LB":
                    lb_order.append(player)
                    self.bench.remove(player)
            except:
                self.bench.remove(player)
        lb_order.sort(key = lambda p: (by_depth(p), by_overall(p)), reverse = True)
        db_order = [self.db1, self.db2, self.db3, self.db4, self.db5, self.db6, self.db7]
        for player in self.bench:
            try:
                if player.position == "DB":
                    db_order.append(player)
                    self.bench.remove(player)
            except:
                self.bench.remove(player)
        db_order.sort(key = lambda p: (by_depth(p), by_overall(p)), reverse = True)
        k_order = [self.k]
        for player in self.bench:
            try:
                if player.position == "K":
                    k_order.append(player)
                    self.bench.remove(player)
            except:
                self.bench.remove(player)
        k_order.sort(key = lambda p: (by_depth(p), by_overall(p)), reverse = True)
        rt_order = [self.rt]
        rt_possibles = []
        rt_possibles.extend(self.bench)
        rt_possibles.extend(wr_order)
        for player in rt_possibles:
            try:
                if player.position in {"RT", "WR"}:
                    rt_order.append(player)
                    if player in self.bench:
                        self.bench.remove(player)
            except:
                if player in self.bench:
                    self.bench.remove(player)
        rt_order.sort(key = lambda p: (by_depth(p), by_overall(p, "RT")), reverse = True)
        self.qb1 = qb_order[0]
        self.qb2 = qb_order[1]
        self.rb1 = rb_order[0]
        self.rb2 = rb_order[1]
        self.rb3 = rb_order[2]
        self.wr1 = wr_order[0]
        self.wr2 = wr_order[1]
        self.wr3 = wr_order[2]
        self.wr4 = wr_order[3]
        self.te1 = te_order[0]
        self.te2 = te_order[1]
        self.te3 = te_order[2]
        self.ol1 = ol_order[0]
        self.ol2 = ol_order[1]
        self.ol3 = ol_order[2]
        self.ol4 = ol_order[3]
        self.ol5 = ol_order[4]
        self.ol6 = ol_order[5]
        self.dl1 = dl_order[0]
        self.dl2 = dl_order[1]
        self.dl3 = dl_order[2]
        self.dl4 = dl_order[3]
        self.dl5 = dl_order[4]
        self.dl6 = dl_order[5]
        self.dl7 = dl_order[6]
        self.lb1 = lb_order[0]
        self.lb2 = lb_order[1]
        self.lb3 = lb_order[2]
        self.lb4 = lb_order[3]
        self.lb5 = lb_order[4]
        self.db1 = db_order[0]
        self.db2 = db_order[1]
        self.db3 = db_order[2]
        self.db4 = db_order[3]
        self.db5 = db_order[4]
        self.db6 = db_order[5]
        self.db7 = db_order[6] 
        self.k = k_order[0]
        self.rt = rt_order[0]
        if len(qb_order) > 2:
            self.bench.extend(qb_order[2:])
        if len(rb_order) > 3:
            self.bench.extend(rb_order[3:])
        if len(wr_order) > 4:
            for i in range(4, len(wr_order)):
                if not wr_order[i] in self.bench:
                    self.bench.append(wr_order[i])
        if len(te_order) > 3:
            self.bench.extend(te_order[3:])
        if len(ol_order) > 6:
            self.bench.extend(ol_order[6:])
        if len(dl_order) > 7:
            self.bench.extend(dl_order[7:])
        if len(lb_order) > 5:
            self.bench.extend(lb_order[5:])
        if len(db_order) > 7:
            self.bench.extend(db_order[7:])
        if len(k_order) > 1:
            self.bench.extend(k_order[1:])
        if len(rt_order) > 1:
            for i in range(1, len(rt_order)):
                if not rt_order[i] in self.bench and not rt_order[i] in {self.wr1, self.wr2, self.wr3, self.wr4}:
                    self.bench.append(rt_order[i])
        self.sync_line_up()
        
    def clear_team(self):
        self.line_up = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
        self.sync_starters()
        self.bench = []
        self.Players = []
        
    def random_bench(self, ovr):
        self.bench = []
        for x in range(0,14):
            age = random_starting_age()
            p_ovr = random_ovr_from_age(age, ovr - 75)
            new_player = Player(random_position(), p_ovr[0], p_ovr[1])
            new_player.set_age(age)
            self.bench.append(new_player)
                                
    def set_random_team(self, ovr):
        std_dev = 8
        #players = [self.qb1, self.qb2, self.rb1, self.rb2, self.rb3, self.wr1, self.wr2, self.wr3, self.wr4, self.te1, self.te2, self.te3, self.ol1, self.ol2, self.ol3, self.ol4, self.ol5, self.ol6, self.dl1, self.dl2, self.dl3, self.dl4, self.dl5, self.dl6, self.dl7, self.lb1, self.lb2, self.lb3, self.lb4, self.lb5, self.db1, self.db2, self.db3, self.db4, self.db5, self.db6, self.db7, self.k, self.rt]
        positions = ["QB", "QB", "RB", "RB", "RB", "WR", "WR", "WR", "WR", "TE", "TE", "TE", "OL", "OL", "OL", "OL", "OL", "OL", "DL", "DL", "DL", "DL", "DL", "DL", "DL", "LB", "LB", "LB", "LB", "LB", "DB", "DB", "DB", "DB", "DB", "DB", "DB", "K", "RT"]
        for i in range(0, len(self.line_up)):
            age = random_starting_age()
            p_ovr = random_ovr_from_age(age, ovr - 75)
            new_player = Player(positions[i], p_ovr[0], p_ovr[1])
            new_player.set_age(age)
            #players[i] = new_player
            self.line_up[i] = new_player
        self.random_bench(ovr - 5)
        self.sync_starters()
        self.Players = []
        for player in self.line_up:
            if not player == None:
                self.Players.append(player)
        self.Players.extend(self.bench)
        for player in self.Players:
            player.team = self.abbreviation
            player.years_played = 1
            player.draft_position[0] = 8
            player.drafted_by = self.abbreviation
        self.best_lineup()
        for player in self.Players:
            self.sign_player(player, int(random(1, 6)), player.expected_contract())
    
    def _calculate_max_offer(self):
        players = self.fas # number of fas
        for player in self.Players:
            if player.contract_length > 0:
                players += 1
        players = min(52, players)
        if is_number(self.max_cap):
            self.max_offer = self.cap_left - 500000 * (52 - players)
        else:
            self.max_offer = "NA"
        
    def calculate_cap_left(self):
        cost = 0
        for player in self.Players:
            if player.contract_length > 0:
                cost += player.contract_amount
        if is_number(self.max_cap):
            self.cap_left = self.max_cap - cost - self.fa_bids
        else:
            self.cap_left = "NA"
        self._calculate_max_offer()
                        
    def cut_to_53(self):
        done_contracts = 0
        for player in self.Players:
            if player.contract_length <= 0 or not (player.team == self.abbreviation) or player.retired:
                done_contracts += 1
        while done_contracts > 0:
            for player in self.Players:
                if player.contract_length <= 0 or not (player.team == self.abbreviation) or player.retired:
                    self.cut_player(player)
                    done_contracts -= 1
        self.best_lineup()
        self.bench.sort(key = by_overall, reverse = True)
        bench_len = 14
        try:
            if self.rt.position == "WR":
                bench_len = 15
        except:
            pass
        if len(self.bench) > bench_len:
            for player in self.bench[bench_len:]:
                self.cut_player(player)
            
    def sign_53(self):
        self.best_lineup()
        self.Players.sort(key = lambda l: by_value(l, False), reverse = True)
        for player in self.Players:
            try:
                if player.contract_length == 0:
                    self.sign_player(player, int(random(2,7)), player.expected_contract())
            except:
                pass
        #for player in self.line_up:
        #    try:
        #        if player.contract_length == 0:
        #            self.sign_player(player, int(random(2,7)), player.expected_contract())
        #    except:
        #        pass
        i = 0
        while i < min(14, len(self.bench)):
            self.bench.sort(key = lambda l: by_value(l, False), reverse = True)
            try:
                if self.bench[i].contract_length == 0:
                    self.sign_player(self.bench[i], int(random(2,7)), player.expected_contract())
            except:
                self.bench.remove(self.bench[i])
                i -= 1
            i += 1
        self.calculate_cap_left()
        
    def sign_player(self, player, contract_len, contract_mon):
        global season1
        if player.retired:
            return
        if not player.team == self.abbreviation:
            return
        self.calculate_cap_left()
        if self.max_offer == "NA" or contract_mon < self.max_offer:
            try:
                if season1.current_week == season1.resign_week:
                    if self.resignings <= 0:
                        return
                    else:
                        self.resignings -= 1
            except:
                pass
            player.sign_player(self.abbreviation, contract_len, contract_mon)
        self.calculate_cap_left()
        
    def add_player(self, player):
        if player.retired:
            return
        self.bench.append(player)
        self.Players.append(player)
        player.team = self.abbreviation
        self.best_lineup()
        
    def cut_player(self, player):
        if not player == None:
            player.cut_player()
        if player in self.bench:
            self.bench.remove(player)
        elif player in self.line_up:
            for i in range(0, len(self.line_up)):
                if player == self.line_up[i]:
                    self.line_up[i] = None
                    self.sync_starters()
                    self.best_lineup()
        if player in self.Players:
            self.Players.remove(player)
        self.calculate_cap_left()
        
        
    def fill_spots(self):
        global season1
        while len(self.Players) > 52:
            self.cut_player(self.bench[-1])
        i = 0
        self.Players.sort(key = by_contract_amount, reverse = True)
        while self.negotiations > 0 and i < len(self.Players):
            if self.Players[i].will_negotiate():
                self.Players[i].negotiate()
                self.negotiations -= 1
            i += 1
        for player in self.bench:
            try:
                if player.position == "K" or player.position == "RT":
                    self.cut_player(player)
            except:
                pass
        missing = []
        i = 0
        for player in self.line_up:
            if player == None:
                missing.append(i)
            i += 1
        positions = []
        for pos in missing:
            if pos >= 0:
                if pos < 2:
                    positions.append("QB")
                elif pos < 5:
                    positions.append("RB")
                elif pos < 9:
                    positions.append("WR")
                elif pos < 12:
                    positions.append("TE")
                elif pos < 18:
                    positions.append("OL")
                elif pos < 25:
                    positions.append("DL")  #self.line_up = qb2, rb3, wr4, te3, ol6, dl7, lb5, db7, k, rt
                elif pos < 30:
                    positions.append("LB")
                elif pos < 37:
                    positions.append("DB")
                elif pos == 37:
                    positions.append("K")
                elif pos == 38:
                    positions.append("RT")
        self.calculate_cap_left()
        if self.max_offer < 500000:
            for player in self.bench:
                try:
                    if player.contract_amount > 500000:
                        self.cut_player(player)
                except:
                    self.bench.remove(player)
            self.calculate_cap_left()
        while self.max_offer < 500000:
            biggest_contract = 0
            p = None
            for player in self.Players:
                if player.contract_amount > biggest_contract:
                    biggest_contract = player.contract_amount
                    p = player
            self.cut_player(p)
            self.calculate_cap_left()
        check = 0
        #for pos in self.fa_pos:
            #if pos in positions:
                #positions.remove(pos)
        while len(positions) > 0 and check < 100:
            check += 1
            i = 0
            for player in season1.free_agents.players:
                offer = min(season1.free_agents.players[i].min_contract(), self.max_offer)
                if season1.free_agents.bids[i][0] >= offer:
                    offer = min(season1.free_agents.bids[i][0] + 500000, self.max_offer)
                if player.position in positions:
                    worked = season1.free_agents.bid_on_free_agent(player, self, offer)
                    self.fa_bids += offer
                    self.fas += 1
                    self.fa_pos.append(player.position)
                    self.calculate_cap_left()
                    if worked:
                        positions.remove(player.position)
                i += 1
            
    def add_from_trade_block(self, trade_center):
        global season1
        for player in trade_center.trade_block:
            value = self.trade_in_value(player) - player.contract_amount/10000.0
            if value > player.get_value() and player.get_value() > 1000:
                trade_center.ai_trade_block_select(self, player)
                i = 0
                while not trade_center.current_trade.complete:
                    if i < len(self.draft_picks):
                        #pick_value = season1.draft_pick_value(self.draft_picks[i])
                        trade_center.ai_add_to_trade(self, self.draft_picks[i])
                        if 0 > trade_center.current_trade.get_value_from_team(1, True) + trade_center.current_trade.get_value_from_team(1, False): # team num, coming in
                            trade_center.ai_remove_from_trade(self, self.draft_picks[i])
                    else:
                        j = len(self.draft_picks)
                        for player in self.Players:
                            if player.in_trade_block:
                                if j == i:
                                    trade_center.ai_add_to_trade(self, player)
                                    player_value = self.trade_out_value(player)
                                    if 0 > trade_center.current_trade.get_value_from_team(1, True) + trade_center.current_trade.get_value_from_team(1, False): # team num, coming in
                                        trade_center.ai_remove_from_trade(self, player)
                                        break
                                j += 1
                        if j < i:
                            break
                    i += 1
                trade_center.ai_propose_trade(self)
                if trade_center.current_trade.complete and not trade_center.current_trade in trade_center.recent_trades:
                    trade_center.recent_trades.append(trade_center.current_trade)
        
    def send_to_trade_block(self, trade_center):
        global use_overall
        for player in self.Players:
            if player.is_tradeable() and not player.in_trade_block and player.get_value() > 2500:
                if player.contract_amount > 2*player.expected_contract():
                    trade_center.add_to_trade_block(player)
                elif player in {self.qb2, self.rb3, self.wr4, self.te2, self.te3, self.ol6, self.dl5, self.dl6, self.dl7, self.lb4, self.lb5, self.db5, self.db6, self.db7}:
                    if player.contract_amount > 5000000 or player.overall(use_overall) > 80 or player.age >= 33:
                        trade_center.add_to_trade_block(player)
                elif player in self.bench:
                    if player.contract_amount > 2000000 or player.overall(use_overall) > 75 or player.age >= 30:
                        trade_center.add_to_trade_block(player)
            
    def add_free_agents(self):
        global season1, use_overall
        did_bid = False
        ovrs = [[self.qb], [self.rb], [self.wr], [self.te], [self.ol], [self.dl], [self.lb], [self.db], [self.k_ovr], [self.rt_ovr]]
        ovrs.sort(key = lambda l: by_list_index(l, 0), reverse = False)
        pos_ovrs = []
        for ovr in ovrs:
            pos_ovrs.append(ovr[0])
        i = 0
        while i < len(season1.free_agents.players) and season1.free_agents.players[i].overall(use_overall) > pos_ovrs[0] - 2:
            if season1.free_agents.players[i].position in self.biggest_needs[0:5] and not season1.free_agents.players[i].position in self.full_positions():
                k = self.biggest_needs.index(season1.free_agents.players[i].position)
                if season1.free_agents.players[i].overall(use_overall) > pos_ovrs[k] - 2:
                    bid = min(season1.free_agents.players[i].min_contract(), self.max_offer)
                    if season1.free_agents.bids[i][0] >= bid:
                        bid = min(season1.free_agents.bids[i][0] + 500000, self.max_offer)
                    if bid > season1.free_agents.bids[i][0] and bid < season1.free_agents.players[i].expected_contract() + 1000000:
                        season1.free_agents.bid_on_free_agent(season1.free_agents.players[i], self, bid)
                        self.fa_bids += bid
                        self.fas += 1
                        self.fa_pos.append(season1.free_agents.players[i].position)
                        self.calculate_cap_left()
                        did_bid = True
            i += 1
            
        if len(self.Players) + self.fas < 53:
            i = 0
            for player in season1.free_agents.players:
                if player.min_contract() <= 500000 and not player.position in self.full_positions():
                    if len(self.Players) + self.fas < 53:
                        season1.free_agents.bid_on_free_agent(season1.free_agents.players[i], self, player.min_contract())
                        self.fa_bids += player.min_contract()
                        self.fas += 1
                        self.fa_pos.append(season1.free_agents.players[i].position)
                        self.calculate_cap_left()
                        did_bid = True
                    else:
                        return did_bid
                i += 1
        return did_bid
            
    def get_team_overall(self):
        global c, use_overall
        default_overall = 45
        
        position_overalls = [ default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, 
                              default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, 
                              default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, 
                              default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, 
                              default_overall, default_overall, default_overall, default_overall, default_overall, default_overall, default_overall ]
        for i in range(0, len(self.line_up)):
            if not self.line_up[i] == None:
                position_overalls[i] = self.line_up[i].overall(use_overall)
                
        self.qb = 0.97*position_overalls[0] + 0.03*position_overalls[1]

        pass_c = self.pass_chance/100.0
        run_c = 1 - pass_c
        rb1_c = self.rb1_chance/100.0
        rb2_c = 1 - rb1_c
        rb_mult = run_c + pass_c*(self.fave_targets[c.rb1]/100.0 + self.fave_targets[c.rb2]/100.0)
        self.rb = 0.97*((rb1_c*run_c + pass_c*(self.fave_targets[c.rb1]/100.0))*position_overalls[2] + (rb2_c*run_c + pass_c*(self.fave_targets[c.rb2]/100.0))*position_overalls[3])/rb_mult + 0.03*position_overalls[4]

        wr_mult = (self.fave_targets[c.wr1]+self.fave_targets[c.wr2]+self.fave_targets[c.wr3])/100.0
        self.wr = 0.97*((self.fave_targets[c.wr1]/100.0)*position_overalls[5] + (self.fave_targets[c.wr2]/100.0)*position_overalls[6] + (self.fave_targets[c.wr3]/100.0)*position_overalls[7])/wr_mult + 0.03*position_overalls[8]
        
        te_mult = self.pass_chance/100.0 * (self.fave_targets[c.te1]/100.0 + self.fave_targets[c.te2]/100.0)
        self.te = 0.97*((self.pass_chance/100.0 * self.fave_targets[c.te1]/100.0)*position_overalls[9] + (self.pass_chance/100.0 * self.fave_targets[c.te2]/100.0)*position_overalls[10])/te_mult + 0.03*position_overalls[11]

        self.ol = 0.97*(sum(position_overalls[12:17]))/5.0 + 0.03*position_overalls[17]

        self.dl = (1.2*position_overalls[18] + position_overalls[19] + 0.9*position_overalls[20] + 0.6*position_overalls[21] + 0.3*position_overalls[22] + 0.2*position_overalls[23] + 0.05*position_overalls[24])/4.25

        self.lb = (1.2*position_overalls[25] + position_overalls[26] + 0.6*position_overalls[27] + 0.2*position_overalls[28] + 0.05*position_overalls[29])/3.05

        self.db = (1.2*position_overalls[30] + position_overalls[31] + 0.8*position_overalls[32] + 0.6*position_overalls[33] + 0.2*position_overalls[34] + 0.1*position_overalls[35] + 0.05*position_overalls[36])/3.95

        self.k_ovr = position_overalls[37]

        self.rt_ovr = position_overalls[38]
        
        self.offense = (1.2*self.qb + self.rb + self.wr + self.te + self.ol)/5.2
        self.defense = (self.dl + self.lb + self.db)/3.0
        self.special = (4.0*self.k_ovr + self.rt_ovr)/5.0
        
        team =  0.425*self.offense + 0.425*self.defense + 0.15*self.special
        nums = [[self.qb, "QB"], [self.rb, "RB"], [self.wr, "WR"], [self.te, "TE"], [self.ol, "OL"], [self.dl, "DL"], [self.lb, "LB"], [self.db, "DB"], [self.k_ovr, "K"], [self.rt_ovr, "RT"]]
        nums.sort(key = lambda l: by_list_index(l, 0), reverse = False)
        
        self.biggest_needs = []
        for num in nums:
            self.biggest_needs.append(num[1])
        self.bench.sort(key = by_overall, reverse = True)
        return team
    
    def full_positions(self):
        how_many_of_each = [0,0,0,0,0,0,0,0,0,0]
        for player in self.Players:
            pos = "NA"
            try:
                pos = player.position
            except:
                pass
            if pos == "QB":
                how_many_of_each[0] += 1
            elif pos == "RB":
                how_many_of_each[1] += 1
            elif pos == "WR":
                how_many_of_each[2] += 1
            elif pos == "TE":
                how_many_of_each[3] += 1
            elif pos == "OL":
                how_many_of_each[4] += 1
            elif pos == "DL":
                how_many_of_each[5] += 1
            elif pos == "LB":
                how_many_of_each[6] += 1
            elif pos == "DB":
                how_many_of_each[7] += 1
            elif pos == "K":
                how_many_of_each[8] += 1
            elif pos == "RT":
                how_many_of_each[9] += 1
        for pos in self.fa_pos:
            if pos == "QB":
                how_many_of_each[0] += 1
            elif pos == "RB":
                how_many_of_each[1] += 1
            elif pos == "WR":
                how_many_of_each[2] += 1
            elif pos == "TE":
                how_many_of_each[3] += 1
            elif pos == "OL":
                how_many_of_each[4] += 1
            elif pos == "DL":
                how_many_of_each[5] += 1
            elif pos == "LB":
                how_many_of_each[6] += 1
            elif pos == "DB":
                how_many_of_each[7] += 1
            elif pos == "K":
                how_many_of_each[8] += 1
            elif pos == "RT":
                how_many_of_each[9] += 1
        too_many = []
        if how_many_of_each[0] >= 4:
            too_many.append("QB")
        if how_many_of_each[1] >= 6:
            too_many.append("RB")
        if how_many_of_each[2] >= 7:
            too_many.append("WR")
        if how_many_of_each[3] >= 6:
            too_many.append("TE")
        if how_many_of_each[4] >= 10:
            too_many.append("OL")
        if how_many_of_each[5] >= 10:
            too_many.append("DL")
        if how_many_of_each[6] >= 9:
            too_many.append("LB")
        if how_many_of_each[7] >= 10:
            too_many.append("DB")
        if how_many_of_each[8] >= 3:
            too_many.append("K")
        if how_many_of_each[9] >= 3:
            too_many.append("RT")
        return too_many
            
    def trade_out_player(self, player):
        player.contract_length = 0
        if player in self.bench:
            self.bench.remove(player)
        elif player in self.line_up:
            for i in range(0, len(self.line_up)):
                if player == self.line_up[i]:
                    self.line_up[i] = None
                    self.sync_starters()
                    self.best_lineup()
        if player in self.Players:
            self.Players.remove(player)
        self.calculate_cap_left()
                    
    def trade_in(self, players, picks):
        pass
        
    def upgrade_stadium(self):
        pass
        
    def upgrade_scouting(self):
        pass
        
    def increase_fans(self):
        pass
        
    def full_team_yn(self):
        for player in self.line_up:
            if player == None:
                return False
        return True
        
    def draw_stats(self, x, y):
        pass
    

################################################################################TEAM CLASS###########################################################################################
################################################################################TEAM CLASS###########################################################################################
################################################################################TEAM CLASS###########################################################################################
################################################################################TEAM CLASS###########################################################################################


################################################################################TRADE CENTER CLASS###########################################################################################
################################################################################TRADE CENTER CLASS###########################################################################################
################################################################################TRADE CENTER CLASS###########################################################################################
################################################################################TRADE CENTER CLASS###########################################################################################

class TradeCenter(object):
    
    def __init__(self):
        # view trade block, view recent trades, propose trade, view trades proposed to self
        self.buttons = []
        #self.overview_buttons = []
        self.set_buttons()
        self.trade_block = []
        self.search = "NONE"
        self.proposed_trades = []
        self.recent_trades = []
        self.current_trade = 0
        self.team_to_draw = 0
        self.deadline_passed = False
        
    def add_to_trade_block(self, player):
        if not self.deadline_passed and not player.team in {"FREE AGENT", "ROOKIE", "RETIRED"}:
            self.trade_block.append(player)
            player.in_trade_block = True
            
    def remove_from_trade_block(self, player):
        try:
            self.trade_block.remove(player)
        except:
            pass
        player.in_trade_block = False
            
    def end_season(self):
        for player in self.trade_block:
            if player.team in {"FREE AGENT", "ROOKIE", "RETIRED"}:
                self.remove_from_trade_block(player)
        self.trade_block.sort(key = by_overall, reverse = True)
        
    def end_week(self):
        for player in self.trade_block:
            if player.team in {"FREE AGENT", "ROOKIE", "RETIRED"}:
                self.remove_from_trade_block(player)
        self.trade_block.sort(key = by_overall, reverse = True) # sort by overall
        #self.proposed_trades = []
        
    def draw_buttons(self, buttons, screen):
        for button in buttons:
            if screen == button.category or button.category == "ALL":
                button.draw_button()
            
    def check_button_click(self, mouse_x, mouse_y, buttons, screen = "ALL"):
        for button in buttons:
            if button.clicked(mouse_x, mouse_y) and (button.category == "ALL" or button.category == screen):
                return button.do
        return "NONE"
        
    def set_buttons(self):
        # x y sizex sizey text name group
        self.buttons.append(Button(100, 250, 250, 250, "Trade Block", "TRADE BLOCK", "TRADE CENTER"))
        self.buttons.append(Button(350, 250, 250, 250, "Recent Trades", "RECENT TRADES", "TRADE CENTER"))
        self.buttons.append(Button(100, 500, 250, 250, "Propose Trade", "PROPOSE TRADE", "TRADE CENTER"))
        self.buttons.append(Button(350, 500, 250, 250, "My Trades", "MY TRADES", "TRADE CENTER"))
        self.buttons.append(Button(1600, 50, 150,  35, "Trade Center", "TRADE CENTER", "ALL"))
        self.buttons.append(Button(10, 900, 1100, 35, "Team rejects offer", "DECISION", "TRADE OVERVIEW"))
        self.buttons.append(Button(10, 940, 1100, 35, "Propose Trade", "PROPOSE", "TRADE OVERVIEW"))
        
        #self.overview_buttons.append(Button(10, 900, 1100, 35, "Team rejects offer", "DECISION", "DEC"))
        #self.overview_buttons.append(Button(10, 940, 1100, 35, "Propose Trade", "PROPOSE", "PROP"))
        
    def draw_trade_center(self):
        self.draw_buttons(self.buttons, "TRADE CENTER")
        textSize(70)
        text("TRADE CENTER", 5, 75)
        
    def draw_trade_block(self, x, y):
        global use_overall
        self.draw_buttons(self.buttons, "TRADE BLOCK")
        printed = 0
        i = 0
        for player in self.trade_block:
            if not player.is_tradeable():
                self.trade_block.remove(player)
                player.in_trade_block = False
                continue
            if self.search == player.position or self.search == "NONE":
                player.draw_player(x + (printed % 9) * 150, y + (printed / 9) * 175, True, 1, use_ovr = use_overall)
                printed += 1
            i += 1
        fill(150)
        rect(1400, 50, 175, 75, 7)
        fill(0)
        text("Search:\npos: " + self.search, 1400, 50, 175, 75)
        
    def draw_trade_summary(self, trade, x, y, highlight = False):
        global use_overall
        textSize(20)
        fill(150)
        if highlight:
            fill(200, 200, 100)
        rect(x, y, 1300, 120, 7)
        fill(0)
        team1_trade = ""
        for player in trade.team1_offer[0]:
            team1_trade += player.first_name + " " + player.position + " " + str(int(player.overall(use_overall))) + ", "
        for pick in trade.team1_offer[1]:
            team1_trade += "Round " + str(pick[0]) + " pick " + str(pick[1]) + ", "
        text(trade.team1.abbreviation + " trades " + team1_trade[:-2], x + 20, y + 25)
        text("Net value: " + str(round(trade.get_value_from_team(1, True) + trade.get_value_from_team(1, False))), x + 20, y + 55)
        team2_trade = ""
        for player in trade.team2_offer[0]:
            team2_trade += player.first_name + " " + player.position + " " + str(int(player.overall(use_overall))) + ", "
        for pick in trade.team2_offer[1]:
            team2_trade += "Round " + str(pick[0]) + " pick " + str(pick[1]) + ", "
        text(trade.team2.abbreviation + " trades " + team2_trade[:-2], x + 20, y + 85)
        text("Net value: " + str(round(trade.get_value_from_team(2, True) + trade.get_value_from_team(2, False))), x + 20, y + 115)
        
    def draw_recent_trades(self, x, y):
        global user_teams, user_team_number, use_overall
        self.draw_buttons(self.buttons, "RECENT TRADES")
        fill(0)
        textSize(50)
        text("Recent Trades", x + 10, y + 60)
        y += 80
        textSize(20)
        for i in range(0, len(self.recent_trades)):
            trade = self.recent_trades[-i-1]
            if not trade.complete:
                continue
            highlight = user_teams[user_team_number] in [trade.team1, trade.team2]
            self.draw_trade_summary(trade, x+10, y, highlight)
            y += 130
            
    def draw_propose_trade(self, x, y, teams):
        self.draw_buttons(self.buttons, "PROPOSE TRADE")
        textSize(50)
        y += 50
        text("CHOOSE A TEAM TO TRADE WITH", x, y)
        y += 50
        i = 0
        x_now = x
        for team in teams:
            team.draw_team_summary(x_now, y)
            x_now += 200
            i += 1
            if i % 4 == 0:
                y += 200
                x_now = x
                
    def draw_trade_overview(self, x, y):
        global use_overall
        self.draw_buttons(self.buttons, "TRADE OVERVIEW")
        #self.draw_buttons(self.overview_buttons)
        y_in = y
        textSize(50)
        y += 50
        text("TRADE OVERVIEW", x, y)
        fill(150)
        y += 20
        rect(x + 10, y, 500, 35 + 30 * max(len(self.current_trade.team1_offer[0]) + len(self.current_trade.team1_offer[1]), len(self.current_trade.team2_offer[0]) + len(self.current_trade.team2_offer[1])), 7)
        fill(0)
        textSize(25)
        y += 30
        text(self.current_trade.team1.abbreviation + " trade:", x + 20, y)
        textSize(20)
        for player in self.current_trade.team1_offer[0]:
            y += 30
            text(player.name() + player.position + " " + str(int(player.overall(use_overall))) + " OVR " + str(player.age) + " YO " + str(player.contract_length) + "yrs, " + str(round(player.contract_amount/1000000.0,2)) + " mil", x + 20, y)
        for pick in self.current_trade.team1_offer[1]:
            y += 30
            text("Round " + str(pick[0]) + ", pick " + str(pick[1]), x + 20, y)
        y = y_in + 135 + 30 * max(len(self.current_trade.team1_offer[0]) + len(self.current_trade.team1_offer[1]), len(self.current_trade.team2_offer[0]) + len(self.current_trade.team2_offer[1]))
        #text("Value in: " + str(int(self.current_trade.get_value_from_team(1, True))), x + 20, y)
        #text("Value out: " + str(int(self.current_trade.get_value_from_team(1, False))), x + 270, y)
        text("Net value: " + str(int(self.current_trade.get_value_from_team(1, True) + self.current_trade.get_value_from_team(1, False))), x + 20, y)
        text("New cap: " + str(round((self.current_trade.team1.cap_left + self.current_trade.get_net_cap_for_team(1))/1000000.0, 2)) + " million", x + 20, y + 20)
        
        y = y_in
        fill(150)
        y += 70
        rect(x + 600, y, 500, 35 + 30 * max(len(self.current_trade.team1_offer[0]) + len(self.current_trade.team1_offer[1]), len(self.current_trade.team2_offer[0]) + len(self.current_trade.team2_offer[1])), 7)
        fill(0)
        textSize(25)
        y += 30
        text(self.current_trade.team2.abbreviation + " trade:", x + 610, y)
        textSize(20)
        for player in self.current_trade.team2_offer[0]:
            y += 30
            text(player.name() + player.position + " " + str(int(player.overall(use_overall))) + " OVR " + str(player.age) + " YO " + str(player.contract_length) + "yrs, " + str(round(player.contract_amount/1000000.0,2)) + " mil", x + 610, y)
        for pick in self.current_trade.team2_offer[1]:
            y += 30
            text("Round " + str(pick[0]) + ", pick " + str(pick[1]), x + 610, y)
        y = y_in + 135 + 30 * max(len(self.current_trade.team1_offer[0]) + len(self.current_trade.team1_offer[1]), len(self.current_trade.team2_offer[0]) + len(self.current_trade.team2_offer[1]))
        #text("Value in: " + str(int(self.current_trade.get_value_from_team(2, True))), x + 610, y)
        #text("Value out: " + str(int(self.current_trade.get_value_from_team(2, False))), x + 860, y)
        text("Net value: " + str(int(self.current_trade.get_value_from_team(2, True) + self.current_trade.get_value_from_team(2, False))), x + 610, y)
        text("New cap: " + str(round((self.current_trade.team2.cap_left + self.current_trade.get_net_cap_for_team(2))/1000000.0, 2)) + " million", x + 610, y + 20)
        
        #if self.current_trade.get_value_from_team(2, True) + self.current_trade.get_value_from_team(2, False) > 0:
        for button in self.buttons:
            if button.do == "DECISION":
                if self.current_trade.team2_accepts:
                    button.t = self.current_trade.team2.abbreviation + " accept the trade"
                else:
                    button.t = self.current_trade.team2.abbreviation + " reject the trade"
                return
            
    def draw_team_tradeables(self, x, y):
        self.draw_buttons(self.buttons, "TEAM TRADEABLES")
        self.team_to_draw.draw_team(x, y, "TRADE", "NONE", False)
        
    def draw_my_trades(self, x, y):
        global user_teams, user_team_number
        self.draw_buttons(self.buttons, "MY TRADES")
        fill(0)
        textSize(50)
        text("My Trades", x + 10, y + 60)
        i = 0
        for trade in reversed(self.proposed_trades):
            if trade.complete or not trade.is_valid_trade():
                self.proposed_trades.remove(trade)
                continue
            if user_teams[user_team_number] in [trade.team1, trade.team2]:
                self.draw_trade_summary(trade, x + 10, y + 140 + 130*i)
                i += 1
        
    def trade_center_clicked(self, mouse_x, mouse_y):
        screen_change = self.check_button_click(mouse_x, mouse_y, self.buttons, "TRADE CENTER")
        if self.deadline_passed and screen_change in {"PROPOSE TRADE", "TRADE BLOCK"}:
            return
        if not screen_change == "NONE":
            change_screen(screen_change)
            
    def ai_propose_trade(self, team):
        if team in [self.current_trade.team1, self.current_trade.team2]:
            if not self.current_trade in self.proposed_trades:
                #print str(self.current_trade.team1.abbreviation) + " " + str(self.current_trade.team2.abbreviation)
                self.proposed_trades.append(self.current_trade)
            
    def ai_add_to_trade(self, team, to_add):
        if team in [self.current_trade.team1, self.current_trade.team2]:
            self.current_trade.add_to_offer(team, to_add)
            
    def ai_remove_from_trade(self, team, to_remove):
        if team in [self.current_trade.team1, self.current_trade.team2]:
            self.current_trade.add_to_offer(team, to_remove)
            
    def ai_trade_block_select(self, team, player):
        #player = self.trade_block[player_num]
        this_trade = Trade(team, get_team_from_name(player.team))
        this_trade.add_to_offer(get_team_from_name(player.team), player)
        self.current_trade = this_trade
            
    def trade_block_clicked(self, screen_x, screen_y, mouse_x, mouse_y):
        global user_teams, user_team_number
        screen_change = self.check_button_click(mouse_x, mouse_y, self.buttons, "TRADE BLOCK")
        if not screen_change == "NONE":
            change_screen(screen_change)
            return
        x_off = int(mouse_x - screen_x)/150
        y_off = int(mouse_y - screen_y)/175
        if x_off >= 0 and x_off <= 9 and y_off >= 0:
            player_num = x_off + 9*y_off
        else:
            return
        i = -1
        for player in self.trade_block:
            if self.search == player.position or self.search == "NONE":
                i += 1
            if i == player_num:
                this_trade = Trade(user_teams[user_team_number], get_team_from_name(player.team))
                this_trade.add_to_offer(get_team_from_name(player.team), player)
                self.current_trade = this_trade
                change_screen("TRADE OVERVIEW")
                
    def propose_trade_clicked(self, x, y, teams, mouse_x, mouse_y):
        global user_teams, user_team_number
        screen_change = self.check_button_click(mouse_x, mouse_y, self.buttons, "PROPOSE TRADE")
        if not screen_change == "NONE":
            change_screen(screen_change)
            return
        mouse_x -= x
        mouse_y -= 100 + y
        if mouse_x < 0 or mouse_x > 800 or mouse_y < 0 or mouse_y > 1600:
            return
        team_num = int(mouse_x / 200) + 4 * int(mouse_y / 200)
        change_screen("TRADE OVERVIEW")
        new_trade = Trade(user_teams[user_team_number], teams[team_num])
        #self.recent_trades.insert(0, new_trade)
        self.current_trade = new_trade
        for button in self.buttons:
            if button.do == "DECISION":
                button.t = teams[team_num].abbreviation + " reject the offer"
                return
        
    def trade_overview_clicked(self, x, y, mouse_x, mouse_y):
        screen_change = self.check_button_click(mouse_x, mouse_y, self.buttons, "TRADE OVERVIEW")
        if not screen_change in {"NONE", "DECISION", "PROPOSE"}:
            change_screen(screen_change)
            return
        if mouse_x - x > 10 and mouse_x - x < 510 and mouse_y - y > 70 and mouse_y - y < 100:
            change_screen("TEAM TRADEABLES")
            self.team_to_draw = self.current_trade.team1
        elif mouse_x - x > 600 and mouse_x - x < 1100 and mouse_y - y > 70 and mouse_y - y < 100:
            change_screen("TEAM TRADEABLES")
            self.team_to_draw = self.current_trade.team2
        else:
            clicked = self.check_button_click(mouse_x, mouse_y, self.buttons, "TRADE OVERVIEW")
            if clicked == "NONE":
                return
            if clicked == "PROPOSE":
                self.current_trade.accept_trade(self.current_trade.team1)
                if self.current_trade.complete:
                    self.recent_trades.append(self.current_trade)
                elif not self.current_trade in self.proposed_trades:
                    self.proposed_trades.append(self.current_trade)
            
    def team_tradeables_clicked(self, x, y, mouse_x, mouse_y):
        screen_change = self.check_button_click(mouse_x, mouse_y, self.buttons, "TEAM TRADEABLES")
        if not screen_change == "NONE":
            change_screen(screen_change)
            return
        clicked = self.team_to_draw.get_clicked(x, y, "TRADE", mouse_x, mouse_y)
        if clicked == "NONE":
            return
        if self.current_trade.in_trade(clicked):
            self.current_trade.remove_from_offer(self.team_to_draw, clicked)
        else:
            self.current_trade.add_to_offer(self.team_to_draw, clicked)
        change_screen("TRADE OVERVIEW")
        
    def my_trades_clicked(self, x, y, mouse_x, mouse_y):
        global user_teams, user_team_number
        screen_change = self.check_button_click(mouse_x, mouse_y, self.buttons, "MY TRADES")
        if not screen_change == "NONE":
            change_screen(screen_change)
            return
        if mouse_x > x + 10 and mouse_x < x + 1310:
            i = (mouse_y - y - 140) / 70
            j = 0
            for trade in reversed(self.proposed_trades):
                if user_teams[user_team_number] in [trade.team1, trade.team2]:
                    if i == j:
                        if user_teams[user_team_number] == trade.team2:
                            trade.swap_teams()
                        self.current_trade = trade 
                        change_screen("TRADE OVERVIEW")
                    j += 1
                    
    def recent_trades_clicked(self, x, y, mouse_x, mouse_y):
        screen_change = self.check_button_click(mouse_x, mouse_y, self.buttons, "RECENT TRADES")
        if not screen_change == "NONE":
            change_screen(screen_change)
            return

################################################################################TRADE CENTER CLASS###########################################################################################
################################################################################TRADE CENTER CLASS###########################################################################################
################################################################################TRADE CENTER CLASS###########################################################################################
################################################################################TRADE CENTER CLASS###########################################################################################


################################################################################TRADE CLASS###########################################################################################
################################################################################TRADE CLASS###########################################################################################
################################################################################TRADE CLASS###########################################################################################
################################################################################TRADE CLASS###########################################################################################

class Trade(object):
    
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_offer = [[], []] # players, picks
        self.team2_offer = [[], []]
        self.team1_accepts = False
        self.team2_accepts = False
        self.complete = False
        #self.trade_id = 0
        
    def is_fair_draft_picks(self):
        team1_picks = len(self.team2_offer[1]) - len(self.team1_offer[1]) + len(self.team1.draft_picks)
        team2_picks = len(self.team1_offer[1]) - len(self.team2_offer[1]) + len(self.team2.draft_picks)
        if team1_picks < 4 or team2_picks < 4 or team1_picks > 21 or team2_picks > 21:
            return False
        return True
        
    def is_valid_trade(self):
        for player in self.team1_offer[0]:
            if not player in self.team1.Players:
                return False
        for pick in self.team1_offer[1]:
            if not pick in self.team1.draft_picks:
                return False
        for player in self.team2_offer[0]:
            if not player in self.team2.Players:
                return False
        for pick in self.team2_offer[1]:
            if not pick in self.team2.draft_picks:
                return False
        return True
        
    def swap_teams(self):
        self.team1, self.team2 = self.team2, self.team1
        self.team1_offer, self.team2_offer = self.team2_offer, self.team1_offer
        self.team1_accepts, self.team2_accepts = self.team2_accepts, self.team1_accepts
        
    def get_net_cap_for_team(self, team_num):
        net_cap = 0
        for player in self.team2_offer[0]:
            net_cap += player.contract_amount
        for player in self.team1_offer[0]:
            net_cap -= player.contract_amount
        if team_num == 1:
            net_cap = -1*net_cap
        return net_cap
        
    def get_value_from_team(self, team_num, coming_in):
        global c, season1
        val = 0
        net_cap = self.get_net_cap_for_team(team_num)
        is_over_cap = False
        if team_num == 1:
            if self.team1.cap_left + net_cap < 0:
                is_over_cap = True
            if coming_in:
                for player in self.team2_offer[0]:
                    val += self.team1.trade_in_value(player)
                for pick in self.team2_offer[1]:
                    val += season1.draft_pick_value(pick)
            else:
                for player in self.team1_offer[0]:
                    val += self.team1.trade_out_value(player)
                for pick in self.team1_offer[1]:
                    val -= season1.draft_pick_value(pick)
        else:
            if self.team2.cap_left + net_cap < 0:
                is_over_cap = True
            if coming_in:
                for player in self.team1_offer[0]:
                    val += self.team2.trade_in_value(player)
                for pick in self.team1_offer[1]:
                    val += season1.draft_pick_value(pick)
            else:
                for player in self.team2_offer[0]:
                    val += self.team2.trade_out_value(player)
                for pick in self.team2_offer[1]:
                    val -= season1.draft_pick_value(pick)
        if is_over_cap:
            return val*0.6 + (net_cap/10000.0)
        else:
            return val + (net_cap/10000.0)
        
    def in_trade(self, player_or_pick):
        if is_player(player_or_pick):
            if player_or_pick in self.team1_offer[0] or player_or_pick in self.team2_offer[0]:
                return True
        elif player_or_pick in self.team1_offer[1] or player_or_pick in self.team2_offer[1]:
            return True
        return False
        
    def add_to_offer(self, team, addition):
        if not is_team(team):
            return
        self.team1_accepts = False
        self.team2_accepts = False
        offer = 0
        if self.team1.name() == team.name():
            offer = self.team1_offer
        else:
            offer = self.team2_offer
        if is_player(addition) and addition.is_tradeable():
            if not addition in offer[0] and addition in team.Players:
                offer[0].append(addition)
        else:
            if not addition in offer[1] and addition in team.draft_picks:
                offer[1].append(addition)
        if not self.team1.user_type == "USER":
            if self.get_value_from_team(1, True) + self.get_value_from_team(1, False) > 0 and self.is_fair_draft_picks():
                self.accept_trade(self.team1)
        if not self.team2.user_type == "USER":
            if self.get_value_from_team(2, True) + self.get_value_from_team(2, False) > 0 and self.is_fair_draft_picks():
                self.accept_trade(self.team2)
        
    def remove_from_offer(self, team, removal):
        if not is_team(team):
            return
        self.team1_accepts = False
        self.team2_accepts = False
        offer = 0
        if self.team1.name() == team.name():
            offer = self.team1_offer
        else:
            offer = self.team2_offer
        if is_player(removal) and removal in offer[0]:
            offer[0].remove(removal)
        elif removal in offer[1]:
            offer[1].remove(removal)
        if not self.team1.user_type == "USER":
            if self.get_value_from_team(1, True) + self.get_value_from_team(1, False) > 0 and self.is_fair_draft_picks():
                self.accept_trade(self.team1)
        if not self.team2.user_type == "USER":
            if self.get_value_from_team(2, True) + self.get_value_from_team(2, False) > 0 and self.is_fair_draft_picks():
                self.accept_trade(self.team2)
            
    def accept_trade(self, team):
        if team == self.team1 and self.is_fair_draft_picks():
            self.team1_accepts = True
        elif team == self.team2 and self.is_fair_draft_picks():
            self.team2_accepts = True
        if self.team1_accepts and self.team2_accepts:
            self.complete_trade()
        
    def complete_trade(self):
        if not self.is_valid_trade():
            return
        for player in self.team1_offer[0]:
            if not player.is_tradeable():
                return
        for player in self.team2_offer[0]:
            if not player.is_tradeable():
                return
        for player in self.team1_offer[0]:
            contract_amount = player.contract_amount
            contract_length = player.contract_length
            self.team1.trade_out_player(player)
            self.team2.add_player(player)
            self.team2.sign_player(player, contract_length, contract_amount)
            player.trade_player(self.team2.abbreviation)
        for pick in self.team1_offer[1]:
            self.team1.draft_picks.remove(pick)
            self.team2.draft_picks.append(pick)
        for player in self.team2_offer[0]:
            contract_amount = player.contract_amount
            contract_length = player.contract_length
            self.team2.trade_out_player(player)
            self.team1.add_player(player)
            self.team1.sign_player(player, contract_length, contract_amount)
            player.trade_player(self.team1.abbreviation)
        for pick in self.team2_offer[1]:
            self.team2.draft_picks.remove(pick)
            self.team1.draft_picks.append(pick)
        self.complete = True
        if self.team1.user_type == "USER": #or self.team2.user_type == "USER":
            change_screen("SEASON")

################################################################################TRADE CLASS###########################################################################################
################################################################################TRADE CLASS###########################################################################################
################################################################################TRADE CLASS###########################################################################################
################################################################################TRADE CLASS###########################################################################################


################################################################################FA CLASS###########################################################################################
################################################################################FA CLASS###########################################################################################
################################################################################FA CLASS###########################################################################################
################################################################################FA CLASS###########################################################################################

class FreeAgents(object):
    
    def __init__(self, players):
        self.players = players
        self.bids = [[0,0]]*len(players)
        
    def draw_free_agents(self, x, y, search, price, only_rookies = False):
        printed = 0
        i = 0
        for player in self.players:
            if search == player.position and price >= max(self.bids[i][0], player.min_contract()) and (player.years_played == 0 or not only_rookies):
                player.draw_player(x + (printed % 9) * 150, y + (printed / 9) * 175, True, 1)
                if not (self.bids[i][0] == 0):
                    fill(0)
                    text(self.bids[i][1].abbreviation + " $" + str(round(self.bids[i][0]/1000000.0, 2)) + " mil", x + 5 + (printed % 9) * 150, y + 160 + (printed / 9) * 175)
                printed += 1
            elif search == "NONE" and price >= max(self.bids[i][0], player.min_contract()) and (player.years_played == 0 or not only_rookies):
                player.draw_player(x + (printed % 9) * 150, y + (printed / 9) * 175, True, 1)
                if not (self.bids[i][0] == 0):
                    fill(0)
                    text(self.bids[i][1].abbreviation + " $" + str(round(self.bids[i][0]/1000000.0, 2)) + " mil", x + 5 + (printed % 9) * 150, y + 160 + (printed / 9) * 175)
                printed += 1
            i += 1
        fill(150)
        rect(1400, 50, 175, 75, 7)
        fill(0)
        text("Search:\npos: " + search + "\n$" + str(round(price/1000000.0, 2)) + " million", 1400, 50, 175, 75)
            
    def sign_free_agents(self):
        i = 0
        while i < len(self.players):
            if self.bids[i][0] >= self.players[i].min_contract():
                self.bids[i][1].fa_bids -= self.bids[i][0]
                self.bids[i][1].fas -= 1
                self.bids[i][1].calculate_cap_left()
                self.bids[i][1].add_player(self.players[i])
                self.bids[i][1].sign_player(self.players[i], int(random(1, 6)), self.bids[i][0])
                self.players.remove(self.players[i])
                self.bids.remove(self.bids[i])
            else:
                i += 1
        for pos in ["QB", "RB", "WR", "TE", "OL", "DL","LB", "DB", "K", "RT"]:
            count = 0
            for player in self.players:
                if player.position == pos:
                    count += 1
                if count >= 2:
                    break
            if count < 2:
                new_player = Player(pos, 40)
                new_player.team = "FREE AGENT"
                self.add_free_agents([new_player])
    
    def add_free_agents(self, new_players):
        for player in new_players:
            if not player.retired and not player in self.players:
                self.players.append(player)
                self.bids.append([0,0])
                
        
    def bid_on_free_agent(self, player, team, amount):
        i = self.players.index(player)
        if self.bids[i][0] < amount and amount >= player.min_contract():
            if self.bids[i][0] > 0:
                self.bids[i][1].fa_bids -= self.bids[i][0]
                self.bids[i][1].fas -= 1
                self.bids[i][1].calculate_cap_left()
            self.bids[i] = [amount, team]
            return True
        else:
            team.fa_bids -= amount
            team.fas -= 1
            return False
        
    def cut_free_agents(self, num_left):
        self.sort_free_agents()
        self.players = self.players[0:num_left]
        self.bids = self.bids[0:num_left]
    
    def sort_free_agents(self):
        self.players.sort(key = by_overall, reverse = True)  
                    
    def advance_week(self):
        for player in self.players:
            player.end_week()
        for player in self.players:
            if player.retired:
                self.players.remove(player)
        
    def advance_season(self):
        for player in self.players:
            player.end_season()
            if player.retired:
                self.players.remove(player)
        

################################################################################FA CLASS###########################################################################################
################################################################################FA CLASS###########################################################################################
################################################################################FA CLASS###########################################################################################
################################################################################FA CLASS###########################################################################################

################################################################################DRAFT CLASS###########################################################################################
################################################################################DRAFT CLASS###########################################################################################
################################################################################DRAFT CLASS###########################################################################################
################################################################################DRAFT CLASS###########################################################################################

class Draft(object):
    
    def __init__(self, t, r, y, mega_draft):
        self.this_year = y
        self.teams = t
        self.rounds = r
        self.current_pick = -1
        self.current_team = 0
        self.selections = []
        self.is_done = False
        self.prev_pick = 0
        self.prev_team = 0
        self.mega_draft = mega_draft
        self.sort_type = "OVERALL"
        
        self.players = self.generate_players()
        for team in self.teams:
            self.selections.append([])
        self.buttons = [ Button(1400, 500, 150, 50, "By Overall", "OVERALL", "SORT"), Button(1400, 550, 150, 50, "By Value", "VALUE", "SORT"),
                         Button(1400, 600, 150, 50, "My Value", "MY VALUE", "SORT"),
                         Button(1400, 700, 150, 50, "Skip to Next Pick", "SKIP TO USER", "SKIP") ]
        self.buttons[0].highlight = True
        
    
    def sort_by(self, sort_type, team, num):
        if num == "ALL":
            num = len(self.players)
        if num > len(self.players):
            num = len(self.players)
        if not self.sort_type == sort_type or sort_type == "MY VALUE":
            self.sort_type = sort_type
            if sort_type == "OVERALL":
                if self.mega_draft:
                    self.players[0:num].sort(key = by_overall, reverse = True)
                else:
                    self.players[0:num].sort(key = by_proj_overall, reverse = True)
                for button in self.buttons:
                    button.highlight = False
                self.buttons[0].highlight = True
            elif sort_type == "VALUE":
                self.players[0:num].sort(key = lambda l: by_value(l, not self.mega_draft), reverse = True)
                for button in self.buttons:
                    button.highlight = False
                self.buttons[1].highlight = True
            elif sort_type == "MY VALUE":
                self.sort_type = "MY VALUE"
                self.players.sort(key = lambda l: by_team_draft_value(team, l, not self.mega_draft), reverse = True)
                for button in self.buttons:
                    button.highlight = False
                self.buttons[1].highlight = True
    
    def clicked(self, mouse_x, mouse_y, current_team):
        global auto_draft_end
        click = button_clicked(mouse_x, mouse_y, self.buttons, "SORT", "EXCLUSIVE")
        if click == "OVERALL" and not self.sort_type == "OVERALL":
            self.sort_type = "OVERALL"
            if self.mega_draft:
                self.players.sort(key = by_overall, reverse = True)
            else:
                self.players.sort(key = by_proj_overall, reverse = True)
        elif click == "VALUE" and not self.sort_type == "VALUE":
            self.sort_type = "VALUE"
            self.players.sort(key = lambda l: by_value(l, not self.mega_draft), reverse = True)
        elif click == "MY VALUE":
            self.sort_type = "MY VALUE"
            self.players.sort(key = lambda l: by_team_draft_value(current_team, l, not self.mega_draft), reverse = True)
        click = button_clicked(mouse_x, mouse_y, self.buttons, "SKIP", "NONE")
        if click == "SKIP TO USER":
            change_screen("AUTO DRAFTING")
            auto_draft_end = "USER"
        
    def print_selections(self):
        words = "["
        for i in range(0, len(self.selections)):
            words += "["
            for player in self.selections[i]:
                words += player.first_name + ", "
            words += "], "
        words[-1] = "]"
        println(words)
        
    def draw_draft(self, x, y, search, scouting):
        fill(0)
        background(100)
        for button in self.buttons:
            button.draw_button()
        text("Current sort: " + self.sort_type, 1400, 475)
        textSize(15)
        text("Selections:", x, -100 + y - 200*len(self.teams))
        for k in range(0, len(self.teams)):
            positions = {"QB":0, "RB":0, "WR":0, "TE":0, "OL":0, "DL":0, "LB":0, "DB":0, "K":0, "RT":0}
            for m in range(0, len(self.selections[k])):
                self.selections[k][m].draw_player(x + 150 * m, -45 + y - 200 * (len(self.teams) - k), True, 1)
                pos = self.selections[k][m].position
                positions[pos] += 1
            if self.teams[k] == self.current_team:
                fill(0)
                text(str(int(round(self.teams[k].get_team_overall()))) + " OVR " + self.teams[k].abbreviation + ":    QB " + str(int(round(self.teams[k].qb))) + " OVR: " + str(positions["QB"]) + "    RB " + str(int(round(self.teams[k].rb))) + " OVR: "  + str(positions["RB"]) + "    WR " + str(int(round(self.teams[k].wr))) + " OVR: "  + str(positions["WR"]) + "    TE " + str(int(round(self.teams[k].te))) + " OVR: "  + str(positions["TE"]) + "    OL " + str(int(round(self.teams[k].ol))) + " OVR: "  + str(positions["OL"]) + "    DL " + str(int(round(self.teams[k].dl))) + " OVR: "  + str(positions["DL"]) +  "    LB " + str(int(round(self.teams[k].lb))) + " OVR: "  + str(positions["LB"]) + "    DB " + str(int(round(self.teams[k].db))) + " OVR: "  + str(positions["DB"]) + "    K " + str(int(round(self.teams[k].k_ovr))) + " OVR: "  + str(positions["K"]) + "    RT " + str(int(round(self.teams[k].rt_ovr))) + " OVR: "  + str(positions["RT"]) + "   Total: " + str(len(self.selections[k])), x, -50 + y + 25)
            text(str(int(round(self.teams[k].get_team_overall()))) + " OVR " + self.teams[k].abbreviation + ":    QB " + str(int(round(self.teams[k].qb))) + " OVR: " + str(positions["QB"]) + "    RB " + str(int(round(self.teams[k].rb))) + " OVR: "  + str(positions["RB"]) + "    WR " + str(int(round(self.teams[k].wr))) + " OVR: "  + str(positions["WR"]) + "    TE " + str(int(round(self.teams[k].te))) + " OVR: "  + str(positions["TE"]) + "    OL " + str(int(round(self.teams[k].ol))) + " OVR: "  + str(positions["OL"]) + "    DL " + str(int(round(self.teams[k].dl))) + " OVR: "  + str(positions["DL"]) +  "    LB " + str(int(round(self.teams[k].lb))) + " OVR: "  + str(positions["LB"]) + "    DB " + str(int(round(self.teams[k].db))) + " OVR: "  + str(positions["DB"]) + "    K " + str(int(round(self.teams[k].k_ovr))) + " OVR: "  + str(positions["K"]) + "    RT " + str(int(round(self.teams[k].rt_ovr))) + " OVR: "  + str(positions["RT"]) + "   Total: " + str(len(self.selections[k])), x, -50 + y - 200 * (len(self.teams) - k))
        textSize(25)
        fill(0)
        if not self.is_done:
            text("Round " + str(self.get_round()) + ", pick " + str(self.get_pick()) + ": The " + self.current_team.name() + " are on the clock with the #" + str(self.current_pick + 1) + " pick", x + 10, y - 50)
        else:
            text("The draft is over", x + 10, y - 50)
        printed = 0
        show_true_overall = False
        if self.mega_draft:
            show_true_overall = True
        for player in self.players:
            if printed > 200:
                break;
            if search == player.position:
                player.draw_player_scouting(x + (printed % 9) * 150, y + (printed / 9) * 175, show_true_overall, 1, scouting)
                printed += 1
            elif search == "NONE":
                player.draw_player_scouting(x + (printed % 9) * 150, y + (printed / 9) * 175, show_true_overall, 1, scouting)
                printed += 1
        if self.current_pick >= 1:
            fill(0)
            text("Last pick: " + self.prev_team.abbreviation, x + 1450, y - 10)
            self.prev_player.draw_player(x + 1500, y, True, 1)

    def get_round(self):
        if (self.current_pick+1) % len(self.teams) == 0:
            return (self.current_pick + 1) / len(self.teams)
        return (self.current_pick + 1) / len(self.teams) + 1
    
    def get_pick(self):
        return self.current_pick % len(self.teams) + 1
         
    def generate_players(self):
        global ls
        plyrs = []
        num_players = (self.rounds + 5) * (len(self.teams) + 1)
        if self.mega_draft:
            num_players = 2100
        for x in range(0, num_players):
            pos = random_position()
            age = random_starting_age()
            if not self.mega_draft:
                age = int(random(20, 24))
            skew = 0
            if pos == "K":
                skew = 5
            ovr = random_ovr_from_age(age, skew)
            new_player = Player(pos, ovr[0], ovr[1])
            new_player.draft_position[2] = self.this_year
            new_player.set_age(age)
            new_player.adjust_ovr = min_max_skew(0,15)
            plyrs.append(new_player)
        if self.mega_draft:
            plyrs.sort(key = by_overall, reverse = True)
        else:
            plyrs.sort(key = by_proj_overall, reverse = True)
        ls.add_players(plyrs)
        return plyrs
        
    def sign_player(self, player):
        self.prev_player = player
        ind = self.teams.index(self.current_team)
        self.selections[ind].append(player)
        self.current_team.add_player(player)
        player.drafted_by = self.current_team.abbreviation
        player.draft_position[0] = self.get_round()
        player.draft_position[1] = self.get_pick()
        player.draft_position[2] = self.this_year
        self.players.remove(player)
        self.current_team.best_lineup()
        for pick in self.current_team.draft_picks:
            if pick[0] == 1 + self.current_pick / len(self.teams) and pick[1] == 1 + self.current_pick % len(self.teams):
                self.current_team.draft_picks.remove(pick)
                return
        
    def set_pick(self, jump):
        global season1
        self.prev_team = self.current_team
        self.current_pick += jump
        if self.current_pick > self.rounds * len(self.teams) - 1:
            self.is_done = True
            season1.free_agents.add_free_agents(self.players)
            for team in self.teams:
                #team.draft_picks = []
                if self.mega_draft:
                    for i in range(1, 8):
                        team.draft_picks.append([i, team.abbreviation, self.this_year + 2])
                else:
                    for i in range(1, self.rounds + 1):
                        team.draft_picks.append([i, team.abbreviation, self.this_year + 2])
        else:
            for team in self.teams:
                for pick in team.draft_picks:
                    if pick[0] == self.get_round() and pick[1] == self.get_pick() and pick[2] == self.this_year:
                        self.current_team = team
                        return
        #print("error: pick: " + str(self.get_round()) + ", " + str(self.get_pick()) + str(self.this_year) + " not found")
        
################################################################################DRAFT CLASS###########################################################################################
################################################################################DRAFT CLASS###########################################################################################
################################################################################DRAFT CLASS###########################################################################################
################################################################################DRAFT CLASS###########################################################################################


################################################################################LEAGUE STATS CLASS###########################################################################################
################################################################################LEAGUE STATS CLASS###########################################################################################
################################################################################LEAGUE STATS CLASS###########################################################################################
################################################################################LEAGUE STATS CLASS###########################################################################################

class League_Stats(object):
    
    def __init__(self):
        # to add a new stat: 
            # ADD TO make_stats_table
            # ADD TO set_buttons and fix numbers at bottom
            # ADD TO list in draw_leaders
        self.all_players =             []
        self.all_teams =               []
        self.sb_winners =              []
        self.retired =                 0
        self.new_retired =             0
        self.qb_xp =                   0
        self.rb_xp =                   0
        self.wr_xp =                   0
        self.te_xp =                   0
        self.ol_xp =                   0
        self.dl_xp =                   0
        self.lb_xp =                   0
        self.db_xp =                   0
        self.k_xp =                    0
        self.rt_xp =                   0
        self.fatigues = {"QB":0,"RB":0,"WR":0,"TE":0,"OL":0,"DL":0,"LB":0,"DB":0,"K":0,"RT":0}
        self.numbers_scope =           0
        self.numbers_table_sort =      0
        self.numbers_sort_order =      True
        self.add_on_stat =             ""
        self.top_performers =          0
        self.scope =                   0
        self.type =                    "PASS"
        self.pos =                     "ALL"
        self.min_att =                 1
        self.show_num =                10
        self.sort_type =               ""
        self.max_show_list =           5000
        self.this_year =               1966
        self.buttons =                 []
        self.set_buttons()
        
    
    def draw_leaders_ffp(self, scope, this_year, x, y, num = 3, ppr = False):
        positions = ["QB", "RB", "WR", "TE", "K", "RT"]
        self.numbers_table_sort = 5
        self.numbers_sort_order = False
        stat = "FANTASY"
        i = 0
        textSize(20)
        fill(0)
        text(scope + " LEADERS:", x, y)
        buffer = 20
        for pos in positions:
            self.draw_leaders(x, y+buffer+20*(num+2)*i, None, scope, [pos], [stat], num, 1, ["ACTIVE"], [8], False, "", this_year, True)
            i += 1
    
    def end_year(self):
        self.this_year += 1
        for button in self.buttons:
            if button.category == "YEAR" and not button.do == "THIS YEAR":
                if button.x > 1500:
                    button.x = 305
                    button.y += 25
                else:
                    button.x += 75
        self.buttons.append(Button(405, 150, 75, 25, self.this_year - 1, self.this_year - 1, "YEAR"))
    
    def reset_buttons(self):
        for button in self.buttons:
            button.x_off = 0
            button.y_off = 0
        
    def draw_player_stats(self, player, x, y):
        """scope = "GAME"
        for button in self.buttons:
            if button.category == "SCOPE":
                button.y_off = y - button.y
                button.draw_button()
                if button.highlight:
                    scope = button.do"""        
        textSize(20)
        text("SB:       " + str(player.career_stats.get_stat("SB CAREER", "WINS", self.this_year))      + "-" + str(player.career_stats.get_stat("SB CAREER", "LOSSES", self.this_year)),      x - 470, 640 + y)
        text("Playoffs: " + str(player.career_stats.get_stat("PLAYOFF CAREER", "WINS", self.this_year)) + "-" + str(player.career_stats.get_stat("PLAYOFF CAREER", "LOSSES", self.this_year)), x - 470, 660 + y)
        text("Regular:  " + str(player.career_stats.get_stat("REGULAR CAREER", "WINS", self.this_year)) + "-" + str(player.career_stats.get_stat("REGULAR CAREER", "LOSSES", self.this_year)) + "-" + str(player.career_stats.get_stat("REGULAR CAREER", "TIES", self.this_year)), x - 470, 680 + y)
        text("Total:    " + str(player.career_stats.get_stat("CAREER", "WINS", self.this_year))         + "-" + str(player.career_stats.get_stat("CAREER", "LOSSES", self.this_year))         + "-" + str(player.career_stats.get_stat("CAREER", "TIES", self.this_year)),         x - 470, 700 + y)
        tables = 0
        textSize(15)
        for stat in ["RUN", "RECEIVE", "THROW", "BLOCK", "COVER", "BLITZ", "XP", "FG", "PUNT", "KICK OFF", "RETURN", "2pt"]:
            if player.has_stats(stat, "CAREER"):
                #text(stat + " stats, last game:", x, y + 50 + tables*65)
                #make_stats_table(stat, "GAME", self.this_year, [player], x, y + 55 + tables*65, 0, False, -1)
                #tables += 1
                text(stat + " season stats:", x, y + 50 + tables*(85+20*(self.this_year-player.draft_position[2])))
                make_career_table(stat, "SEASON", self.this_year, player, x, y + 55 + tables*(85+20*(self.this_year-player.draft_position[2])), 0, False)
                tables += 1
                #text(stat + " stats, career:", x, y + 50 + tables*65)
                #make_stats_table(stat, "CAREER", self.this_year, [player], x, y + 55 + tables*65, 0, False, -1)
                #tables += 1
                #text(stat + " stats, career highs:", x, y + 50 + tables*65)
                #make_stats_table(stat, "CAREER HIGH", self.this_year, [player], x, y + 55 + tables*65, 0, False, -1)
                #tables += 1
                #text(stat + " stats, season highs:", x, y + 50 + tables*65)
                #make_stats_table(stat, "SEASON HIGH", self.this_year, [player], x, y + 55 + tables*65, 0, False, -1)
                #tables += 1
        
    def draw_team_stats(self, team, x, y):
        scope = "GAME"
        for button in self.buttons:
            if button.category == "SCOPE":
                button.y_off = y - button.y
                button.draw_button()
                if button.highlight:
                    scope = button.do
        
        num_players = 0
        for stat in ["THROW", "RECEIVE", "RUN", "BLOCK", "COVER", "BLITZ", "XP", "FG", "PUNT", "KICK OFF", "RETURN", "2pt"]:
            players = [team]
            for player in team.Players:
                if player.has_stats(stat, scope, self.this_year):
                    players.insert(0, player)
                    num_players += 1
            make_stats_table_h(stat, scope, self.this_year, players, x, y + 100 + 20 * (num_players - len(players) - 1), self.numbers_table_sort, self.numbers_sort_order, -1, False, True)
            y += 50
        
    def get_top_rated(self, pos, scope, stat_type, conf, min_att, num_to_return, years_in_nfl):
        afc_teams = ["NE", "BUF", "MIA", "NYJ", "IND", "HOU", "JAX", "TEN", "PIT", "BAL", "CLE", "CIN", "KC", "LAC", "DEN", "LV"]
        nfc_teams = ["WAS", "NYG", "DAL", "PHI", "NO", "TB", "CAR", "ATL", "GB", "MIN", "DET", "CHI", "SEA", "SF", "LAR", "ARI"]
        offense = ["QB", "RB", "WR", "TE", "OL"]
        defense = ["DL", "LB", "DB"]
        
        type = stat_type
        if stat_type in {"MVP", "OROY", "DROY", "OPOY", "DPOY"}:
            type = "ALL"
        
        qualifying_players = []
        for player in self.all_players:
            if (player.position == pos or pos == "ANY" or (pos == "OFFENSE" and player.position in offense) or (pos == "DEFENSE" and player.position in defense)) and (player.has_stats_min_att(type, scope, self.this_year, min_att)) and ((player.team in afc_teams and conf == "AFC") or (player.team in nfc_teams and conf == "NFC") or (conf == "ANY")) and (years_in_nfl == "ANY" or player.years_played == years_in_nfl):
                qualifying_players.append(player)
        if stat_type in {"MVP", "OROY", "DROY", "OPOY", "DPOY"}:
            record_matters = (stat_type == "MVP")
            qualifying_players.sort(key = lambda l: by_mvp_points(l, scope, self.this_year, record_matters), reverse = True)
        else:
            qualifying_players.sort(key = lambda l: by_rating(l, scope, stat_type, self.this_year), reverse = True)
        if len(qualifying_players) < num_to_return:
            return qualifying_players
        else:
            return qualifying_players[0:num_to_return]
        
    def draw_buttons(self):
        for button in self.buttons:
            button.draw_button()
            
    def check_button_click(self, mouse_x, mouse_y, category = "ALL"):
        for button in self.buttons:
            if button.category == category or category == "ALL":
                if button.clicked(mouse_x, mouse_y):
                    if button.category in {"POS", "TEAM", "ROUND"}: # can toggle each one on/off
                        button.highlight = not button.highlight
                    else:
                        button.highlight = True
                    if button.category in {"SCOPE", "ATT", "TOP", "LOC", "TYPE", "STAT", "YEAR"} or "ADD ON" in button.category: # exclusive, only one can be on
                        for button2 in self.buttons:
                            if "ADD ON" in button2.category and not "ADD ON" in button.category:
                                if button.do in {"BLOCK", "COVER", "RETURN"}:
                                    if button.do in button2.category:
                                        button2.show()
                                        button2.highlight = False
                                    elif "ALL" in button2.category:
                                        button2.show()
                                        button2.highlight = True
                                    else:
                                        button2.hide()
                                        button2.highlight = False
                                else:
                                    button2.hide()
                                    if button2.do == "":
                                        button2.highlight = True
                                    else:
                                        button2.highlight = False
                            elif button2.category == button.category and not button2.do == button.do:
                                button2.highlight = False
                            elif "ADD ON" in button2.category and "ADD ON" in button.category and not button2.do == button.do:
                                button2.highlight = False
    
    def set_buttons(self):
        self.buttons.append(Button(305,  0, 75, 25, "Game",           "GAME",           "SCOPE"))
        self.buttons.append(Button(380,  0, 75, 25, "Season",         "SEASON",         "SCOPE"))
        self.buttons.append(Button(455,  0, 75, 25, "Playoffs",       "PLAYOFF",        "SCOPE"))
        self.buttons.append(Button(530,  0, 75, 25, "Year",           "YEAR",           "SCOPE"))
        self.buttons.append(Button(605,  0, 150, 25, "Season Career", "REGULAR CAREER", "SCOPE"))
        self.buttons.append(Button(755,  0, 150, 25, "Playoff Career","PLAYOFF CAREER", "SCOPE"))
        self.buttons.append(Button(905,  0, 125, 25, "SB Career",     "SB CAREER",      "SCOPE"))
        self.buttons.append(Button(1030, 0, 125, 25, "PRO BOWL",      "PRO BOWL CAREER", "SCOPE"))
        self.buttons.append(Button(1155, 0, 75, 25, "Career",         "CAREER",         "SCOPE"))
        self.buttons.append(Button(1230, 0, 125, 25, "Season High",   "SEASON HIGH",    "SCOPE"))
        self.buttons.append(Button(1355, 0, 125, 25, "Career High",   "CAREER HIGH",    "SCOPE"))
        
        self.buttons.append(Button(305, 50, 75, 25, "Pass",    "PASS",     "STAT"))
        self.buttons.append(Button(380, 50, 75, 25, "Run",     "RUN",      "STAT"))
        self.buttons.append(Button(455, 50, 75, 25, "Catch",   "CATCH",    "STAT"))
        self.buttons.append(Button(530, 50, 75, 25, "Block",   "BLOCK",    "STAT"))
        self.buttons.append(Button(605, 50, 75, 25, "Cover",   "COVER",    "STAT"))
        self.buttons.append(Button(680, 50, 75, 25, "Blitz",   "BLITZ",    "STAT"))
        self.buttons.append(Button(755, 50, 75, 25, "XP",      "XP",       "STAT"))
        self.buttons.append(Button(830, 50, 75, 25, "FG",      "FG",       "STAT"))
        self.buttons.append(Button(905, 50, 75, 25, "Punt",    "PUNT",     "STAT"))
        self.buttons.append(Button(980, 50, 75, 25, "Kickoff", "KICK OFF",  "STAT"))
        self.buttons.append(Button(1055,50, 75, 25, "Return",  "RETURN",   "STAT"))
        self.buttons.append(Button(1130,50, 75, 25, "2pt",     "2pt",      "STAT"))
        self.buttons.append(Button(1205,50, 75, 25, "Record",  "RECORD",   "STAT"))
        self.buttons.append(Button(1280,50, 75, 25, "Overall", "OVERALL",  "STAT"))
        self.buttons.append(Button(1355,50, 75, 25, "Awards",  "AWARDS",   "STAT"))
        self.buttons.append(Button(1430,50, 75, 25, "Misc",    "MISC",     "STAT"))
        self.buttons.append(Button(1505,50, 75, 25, "Rate 1",  "RATINGS1", "STAT"))
        self.buttons.append(Button(1580,50, 75, 25, "Rate 2",  "RATINGS2", "STAT"))
        self.buttons.append(Button(1655,50, 75, 25, "Fantasy", "FANTASY",  "STAT"))
        
        self.buttons.append(Button(305, 25, 75, 25, "QB", "QB", "POS"))
        self.buttons.append(Button(380, 25, 75, 25, "RB", "RB", "POS"))
        self.buttons.append(Button(455, 25, 75, 25, "WR", "WR", "POS"))
        self.buttons.append(Button(530, 25, 75, 25, "TE", "TE", "POS"))
        self.buttons.append(Button(605, 25, 75, 25, "OL", "OL", "POS"))
        self.buttons.append(Button(680, 25, 75, 25, "DL", "DL", "POS"))
        self.buttons.append(Button(755, 25, 75, 25, "LB", "LB", "POS"))
        self.buttons.append(Button(830, 25, 75, 25, "DB", "DB", "POS"))
        self.buttons.append(Button(905, 25, 75, 25, "K", "K", "POS"))
        self.buttons.append(Button(980, 25, 75, 25, "RT", "RT", "POS"))
        self.buttons.append(Button(1055,25, 75, 25, "ALL", "ALL", "POS"))
        
        self.buttons.append(Button(305, 75, 75, 25, "Min 1", 1, "ATT"))
        self.buttons.append(Button(380, 75, 75, 25, "Min 10", 10, "ATT"))
        self.buttons.append(Button(455, 75, 75, 25, "Min 50", 50, "ATT"))
        self.buttons.append(Button(530, 75, 85, 25, "Min 100", 100, "ATT"))
        self.buttons.append(Button(615, 75, 85, 25, "Min 500", 500, "ATT"))
        self.buttons.append(Button(700, 75, 100,25, "Min 1000", 1000, "ATT"))
        
        self.buttons.append(Button(305, 100, 90, 25, "Show 10", 10, "TOP"))
        self.buttons.append(Button(395, 100, 90, 25, "Show 25", 25, "TOP"))
        self.buttons.append(Button(485, 100, 90, 25, "Show 50", 50, "TOP"))
        self.buttons.append(Button(575, 100, 105, 25, "Show 100", 100, "TOP"))
        
        self.buttons.append(Button(305, 150, 100, 25, "This year", "THIS YEAR", "YEAR"))
        
        y = 175
        x = 1650
        self.buttons.append(Button(x,       y, 100, 25, "TEAM", "TEAM", "TYPE"))
        self.buttons.append(Button(x + 100, y, 100, 25, "PLAYER", "PLAYER", "TYPE"))
        y += 25
        self.buttons.append(Button(x,       y, 125, 25, "Drafted by", "DRAFTED", "LOC"))
        self.buttons.append(Button(x + 125, y, 50, 25, "On", "ON", "LOC"))
        self.buttons.append(Button(x + 175, y, 50, 25, "ALL", "ALL", "TEAM"))
        self.buttons.append(Button(x + 225, y, 75, 25, "NONE", "UNDRAFTED", "TEAM"))
        y += 25
        self.buttons.append(Button(x      , y, 100, 25, "Bears", "CHI", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Bengals", "CIN", "TEAM"))
        self.buttons.append(Button(x + 200, y, 100, 25, "Active", "ACTIVE", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Bills", "BUF", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Broncos", "DEN", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Browns", "CLE", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Buccs", "TB", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Colts", "IND", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Cards", "ARI", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Chargers", "LAC", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Chiefs", "KC", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Cowboys", "DAL", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Dolphins", "MIA", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Eagles", "PHI", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Falcons", "ATL", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Giants", "NYG", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Jaguars", "JAX", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Jets", "NYJ", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Lions", "DET", "TEAM"))
        y += 25
        self.buttons.append(Button(x, y, 100, 25, "Packers", "GB", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Panthers", "CAR", "TEAM"))
        y += 25
        self.buttons.append(Button(x,        y, 100, 25, "Patriots", "NE", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "WAS", "WAS", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Raiders", "LV", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Rams", "LAR", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Ravens", "BAL", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Saints", "NO", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Seahawks", "SEA", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Steelers", "PIT", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Texans", "HOU", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "Titans", "TEN", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "Vikings", "MIN", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "49ers", "SF", "TEAM"))
        y += 25
        self.buttons.append(Button(x,       y, 100, 25, "FA", "FREE AGENT", "TEAM"))
        self.buttons.append(Button(x + 100, y, 100, 25, "RETIRED", "RETIRED", "TEAM"))
        self.buttons.append(Button(x + 200, y, 100, 25, "HOF", "HOF", "TEAM"))
        
        y += 50
        self.buttons.append(Button(x, y, 100, 25, "ROUND 1", 1, "ROUND"))
        y += 25
        self.buttons.append(Button(x, y, 100, 25, "ROUND 2", 2, "ROUND"))
        y += 25
        self.buttons.append(Button(x, y, 100, 25, "ROUND 3", 3, "ROUND"))
        y += 25
        self.buttons.append(Button(x, y, 100, 25, "ROUND 4", 4, "ROUND"))
        y += 25
        self.buttons.append(Button(x, y, 100, 25, "ROUND 5", 5, "ROUND"))
        y += 25
        self.buttons.append(Button(x, y, 100, 25, "ROUND 6", 6, "ROUND"))
        y += 25
        self.buttons.append(Button(x, y, 100, 25, "ROUND 7", 7, "ROUND"))
        y += 25
        self.buttons.append(Button(x, y, 100, 25, "UNDRAFTED", 0, "ROUND"))
        y += 25
        self.buttons.append(Button(x, y, 100, 25, "ALL", 8, "ROUND"))
        
        self.buttons.append(Button(305, 125, 75, 25, "None", "",     "ADD ON ALL"))
        self.buttons.append(Button(380, 125, 75, 25, "Run",  "RUN",  "ADD ON BLOCK"))
        self.buttons.append(Button(455, 125, 75, 25, "Pass", "PASS", "ADD ON BLOCK"))
        self.buttons.append(Button(380, 125, 75, 25, "Run",  "RUN",  "ADD ON COVER"))
        self.buttons.append(Button(455, 125, 75, 25, "Man",  "MAN",  "ADD ON COVER"))
        self.buttons.append(Button(530, 125, 75, 25, "Zone", "ZONE", "ADD ON COVER"))
        self.buttons.append(Button(380, 125, 75, 25, "Kick", "KICK", "ADD ON RETURN"))
        self.buttons.append(Button(455, 125, 75, 25, "Punt", "PUNT", "ADD ON RETURN"))
        
        for i in [0, 11, 40, 41, 49, 51, 52, 55, 56, 102, 103]:
            self.buttons[i].highlight = True
        for i in range(103, len(self.buttons)):
            self.buttons[i].hide()
        
    def get_retired(self):
        ret = 0
        for player in self.all_players:
            if player.retired:
                ret += 1
        self.new_retired = ret - self.retired
        self.retired = ret
        
    def clicked(self, x, y, category = "ALL", x2 = 305):
        global scroll
        if y < 175 or x > 1600:
            self.check_button_click(x,y, category)
        else:
            sort_start = self.numbers_table_sort 
            if x > x2:
                if x < x2 + 125:
                    self.numbers_table_sort = 1
                else:
                    self.numbers_table_sort = int(x - (x2+125)) / 75 + 1
            if sort_start == self.numbers_table_sort:
                self.numbers_sort_order = not self.numbers_sort_order
                
    def add_sb(self, team1, team2, score1, score2):
        self.sb_winners.insert(0, [self.this_year, team1, team2, score1, score2])
        
    def add_players(self, players):
        self.all_players.extend(players)
        self.get_retired()
        
    def update_all_players(self, season1):
        self.all_teams = []
        for player in season1.free_agents.players:
            if not (player in self.all_players):
                self.all_players.append(player)
        self.all_teams.extend(season1.teams)
        for team in season1.teams:
            for player in team.Players:
                if not (player in self.all_players):
                    self.all_players.append(player)
        self.get_retired()     
        self.cut_extras()
        
    def cut_extras(self):
        min_att = 5
        for player in self.all_players:
            if player.retired:
                is_important = False
                for stat in ["THROW", "RECEIVE", "RUN", "BLOCK", "COVER", "BLITZ", "XP", "FG", "PUNT", "KICK OFF", "RETURN", "2pt"]:
                    if player.has_stats_min_att("CAREER", type, 0, min_att, False):
                        is_important = True
                        break
                if not is_important:
                    self.players.remove(player)
        
    def draw_leaders(self, x, y, buttons = "SELF", scope = "", positions = [], stats = [], num_leaders = 10, min_attempts = 1, teams = [], rounds = [], is_drafted_team = False, add_on_stat = "", this_year = "SELF", show_players = True):
        if buttons == "SELF":
            buttons = self.buttons
            positions = []
            teams = []
            rounds = []
        else:
            buttons = None
            
        if this_year == "SELF":
            this_year = self.this_year
            
        if not buttons == None:
            self.draw_buttons()
        textSize(20)

        num_players = 0
        num_teams = 0
        buffer = 150
        
        if buttons == None:
            self.numbers_scope = scope
            self.add_on_stat = add_on_stat
            buffer = 0
        else:
            for button in buttons:
                if button.highlight:
                    if button.category == "SCOPE":
                        self.numbers_scope = button.do
                    if button.category == "POS":
                        positions.append(button.do)
                    elif button.category == "STAT":
                        stats =  [button.do]
                    elif button.category == "TOP":
                        num_leaders = button.do
                    elif button.category == "ATT":
                        min_attempts = button.do
                    elif button.category == "TEAM":
                        teams.append(button.do)
                    elif button.category == "ROUND":
                        rounds.append(button.do)
                    elif button.category == "LOC":
                        is_drafted_team = (button.do == "DRAFTED")
                    elif "ADD ON" in button.category:
                        self.add_on_stat = button.do
                    elif button.category == "YEAR":
                        if button.do == "THIS YEAR":
                            this_year = self.this_year
                        else:
                            this_year = button.do
                    elif button.category == "TYPE":
                        show_players = (button.do == "PLAYER")
        
        for stat in ["PASS", "CATCH", "RUN", "BLOCK", "COVER", "BLITZ", "XP", "FG", "PUNT", "KICK OFF", "RETURN", "2pt", "OVERALL", "RECORD", "AWARDS", "MISC", "RATINGS1", "RATINGS2", "FANTASY"]:
            if stat in stats and show_players:
                if not self.add_on_stat == "":
                    stat = self.add_on_stat + " " + stat
                players = []
                for player in self.all_players:
                    if (player.has_stats_min_att(stat, self.numbers_scope, this_year, min_attempts) or stat in {"MISC", "OVERALL"}) and (player.position in positions or "ALL" in positions) and (player.draft_position[0] in rounds or 8 in rounds) and ((not is_drafted_team and player.team in teams or "ALL" in teams or ("ACTIVE" in teams and not player.team == "RETIRED")) or (is_drafted_team and (player.drafted_by in teams or "ALL" in teams))):
                        players.append(player)
                if (len(players) > 250 and stat in ["RATINGS1", "RATINGS2"]):
                    return
                make_stats_table_h(stat, self.numbers_scope, this_year, players, x + 5, y + buffer + 20 * num_players, self.numbers_table_sort, self.numbers_sort_order, num_leaders, True, True)
                num_players += min(num_leaders, len(players))
                buffer += 50
                
        for stat in ["PASS", "CATCH", "RUN", "BLOCK", "COVER", "BLITZ", "XP", "FG", "PUNT", "KICK OFF", "RETURN", "2pt", "OVERALL", "RECORD", "AWARDS", "MISC", "RATINGS1", "RATINGS2", "FANTASY"]:
            if stat in stats and not show_players:
                if not self.add_on_stat == "":
                    stat = self.add_on_stat + " " + stat
                make_stats_table_h(stat, self.numbers_scope, this_year, self.all_teams, x + 5, y + buffer + 20 * num_teams, self.numbers_table_sort, self.numbers_sort_order, num_leaders, True, True)
                num_teams += 32
                buffer += 50
            
    def total_players(self):
        return len(self.all_players)
    
    def count_players(self, pos):
        count = 0
        for player in self.all_players:
            if player.position == pos and not player.retired:
                count += 1
        return count
    
    def total_xp(self):
        return self.qb_xp + self.rb_xp + self.wr_xp + self.te_xp + self.ol_xp + self.dl_xp + self.lb_xp + self.db_xp + self.k_xp + self.rt_xp
    
    def add_fatigue(self, position, amount):
        self.fatigues[position] = amount
    
    def add_xp(self, position, amount):
        if position == "QB":
            self.qb_xp += amount
        elif position == "RB":
            self.rb_xp += amount
        elif position == "WR":
            self.wr_xp += amount
        elif position == "TE":
            self.te_xp += amount
        elif position == "OL":
            self.ol_xp += amount
        elif position == "DL":
            self.dl_xp += amount
        elif position == "LB":
            self.lb_xp += amount
        elif position == "DB":
            self.db_xp += amount
        elif position == "K":
            self.k_xp += amount
        elif position == "RT":
            self.rt_xp += amount
            
    def draw_sbs(self, x, y):
        fill(150)
        stroke(0)
        rect(x, y, 250, 30 + 20*len(self.sb_winners), 7)
        fill(0)
        text("Superbowls", x + 5, y + 20)
        i = 0
        for sb in self.sb_winners:
            text(str(sb[0]) + ": " + str(sb[3]) + " " + sb[1] + " " + sb[2] + " " + str(sb[4]), x + 5, y + 40 + 20 * i)
            i += 1
    
    def draw_stats(self, x, y):
        textSize(15)
        fill(150)
        stroke(0)
        rect(x, y, 250, 310, 7)
        fill(0)
        text("Players: " + str(self.total_players()), x + 5, y + 20)
        y_off = 40
        for pos in ["QB", "RB","WR", "TE", "OL", "DL", "LB", "DB", "K", "RT"]:
            text(pos + "s: " + str(self.count_players(pos)), x + 20, y + y_off)
            y_off += 20
        text("New: 396", x + 5, y + 240)
        text("Recently Retired: " + str(self.new_retired), x + 5, y + 260)
        text("Retired: " + str(self.retired), x + 5, y + 280)
        text("Active: " + str(self.total_players() - self.retired), x + 5, y + 300)
        
        for pos in self.fatigues:
            y += 20
            text(pos + "s: " + str(int(self.fatigues[pos])), x+135, y)        
        """
        text("XP: " + str(int(self.total_xp())), x + 115, y + 20)
        text("QBs: " + str(int(self.qb_xp) / 6), x + 135, y + 40)
        text("RBs: " + str(int(self.rb_xp) / 12), x + 135, y + 60)
        text("WRs: " + str(int(self.wr_xp) / 15), x + 135, y + 80)
        text("TEs: " + str(int(self.te_xp / 10.5)), x + 135, y + 100)
        text("OLs: " + str(int(self.ol_xp) / 10), x + 135, y + 120)
        text("DLs: " + str(int(self.dl_xp / 27.5)), x + 135, y + 140)
        text("LBs: " + str(int(self.lb_xp) / 36), x + 135, y + 160)
        text("DBs: " + str(int(self.db_xp) / 44), x + 135, y + 180)
        text("Ks: " + str(int(self.k_xp) / 6), x + 135, y + 200)
        text("RTs: " + str(int(self.rt_xp) / 3), x + 135, y + 220)
        """

################################################################################LEAGUE STATS CLASS###########################################################################################
################################################################################LEAGUE STATS CLASS###########################################################################################
################################################################################LEAGUE STATS CLASS###########################################################################################
################################################################################LEAGUE STATS CLASS###########################################################################################

################################################################################BUTTON CLASS###########################################################################################
################################################################################BUTTON CLASS###########################################################################################
################################################################################BUTTON CLASS###########################################################################################
################################################################################BUTTON CLASS###########################################################################################

class Button(object):
    
    def __init__(self, x, y, w, h, t, do, cat):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.t = t
        self.do = do
        self.highlight = False
        self.category = cat
        self.x_off = 0
        self.y_off = 0
        self.showing = True
        self.clickable = True
    
    def hide(self):
        self.showing = False
        
    def show(self):
        self.showing = True
        
    def draw_button(self):
        if not self.showing:
            return
        strokeWeight(1)
        stroke(0)
        if not self.highlight:
            fill(150)
        else:
            fill(200,200,0)
        rect(self.x + self.x_off,self.y + self.y_off,self.w,self.h,7)
        textSize(20)
        fill(0)
        text(str(self.t),self.x+5 + self.x_off,self.y + self.y_off,self.w,self.h)
        
    def clicked(self, mouse_x, mouse_y):
        if not self.showing:
            return False
        if not self.clickable:
            return False
        if mouse_x > self.x + self.x_off and mouse_x < self.x + self.x_off + self.w and mouse_y > self.y + self.y_off and mouse_y < self.y + self.y_off + self.h:
            return True
        return False
        
        
################################################################################BUTTON CLASS###########################################################################################
################################################################################BUTTON CLASS###########################################################################################
################################################################################BUTTON CLASS###########################################################################################
################################################################################BUTTON CLASS###########################################################################################



################################################################################CONSTANTS CLASS###########################################################################################
################################################################################CONSTANTS CLASS###########################################################################################
################################################################################CONSTANTS CLASS###########################################################################################
################################################################################CONSTANTS CLASS###########################################################################################

class Constants(object):
    
    def __init__(self):
        self.injury_chance_avg =    0.018
        self.injury_jump =          0.001
        self.block_chance_avg =     93.3
        self.block_jump =           0.4
        self.sack_avg =             6.7
        self.rating_sack_avg =      1.5
        self.sack_jump =            0.4
        self.int_avg =              2.5
        self.int_jump =             0.1
        self.complete_avg =         59.5
        self.complete_jump =        0.4
        self.scramble_avg =         4.0
        self.scramble_jump =        0.5
        self.air_yds_avg =          7.1
        self.air_yds_jump =         0.15
        self.fumble_avg =           1.0
        self.fumble_jump =          0.1
        self.drop_avg =             5.0
        self.drop_jump =            0.3
        self.YAC_avg =              4.0
        self.YAC_jump =             0.15
        self.run_avg =              4.25
        self.run_jump =             0.13
        self.fg_range_avg =         54.0
        self.rating_fg_range_avg =  30.0
        self.fg_range_jump =        0.25
        self.fg_chance_avg =        90.0
        self.fg_chance_jump =       0.3
        self.punt_avg =             45.0
        self.rating_punt_avg =      35.0
        self.punt_jump =            0.4
        self.return_avg =           20.0
        self.rating_return_avg =    12.0
        self.return_jump =          0.3
        self.pin_avg =              40.0
        self.rating_pin_avg =       20.0
        self.pin_jump =             0.5
        self.touchback_avg =        88.0
        self.touchback_jump =       0.3
        self.onside_avg =           15.0
        self.onside_jump =          0.1
        self.td_avg =               3.0
        self.td_jump =              0.15
        self.rating_tackle_avg =    7.5
        self.rating_tackle_jump =   0.5
        self.goal_line =            0
        self.i =                    1
        self.singleback =           2
        self.spread =               3
        self.three_four =           1
        self.four_three =           2
        self.nickel =               3
        self.dime =                 4
        self.quarter =              5
        self.wr1 =                  0
        self.wr2 =                  1
        self.wr3 =                  2
        self.te1 =                  3
        self.te2 =                  4
        self.rb1 =                  5
        self.rb2 =                  6
        self.game =                 0
        self.season =               1
        self.career =               2
        self.career_high =          3
        self.wins =                 0 
        self.losses =               1
        self.ties =                 2
        self.seasons =              3
        self.yards =                0
        self.games =                1
        self.superbowls =           4
        
        
    def clock_runoff(self, play_type, distance):
        if play_type == "PASS":
            return 8.0*random(0.5, 1.5)*log(0.1*abs(distance) + math.e)
        elif play_type == "RUN":
            return 8.0*random(0.5, 1.5)*log(0.15*abs(distance) + math.e)
        elif play_type == "SCRAMBLE":
            return 8.0*random(1.0, 2.0)*log(abs(distance) + math.e)
        elif play_type in {"EXTRA POINT"}:
            return 0.0
        elif play_type == "PUNT":
            return random(5, 15)
        elif play_type == "KICK OFF":
            return random(4, 12)
        else:
            return 4.0
        
    def stat_xp(self, stat):
        if stat in {"PASS ATTEMPTS", "ROUTES RUN", "PASS BLOCK ATTEMPTS", "RUN BLOCK ATTEMPTS", "BLITZES", "RUN COVERS", "SNAPS PLAYED", "MAN COVERS", "ZONE COVERS", "RUN COVERS", "ONSIDE KICK ATTEMPTS", "KICK OFF ATTEMPTS", "KICK OFF TB", "2pt PASS ATTEMPTS", "2pt CARRIES", "2pt TARGETS"}:
            return 1.0
        elif stat in {"RECEIVING YARDS", "RUSH YARDS", "PUNT RETURN YARDS", "KICK RETURN YARDS"}:
            return 1.0
        elif stat in {"SACK YARDS", "BLITZ RUN STUFF YARDS", "RUN COVER RUN STUFF YARDS", "BLITZ FF RETURN YARDS", "RUN COVER FF RETURN YARDS", "MAN COVER FF RETURN YARDS", "ZONE COVER FF RETURN YARDS", "MAN PICK RETURN YARDS", "ZONE PICK RETURN YARDS"}:
            return 1.0
        elif stat in {"FG DISTANCE", "PUNT YARDS"}:
            return 0.4
        elif stat in {"PASS YARDS"}:
            return 0.4
        elif stat in {"PASS COMPLETIONS", "TARGETS", "CARRIES", "PASS BLOCKS MADE", "RUN BLOCKS MADE", "MAN TARGETED", "ZONE TARGETED", "XP ATTEMPTS", "PUNTS", "KICK OFFS", "PUNT RETURNS", "KICK RETURNS", "GAME ON ROSTER", "YAC"}:
            return 2.0
        elif stat in {"CATCHES", "BLITZ TACKLES", "RUN COVER TACKLES", "MAN COVER TACKLES", "ZONE COVER TACKLES", "FG ATTEMPTS", "PUNT TB", "KICK OFF TB", "PUNT RETURN TB", "KICK RETURN TB", "GAMES PLAYED"}:
            return 3.0
        elif stat in {"SACKS", "BLITZ RUN STUFFS", "RUN COVER RUN STUFFS", "XP MADE", "PUNT RETURNS", "KICK RETURNS", "GAMES STARTED"}:
            return 5.0
        elif stat in {"BLITZ FF", "RUN COVER FF", "MAN COVER FF", "ZONE COVER FF", "MAN PICKS", "ZONE PICKS"}:
            return 10.0
        elif stat in {"PASS TDS", "FG MADE", "PUNT PINS", "ONSIDE KICK SUCCESS"}:
            return 10.0
        elif stat in {"2pt PASS SUCCESS", "2pt RUSH SUCCESS", "2pt CATCH SUCCESS"}:
            return 20.0
        elif stat in {"RECEIVING TDS", "RUSH TDS", "BLITZ FF TDS", "RUN COVER FF TDS", "MAN COVER FF TDS", "ZONE COVER FF TDS", "MAN PICK SIXES", "ZONE PICK SIXES", "PUNT RETURN TDS", "KICK RETURN TDS"}:
            return 60.0
        elif stat in {"BLITZ SAFETIES", "RUN COVER SAFETIES", "MAN COVER SAFETIES", "ZONE COVER SAFETIES"}:
            return 60.0
        elif stat in {"TIES"}:
            return 40.0
        elif stat in {"PLAYED TIES"}:
            return 45.0
        elif stat in {"STARTER TIES"}:
            return 50.0
        elif stat in {"WINS"}:
            return 65.0
        elif stat in {"PLAYED WINS"}:
            return 70.0
        elif stat in {"STARTER WINS"}:
            return 75.0
        elif stat in {"LOSSES"}:
            return 90.0
        elif stat in {"PLAYED LOSSES"}:
            return 95.0
        elif stat in {"STARTER LOSSES"}:
            return 100.0
        elif stat in {"SEASON"}:
            return 150.0
        elif stat in {"MVPS", "OPOYS", "DPOYS", "OROYS", "DROYS", "PRO BOWLS"}:
            return 25.0
        elif stat in {"PASS INTS", "POCKET FUMBLES", "TIMES SACKED", "SACKED YARDS", "RECEIVER FUMBLES", "DROPS", "RUSH FUMBLES", "RUSH YARDS ALLOWED", "RUSH TDS ALLOWED", "PUNT RETURN FUMBLES", "KICK RETURN FUMBLES"}:
            return 0.0
        elif stat in {"MAN COMPLETIONS ALLOWED", "ZONE COMPLETIONS ALLOWED", "MAN PASS YARDS ALLOWED", "ZONE PASS YARDS ALLOWED", "MAN PASS TDS ALLOWED", "ZONE PASS TDS ALLOWED", "MAN YAC ALLOWED", "ZONE YAC ALLOWED"}:
            return 0.0
        elif stat in {"PUNT TACKLES", "KICK TACKLES", "PUNT FF", "KICK FF", "PUNT FF RETURN YARDS", "KICK FF RETURN YARDS", "PUNT FF TDS", "KICK FF TDS", "KICK SAFETIES", "PUNT SAFETIES"}:
            return 0.0
        elif stat in {"WIN", "LOSS", "TIE", "SALARY"}:
            return 0.0
        else:
            print("error: unknown stat in stat_xp - " + str(stat))
            return 0.0
        
    def fatigue_calc(self, xp, pos, stamina):
        multip = 0
        if pos == "QB":
            multip = 0.700
        elif pos == "WR":
            multip = 2.000
        elif pos == "RB":
            multip = 1.300
        elif pos == "TE":
            multip = 1.300
        elif pos == "OL":
            multip = 4.000
        elif pos == "DL":
            multip = 2.000
        elif pos == "LB":
            multip = 0.700
        elif pos == "DB":
            multip = 0.900
        elif pos == "K":
            multip = 0.750
        elif pos == "RT":
            multip = 1.000
        else:
            print("error: unknown position - " + str(pos))
            return 0.0
        return max(0, xp*multip*0.01*(1-(0.1*stamina**1.2)/100.0))
        
        
    def position_xp_multiplier(self, pos):
        multip = 0
        if pos == "QB":
            multip = 0.955
        elif pos == "WR":
            multip = 0.555
        elif pos == "RB":
            multip = 0.855
        elif pos == "TE":
            multip = 0.800
        elif pos == "OL":
            multip = 0.290
        elif pos == "DL":
            multip = 0.460
        elif pos == "LB":
            multip = 1.600
        elif pos == "DB":
            multip = 1.105
        elif pos == "K":
            multip = 1.250
        elif pos == "RT":
            multip = 1.000
        else:
            print("error: unknown position - " + str(pos))
            return 0.0
        return multip*0.95
        
    def game_xp_multiplier(self, game):
        if game == "PRE SEASON":
            return 0.0
        elif game == "REGULAR":
            return 1.0
        elif game == "PLAYOFF":
            return 1.5
        elif game == "PRO BOWL":
            return 0.05
        elif game == "SB":
            return 2.0
        elif game == "AWARDS":
            return 1.0
        else:
            print("error: unknown game in xp_multiplier - " + str(game))
            return 0.0
        
    def position_value(self, pos):
        if pos == "QB":
            return 1.0
        elif pos == "WR":
            return 0.85
        elif pos == "RB":
            return 0.95
        elif pos == "TE":
            return 0.80
        elif pos == "OL":
            return 0.85
        elif pos == "DL":
            return 0.90
        elif pos == "LB":
            return 0.85
        elif pos == "DB":
            return 0.90
        elif pos == "K":
            return 0.15
        elif pos == "RT":
            return 0.10
        else:
            print("error: unknown position in position_value - " + str(pos))
            return 0.0
                
    def contract_multiplier(self, pos):
        if pos == "QB":
            return 1.75
        elif pos == "WR":
            return 1.05
        elif pos == "RB":
            return 0.93
        elif pos == "TE":
            return 0.87
        elif pos == "OL":
            return 0.89
        elif pos == "DL":
            return 1.05
        elif pos == "LB":
            return 1.1
        elif pos == "DB":
            return 1.05
        elif pos == "K":
            return 0.3
        elif pos == "RT":
            return 0.25
        else:
            print("error: unknown position in contract_multiplier - " + str(pos))
            return 0.0

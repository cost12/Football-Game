"""
        self.run_stats =                  [[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4],[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4],[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4],[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4]]
        self.receive_stats =              [[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4, c.o_complete - 5, c.o_drops - 6, c.o_yac - 7, c.o_targets - 8],[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4, c.o_complete - 5, c.o_drops - 6, c.o_yac - 7, c.o_targets - 8],[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4, c.o_complete - 5, c.o_drops - 6, c.o_yac - 7, c.o_targets - 8],[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4, c.o_complete - 5, c.o_drops - 6, c.o_yac - 7, c.o_targets - 8]]
        self.throw_stats =                [[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4, c.o_complete - 5, c.o_ints - 6, c.o_sacked - 7, c.o_sack_yards - 8],[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4, c.o_complete - 5, c.o_ints - 6, c.o_sacked - 7, c.o_sack_yards - 8],[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4, c.o_complete - 5, c.o_ints - 6, c.o_sacked - 7, c.o_sack_yards - 8],[c.o_attempts, c.o_yards - 1, c.o_td - 2, c.o_long - 3, c.o_fumbles - 4, c.o_complete - 5, c.o_ints - 6, c.o_sacked - 7, c.o_sack_yards - 8]]
        self.block_stats =                [[c.o_attempts, c.o_blocks - 1], [c.o_attempts, c.o_blocks - 1], [c.o_attempts, c.o_blocks - 1], [c.o_attempts, c.o_blocks - 1]]
        self.cover_stats =                [[c.d_tackle, c.d_safeties - 1, c.d_ff - 2, c.d_ff_ret - 3, c.d_ff_td - 4, c.d_attempts - 5, c.d_targets - 6, c.d_complete - 7, c.d_pass_yards - 8, c.d_pass_tds - 9, c.d_ints - 10, c.d_int_ret - 11, c.d_int_td - 12],[c.d_tackle, c.d_safeties - 1, c.d_ff - 2, c.d_ff_ret - 3, c.d_ff_td - 4, c.d_attempts - 5, c.d_targets - 6, c.d_complete - 7, c.d_pass_yards - 8, c.d_pass_tds - 9, c.d_ints - 10, c.d_int_ret - 11, c.d_int_td - 12],[c.d_tackle, c.d_safeties - 1, c.d_ff - 2, c.d_ff_ret - 3, c.d_ff_td - 4, c.d_attempts - 5, c.d_targets - 6, c.d_complete - 7, c.d_pass_yards - 8, c.d_pass_tds - 9, c.d_ints - 10, c.d_int_ret - 11, c.d_int_td - 12],[c.d_tackle, c.d_safeties - 1, c.d_ff - 2, c.d_ff_ret - 3, c.d_ff_td - 4, c.d_attempts - 5, c.d_targets - 6, c.d_complete - 7, c.d_pass_yards - 8, c.d_pass_tds - 9, c.d_ints - 10, c.d_int_ret - 11, c.d_int_td - 12]]
        self.blitzer_stats =              [[c.d_tackle, c.d_safeties - 1, c.d_ff - 2, c.d_ff_ret - 3, c.d_ff_td - 4, c.d_attempts - 5, c.d_sacks - 6, c.d_sack_yds - 7, c.d_run_stops - 8, c.run_stop_yds - 9],[c.d_tackle, c.d_safeties - 1, c.d_ff - 2, c.d_ff_ret - 3, c.d_ff_td - 4, c.d_attempts - 5, c.d_sacks - 6, c.d_sack_yds - 7, c.d_run_stops - 8, c.run_stop_yds - 9],[c.d_tackle, c.d_safeties - 1, c.d_ff - 2, c.d_ff_ret - 3, c.d_ff_td - 4, c.d_attempts - 5, c.d_sacks - 6, c.d_sack_yds - 7, c.d_run_stops - 8, c.run_stop_yds - 9],[c.d_tackle, c.d_safeties - 1, c.d_ff - 2, c.d_ff_ret - 3, c.d_ff_td - 4, c.d_attempts - 5, c.d_sacks - 6, c.d_sack_yds - 7, c.d_run_stops - 8, c.run_stop_yds - 9]]
        self.xp_stats =                   [[c.fg_made, c.fg_attempted - 1],[c.fg_made, c.fg_attempted - 1],[c.fg_made, c.fg_attempted - 1],[c.fg_made, c.fg_attempted - 1]]
        self.fg_stats =                   [[c.fg_made, c.fg_attempted - 1, c.fg_distance - 2, c.fg_long - 3],[c.fg_made, c.fg_attempted - 1, c.fg_distance - 2, c.fg_long - 3],[c.fg_made, c.fg_attempted - 1, c.fg_distance - 2, c.fg_long - 3],[c.fg_made, c.fg_attempted - 1, c.fg_distance - 2, c.fg_long - 3]]
        self.punt_stats =                 [[c.punts, c.punt_tb - 1, c.punt_yds - 2, c.punt_pin - 3],[c.punts, c.punt_tb - 1, c.punt_yds - 2, c.punt_pin - 3],[c.punts, c.punt_tb - 1, c.punt_yds - 2, c.punt_pin - 3],[c.punts, c.punt_tb - 1, c.punt_yds - 2, c.punt_pin - 3]]
        self.return_stats =







UPGRADABLE
            self.injury_chance =
            self.block_chance =            
            self.sack_allowed_chance =    
            self.int_chance =             
            self.complete_chance =           
            self.air_yds_throw =           
            self.fumble_chance =            
            self.drop_chance =          
            self.target_dist =            
            self.YAC =      
            self.run_dist =   
            self.air_yds_allowed =         
            self.int_catch_chance =       
            self.complete_chance_allowed =   
            self.YAC_allowed =          
            self.sack_chance =     
            self.blocked_chance =      
            self.run_dist_allowed =       
            self.ff_chance =
            self.fg_range = 
            self.fg_made_chance =  
            self.punt_dist =  
            self.kick_return_allowed =      
            self.touchback_forced_chance =   
            self.pin_chance =           
            self.kick_return_dist =        
            self.touchback_chance =  
        
        
        
        
        
        
        
        
        
        
        self.block_chance = 
        self.sack_allowed_chance = 
        self.int_chance = 
        self.dist_effect_int = 
        self.complete_chance =
        self.dist_effect_complete = 
        self.scramble_chance = 
        self.air_yds_throw = 
        self.stdev_air_yds_throw = 
        self.fumble_chance =
        self.drop_chance = 
        self.dist_effect_drop = 
        self.target_dist = 
        self.stdev_target_dist = 
        self.YAC =
        self.stdev_YAC = 
        self.run_dist = 
        self.stdev_run_dist = 
        self.catch_boost = 
        self.air_yds_allowed = 
        self.stdev_air_yds_allowed = 
        self.int_catch_chance = 
        self.def_return_dist = 
        self.stdev_def_return_dist = 
        self.complete_chance_allowed = 
        self.YAC_allowed = 
        self.stdev_YAC_allowed = 
        self.sack_chance =
        self.blocked_chance = 
        self.run_dist_allowed = 
        self.stdev_run_dist_allowed =
        self.ff_chance = 
        self.fg_range = 
        self.fg_made_chance = 
        self.punt_dist = 
        self.stdev_punt_dist =
        self.kick_return_allowed = 
        self.stdev_kick_return_allowed = 
        self.touchback_forced_chance = 
        self.pin_chance = 
        self.kick_return_dist =
        self.stdev_kick_return_dist = 
        self.touchback_chance =


class Player(object):

        def __init__(self, pos, ovr):
        self.first_name = rand_first_name()
        self.last_name = rand_last_name()
        self.position = pos
        self.age = int(random(19,22))
        self.age_type = rand_ability_type()
        self.xp = 0
        self.upgrade_type = rand_ability_type()
        self.team = "rookie"
        self.projected_ovr = ovr
        self.contract_amount = 0
        self.contract_length = 0
        self.loyalty = min_max_skew(10,40)
        self.stamina = random_skew(ovr, 2)
        self.injured = false
        self.injury_length = 0
        self.injury_chance = min_max_skew(0.025, 0.07)
        self.block_chance = random_skew(0.275*ovr + 72.675, 0.5) 
        self.sack_allowed_chance = 100 - random_skew(0.275*ovr + 72.675, 0.5)
        self.int_chance = 10 - random_skew(0.10416667*ovr - 5.3125, 0.2)
        self.dist_effect_int = rand_ability_type()
        self.complete_chance = random_skew(1.479167*ovr - 47.4375, 0.2)
        self.dist_effect_complete = rand_ability_type()
        self.scramble_chance = random(0,10)
        self.air_yds_throw = random_skew(0.96*ovr, 0.5)
        self.stdev_air_yds_throw = random(3,7)
        self.fumble_chance = random(140,160)/ovr
        self.drop_chance = random(350,400)/ovr
        self.dist_effect_drop = rand_ability_type()
        self.target_dist = random_skew(0.96*ovr, 0.5)
        self.stdev_target_dist = random(3,7)
        self.YAC = random_skew(0.56*ovr, 1)
        self.stdev_YAC = random(3,7)
        self.run_dist = random_skew(0.6*ovr, 1)
        self.stdev_run_dist = random(2,4)
        self.catch_boost = rand_ability_type()
        self.air_yds_allowed = 7.2 - reverse_skew(-0.96*(ovr - 75), 1)
        self.stdev_air_yds_allowed = random(3,7)
        self.int_catch_chance = random_skew(0.10416667ovr - 5.3125, 0.2)
        self.def_return_dist = random_skew(0.6*ovr, 1)
        self.stdev_def_return_dist = random(3,7)
        self.complete_chance_allowed = 63.5 - reverse_skew(-1.479167*(ovr - 75) - 47.4375, 0.2)
        self.YAC_allowed = 4.2 - reverse_skew(0.56*(ovr-75), 1)
        self.stdev_YAC_allowed = random(3,7)
        self.sack_chance = random_skew(0.275*ovr - 13.925, 0.5)
        self.blocked_chance = 100 - reverse_skew(-0.275*ovr + 13.925, 0.5)
        self.run_dist_allowed = 4.5 - reverse_skew(-0.6*(ovr - 75), 1)
        self.stdev_run_dist_allowed = random(3,7)
        self.ff_chance = random(140, 160)/ovr
        self.fg_range = random_skew(0.56*ovr + 8, 1)
        self.fg_made_chance = random_skew(0.58*ovr + 43.5, 1)
        self.punt_dist = random_skew(0.6*ovr, 1)
        self.stdev_punt_dist = random(3,7)
        self.kick_return_allowed = 20 - reverse_skew(-0.5*(ovr - 75), 1)
        self.stdev_kick_return_allowed = random(3,7)
        self.touchback_forced_chance = random_skew(0.5*ovr + 47.5, 1)
        self.pin_chance = random_skew(0.5*ovr, 1)
        self.kick_return_dist = 20 + random_skew(0.5*(ovr-75), 1)
        self.stdev_kick_return_dist = random(3,7)
        self.touchback_chance = 85 - reverse_skew(-0.5*(ovr - 75), 1)
        
        self.run_stats = []
        self.receive_stats = []
        self.throw_stats = []
        self.cover_stats = []
        self.sack_stats = []
        self.tackle_stats = []
        self.ff_stats = []
        self.xp_stats = []
        self.fg_stats = []
        self.punt_stats = []
        self.return_stats = [] 
        self.points_stats = []
        self.record_stats = []
        
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
            self.ajdust_ovr_for_rt()
        self.fix_chances()
            
    def draw_player(self):
        pass
    
    def upgrade_player(self, trait):
        pass
        
    def get_overall(self):
        pass
        
    def sign_player(self, new_team, contract):
        pass
    
    def cut_player(self):
        pass
        
    def trade_player(self, new_team):
        pass
        
    def get_rating(self):
        pass
        
    def change_position(self):
        pass
        

        
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
        self.run_allowed *= 2
        self.ff_chance *= 0.2
        self.fg_range *= 0.2
        self.fg_made_chance *= 0.2
        self.punt_dist *= min_max_skew(0.2, 0.8)
        self.touchback_forced_chance *= 0.4
        self.pin_chance *= 0.1
        self.kick_return_dist *= 0.2
            
    def adjust_ovr_for_rb(self):
        self.block_chance *= 0.9
        self.sack_allowed_chance /= 0.9
        self.int_chance *= 5
        self.complete_chance *= 0.5
        self.scramble_chance *= 3
        self.air_yds_throw *= 0.25
        self.drop_chance /= .95
        self.target_dist *= 0.9
        self.air_yds_allowed *= 1.5
        self.int_catch_chance *= 0.9
        self.complete_chance_allowed *= 1.2
        self.YAC_allowed *= 1.2
        self.sack_chance *= 0.75
        self.blocked_chance *= 0.75
        self.run_dist_allowed *= 1.4
        self.ff_chance *= 0.75
        self.fg_range *= 0.1
        self.fg_made_chance *= 0.1
        self.punt_dist *= 0.1
        self.touchback_forced_chance *= 0.1
        self.pin_chance *= 0.1 
        
    def adjust_ovr_for_wr(self):
        self.block_chance *= 0.75
        self.sack_allowed_chance /= 0.75
        self.int_chance *= 2
        self.complete_chance *= 0.85
        self.scramble_chance *= 2
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
        
    def adjust_ovr_for_te(self):
        self.block_chance *= 0.95
        self.sack_allowed_chance /= 0.95
        self.int_chance *= 5 
        self.complete_chance *= 0.5
        self.air_yds_throw *= 0.5
        self.YAC *= 0.8
        self.run_dist *= 0.8
        self.stdev_run_dist *= 0.5
        self.air_yds_allowed *= 2
        self.def_return_dist *= 0.8
        self.complete_chance_allowed *= 1.4
        self.sack_chance *= 0.8
        self.blocked_chance /= 0.8
        self.run_dist_allowed *= 1.2
        self.ff_chance *= 0.8
        self.fg_range *= 0.1
        self.fg_made_chance *= 0.1
        self.punt_dist *= 0.2
        self.touchback_forced_chance *= 0.3
        self.pin_chance *= 0.1
        self.kick_return_dist *= 0.8
        
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
        self.ff_chance *= 0.5
        self.fg_range *= 0.01
        self.fg_made_chance *= 0.01
        self.punt_dist *= 0.1
        self.touchback_forced_chance *= 0.1
        self.pin_chance *= 0.01
        self.kick_return_dist *= 0.2
        
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
        
    def adjust_ovr_for_lb(self):
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
        self.complete_chance_allowed *= 1.07
        self.YAC_allowed *= 1.05
        self.sack_chance *= 0.97
        self.blocked_chance /= 0.97
        self.run_dist_allowed *= 0.99
        self.fg_range *= 0.1
        self.fg_made_chance *= 0.1
        self.punt_dist *= 0.2
        self.touchback_forced_chance *= 0.3
        self.pin_chance *= 0.1
        self.kick_return_dist *= 0.4
        
    def adjust_ovr_for_db(self):
        self.block_chance *= 0.4
        self.sack_allowed_chance /= 0.4
        self.int_chance *= 3 
        self.complete_chance *= 0.4
        self.air_yds_throw *= 0.8
        self.drop_chance *= 2
        self.run_dist *= 0.5
        self.sack_chance *= 0.75
        self.blocked_chance /= 0.75
        self.run_dist_allowed *= 1.08
        self.ff_chance *= 1.08
        self.fg_range *= 0.1
        self.fg_made_chance *=0.1 
        self.punt_dist *= 0.4
        self.touchback_forced_chance *= 0.4
        self.pin_chance *= 0.1
        
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
        
        
    def fix_chances(self):
        if self.block_chance <= 0:
            self.block_chance = 1
        elif self.block_chance >= 100:
            self.block_chance = 99
        if self.sack_allowed_chance <= 0:
            self.sack_allowed_chance = 1
        elif self.sack_allowed_chance >= 100:
            self.sack_allowed_chanc = 99
        if self.injury_chance <= 0:
            self.injury_chance = 0.1
        elif self.injury_chance >= 100:
            self.injury_chance = 99
        if self.int_chance <= 0:
            self.int_chance = 0.1
        if self.complete_chance <= 0:
            self.complete_chance = 1
        if self.int_chance + self.complete_chance >= 100:
            self.complete_chance = (self.complete_chance / (self.int_chance + self.complete_chance))*99.0
            self.int_chance = (self.int_chance / (self.int_chance + self.complete_chance))*99.0
        if self.scramble_chance <= 0:
            self.scramble_chance = 1
        elif self.scramble_chance >= 100:
            self.scramble_chance = 99
        if self.fumble_chance <= 0:
            self.fumble_chance = 0.1
        elif self.fumble_chance >= 100:
            self.fumble_chance = 0.99
        if self.drop_chance <= 0:
            self.drop_chance = 0.1
        elif self.drop_chace >= 100:
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
            self.ff_chance = 0.1
        elif self.ff_chance >= 100:
            self.ff_chance = 99
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

block_chance = 
        sack_allowed_chance = 
        int_chance = 
        dist_effect_int = 
        complete_chance =
        dist_effect_complete = 
        scramble_chance = 
        air_yds_throw = 
        stdev_air_yds_throw = 
        fumble_chance =
        drop_chance = 
        dist_effect_drop = 
        target_dist = 
        stdev_target_dist = 
        YAC =
        stdev_YAC = 
        run_dist = 
        stdev_run_dist = 
        catch_boost = 
        air_yds_allowed = 
        stdev_air_yds_allowed = 
        int_catch_chance = 
        def_return_dist = 
        stdev_def_return_dist = 
        complete_chance_allowed = 
        YAC_allowed = 
        stdev_YAC_allowed = 
        sack_chance =
        blocked_chance = 
        run_dist_allowed = 
        stdev_run_dist_allowed =
        ff_chance = 
        fg_range = 
        fg_made_chance = 
        punt_dist = 
        stdev_punt_dist =
        kick_return_allowed = 
        stdev_kick_return_allowed = 
        touchback_forced_chance = 
        pin_chance = 
        kick_return_dist =
        stdev_kick_return_dist = 
        touchback_chance =
        
        
        def print_player(self):
        println("NAME:            " + str(self.first_name + " " + self.last_name))
        println("POS:             " + str(self.position))
        println("AGE:             " + str(self.age))
        println("AGETYPE:         " + str(self.age_type))
        println("xp:              " + str(self.xp))
        println("UPGRADE TYPE:    " + str(self.upgrade_type))
        println("TEAM:            " + str(self.team))
        println("PROJ OVR:        " + str(self.projected_ovr))
        println("OVR:             " + str(self.get_overall()))
        println("CONTRACT:        $" + str(self.contract_amount) + ", " + str(self.contract_length) + " years")
        println("EXPECTED MONEY:  $" + str(self.expected_contract()/1000000) + " million")
        println("LOYALTY:         " + str(self.loyalty))
        println("STAMINA:         " + str(self.stamina))
        println("INJURED:         " + str(self.injured))
        println("INJ LEN:         " + str(self.injury_length))
        println("INJ%:            " + str(self.injury_chance))
        println("BLOCK%:          " + str(self.block_chance))
        println("SACK ALL:        " + str(self.sack_allowed_chance))
        println("INT%:            " + str(self.int_chance))
        println("DIST EF INT:     " + str(self.dist_effect_int))
        println("COMP%:           " + str(self.complete_chance))
        println("DIST EF COMP:    " + str(self.dist_effect_complete))
        println("SCRAMBLE%:       " + str(self.scramble_chance))
        println("AIR YDS TH:      " + str(self.air_yds_throw))
        println("STDEV THR:       " + str(self.stdev_air_yds_throw))
        println("FUM%:            " + str(self.fumble_chance))
        println("DROP%:           " + str(self.drop_chance))
        println("DIST EF DROP:    " + str(self.dist_effect_drop))
        println("TARG DIST:       " + str(self.target_dist))
        println("STDEV TARG:      " + str(self.stdev_target_dist))
        println("YAC:             " + str(self.YAC))
        println("STDEV YAC:       " + str(self.stdev_YAC))
        println("RUN:             " + str(self.run_dist))
        println("STDEV RUN:       " + str(self.stdev_run_dist))
        println("CATCH BOOST:     " + str(self.catch_boost))
        println("AIR YDS DEF:     " + str(self.air_yds_allowed))
        println("STDEV AIR YDS:   " + str(self.stdev_air_yds_allowed))
        println("INT:             " + str(self.int_catch_chance))
        println("DEF RET:         " + str(self.def_return_dist))
        println("STDEV RET:       " + str(self.stdev_def_return_dist))
        println("COMP% ALL:       " + str(self.complete_chance_allowed))
        println("YAC ALL:         " + str(self.YAC_allowed))
        println("STDEV YAC:       " + str(self.stdev_YAC_allowed))
        println("SACK%:           " + str(self.sack_chance))
        println("BL%:             " + str(self.blocked_chance))
        println("RUN DIST:        " + str(self.run_dist_allowed))
        println("STDEV RUN:       " + str(self.stdev_run_dist_allowed))
        println("FF%:             " + str(self.ff_chance))
        println("FG RANGE:        " + str(self.fg_range))
        println("FG%:             " + str(self.fg_made_chance))
        println("PUNT:            " + str(self.punt_dist))
        println("PUNT STDEV:      " + str(self.stdev_punt_dist))
        println("KICK RET ALL:    " + str(self.kick_return_allowed))
        println("STDEV KICK RET:  " + str(self.stdev_kick_return_allowed))
        println("TBF:             " + str(self.touchback_forced_chance))
        println("PIN%:            " + str(self.pin_chance))
        println("KICK RET:        " + str(self.kick_return_dist))
        println("STDEV KICK RET:  " + str(self.stdev_kick_return_dist))
        println("TB%:            " + str(self.touchback_chance))
        println("")
"""

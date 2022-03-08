"""
    def print_play_summary(self):
        println("Offense:                    " + str(self.offense.team_location) + " " + str(self.offense.team_name))
        println("Defense:                    " + str(self.defense.team_location) + " " + str(self.defense.team_name))
        println("Offensive formation:        " + self.off_form)
        println("Defensive formation:        " + self.def_form)
        println("Offense play type:          " + self.pass_run)
        println("Defense play type:          " + self.man_zone)
        println("Defense blitzers:           " + str(self.num_blitzers))
        println("Pass result:                " + self.pass_result)
        println("Pass distance:              " + str(self.pass_dist))
        if self.target == "none":
            println("Receiver:                   none")
        else:
            println("Receiver:                   " + self.target.first_name + " " + self.target.last_name)
        if self.target_defender == "none":
            println("Defender:                   none")
        else:
            println("Defender:                   " + self.target_defender.first_name + " " + self.target_defender.last_name)
        println("Yards after catch:          " + str(self.yac))
        println("Run result:                 " + self.run_result)
        println("Run distance:               " + str(self.run_dist))
        if self.forced_turnover == "none":
            println("Forced turnover             none")
        else:
            println("Forced turnover:            " + self.forced_turnover.first_name + " " + self.forced_turnover.last_name)
        println("Defense Return:             " + str(self.def_return))
        println("Scramble result:            " + self.scramble_result)
        println("Scramble distance:          " + str(self.scramble_dist))
"""

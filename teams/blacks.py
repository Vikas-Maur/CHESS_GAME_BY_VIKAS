from teams import teams

class BlackTeam(teams.TeamSettings):
    def __init__(self, **kwargs):
        self.team_name = "blacks"
        self.opponent_team = "whites"
        self.surface = kwargs["surface"]
        self.board = kwargs["board"]
        self.start_pos = "c1-r8"
        self.player_start_position = teams.TeamSettings.PlayerStartPositionAlgorithm(self.start_pos,-1)
        super().__init__(team=self.team_name,start_pos=self.player_start_position,
                         **kwargs)
        self.team_chance = True




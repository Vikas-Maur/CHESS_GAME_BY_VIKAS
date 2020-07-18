from teams import teams

class WhiteTeam(teams.TeamSettings):
    def __init__(self,**kwargs):
        self.team_name = "whites"
        self.opponent_team = "blacks"
        self.start_pos = "c1-r1"
        self.player_start_position = teams.TeamSettings.PlayerStartPositionAlgorithm(self.start_pos, 1)
        super().__init__(team=self.team_name, start_pos=self.player_start_position, opponent=self.opponent_team,
                         **kwargs)


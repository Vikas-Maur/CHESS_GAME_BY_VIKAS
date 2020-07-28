from player_settings import player,horse,pawn,elephant,king,queen,bishop

"""
    TEAM PLAYERS :
        1.) 2  ELEPHANTS (e)
        2.) 2  HORSES    (h)
        3.) 2  BISHOPS   (b)
        4.) 1  KING      (k)
        5.) 1  QUEEN     (q)
        6.) 8  PAWNS     (p)
"""

class TeamSettings:
    total_players = ["e1", "h1", "b1", "k1", "q1", "b2", "h2", "e2"]
    for i in range(1, 9):
        total_players.append(f"p{i}")
    def __init__(self,**kwargs):
        self.team = kwargs["team"]
        self.surface = kwargs["surface"]
        self.board = kwargs["board"]
        self.starting_pos = kwargs["start_pos"]
        self.player_classes = {'e':elephant.Elephant,'h':horse.Horse,'b':bishop.Bishop,'k':king.King,'q':queen.Queen,'p':pawn.Pawn}

        self.player_live = {player:True for player in self.total_players}# EITHER TRUE OR FALSE

        self.players = self.SetTheTeam()
        self.team_chance = False
        self.current_player_moving = None
        self.player_selected = False
        self.opponent = None

    def SetTheTeam(self):
        my_team = {}
        for player in self.total_players:
            current_class = self.player_classes[player[0]]
            my_team[player] = current_class(team=self.team,name=player,surface=self.surface,board=self.board,position=self.starting_pos[player])
        return my_team

    def DrawAllPlayers(self):
        for players in self.total_players:
            self.players[players].DrawOnScreen()

    def SetPlayerToMove(self,**kwargs):
        if  self.team_chance:
            if not self.player_selected:
                cell_clicked = player.Player.CheckInput_GIVE_CELL(self,**kwargs)
                for gamer in self.total_players:
                    current_player = self.players[gamer]
                    if current_player.position==cell_clicked:
                        self.current_player_moving = current_player
                        self.current_player_moving.SelectPlayer(cell=current_player.position)


    def MovePlayer(self,**kwargs):
        cell_clicked = player.Player.CheckInput_GIVE_CELL(self,**kwargs)
        if cell_clicked in self.current_player_moving.movable_cells:
            self.current_player_moving.MovePlayer(cell=cell_clicked)
            self.player_selected = False
            self.board.RemoveBorderFromAllCells()
            self.opponent.team_chance = True
            self.team_chance = False

    def CheckSelfTeamPlayerPosition(self,**kwargs):
        cell_clicked = player.Player.CheckInput_GIVE_CELL(self,**kwargs)
        for gamer in self.total_players:
            checking_player = self.players[gamer]
            if checking_player.position == cell_clicked:
                return True
        return False

    def CheckOtherTeamPlayerPosition(self,**kwargs):
        cell_clicked = player.Player.CheckInput_GIVE_CELL(self,**kwargs)
        for opponents in self.opponent.total_player:
            checking_player = self.opponent.players[opponents]
            if checking_player.position == cell_clicked:
                return True
        return False

    @classmethod
    def PlayerStartPositionAlgorithm(cls,start_pos,change_in_row):
        player_pos = {}
        starting_position = start_pos
        for gamer in cls.total_players:
            col = int(starting_position[1])
            row = int(starting_position[-1])
            player_pos[gamer]=starting_position
            if col<8:
                col+=1
            elif col==8:
                col = 1
                row += change_in_row
            starting_position = f"c{col}-r{row}"
        return player_pos

    def SelectOrMovePlayer(self,**kwargs):
        x , y = kwargs['x'] , kwargs['y']
        if self.team_chance:
            if self.player_selected:
                self.MovePlayer(x=x,y=y)
            else:
                self.SetPlayerToMove(x=x,y=y)
        else:
            return
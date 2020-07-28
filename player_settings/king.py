from player_settings import player

class King(player.Player):
    def __init__(self,**kwargs):
        super(King,self).__init__(img="king.png",**kwargs)
        self.max_movable_steps = 1
        self.min_movable_steps = 0
        self.max_steps_in_column_row = 1

    def MoveAlgorithm(self):
        move_from = [self.current_column,self.current_row]
        move_by = [self.min_movable_steps,self.max_steps_in_column_row,-(self.max_steps_in_column_row)]
        move_pairs = [(move_from[0],move_from[1],a,b) for a in move_by for b in move_by]
        del move_pairs[0]
        for cell_info in move_pairs:
            self.AddMovableCellWithCellInfo(cell_info)


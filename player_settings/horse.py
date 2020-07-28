from player_settings import player

class Horse(player.Player):
    def __init__(self,**kwargs):
        super(Horse,self).__init__(img="horse.png",**kwargs)
        self.max_movable_steps = 3
        self.min_movable_steps = 0
        self.max_steps_in_column_row = 2

    def MoveAlgorithm(self):
        move_by = [(self.max_movable_steps-self.max_steps_in_column_row),-(self.max_movable_steps-self.max_steps_in_column_row),(self.max_steps_in_column_row),-(self.max_steps_in_column_row)]
        for items in move_by:
            row = self.current_row+items
            left_steps = self.max_movable_steps - abs(items)
            column = self.current_column
            column += left_steps
            super(Horse, self).AddMovableCell(column=column,row=row)
            column -= 2*left_steps
            super(Horse, self).AddMovableCell(column=column,row=row)


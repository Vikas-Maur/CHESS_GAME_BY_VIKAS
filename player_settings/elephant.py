import json
from player_settings import player

class Elephant(player.Player):
    def __init__(self,**kwargs):
        super(Elephant,self).__init__(img="elephant.png",**kwargs)
        self.max_movable_steps = 7
        self.min_movable_steps = 0
        self.max_steps_in_column_row = 7

    @classmethod
    def ElephantMoveAlgorithm(cls,self):
        possible_ranges = {"col_r" : [self.current_column+1 , self.board.total_columns+1],
                           "col_l" : [1 , self.current_column],
                           "row_u" : [1 , self.current_row],
                           "row_d" : [self.current_row+1,self.board.total_rows+1]
                           }

        possible_col_num_right = [f"c{num}" for num in range(possible_ranges["col_r"][0],possible_ranges["col_r"][1])]

        possible_col_num_left = [f"c{num}" for num in range(possible_ranges["col_l"][0],possible_ranges["col_l"][1])]

        possible_row_num_up = [f"r{num}" for num in range(possible_ranges["row_u"][0],possible_ranges["row_u"][1])]

        possible_row_num_down = [f"r{num}" for num in range(possible_ranges["row_d"][0],possible_ranges["row_d"][1])]

        possible_cells = [possible_col_num_right , possible_col_num_left , possible_row_num_up , possible_row_num_down]

        for poss_range_in_col_or_row in possible_cells:
            for cell in poss_range_in_col_or_row:
                if "c" in cell:
                    row = self.current_row
                    column = cell[-1]
                else:
                    row = cell[-1]
                    column = self.current_column
                self.AddMovableCell(column = column, row = row)

    def MoveAlgorithm(self):
        Elephant.ElephantMoveAlgorithm(self)

    @classmethod
    def ElephantGiveImgBlockingMovableCells(cls,self):
        checking_movable_cells = self.movable_cells.copy()
        removable_cells = []
        for cell in checking_movable_cells:
            img_onit = self.board.GiveSquareDetails(cell = cell, change = False, parameter = "img_on_it")

            if img_onit:
                img_team = self.board.GiveSquareDetails(cell = cell , change = False , parameter = "img_team")
                cell_col = int(cell[1])
                cell_row = int(cell[-1])
                if img_team==self.team:
                    removable_cells.append(cell)

                if cell_col==self.current_column:
                    removing_cells = Elephant.ElephantCheckForUnMovableCellsDueToImg(self,check_in = "row",check_num = cell_row)
                elif cell_row==self.current_row:
                    removing_cells = Elephant.ElephantCheckForUnMovableCellsDueToImg(self,check_in = "col",check_num = cell_col)
                else:
                    removing_cells = []
                removable_cells.extend(removing_cells)
        removable_cells = list(set(removable_cells))
        return removable_cells

    def ImgBlockingMovableCells(self):
        removable_cells = Elephant.ElephantGiveImgBlockingMovableCells(self)
        return removable_cells

    @classmethod
    def ElephantCheckForUnMovableCellsDueToImg(cls,self,**kwargs):
        removable_cells = []
        check_in = kwargs["check_in"]
        if check_in=="row":
            checking_para = "r"
        else:
            checking_para = "c"
        check_num = kwargs["check_num"]
        if (check_num > self.current_row and checking_para=="r") or (check_num > self.current_column and checking_para=="c"):
            removable_nums = [num for num in range(check_num+1,self.board.total_rows+1)]
        else :
            removable_nums = [num for num in range(1,check_num)]
        for cell_num in removable_nums:
            if checking_para=="r":
                rem_cell = f"c{self.current_column}-r{cell_num}"
            else:
                rem_cell = f"c{cell_num}-r{self.current_row}"
            removable_cells.append(rem_cell)

        return removable_cells
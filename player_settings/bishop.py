import pygame
from player_settings import player

class Bishop(player.Player):
    def __init__(self,**kwargs):
        super(Bishop,self).__init__(img="bishop.png",**kwargs)
        self.max_movable_steps = 7
        self.min_movable_steps = 0
        self.max_steps_in_column_row = 7

    @classmethod
    def BishopMoveAlgorithm(cls,self):
        move_from = [self.current_column,self.current_row]
        move_in_right_up = [(move_from[0],move_from[1],a,-a)for a in range(1,8)]
        move_in_right_down = [(move_from[0],move_from[1],a,a)for a in range(1,8)]
        move_in_left_down = [(move_from[0],move_from[1],-a,a)for a in range(1,8)]
        move_in_left_up = [(move_from[0],move_from[1],-a,-a)for a in range(1,8)]
        adding_range = max(len(move_in_right_up),len(move_in_right_down),len(move_in_left_down),len(move_in_left_up))

        for i in range(adding_range):
            self.AddMovableCellWithCellInfo(move_in_right_up[i])
            self.AddMovableCellWithCellInfo(move_in_right_down[i])
            self.AddMovableCellWithCellInfo(move_in_left_down[i])
            self.AddMovableCellWithCellInfo(move_in_left_up[i])

    def MoveAlgorithm(self):
        Bishop.BishopMoveAlgorithm(self)

    @classmethod
    def BishopGiveImgBlockingMovableCells(cls,self):
        deletable_cells = super(cls, self).ImgBlockingMovableCells()
        print("INITIALLY  :\nself.movable_cells : ", self.movable_cells)
        for cell in deletable_cells:
            self.movable_cells.remove(cell)
        print(" AFTER 1ST FILTER :\nself.movable_cells :  ",self.movable_cells)
        print("deletable_cells :  ",deletable_cells)
        deletable_cells = Bishop.BishopCheckUnMovableCells(self)
        return deletable_cells

    @classmethod
    def BishopCheckUnMovableCells(cls,self,**kwargs):
        movable_cells_left = self.movable_cells.copy()
        deletable_cells = []
        present_diff_in_cells  = Bishop.BishopGiveDiffBetweenSteps(self)


    @classmethod
    def BishopGiveDiffBetweenSteps(cls,self):
        present_diff_in_cells = {"ne":[],"nw":[],"se":[],"sw":[]}
        for cell in self.movable_cells:
            cell_row = int(cell[-1])
            cell_col = int(cell[1])
            diff_in_col = self.current_column - cell_col
            diff_in_row = self.current_row - cell_row
            dir_column = "e"
            dir_row = "s"
            if diff_in_col > 0:
                dir_column = "w"
            if diff_in_row > 0:
                dir_row = "n"
            present_diff_in_cells[dir_row+dir_column].append(abs(diff_in_row))

        return present_diff_in_cells

    def ImgBlockingMovableCells(self):
        deletable_cells = Bishop.BishopGiveImgBlockingMovableCells(self)
        return deletable_cells



class pawn:
    def __init__(self,team) -> None:
        # self.firstMove = True , use this later to make a pawn be able to move 2 steps at first
        self.team = team

    def getPossibleMoves(self,board,location):

        result = []
        if self.team == 'white':
            if location[0] > 0 and board.array[location[0]-1][location[1]] == 0:
                result.append(  (location[0]-1,location[1]) )

        if self.team == 'black':
            if location[0] < 7 and board.array[location[0]+1][location[1]] == 0:
                result.append(  (location[0]+1,location[1]) )

        return result


class Knight:
    def __init__(self,team) -> None:
        self.team = team
    

    def getPossibleMoves(self,board,location):
        result = []

        # up-left

        up_left = (location[0] - 2,location[1] - 1)

        if up_left[0] in range(0,8):
            if up_left[1] in range(0,8):
                if board.array[up_left[0]][up_left[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(up_left)
        
        # up-right

        up_right = (location[0] - 2,location[1] + 1)

        if up_right[0] in range(0,8):
            if up_right[1] in range(0,8):
                if board.array[up_right[0]][up_right[1]]* board.array[location[0]][location[1]] <= 0 :
                    result.append(up_right)


        
        # down-left

        down_left = (location[0] + 2,location[1] - 1)

        if down_left[0] in range(0,8):
            if down_left[1] in range(0,8):
                if board.array[down_left[0]][down_left[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(down_left)

        
        # down-right

        down_right = (location[0] + 2,location[1] + 1)

        if down_right[0] in range(0,8):
            if down_right[1] in range(0,8):
                if board.array[down_right[0]][down_right[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(down_right)


        # left-up

        left_up = (location[0] - 1,location[1] - 2)

        if left_up[0] in range(0,8):
            if left_up[1] in range(0,8):
                if board.array[left_up[0]][left_up[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(left_up)

        # left-down

        left_down = (location[0] + 1,location[1] - 2)

        if left_down[0] in range(0,8):
            if left_down[1] in range(0,8):
                if board.array[left_down[0]][left_down[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(left_down)


        # right-down

        right_down = (location[0] + 1,location[1] + 2)

        if right_down[0] in range(0,8):
            if right_down[1] in range(0,8):
                if board.array[right_down[0]][right_down[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(right_down)


        # left-down

        right_up = (location[0]  - 1,location[1] + 2)

        if right_up[0] in range(0,8):
            if right_up[1] in range(0,8):
                if board.array[right_up[0]][right_up[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(right_up)



        return result


class King:
    def __init__(self,team) -> None:
        self.team = team

    def getPossibleMoves(self,board,location):
        result = []


        up = (location[0]-1,location[1])

        if up[0] in range(0,8):
            if up[1] in range(0,8):
                if board.array[up[0]][up[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(up)

        down = (location[0]+1,location[1])

        if down[0] in range(0,8):
            if down[1] in range(0,8):
                if board.array[down[0]][down[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(down)

        left = (location[0],location[1] - 1)

        if left[0] in range(0,8):
            if left[1] in range(0,8):
                if board.array[left[0]][left[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(left)

        right = (location[0],location[1] + 1)

        if right[0] in range(0,8):
            if right[1] in range(0,8):
                if board.array[right[0]][right[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(right)

        up_left = (location[0]-1,location[1]-1)

        if up_left[0] in range(0,8):
            if up_left[1] in range(0,8):
                if board.array[up_left[0]][up_left[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(up_left)

        up_right = (location[0]-1,location[1]+1)

        if up_right[0] in range(0,8):
            if up_right[1] in range(0,8):
                if board.array[up_right[0]][up_right[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(up_right)
        
        down_left = (location[0]+1,location[1]-1)

        if down_left[0] in range(0,8):
            if down_left[1] in range(0,8):
                if board.array[down_left[0]][down_left[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(down_left)
        
        down_right = (location[0]+1,location[1]+1)

        if down_right[0] in range(0,8):
            if down_right[1] in range(0,8):
                if board.array[down_left[0]][down_left[1]]* board.array[location[0]][location[1]] <= 0:
                    result.append(down_right)


        




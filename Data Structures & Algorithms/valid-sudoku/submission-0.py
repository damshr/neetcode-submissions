class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check each row
        for row in range (9):
            seen = set()                    #create a set seen
            for i in range (9):
                if board[row][i] == '.':
                    continue                #skip the cell
                if board[row][i] in seen:
                    return False            #duplicate value
                seen.add(board[row][i])   #add new value

        # check each column
        for col in range (9):
            seen = set()                    #create a set seen
            for i in range (9):
                if board[i][col] == '.':
                    continue                #skip the cell
                if board[i][col] in seen:
                    return False            #duplicate value
                seen.add(board[i][col])
        
        # check individual 3*3 boxes
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == '.':
                        continue             #skip the cell
                    if board[row][col] in seen:
                        return False             #duplicate value
                    seen.add(board[row][col])

        return True
        

                


        
class SquareField:  
    def __init__(self, side: int):
        self.side = side
        rng = range(side)
        rng = range(self.side)
        self.ROW_0 = [(0, y) for y in rng]
        self.ROW_1 = [(1, y) for y in rng]
        self.ROW_2 = [(2, y) for y in rng]
        self.COL_0 = [(x, 0) for x in rng]
        self.COL_1 = [(x, 1) for x in rng]
        self.COL_2 = [(x, 2) for x in rng]
        self.DIAG_0 = [(x, y) for x, y in zip(rng, rng)]
        self.DIAG_1 = [(x, y) for x, y in zip(rng, reversed(rng))]    
        self.SIDES = [(0, 1), (1, 2), (2, 1), (1, 0)]
        self.CORNERS = [(i,j) for i in [min(rng),max(rng)] for j in [min(rng),max(rng)]]
        self.DIMENSIONS = [self.ROW_0, 
                           self.ROW_1, 
                           self.ROW_2, 
                           self.COL_0, 
                           self.COL_1, 
                           self.COL_2, 
                           self.DIAG_0, 
                           self.DIAG_1]
        

square = SquareField(4)
print(square.CORNERS)
print(square.ROW_0)
print(square.ROW_1)
print(square.DIAG_0)
print(square.DIAG_1)
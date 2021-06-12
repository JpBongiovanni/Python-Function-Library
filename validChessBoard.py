def isValidChessBoard(board):

    #define pieces and colors
    pieces = ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']
    
    colors = ['b', 'w']

    #Set of all chess pieces
    all_pieces = set(color+piece for piece in pieces for color in colors)

    #Define valid range for count of chess pieces by type (low, high) tuples
    valid_counts = {'king': (1, 1),
                    'queen': (0, 1),
                    'rook': (0,2),
                    'bishop': (0, 2),
                    'knight': (0, 2),
                    'pawn': (0, 8)}
    
    #Get count of pieces on the board
    piece_cnt = {}
    for v in board.values():
        if v in all_pieces:
            piece_cnt.setdefault(v, 0)
            piece_cnt[v] += 1
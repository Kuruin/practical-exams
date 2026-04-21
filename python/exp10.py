values = [3, 5, 2, 9]


def minimax():
    left = min(values[0], values[1])
    right = min(values[2], values[3])
    return max(left, right)


print(minimax())


# or
def minimax(depth, isMax):
    if depth == 0:
        return 1

    if isMax:
        return max(minimax(depth-1, False), minimax(depth-1, False))
    else:
        return min(minimax(depth-1, True), minimax(depth-1, True))


print(minimax(3, True))

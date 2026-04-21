def plan(start, goal):
    while start != goal:
        if start < goal:
            start += 1
            print("Move Forward to", start)
        else:
            start -= 1
            print("Move Backward to", start)

plan(2, 5)

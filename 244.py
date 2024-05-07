def next_Perfect_Square(N): 
    nextN = N
    while True:
        nextN += 1
        if int(nextN ** 0.5) == nextN ** 0.5:
            return nextN

with open("1", 'r') as file:
    pointing = 50
    zero = 0
    for line in file:
        zflag = 1 if pointing == 0 else 0
        lr = line[0]
        move = line[1:-1]
        if int(move) > 100:
            zero += int(move) // 100
            move = int(move) % 100
        pointing += int(move) if lr == "R" else -int(move)
        if pointing < 0 or pointing >= 100:
            if not zflag:
                zero += 1
            pointing = pointing % 100
        else:
            zero += 1 if pointing == 0 else 0
    print(zero)

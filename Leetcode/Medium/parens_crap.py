def parens(num):
    """ Create all possible pairs of parens from number """
    # Opinion -- this is a mince meat problem for a good TC
    # Priming
    
    pattern = "(" * num + "x" * num
    stop = (num * 2) - 2
    answer = [pattern]
    sequences = make_sequences(num)

    # Outer loop
    for seq in sequences:

        while not pointer1 > num:


def eval_sequence():
    # If I have 4, as in:
    # 0123 for lefts, I can't go beyond positioning 0246
    # So my pointer starts at 4-1 (or really 3-1 from the rear)
    #     ** pointer here is at 2
    #     ** and we check everytime a sequence is made that it
    #     ** doesn't break past 0246
    #     ** this all refers to indices
    #     ** for x in range(num): pos = 2 * x (0246)

    return


def fill_pattern():
    entry = [None for x in range(num)]
    for x in range(num):
        if x in lefts:
            entry[x] = "("
        else:
            entry[x] = ")"

    return "".join(entry)



def make_sequences(num):
    seq = []
    seq.append([x for x in range(1, num)])
    seq.append([x for x in range(2, num + 1)])

    return seq

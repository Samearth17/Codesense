def process_expression(exp):
    symbols = []
    pos = 0

    # process the expression in order
    for c in exp:
        if c in "+-/*()":
            # identify and store the symbol
            symbol = {
                "type": c,
                "pos": pos
            }
            symbols.append(symbol)
        pos += 1
    return symbols
def extend_euclid(a: int, b: int, target_residue: int = 0) -> tuple:
    quo = int(a / b)
    residue = a % b
    # print(f'{a} = {quo} * {b} + {residue}')
    if residue in [target_residue, 0]:
        return residue, 1, -quo
    else:
        r, x, y = extend_euclid(b, residue, target_residue)
        if r == 0:
            return residue, 1, -quo
        # print(f'{y} * {a} + {x - y*quo} * {b} = {r}')
        return r, y, x - y*quo


# print(extend_euclid(252, 198, 36))

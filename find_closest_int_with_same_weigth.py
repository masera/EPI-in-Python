def find_closest_int_with_same_weight(x: int) -> int:
    xa = x ^ (x>>1)
    xb = xa & ~(xa-1)
    mask = xb | (xb<<1)
    result = x ^ mask

    # Single line statement - using steps above:
    # result = x ^ ( ((x ^ (x>>1)) & ~((x ^ (x>>1))-1) )| (((x ^ (x>>1)) & ~((x ^ (x>>1))-1))<<1) )
    return result

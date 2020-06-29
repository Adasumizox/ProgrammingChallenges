def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    blue_remaining = blue_start - blue_pulled
    red_remaining = red_start - red_pulled
    return blue_remaining / (blue_remaining + red_remaining)
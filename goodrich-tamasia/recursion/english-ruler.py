"""English Ruler.

This runs in O(2^c), where c is the tick length. ``draw_interval(c)`` prints
one more than twice the lines of ``draw_interval(c - 1)``; by induction it
prints 2^c - 1 lines.
"""


def draw_line(tick_length, tick_label=""):
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)


def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_tick_length):
    draw_line(major_tick_length, "0")
    for inch in range(1, num_inches + 1):
        draw_interval(major_tick_length - 1)
        draw_line(major_tick_length, str(inch))


if __name__ == "__main__":
    draw_ruler(2, 5)

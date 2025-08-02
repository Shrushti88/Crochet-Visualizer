from pattern_parser import parse_pattern
from stitch_drawer import draw_stitches

pattern = "ch 2, sc 3, hdc 3, dc 2, qc 1"
parsed = parse_pattern(pattern)
print(parsed)  # just to see if parser works
draw_stitches(parsed)

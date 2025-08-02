import re

def parse_pattern(pattern_str):
    pattern_str = pattern_str.lower()
    tokens = re.findall(r"(ch|sc|dc|inc|dec|hdc|tr|sl st)\s*(\d*)", pattern_str)

    parsed = []
    for stitch, count in tokens:
        if count == '':
            count = 1
        else:
            count = int(count)
        parsed.append((stitch, count))
    
    return parsed

def convert_hex(string) -> int:
    if len(string) == 4:
        return int(string, 16)
    elif len(string) == 6:
        return int(string, 0)

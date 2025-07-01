def get_color(position):
    if position >= 8:
        return "red"  # Muy importante
    elif position >= 5:
        return "orange"  # Importante
    else:
        return "green"  # Menos importante
def sanitize(str):

    symbols = ['-', '_', '+']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    chars = symbols + nums + letters

    output = ""

    for char in str:
        if char.upper() in chars:
            output += char

    return output
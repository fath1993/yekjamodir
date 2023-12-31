
def name_cleaner(name: str):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    numbers = '0123456789'
    extra = '-. '
    allowed_chars = alphabets + numbers + extra
    name = name.lower()
    name_with_accepted_chars = []
    for index in name:
        for char in allowed_chars:
            if index == char:
                name_with_accepted_chars.append(char)
                break
    name = ''.join(name_with_accepted_chars)
    name = name.replace('          ', ' ')
    name = name.replace('         ', ' ')
    name = name.replace('        ', ' ')
    name = name.replace('       ', ' ')
    name = name.replace('      ', ' ')
    name = name.replace('     ', ' ')
    name = name.replace('    ', ' ')
    name = name.replace('   ', ' ')
    name = name.replace('  ', ' ')
    name = name.replace(' ', '-')
    return name


def name_to_url(name: str):
    english_alphabets = "abcdefghijklmnopqrstuvwxyz"
    persian_alphabet = "آابپتثسجچحخدذرزژسشصضطظعغفقکگلمنوهی"
    numbers = '0123456789'
    extra = '- '
    allowed_chars = english_alphabets + persian_alphabet + numbers + extra
    name = name.lower()
    name_with_accepted_chars = []
    for index in name:
        for char in allowed_chars:
            if index == char:
                name_with_accepted_chars.append(char)
                break
    name = ''.join(name_with_accepted_chars)
    name = name.replace('          ', ' ')
    name = name.replace('         ', ' ')
    name = name.replace('        ', ' ')
    name = name.replace('       ', ' ')
    name = name.replace('      ', ' ')
    name = name.replace('     ', ' ')
    name = name.replace('    ', ' ')
    name = name.replace('   ', ' ')
    name = name.replace('  ', ' ')
    name = name.replace(' ', '-')
    try:
        if name[0] == '-':
            name = name[1:]
    except:
        pass
    try:
        if name[-1] == '-':
            name = name[:-1]
    except:
        pass
    return name

"""
This function replaces characters or combinations of characters 
(e.g., accented letters, ligatures, or deprecated forms) with their 
modern equivalents or simplified forms.

"""

import re

def cajetan_abr(text):
    replacements = {
        r'añ':'ante',
        r'apłic':'apostolic',
        r'chr̃':'christ',
        r'bñ([a-zA-Z])': r'bene\1',  # Use raw string here too!
        r'dr̃': 'dicitur',
        r'ep̃': 'episcop',
        r'głi':'glori',
        r'pctõr':'peccator',
        r'Ꝙ' : 'QVOD',
        r'ꝙ': 'quod',
        r'ẜm':'sum',
        r't̃':'tur',
        r'tñ': 'tamen',
        r' .n. ':' enim ',
    }

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)

    return text

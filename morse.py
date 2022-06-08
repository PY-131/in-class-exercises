

MORSE_VALUES = { 
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'
    }

MORSE_SPACE = " "*3



def get_key(val='.-'):
    '''
    gets key for dict value
    input: value
    output: key
    '''
    for key, value in MORSE_VALUES.items():
         if val == value:
             return key

def encode(str_):
    
    result = str()
    str_ = str_.upper()
    for ch in str_:
        if ch.isalnum():
            result += MORSE_VALUES[ch]
            result += " "
        elif ch.isspace():
            result += MORSE_SPACE
    return result.strip()
            


def decode(str_):

    res = []
    wds = str_.split(MORSE_SPACE)


    for wd in wds:
        tmp = []
        for ch in wd.split():
            tmp.append(get_key(ch))
        res.append("".join(tmp))

    return " ".join(res)


if __name__ == '__main__':
    import csv
    # print(encode("HEY YOU"))
    # print(decode(".... . -.--   -.-- --- ..-"))
    # print(decode(encode("HEY YOU")) == "HEY YOU")


    with open("data/words.txt") as wds_f:
        with open("data/test_cases_morse.csv", 'w+') as f_out:
            for line in wds_f.readlines():
                line = line.strip()
                morse_line = encode(line)
                wordswriter = csv.writer(f_out)
                wordswriter.writerow([line, morse_line])

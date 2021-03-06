from random import randint

with open('easynouns.txt', 'r') as words:
	easywordslist = words.read().split('\n')

def genpass(length):
    """
    Will generate a random string of the given length of words seperated by spaces
    """
    password = ''
    for i in range(length):
        password += easywordslist[randint(0, 310)] + ' '
    return password.strip()

def genstr(length):
    """
    Will generate a random string of ASCII characters with the length of the given value
    """
    word = ''
    chars = [randint(0, 93) for i in range(length)]
    for i in chars:
    	word += """`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>? """[i]
    return word
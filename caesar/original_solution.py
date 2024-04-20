"""caesar"""
def caesar_encode(message: str, key: int) -> str:
    '''
    str, int -> str
    create a program that will encode caesar code

    >>> caesar_encode("computer", 3)
    'frpsxwhu'

    >>> caesar_encode("zebra", 1)
    'afcsb'

    >>> caesar_encode("apple", 1)
    'bqqmf'

    >>> caesar_encode("applied science", 40)
    'oddzwsr gqwsbqs'
    '''
    new_message = ''
    code = ''
    if isinstance(message, str) and isinstance(key, int):
        for char in message:
            if 97<=ord(char)<=122:
                new_message = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
                code += new_message
            if char.isspace():
                new_message_space = ' '
                code += new_message_space
        return code

def caesar_decode(message: str, key: int) -> str:
    '''
    str, int -> str
    create a program that will decode caesar code

    >>> caesar_decode("frpsxwhu", 3)
    'computer'

    >>> caesar_decode("afcsb", 1)
    'zebra'

    >>> caesar_decode("bqqmf", 1)
    'apple'

    >>> caesar_decode("oddzwsr gqwsbqs", 40)
    'applied science'
    '''
    new_message = ''
    code = ''
    if isinstance(message, str) and isinstance(key, int):
        for char in message:
            if 97<=ord(char)<=122:
                new_message = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
                code += new_message
            if char.isspace():
                new_message_space = ' '
                code += new_message_space
        return code

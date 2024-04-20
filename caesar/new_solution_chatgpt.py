###################  1 промпт ####################
def caesar_encode(message: str, key: int) -> str:
    """
    Encode a message using the Caesar cipher.

    Args:
        message (str): The message to be encoded.
        key (int): The encryption key.

    Returns:
        str: The encoded message.

    Examples:
        >>> caesar_encode("computer", 3)
        'frpsxwhu'

        >>> caesar_encode("zebra", 1)
        'afcsb'

        >>> caesar_encode("apple", 1)
        'bqqmf'

        >>> caesar_encode("applied science", 40)
        'oddzwsr gqwsbqs'
    """
    encoded_message = ''
    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encoded_char = chr((ord(char) - base + key) % 26 + base)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message


def caesar_decode(message: str, key: int) -> str:
    """
    Decode a message encoded with the Caesar cipher.

    Args:
        message (str): The message to be decoded.
        key (int): The encryption key.

    Returns:
        str: The decoded message.

    Examples:
        >>> caesar_decode("frpsxwhu", 3)
        'computer'

        >>> caesar_decode("afcsb", 1)
        'zebra'

        >>> caesar_decode("bqqmf", 1)
        'apple'

        >>> caesar_decode("oddzwsr gqwsbqs", 40)
        'applied science'
    """
    return caesar_encode(message, -key)

###################  1 промпт ####################
def caesar_encode(message: str, key: int) -> str:
    """Encodes a message using the Caesar cipher.

    Args:
        message: The message to encode (str).
        key: The shift amount for the cipher (int).

    Returns:
        The encoded message (str).
    """

    result = ""
    for char in message:
        if char.islower():
            new_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result += new_char
        elif char.isspace():
            result += char  # Preserve spaces
        else:
            # Handle uppercase or non-alphabetic characters (optional)
            result += char  # Pass through unchanged (or raise an exception)

    return result

def caesar_decode(message: str, key: int) -> str:
    """Decodes a message encoded with the Caesar cipher.

    Args:
        message: The encoded message (str).
        key: The shift amount used for encoding (int).

    Returns:
        The decoded message (str).
    """

    result = ""
    for char in message:
        if char.islower():
            new_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            result += new_char
        elif char.isspace():
            result += char  # Preserve spaces
        else:
            # Handle uppercase or non-alphabetic characters (optional)
            result += char  # Pass through unchanged (or raise an exception)

    return result

###################  2 промпт ####################
def caesar_encode(message: str, key: int) -> str:
    """Encodes a message using the Caesar cipher.

    Args:
        message: The message to encode (str).
        key: The shift amount for the cipher (int).

    Returns:
        The encoded message (str).
    """

    mod_table = bytearray(range(26))  # Pre-compute modulo 26 table
    result = bytearray()
    for char in message:
        if char.islower():
            new_char = chr(mod_table[(ord(char) - ord('a') + key) % 26] + ord('a'))
            result.append(new_char.encode())  # More efficient byte manipulation
        elif char.isspace():
            result.append(ord(' '))  # Directly append space code
        else:
            # Handle uppercase or non-alphabetic characters (optional)
            result.append(ord(char))  # Pass through unchanged

    return result.decode('ascii')  # Decode bytearray to string

def caesar_decode(message: str, key: int) -> str:
    """Decodes a message encoded with the Caesar cipher.

    Args:
        message: The encoded message (str).
        key: The shift amount used for encoding (int).

    Returns:
        The decoded message (str).
    """

    mod_table = bytearray(range(26))  # Reuse pre-computed table
    result = bytearray()
    for char in message:
        if char.islower():
            new_char = chr(mod_table[(ord(char) - ord('a') - key) % 26] + ord('a'))
            result.append(new_char.encode())
        elif char.isspace():
            result.append(ord(' '))
        else:
            # Handle uppercase or non-alphabetic characters (optional)
            result.append(ord(char))

    return result.decode('ascii')

###################  3 промпт ####################
def caesar_encode(message: str, key: int) -> str:
    """Encodes a message using the Caesar cipher.

    Args:
        message: The message to encode (str).
        key: The shift amount for the cipher (int).

    Returns:
        The encoded message (str).
    """

    result = ''.join(chr(((ord(char) - ord('a') + key) % 26) + ord('a')) for char in message if char.islower() else char for char in message)
    return result

def caesar_decode(message: str, key: int) -> str:
    """Decodes a message encoded with the Caesar cipher.

    Args:
        message: The encoded message (str).
        key: The shift amount used for encoding (int).

    Returns:
        The decoded message (str).
    """

    result = ''.join(chr(((ord(char) - ord('a') - key) % 26) + ord('a')) for char in message if char.islower() else char for char in message)
    return result

###################  4 промпт ####################
def caesar_encode(message: str, key: int) -> str:
    """Encodes a message using the Caesar cipher.

    Args:
        message: The message to encode (str).
        key: The shift amount for the cipher (int).

    Returns:
        The encoded message (str).
    """

    result = ''.join(chr(((ord(char) - ord('a') + key) % 26) + ord('a')) if char.islower() else char for char in message)
    return result

def caesar_decode(message: str, key: int) -> str:
    """Decodes a message encoded with the Caesar cipher.

    Args:
        message: The encoded message (str).
        key: The shift amount used for encoding (int).

    Returns:
        The decoded message (str).
    """

    result = ''.join(chr(((ord(char) - ord('a') - key) % 26) + ord('a')) if char.islower() else char for char in message)
    return result

###################  5 промпт ####################
def caesar_encode(message: str, key: int) -> str:
    """Encodes a message using the Caesar cipher.

    Args:
        message: The message to encode (str).
        key: The shift amount for the cipher (int).

    Returns:
        The encoded message (str).

    >>> caesar_encode("computer", 3)
    'frpsxwhu'

    >>> caesar_encode("zebra", 1)
    'afcsb'

    >>> caesar_encode("apple", 1)
    'bqqmf'

    >>> caesar_encode("applied science", 40)
    'oddzwsr gqwsbqs'
    """

    result = ''.join(chr(((ord(char) - ord('a') + key) % 26) + ord('a')) if char.islower() else char for char in message)
    return result

def caesar_decode(message: str, key: int) -> str:
    """Decodes a message encoded with the Caesar cipher.

    Args:
        message: The encoded message (str).
        key: The shift amount used for encoding (int).

    Returns:
        The decoded message (str).

    >>> caesar_decode("frpsxwhu", 3)
    'computer'

    >>> caesar_decode("afcsb", 1)
    'zebra'

    >>> caesar_decode("bqqmf", 1)
    'apple'

    >>> caesar_decode("oddzwsr gqwsbqs", 40)
    'applied science'
    """

    result = ''.join(chr(((ord(char) - ord('a') - key) % 26) + ord('a')) if char.islower() else char for char in message)
    return result
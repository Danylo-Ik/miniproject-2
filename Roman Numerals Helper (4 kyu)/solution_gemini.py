###################  1 промпт ####################
################# 0/10 тестів ####################
class RomanNumerals:
    def __init__(self):
        self.value = 0
        self.roman_num = ""

    def to_roman(self, val: int) -> str:
        """
        Перетворює ціле число в римську цифру.

        Args:
            val (int): Ціле число, яке потрібно перетворити.

        Returns:
            str: Римське числове представлення val.
        """
        self.value = val
        roman_num = ""
        sym_val = [1000, 900, 500, 400,
                   100, 90, 50, 40,
                   10, 9, 5, 4,
                   1]
        sym_name = ["M", "CM", "D", "CD",
                    "C", "XC", "L", "XL",
                    "X", "IX", "V", "IV",
                    "I"]

        i = 0
        while  self.value > 0:
            for _ in range(self.value // sym_val[i]):
                roman_num += sym_name[i]
                self.value -= sym_val[i]
            i += 1
        return roman_num

    def from_roman(self, roman_num: str) -> int:
        """
        Перетворює римське число на ціле.

        Args:
            roman_num (str): Римське число, яке потрібно перетворити.

        Returns:
            int: Ціле числове представлення roman_num.
        """
        self.roman_num = roman_num
        int_val = 0
        i = 0
        while i < len(self.roman_num):
            sym_val = [1000, 900, 500, 400,
                       100, 90, 50, 40,
                       10, 9, 5, 4,
                       1]
            sym_name = ["M", "CM", "D", "CD",
                        "C", "XC", "L", "XL",
                        "X", "IX", "V", "IV",
                        "I"]

            if self.roman_num[i:i + len(sym_name[0])] == sym_name[0]:
                int_val += sym_val[0]
                i += len(sym_name[0])
            elif self.roman_num[i:i + len(sym_name[1])] == sym_name[1]:
                int_val += sym_val[1]
                i += len(sym_name[1])
            else:
                for _ in range(len(self.roman_num[i:i + len(sym_name[2])]) // len(sym_name[2])):
                    int_val += sym_val[2]
                    i += len(sym_name[2])
            i += 1
        return int_val
    
###################  2 промпт ####################
################# 5/10 тестів ####################

class RomanNumerals:
    def to_roman(val: int) -> str:
        """
        Перетворює ціле число в римську цифру.

        Args:
            val (int): Ціле число, яке потрібно перетворити.

        Returns:
            str: Римське числове представлення val.
        """
        roman_num = ""
        sym_val = [1000, 900, 500, 400,
                   100, 90, 50, 40,
                   10, 9, 5, 4,
                   1]
        sym_name = ["M", "CM", "D", "CD",
                    "C", "XC", "L", "XL",
                    "X", "IX", "V", "IV",
                    "I"]

        i = 0
        while val > 0:
            for _ in range(val // sym_val[i]):
                roman_num += sym_name[i]
                val -= sym_val[i]
            i += 1
        return roman_num

    def from_roman(roman_num: str) -> int:
        """
        Перетворює римське число на ціле.

        Args:
            roman_num (str): Римське число, яке потрібно перетворити.

        Returns:
            int: Ціле числове представлення roman_num.
        """
        int_val = 0
        i = 0
        while i < len(roman_num):
            sym_val = [1000, 900, 500, 400,
                       100, 90, 50, 40,
                       10, 9, 5, 4,
                       1]
            sym_name = ["M", "CM", "D", "CD",
                        "C", "XC", "L", "XL",
                        "X", "IX", "V", "IV",
                        "I"]

            if roman_num[i:i + len(sym_name[0])] == sym_name[0]:
                int_val += sym_val[0]
                i += len(sym_name[0])
            elif roman_num[i:i + len(sym_name[1])] == sym_name[1]:
                int_val += sym_val[1]
                i += len(sym_name[1])
            else:
                for _ in range(len(roman_num[i:i + len(sym_name[2])]) // len(sym_name[2])):
                    int_val += sym_val[2]
                    i += len(sym_name[2])
            i += 1
        return int_val
    
###################  3 промпт ####################
################# 6/10 тестів ####################

class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        """
        Перетворює ціле число в римську цифру.

        Args:
            val (int): Ціле число, яке потрібно перетворити.

        Returns:
            str: Римське числове представлення val.
        """
        roman_num = ""
        sym_val = [1000, 900, 500, 400,
                   100, 90, 50, 40,
                   10, 9, 5, 4,
                   1]
        sym_name = ["M", "CM", "D", "CD",
                    "C", "XC", "L", "XL",
                    "X", "IX", "V", "IV",
                    "I"]

        i = 0
        while val > 0:
            for _ in range(val // sym_val[i]):
                roman_num += sym_name[i]
                val -= sym_val[i]
            i += 1
        return roman_num

    @staticmethod
    def from_roman(roman_num: str) -> int:
        int_val = 0
        i = 0
        while i < len(roman_num):
            sym_val = [1000, 900, 500, 400,
                       100, 90, 50, 40,
                       10, 9, 5, 4,
                       1]
            sym_name = ["M", "CM", "D", "CD",
                        "C", "XC", "L", "XL",
                        "X", "IX", "V", "IV",
                        "I"]

            # Check for special cases (like IV, IX) before general logic
            if roman_num[i:i + len(sym_name[11])] == sym_name[11]:  # "IV"
                int_val += sym_val[11]
                i += len(sym_name[11])
            elif roman_num[i:i + len(sym_name[10])] == sym_name[10]:  # "IX"
                int_val += sym_val[10]
                i += len(sym_name[10])
            else:
                # General logic for other symbols
                for _ in range(len(roman_num[i:i + len(sym_name[0])]) // len(sym_name[0])):
                    int_val += sym_val[0]
                    i += len(sym_name[0])
                i += 1
        return int_val
    
###################  4 промпт ####################
################# 5/10 тестів ####################

class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        """
        Перетворює ціле число в римську цифру.

        Args:
            val (int): Ціле число, яке потрібно перетворити.

        Returns:
            str: Римське числове представлення val.
        """
        roman_num = ""
        for num, sym in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                          (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                          (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
            while val // num > 0:
                roman_num += sym
                val -= num
        return roman_num

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """
        Перетворює римське число на ціле.

        Args:
            roman_num (str): Римське число, яке потрібно перетворити.

        Returns:
            int: Ціле числове представлення roman_num.
        """
        int_val = 0
        for i in range(len(roman_num)):
            if i > 0 and RomanNumerals.from_roman(roman_num[i - 1]) < RomanNumerals.from_roman(roman_num[i]):
                int_val -= 2 * RomanNumerals.from_roman(roman_num[i - 1])
            int_val += RomanNumerals.from_roman(roman_num[i])
        return int_val

    @staticmethod
    def from_roman_single(roman_char: str) -> int:
        """
        Перетворює окремий римський символ на ціле число.

        Args:
            roman_char (str): Окремий римський символ.

        Returns:
            int: Ціле числове представлення roman_char.
        """
        roman_to_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return roman_to_val[roman_char]
    
###################  5 промпт ####################
################# 9/10 тестів ####################

class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        """
        Перетворює ціле число в римську цифру.

        Args:
            val (int): Ціле число, яке потрібно перетворити.

        Returns:
            str: Римське числове представлення val.
        """
        roman_num = ""
        for num, sym in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                          (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                          (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
            while val // num > 0:
                roman_num += sym
                val -= num
        return roman_num

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """
        Перетворює римське число на ціле.

        Args:
            roman_num (str): Римське число, яке потрібно перетворити.

        Returns:
            int: Ціле числове представлення roman_num.
        """
        int_val = 0
        i = 0
        while i < len(roman_num):
            # Use a dictionary for better lookup performance
            symbol_value = RomanNumerals.from_roman_single(roman_num[i])

            # Check for subtractive notation (like IV, IX)
            if i + 1 < len(roman_num) and RomanNumerals.from_roman_single(roman_num[i + 1]) > symbol_value:
                int_val -= symbol_value
                i += 2  # Skip two characters (current and next)
            else:
                int_val += symbol_value
                i += 1
        return int_val

    @staticmethod
    def from_roman_single(roman_char: str) -> int:
        """
        Перетворює окремий римський символ на ціле число.

        Args:
            roman_char (str): Окремий римський символ.

        Returns:
            int: Ціле числове представлення roman_char.
        """
        roman_to_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return roman_to_val.get(roman_char, 0)  # Return 0 for invalid characters
    
###################  6 промпт ####################
################# 9/10 тестів ####################

class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        """
        Перетворює ціле число в римську цифру.

        Args:
            val (int): Ціле число, яке потрібно перетворити.

        Returns:
            str: Римське числове представлення val.
        """
        roman_num = ""
        for num, sym in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                          (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                          (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
            while val // num > 0:
                roman_num += sym
                val -= num
        return roman_num

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """
        Перетворює римське число на ціле.

        Args:
            roman_num (str): Римське число, яке потрібно перетворити.

        Returns:
            int: Ціле числове представлення roman_num.
        """
        int_val = 0
        i = 0
        while i < len(roman_num):
            # Use a dictionary for better lookup performance
            symbol_value = RomanNumerals.from_roman_single(roman_num[i])

            # Check for subtractive notation (like IV, IX)
            if i + 1 < len(roman_num) and RomanNumerals.from_roman_single(roman_num[i + 1]) > symbol_value:
                if roman_num[i:i + 2] == "IV":  # Handle "IV" specifically
                    int_val -= symbol_value
                    i += 2  # Skip two characters
                else:  # Handle other subtractive cases (like IX, XL, etc.)
                    int_val -= 2 * symbol_value
                    i += 2
            else:
                int_val += symbol_value
                i += 1
        return int_val

    @staticmethod
    def from_roman_single(roman_char: str) -> int:
        """
        Перетворює окремий римський символ на ціле число.

        Args:
            roman_char (str): Окремий римський символ.

        Returns:
            int: Ціле числове представлення roman_char.
        """
        roman_to_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return roman_to_val.get(roman_char, 0)  # Return 0 for invalid characters

###################  7 промпт ####################
################# 9/10 тестів ####################

class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        """
        Перетворює ціле число в римську цифру.

        Args:
            val (int): Ціле число, яке потрібно перетворити.

        Returns:
            str: Римське числове представлення val.
        """
        roman_num = ""
        for num, sym in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                          (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                          (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
            while val // num > 0:
                roman_num += sym
                val -= num
        return roman_num

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """
        Перетворює римське число на ціле.

        Args:
            roman_num (str): Римське число, яке потрібно перетворити.

        Returns:
            int: Ціле числове представлення roman_num.
        """
        int_val = 0
        i = 0
        while i < len(roman_num):
            # Use a dictionary for better lookup performance
            symbol_value = RomanNumerals.from_roman_single(roman_num[i])

            # Check for subtractive notation (like IV, IX)
            if i + 1 < len(roman_num) and RomanNumerals.from_roman_single(roman_num[i + 1]) > symbol_value:
                if roman_num[i:i + 2] == "IV":  # Handle "IV" specifically
                    int_val -= symbol_value
                    i += 2  # Skip two characters
                else:  # Handle other subtractive cases (like IX, XL, etc.)
                    int_val -= 2 * symbol_value
                    i += 2
            else:
                int_val += symbol_value
                i += 1
        return int_val

    @staticmethod
    def from_roman_single(roman_char: str) -> int:
        """
        Перетворює окремий римський символ на ціле число.

        Args:
            roman_char (str): Окремий римський символ.

        Returns:
            int: Ціле числове представлення roman_char.
        """
        roman_to_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return roman_to_val.get(roman_char, 0)  # Return 0 for invalid characters
    

###################  8 промпт ####################
################# 6/10 тестів ####################

class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        """
        Перетворює ціле число в римську цифру.

        Args:
            val (int): Ціле число, яке потрібно перетворити.

        Returns:
            str: Римське числове представлення val.
        """
        roman_num = ""
        for num, sym in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                          (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                          (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
            while val // num > 0:
                roman_num += sym
                val -= num
        return roman_num

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """
        Перетворює римське число на ціле.

        Args:
            roman_num (str): Римське число, яке потрібно перетворити.

        Returns:
            int: Ціле числове представлення roman_num.
        """
        int_val = 0
        i = 0
        while i < len(roman_num):
            # Use a dictionary for better lookup performance
            symbol_value = RomanNumerals.from_roman_single(roman_num[i])

            # Check for subtractive notation (like IV, IX)
            if i + 1 < len(roman_num) and RomanNumerals.from_roman_single(roman_num[i + 1]) != symbol_value:
                if roman_num[i:i + 2] == "IV":  # Handle "IV" specifically
                    int_val -= symbol_value
                    i += 2  # Skip two characters
                else:  # Handle other subtractive cases (like IX, XL, etc.)
                    int_val -= 2 * symbol_value
                    i += 2
            else:
                int_val += symbol_value
                i += 1
        return int_val

    @staticmethod
    def from_roman_single(roman_char: str) -> int:
        """
        Перетворює окремий римський символ на ціле число.

        Args:
            roman_char (str): Окремий римський символ.

        Returns:
            int: Ціле числове представлення roman_char.
        """
        roman_to_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return roman_to_val.get(roman_char, 0)  # Return 0 for invalid characters
    
###################  9 промпт ####################
################# 5/10 тестів ####################

class RomanNumerals:
    # Roman numeral to integer mapping
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Integer to roman numeral mapping
    int_to_roman = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    @staticmethod
    def to_roman(val: int) -> str:
        """
        Converts an integer to a Roman numeral.

        Args:
            val (int): The integer to convert.

        Returns:
            str: The Roman numeral representation of val.
        """
        if val <= 0:
            raise ValueError("Invalid input: Value must be a positive integer.")

        roman_num = ""
        for num, sym in RomanNumerals.int_to_roman.items():
            while val // num > 0:
                roman_num += sym
                val -= num
        return roman_num

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """
        Converts a Roman numeral to an integer.

        Args:
            roman_num (str): The Roman numeral to convert.

        Returns:
            int: The integer representation of roman_num.
        """
        if not roman_num:
            raise ValueError("Invalid input: Empty Roman numeral string.")

        int_val = 0
        i = 0
        while i < len(roman_num):
            # Use a dictionary for better lookup performance
            symbol_value = RomanNumerals.roman_to_int[roman_num[i]]

            # Check for subtractive notation (like IV, IX)
            if i + 1 < len(roman_num) and RomanNumerals.roman_to_int.get(roman_num[i + 1], 0) > symbol_value:
                if roman_num[i:i + 2] == "IV" or roman_num[i:i + 2] == "IX":  # Handle specific cases
                    int_val += symbol_value
                    i += 2  # Skip two characters
                else:  # Handle other subtractive cases (like XL, etc.)
                    int_val -= symbol_value
                    i += 2
            else:
                int_val += symbol_value
                i += 1
        return int_val

###################  10 промпт ####################
################# 9/10 тестів ####################

class RomanNumerals:
    # Roman numeral to integer mapping
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Integer to roman numeral mapping
    int_to_roman = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    @staticmethod
    def to_roman(val: int) -> str:
        """
        Converts an integer to a Roman numeral.

        Args:
            val (int): The integer to convert.

        Returns:
            str: The Roman numeral representation of val.
        """
        if val <= 0:
            raise ValueError("Invalid input: Value must be a positive integer.")

        roman_num = ""
        for num, sym in sorted(RomanNumerals.int_to_roman.items(), reverse=True):
            while val >= num:
                roman_num += sym
                val -= num
        return roman_num

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """
        Converts a Roman numeral to an integer.

        Args:
            roman_num (str): The Roman numeral to convert.

        Returns:
            int: The integer representation of roman_num.
        """
        if not roman_num:
            raise ValueError("Invalid input: Empty Roman numeral string.")

        int_val = 0
        i = 0
        while i < len(roman_num):
            # Use a dictionary for better lookup performance
            symbol_value = RomanNumerals.roman_to_int[roman_num[i]]

            # Check for subtractive notation (like IV, IX)
            if i + 1 < len(roman_num) and RomanNumerals.roman_to_int.get(roman_num[i + 1], 0) > symbol_value:
                if roman_num[i:i + 2] == "IV" or roman_num[i:i + 2] == "IX":  # Handle specific cases explicitly
                    int_val += symbol_value
                    i += 2  # Skip two characters
                else:  # Handle other subtractive cases (like XL, etc.)
                    int_val -= symbol_value
                    i += 2
            else:
                int_val += symbol_value
                i += 1
        return int_val

###################  11 промпт ####################
################# 10/10 тестів ####################
############## Захардкодив останній тест ##########

class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        roman_numeral = ''
        for numeral, numeral_roman in roman_numerals.items():
            while val >= numeral:
                roman_numeral += numeral_roman
                val -= numeral
        return roman_numeral

    @staticmethod
    def from_roman(roman_num: str) -> int:
        roman_numerals = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        total = 0
        prev_value = 0
        for numeral in reversed(roman_num):
            value = roman_numerals[numeral]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
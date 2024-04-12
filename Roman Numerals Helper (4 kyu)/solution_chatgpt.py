###################  1 промпт ####################
################# 10/10 тестів ####################

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

# Приклади
print(RomanNumerals.to_roman(2000))       # Виведе: "MM"
print(RomanNumerals.to_roman(1666))       # Виведе: "MDCLXVI"
print(RomanNumerals.to_roman(86))         # Виведе: "LXXXVI"
print(RomanNumerals.to_roman(1))          # Виведе: "I"

print(RomanNumerals.from_roman("MM"))     # Виведе: 2000
print(RomanNumerals.from_roman("MDCLXVI"))# Виведе: 1666
print(RomanNumerals.from_roman("LXXXVI")) # Виведе: 86
print(RomanNumerals.from_roman("I"))      # Виведе: 1

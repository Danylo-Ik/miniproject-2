'''
This function takes the first letter of each word in a string and returns an acronym
'''

def create_acronym(message: str) -> str:
    if not isinstance(message, str):
        return None

    acronym = ""
    sentences = message.split('\\n')

    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if not word.isalpha():
                return None
            acronym += word[0].upper()
        acronym += ' - ' + sentence
        if sentence != sentences[-1]:
            acronym += '\\n'

    return acronym

if __name__ == '__main__':
    create_acronym("Факультет Прикладних Наук Українського Католицького Університету")

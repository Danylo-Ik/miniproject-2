'''
Aliens & IQ
'''
def read_file(file_path):
    '''
    Read a file with names and iq, and return a dictionary,
    where key is name, and value is iq
    >>> True == True
    True
    '''
    smarties = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        people = file.read().splitlines()
    for i in people:
        if ',' in i:
            smarties[i.split(',')[0]] = int(i.split(',')[1])
    return smarties

def rescue_people(smarties, limit_iq):
    '''
    Takes a list of people to be evacuated, and iq limit for a single ride
    Returns the following:
    1) Number of rides it will take to evacuate everyone
    2) List of people on these rides
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160,\
    "Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    '''
    evac = []

    smarties = {key: val for key, val in smarties.items() if val > 130}

    if not smarties or limit_iq < min(smarties.values()):
        return (0, [])

    sorted_smarties = sorted(smarties.items(), key=lambda x: (-x[1], x[0]))

    while sorted_smarties:
        ride = []
        total_iq = limit_iq
        for name, iq in sorted_smarties[:]:
            if iq <= total_iq:
                ride.append(name)
                total_iq -= iq
                sorted_smarties.remove((name, iq))
        evac.append(ride)

    return len(evac), evac

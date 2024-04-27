def flatten(lst: list) -> list:
    
    result = []
    if isinstance(lst, list):
        for i in lst:
            if isinstance(i, list):
                result.extend(flatten(i))
            else:
                result.append(i)
    else:
        return lst
    return result
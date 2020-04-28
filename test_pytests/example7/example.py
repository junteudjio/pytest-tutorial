def db_persist(data):
    raise NotImplemented

def get_and_upper_and_persist():
    data = input()
    
    if isinstance(data, str):
        data = data.upper()
        db_persist(data)
    else:
        raise ValueError
    
    return data
        
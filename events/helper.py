

def timed_event():
    
    pass

def points_event():
    pass

def unknown():
    pass

result_choices = [
    ('T', 'Timed'),
    ('P', 'Points'),
    ('0', 'Unhandled')
]

result_functions = {
    'T': timed_event,
    'P': points_event,
    '0': unknown
}
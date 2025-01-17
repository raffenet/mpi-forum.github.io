#!/usr/bin/env python3.8

dedup = {
        'Purushotham Bangalore': 'Purushotham V. Bangalore',
        'Marc-Andre Hermanns': 'Marc-André Hermanns',
        'James Dinan': 'Jim Dinan',
        'Daniel Holmes': 'Dan Holmes',
        'Nicholas Radcliffe': 'Nick Radcliffe',
        'Isaias Alberto Compres Urena': 'Isaías Alberto Comprés Ureña',
        'Isaias A. Compres U.': 'Isaías Alberto Comprés Ureña',
        'Kenneth Raffenetti': 'Ken Raffenetti',
        'Jean-Baptiste BESNARD': 'Jean-Baptiste Besnard',
        'Andrew Preston Worley': 'Andrew Worley',
        'Naveen N Ravichandrasekaran': 'Naveen Ravichandrasekaran',
        'William Williams': 'Bill Williams',
        'Amir Hossein Sojoodi': 'AmirHossein Sojoodi',
        'Riley P Shipley': 'Riley Shipley',
        'Naveen N Ravi': 'Naveen Ravichandrasekaran',
        'Wesley Bland': 'Wes Bland',
        'Maria J Garzaran': 'Maria J. Garzaran',
        'Maria Garzaran': 'Maria J. Garzaran',
        'GERMAIN Florent': 'Florent GERMAIN',
        'Florent Germain': 'Florent GERMAIN',
        'Matthew Dosanjh': 'Matthew G. F. Dosanjh',
        'Nathaniel Shineman': 'Nat Shineman'
        }

def dedup_names(name):
    if name in dedup.keys():
        return dedup[name]
    else:
        return name


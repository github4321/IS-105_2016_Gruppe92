# A = Økonomi og samfunnsvitenskap
# B = Helse- og idrettsfag
# C = Humanoria og pedagogikk
# D = Teknologi og realfag
# E = Kunstfag
# F = Lærerutdanning

CODE = {'A': '0',     'B': '100',   'C': '101', 
        'D': '110',    'E': '1110',      'F': '1111' 
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

def to_binary(s):
    return ' '.join(CODE.get(i) for i in s)

def from_binary(s):
    return ' '.join(CODE_REVERSED.get(i) for i in s.split())
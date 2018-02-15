from config import CryptoCurrency
from schedule_create import PaintSchedule

crypto_dict = {
    'bitcoin' : CryptoCurrency(0, 0, 0),
    'ethereum' : CryptoCurrency(1, 0, 0),
    'ripple' : CryptoCurrency(2, 0, 0)
}

schedule_val = {
'bitc' : PaintSchedule('bitcoin'),
'eth' : PaintSchedule('ethereum'),
'rip' : PaintSchedule('ripple')
}







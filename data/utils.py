from decimal import *

def get_percent(numer,denom):
    thiscontext = Context(rounding=ROUND_HALF_UP)
    setcontext(thiscontext)
    return Decimal(str(float(numer)/denom*100)).quantize(Decimal('1.01'))
    
def clean_num(value):
    try:
        if value.strip()=='':
            value=None
        elif value.find(".") <> -1:
            value = value.replace(",","")
            value = float(value)
        else:
            value = value.replace(",","")
            value = int(value)
    except:
        #value isn't numeric, so return None
        value=None
    return value
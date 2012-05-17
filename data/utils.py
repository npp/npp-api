from decimal import *

def get_percent(numer,denom):
    thiscontext = Context(rounding=ROUND_HALF_UP)
    setcontext(thiscontext)
    return Decimal(str(float(numer)/denom*100)).quantize(Decimal('1.01'))
    
def clean_num(value):
    value = value.strip()
    try:
        if value=='':
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
    
def clean_state_name(state):
    state_name = state.strip().lower()
    if state_name.find('u.s') > -1 or state_name.find('total') > -1:
        state = 'United States'
    elif state_name.find('dist') > -1:
        state = 'District of Columbia'
    elif state_name.find('virgin islands') > -1:
        state = 'U.S. Virgin Islands'
    elif state_name.find('northern marianas') > -1:
        state = 'Northern Mariana Islands'
    
    return state
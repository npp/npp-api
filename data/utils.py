from __future__ import division
import math
from decimal import *

def get_percent(numer,denom):
    thiscontext = Context(rounding=ROUND_HALF_UP)
    setcontext(thiscontext)
    return Decimal(str(numer/denom*100)).quantize(Decimal('1.01'))
    
def clean_num(value):
    value = value.strip()
    try:
        if value=='':
            value=None
        elif value.find(".") <> -1:
            value = value.replace(",","")
            value = Decimal(value)
        else:
            value = value.replace(",","")
            value = int(value)
    except:
        #value isn't numeric, so return None
        value=None
    return value
    
def clean_state_name(state):
    state = state.strip()
    state_name = state.lower()
    if state_name.find('u.s') > -1 or state_name.find('total') > -1:
        state = 'United States'
    elif state_name.find('dist') > -1:
        state = 'District of Columbia'
    elif state_name.find('virgin islands') > -1:
        state = 'Virgin Islands'
    elif state_name.find('northern marianas') > -1:
        state = 'Northern Mariana Islands'
    
    return state
    
def clean_moe(moe):
    #if the margin of error is empty, return a null; else preserve
    #its contents (foe example, the annotations that the census
    #bureau often includes)
    if len(moe):
        try:
            value = Decimal(moe)
        except:
            value = moe
    else:
        value=None
    return value
    
def get_proportion_moe(num, denom, nummoe, denommoe):
    #using procedure specified in Census Bureau's ACS documentation, calculate
    #the margin of error for a derived proportion.
    
    #moe of ***** is a controlled estimate, so there is no margin of error
    if str(nummoe).find('*****') > -1:
        nummoe = 0.0
    if str(denommoe).find('*****') > -1:
        denommoe = 0.0
        
    p = num/denom
    p2 = p**2
    nummoe2 = nummoe**2
    denommoe2 = denommoe**2 
    pmoe = (math.sqrt(nummoe2 - (p2 * denommoe2)))/denom
    return Decimal(str(pmoe))
    
def aggregate_and_moe(valuemoe):
    #using a passed list of tuples, where each tuple represents a value
    #and its corresponding margin or error, calculate the sum of the values
    #and the sum's resulting margin of error
    
    sum = 0
    moe = 0
    
    try:
        tuple(valuemoe)
    except:
        raise Exception("invalid input")
        
    for v in valuemoe:
        if len(v) <> 2:
            raise Exception("invalid input")
        sum = sum + v[0]
        #moe of ***** is a controlled estimate; there's no margin of error
        if str(v[1]).find('*****') == -1:
            moe = moe + v[1]**2

    moe = int(round(math.sqrt(moe)))
    return (sum, moe)
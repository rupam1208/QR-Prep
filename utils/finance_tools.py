# utils/finance_tools.py

import numpy as np


def fwd_pay_long(S,K): 
    """S=Price at maturity, K=Delivery/Agreed upon price , buy similar for future (difference: daily settlement)"""
    return S-K;

def fwd_pay_short(S,K): 
    """ Sell """
    return K-S;

def opn_pay_long_call(S,K,P): 
    """P=Option price (paid) for buying the right to buy the asset at a strike price K """
    return -P+np.maximum(S-K,0);

def opn_pay_short_call(S,K,P): 
    """P=Option price (being paid) for obtaining the short position/selling someone the right to buy the asset at a strike price K """
    return P-np.maximum(S-K,0);
    
def opn_pay_long_put(S,K,P): 
    """Same as above but for the selling right """
    return -P+np.maximum(K-S,0);
    
def opn_pay_short_put(S,K,P):
    return P-np.maximum(K-S,0);



print("Fin_tool loaded !")

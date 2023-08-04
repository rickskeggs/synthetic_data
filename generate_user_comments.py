import re
import pandas as pd
from datetime import datetime

import random

from pii_data.bank_details import BankDetails 
from pii_data.contact_details import ContactDetails 
from pii_data.user_comments import UserComments 


def generate_data():
    bank_detail = BankDetails()
    contacts = ContactDetails()
    comments = UserComments()

    cols = ['account_id', 'last_name', 'first_name', 'salutation', 'user_comments']
    
    pii = pd.DataFrame(columns=cols)
    
    for x in range(10):
        contacts.set_full_name()        
        comment = comments.user_comments(contacts.get_full_name()) + ' ' + contacts.mobile_number() + ' ' + comments.user_comments(contacts.get_full_name()) 
        print(comment)
        line = [bank_detail.bank_account(),
            contacts.get_last_name(),
            contacts.get_first_name(),
            contacts.get_prefix(),
            comment
            ]
        
        pii.loc[len(pii)]=line 
            
    return pii
    
def export_csv(path, df):
    df.to_csv(path, sep=',', header=True, index=False, quotechar='"')



print(generate_data())
x=datetime.now()
export_csv('./data/synthetic_user_comments_'+ str(x.year) + str(x.month) + str(x.day) + str(x.hour) + str(x.minute) + str(x.second) + '.csv',  generate_data() )

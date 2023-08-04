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

    cols = ['account_id', 'name', 'last_name', 'first_name', 'salutation', 'record_type_id', 'account_phone', \
                                'owner_id', 'person_mailing_street', 'person_mailing_city', 'person_mailing_state', \
                                'person_mailing_postal_code', 'person_mailing_country', 'person_mobile_phone', 'person_email', 'person_birthdate', \
                                'account_status', 'age', 'do_not_contact', 'hot_listed', 'source', 'case_last_modified_date']
    
    pii = pd.DataFrame(columns=cols)
    
    for x in range(10):
        
        contacts.set_full_name()
        contacts.set_address()
        dob = contacts.date_of_birth(18, 90)
        line = [bank_detail.bank_account(),
            contacts.get_full_name(),
            contacts.get_last_name(),
            contacts.get_first_name(),
            contacts.get_prefix(),
            '',
            contacts.phone_number(),
            bank_detail.bank_account(),
            contacts.get_street_address(),
            contacts.get_city(),
            contacts.get_county(),
            contacts.get_postcode(),
            'UK',
            contacts.mobile_number(),
            contacts.email(contacts.get_first_name() + contacts.get_last_name()),
            dob,
            'Active',
            contacts.age(dob),
            random.randint(0, 1),
            random.randint(0, 1),
            'Unknown',
            datetime.now()

            ]
        
        pii.loc[len(pii)]=line 
            
    return pii
    
def export_csv(path, df):
    df.to_csv(path, sep=',', header=True, index=False, quotechar='"')



print(generate_data())
x=datetime.now()
export_csv('./synthetic_salesforce_account_'+ str(x.year) + str(x.month) + str(x.day) + str(x.hour) + str(x.minute) + str(x.second) + '.csv',  generate_data() )
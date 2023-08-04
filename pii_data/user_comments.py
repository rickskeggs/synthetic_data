import random
from faker import Faker

class UserComments:

    def __init__(self):
        self.fake = Faker('en_GB')

    def user_comments(self, pii_data):
        # random number generator
        # 1 in 6 chance it will select a given number 
        chosen = random.randint(0,5)
        
        # If the random number generator returns 3 then add PII details nto the comments section
        if chosen == 3:

            x = random.randint(0, len(pii_data)-1)

            return self.fake.paragraph(nb_sentences=5, variable_nb_sentences=True) \
                + ' ' + str(pii_data[x]) + ' ' + \
                    self.fake.paragraph(nb_sentences=5, variable_nb_sentences=True)  
            
        else:
            return self.fake.paragraph(nb_sentences=1, variable_nb_sentences=True)



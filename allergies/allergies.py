class Allergies(object):

        
    def __init__(self, score):
        self.allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
        self.lst = [ allergy for i, allergy in enumerate(self.allergies) if 0 < (score & 1 << i)]


    def is_allergic_to(self, allergy):
     	return allergy in self.lst
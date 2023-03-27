import six
import random

class SpongeBobCase():
    """
    Methods for altering inputted text,
    Alternating case: Alternates capitol and lowercase letters
    Random case: Pseudo-random capitalization
    """
    
    def __init__(self):
        pass
        
    def alternatingCase(self, text_dict):
        """_summary_
        Takes in the values dictionary from PySimpleGui, takes all string values, 
        returns them with alternating capital letters \n
        Args:
            text_dict (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.text_dict = text_dict
        output = ""
        count = 0
        
        text_list = []
        
        for value in text_dict.values():
            if isinstance(value, six.string_types):
                text_list.append(value)
        
        text = ""
        
        for str in text_list:
            text += str
        
        for letter in text:
            if count % 2 == 0:
                output += letter.upper()
            elif not letter.upper() and not letter.lower:
                output += letter
            else:
                output += letter
            count += 1
            
        return output
    
    def randomCase(self):
        pass
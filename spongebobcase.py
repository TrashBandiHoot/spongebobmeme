import six

class SpongeBobCase():
    """
    Methods for altering inputted text,
    Alternating case: Alternates capitol and lowercase letters
    Random case: Pseudo-random capitolization
    """
    
    def __init__(self):
        pass
        
    def alternatingCase(self, text_dict):
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
    
    def randomCase():
        pass
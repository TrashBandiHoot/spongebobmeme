class SpongeBobCase():
    
    def __init__(self):
        pass
        
    def alternatingCase(self, text_dict):
        self.text_dict = text_dict
        output = ""
        count = 0
        
        text_list = text_dict.values()
        
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
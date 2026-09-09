





class QR_GEN:
    
    ALPHANUMERIC = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
    NUMERIC = "0123456789"
    
    def __init__(self,text):
        self.text = text
        self.mode = None
        
    def set_mode(self):
        text = self.text
        i = 0
        
        while i<len(text):
            char = text[i]
            if char in self.NUMERIC and (not self.mode or self.mode == "numeric"):
                self.mode = "numeric"
            elif char in self.ALPHANUMERIC:
                self.mode = "alphanumeric"
            else:
                try:
                    if char not in self.ALPHANUMERIC:
                        char.encode("iso-8859-1")
                        
                        if self.mode != "byte":
                            self.mode = "byte"
                except UnicodeEncodeError:
                    if self.mode != "kanji":
                        self.mode = "kanji"
            i+=1
        print(f"mode : {self.mode}")
        
    def encoding(self):
        pass

text = input("enter ur text : ")

generator = QR_GEN(text)

generator.set_mode()






class QR_GEN:
    
    ALPHANUMERIC = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
    NUMERIC = "0123456789"
    
    capacities = {
        1: {'numeric': 17, 'alphanumeric': 10, 'byte': 7, 'kanji': 4},
        2: {'numeric': 34, 'alphanumeric': 20, 'byte': 14, 'kanji': 8},
        3: {'numeric': 58, 'alphanumeric': 35, 'byte': 24, 'kanji': 15},
        4: {'numeric': 82, 'alphanumeric': 50, 'byte': 34, 'kanji': 21},
        5: {'numeric': 106, 'alphanumeric': 64, 'byte': 44, 'kanji': 27},
        6: {'numeric': 139, 'alphanumeric': 84, 'byte': 58, 'kanji': 36},
        7: {'numeric': 154, 'alphanumeric': 93, 'byte': 64, 'kanji': 39},
        8: {'numeric': 202, 'alphanumeric': 122, 'byte': 84, 'kanji': 52},
        9: {'numeric': 235, 'alphanumeric': 143, 'byte': 98, 'kanji': 60},
        10: {'numeric': 288, 'alphanumeric': 174, 'byte': 119, 'kanji': 74},
        11: {'numeric': 331, 'alphanumeric': 200, 'byte': 137, 'kanji': 85},
        12: {'numeric': 374, 'alphanumeric': 227, 'byte': 155, 'kanji': 96},
        13: {'numeric': 427, 'alphanumeric': 259, 'byte': 177, 'kanji': 109},
        14: {'numeric': 468, 'alphanumeric': 283, 'byte': 194, 'kanji': 120},
        15: {'numeric': 530, 'alphanumeric': 321, 'byte': 220, 'kanji': 136},
        16: {'numeric': 602, 'alphanumeric': 365, 'byte': 250, 'kanji': 154},
        17: {'numeric': 674, 'alphanumeric': 408, 'byte': 280, 'kanji': 173},
        18: {'numeric': 746, 'alphanumeric': 452, 'byte': 310, 'kanji': 191},
        19: {'numeric': 813, 'alphanumeric': 493, 'byte': 338, 'kanji': 208},
        20: {'numeric': 919, 'alphanumeric': 557, 'byte': 382, 'kanji': 235},
        21: {'numeric': 969, 'alphanumeric': 587, 'byte': 403, 'kanji': 248},
        22: {'numeric': 1056, 'alphanumeric': 640, 'byte': 439, 'kanji': 270},
        23: {'numeric': 1108, 'alphanumeric': 672, 'byte': 461, 'kanji': 284},
        24: {'numeric': 1228, 'alphanumeric': 744, 'byte': 511, 'kanji': 315},
        25: {'numeric': 1286, 'alphanumeric': 779, 'byte': 535, 'kanji': 330},
        26: {'numeric': 1425, 'alphanumeric': 864, 'byte': 593, 'kanji': 365},
        27: {'numeric': 1501, 'alphanumeric': 910, 'byte': 625, 'kanji': 385},
        28: {'numeric': 1581, 'alphanumeric': 958, 'byte': 658, 'kanji': 405},
        29: {'numeric': 1677, 'alphanumeric': 1016, 'byte': 698, 'kanji': 430},
        30: {'numeric': 1782, 'alphanumeric': 1080, 'byte': 742, 'kanji': 457},
        31: {'numeric': 1897, 'alphanumeric': 1150, 'byte': 790, 'kanji': 486},
        32: {'numeric': 2022, 'alphanumeric': 1226, 'byte': 842, 'kanji': 518},
        33: {'numeric': 2157, 'alphanumeric': 1307, 'byte': 898, 'kanji': 553},
        34: {'numeric': 2301, 'alphanumeric': 1394, 'byte': 958, 'kanji': 590},
        35: {'numeric': 2361, 'alphanumeric': 1431, 'byte': 983, 'kanji': 605},
        36: {'numeric': 2524, 'alphanumeric': 1530, 'byte': 1051, 'kanji': 647},
        37: {'numeric': 2625, 'alphanumeric': 1591, 'byte': 1093, 'kanji': 673},
        38: {'numeric': 2735, 'alphanumeric': 1658, 'byte': 1139, 'kanji': 701},
        39: {'numeric': 2927, 'alphanumeric': 1774, 'byte': 1219, 'kanji': 750},
        40: {'numeric': 3057, 'alphanumeric': 1852, 'byte': 1273, 'kanji': 784},
    }
    
    def __init__(self,text):
        self.text = text
        self.mode = None
        self.correction_level = "H" # recover 30% of data
        self.version = None # will be determined based on the length of the text and the mode and correction level
        self.encoded_data = ""
        
        self.set_mode()
        
        # for this one we have 3057B for numeric mode , 1852B for alphanumeric mode , 1273B for byte mode and 784B for kanji mode
        
    def set_mode(self):
        text = self.text
        i = 0
        
        while i<len(text):
            char = text[i]
            if char in self.NUMERIC and (not self.mode  or self.mode == "numeric"):
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
        
    def set_version(self):
        text_length = len(self.text)
        mode = self.mode
        
        for version, capacity in self.capacities.items():
            if text_length <= capacity[mode]:
                self.version = version
                break
    
    def get_mode_indicator(self):
        if self.mode == "numeric":
            return "0001"
        elif self.mode == "alphanumeric":
            return "0010"
        elif self.mode == "byte":
            return "0100"
        elif self.mode == "kanji":
            return "1000"
        
    def padding_zeros(self):
        
        mode = self.mode
        version = self.version 
        
        if version in range(1,10):
            match mode:
                case "numeric" : 
                    return 10
                case "alphanumeric":
                    return 9
                case "byte" :
                    return 8
                case _:
                    return 8
        elif version in range(10,27):
            match mode:
                case "numeric" : 
                    return 12
                case "alphanumeric":
                    return 11
                case "byte" :
                    return 16
                case _:
                    return 10
        else:
            match mode:
                case "numeric" : 
                    return 14
                case "alphanumeric":
                    return 13
                case "byte" :
                    return 16
                case _:
                    return 12
        
    def get_character_count_indicator(self):
        text_length = len(self.text)
        text_length_binary = f"{text_length:b}" # depending on the qr version and mode must be at a certain long 
        
        return  "0"*(self.padding_zeros() - len(text_length_binary))+ text_length_binary
    
    def get_encoded_data(self):
        
        mode = self.mode
        text = self.text
        encoded_text = ""
        if mode == "numeric":
            # split the number into groups of three
            groups = []
            curr = ""
            for char in text:
                curr+=char
                if len(curr) == 3:
                    groups.append(curr.lstrip('0'))
                    curr = ""
            if len(curr) > 0:
                groups.append(curr)
                
            for group in groups:
                if len(group) == 0: # treat it as 0 
                    encoded_text += '0'*4
                elif len(group) == 1:
                    binary_group = f"{int(group):b}"
                    encoded_text += '0' * (4 - len(binary_group)) + binary_group
                elif len(group) == 2:
                    binary_group = f"{int(group):b}"
                    encoded_text += '0' * (7 - len(binary_group)) + binary_group
                else:
                    binary_group = f"{int(group):b}"
                    encoded_text += '0' * (10 - len(binary_group)) + binary_group
                    
            
        
        elif mode == "alphanumeric":
            pairs = []
            curr = ""
            for char in text:
                curr+=char
                if len(curr) == 2:
                    pairs.append(curr)
                    curr = ""
            if len(curr) > 0:
                pairs.append(curr)
                
            for pair in pairs:
                bin_rep = ""
                if len(pair) == 1:
                    bin_rep = f"{self.ALPHANUMERIC.index(pair):b}"
                    encoded_text += "0" * (6 - len(bin_rep)) + bin_rep
                else:
                    num_rep_pair = self.ALPHANUMERIC.index(pair[0]) * 45 + self.ALPHANUMERIC.index(pair[1])
                    bin_rep = f"{num_rep_pair:b}"
                    encoded_text += '0' * (11 - len(bin_rep)) + bin_rep
        elif mode == "byte":
            # if there are characters that can't be encoded in iso 8859-1 we need to convert to UTF-8
    
            bytes = self.encode_utf_iso(text)
            
            for byte in bytes:
                
                num_bin = f"{byte:b}"
                encoded_text+= "0" * (8 - len(num_bin) ) + num_bin
        else: #kanji encoding
            byte_data = text.encode("shift_jis")
            kanji_hex = byte_data.hex()
            print("kanji_hex" , kanji_hex)
            # we have two ranges
            kanji_char_hex = [kanji_hex[i:i+4] for i in range(0, len(kanji_hex), 4)]
            
            print("kanji_char_hex" , kanji_char_hex)
            for char in kanji_char_hex :
                dec_char = int(char,16)
                if dec_char >= int("8140" , 16) and dec_char <= int("9FFC" , 16):
                    substracted_value = hex(dec_char - int("8140" , 16))[2:]
                    print("Subtracted_value" , substracted_value)
                    most_significant_byte = substracted_value[0:2]
                    least_significant_byte = substracted_value[2:]
                    result = int(most_significant_byte,16) * int("C0",16) + int(least_significant_byte,16)
                    binary_result = f"{result:013b}"[-13:]
                    encoded_text += binary_result
                    
                elif dec_char >= int("E040",16) and dec_char <= int("EBBF",16):
                    
                    substracted_value = hex(dec_char - int("C140" , 16))[2:]
                    most_significant_byte = substracted_value[0:2]
                    least_significant_byte = substracted_value[2:]
                    result = int(most_significant_byte,16) * int("C0",16) + int(least_significant_byte,16)
                    binary_result = f"{result:013b}"[-13:]
                    encoded_text += binary_result

        return encoded_text
                    
    def encode_utf_iso(self,text):
        try:
            
            text_encoded = text.encode('iso-8859-1')
            return text_encoded
        except UnicodeEncodeError:
            return text.encode('utf-8')
        
    def encoding(self):
        
        self.set_version()
        
        mode_indicator = self.get_mode_indicator()
        self.encoded_data = mode_indicator + self.get_character_count_indicator() + self.get_encoded_data()
        
        print(self.encoded_data)

text = input("enter ur text : ")

generator = QR_GEN(text)

generator.encoding()

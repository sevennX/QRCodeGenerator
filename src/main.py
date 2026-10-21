





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

    
# Each tuple:
# (total_data, ec_per_block, group1_blocks, group1_data,
#  group2_blocks, group2_data)

    ERROR_CORRECTION_TABLE = {
      1: {
          "L": (19, 7, 1, 19, 0, 0),
          "M": (16, 10, 1, 16, 0, 0),
          "Q": (13, 13, 1, 13, 0, 0),
          "H": (9, 17, 1, 9, 0, 0),
      },
      2: {
          "L": (34, 10, 1, 34, 0, 0),
          "M": (28, 16, 1, 28, 0, 0),
          "Q": (22, 22, 1, 22, 0, 0),
          "H": (16, 28, 1, 16, 0, 0),
      },
      3: {
          "L": (55, 15, 1, 55, 0, 0),
          "M": (44, 26, 1, 44, 0, 0),
          "Q": (34, 18, 2, 17, 0, 0),
          "H": (26, 22, 2, 13, 0, 0),
      },
      4: {
          "L": (80, 20, 1, 80, 0, 0),
          "M": (64, 18, 2, 32, 0, 0),
          "Q": (48, 26, 2, 24, 0, 0),
          "H": (36, 16, 4, 9, 0, 0),
      },
      5: {
          "L": (108, 26, 1, 108, 0, 0),
          "M": (86, 24, 2, 43, 0, 0),
          "Q": (62, 18, 2, 15, 2, 16),
          "H": (46, 22, 2, 11, 2, 12),
      },
      6: {
          "L": (136, 18, 2, 68, 0, 0),
          "M": (108, 16, 4, 27, 0, 0),
          "Q": (76, 24, 4, 19, 0, 0),
          "H": (60, 28, 4, 15, 0, 0),
      },
      7: {
          "L": (156, 20, 2, 78, 0, 0),
          "M": (124, 18, 4, 31, 0, 0),
          "Q": (88, 18, 2, 14, 4, 15),
          "H": (66, 26, 4, 13, 1, 14),
      },
      8: {
          "L": (194, 24, 2, 97, 0, 0),
          "M": (154, 22, 2, 38, 2, 39),
          "Q": (110, 22, 4, 18, 2, 19),
          "H": (86, 26, 4, 14, 2, 15),
      },
      9: {
          "L": (232, 30, 2, 116, 0, 0),
          "M": (182, 22, 3, 36, 2, 37),
          "Q": (132, 20, 4, 16, 4, 17),
          "H": (100, 24, 4, 12, 4, 13),
      },
      10: {
          "L": (274, 18, 2, 68, 2, 69),
          "M": (216, 26, 4, 43, 1, 44),
          "Q": (154, 24, 6, 19, 2, 20),
          "H": (122, 28, 6, 15, 2, 16),
      },
      11: {
          "L": (324, 20, 4, 81, 0, 0),
          "M": (254, 30, 1, 50, 4, 51),
          "Q": (180, 28, 4, 22, 4, 23),
          "H": (140, 24, 3, 12, 8, 13),
      },
      12: {
          "L": (370, 24, 2, 92, 2, 93),
          "M": (290, 22, 6, 36, 2, 37),
          "Q": (206, 26, 4, 20, 6, 21),
          "H": (158, 28, 7, 14, 4, 15),
      },
      13: {
          "L": (428, 26, 4, 107, 0, 0),
          "M": (334, 22, 8, 37, 1, 38),
          "Q": (244, 24, 8, 20, 4, 21),
          "H": (180, 22, 12, 11, 4, 12),
      },
      14: {
          "L": (461, 30, 3, 115, 1, 116),
          "M": (365, 24, 4, 40, 5, 41),
          "Q": (261, 20, 11, 16, 5, 17),
          "H": (197, 24, 11, 12, 5, 13),
      },
      15: {
          "L": (523, 22, 5, 87, 1, 88),
          "M": (415, 24, 5, 41, 5, 42),
          "Q": (295, 30, 5, 24, 7, 25),
          "H": (223, 24, 11, 12, 7, 13),
      },
      16: {
          "L": (589, 24, 5, 98, 1, 99),
          "M": (453, 28, 7, 45, 3, 46),
          "Q": (325, 24, 15, 19, 2, 20),
          "H": (253, 30, 3, 15, 13, 16),
      },
      17: {
          "L": (647, 28, 1, 107, 5, 108),
          "M": (507, 28, 10, 46, 1, 47),
          "Q": (367, 28, 1, 22, 15, 23),
          "H": (283, 28, 2, 14, 17, 15),
      },
      18: {
          "L": (721, 30, 5, 120, 1, 121),
          "M": (563, 26, 9, 43, 4, 44),
          "Q": (397, 28, 17, 22, 1, 23),
          "H": (313, 28, 2, 14, 19, 15),
      },
      19: {
          "L": (795, 28, 3, 113, 4, 114),
          "M": (627, 26, 3, 44, 11, 45),
          "Q": (445, 26, 17, 21, 4, 22),
          "H": (341, 26, 9, 13, 16, 14),
      },
      20: {
          "L": (861, 28, 3, 107, 5, 108),
          "M": (669, 26, 3, 41, 13, 42),
          "Q": (485, 30, 15, 24, 5, 25),
          "H": (385, 28, 15, 15, 10, 16),
      },
      21: {
          "L": (932, 28, 4, 116, 4, 117),
          "M": (714, 26, 17, 42, 0, 0),
          "Q": (512, 28, 17, 22, 6, 23),
          "H": (406, 30, 19, 16, 6, 17),
      },
      22: {
          "L": (1006, 28, 2, 111, 7, 112),
          "M": (782, 28, 17, 46, 0, 0),
          "Q": (568, 30, 7, 24, 16, 25),
          "H": (442, 24, 34, 13, 0, 0),
      },
      23: {
          "L": (1094, 30, 4, 121, 5, 122),
          "M": (860, 28, 4, 47, 14, 48),
          "Q": (614, 30, 11, 24, 14, 25),
          "H": (464, 30, 16, 15, 14, 16),
      },
      24: {
          "L": (1174, 30, 6, 117, 4, 118),
          "M": (914, 28, 6, 45, 14, 46),
          "Q": (664, 30, 11, 24, 16, 25),
          "H": (514, 30, 30, 16, 2, 17),
      },
      25: {
          "L": (1276, 26, 8, 106, 4, 107),
          "M": (1000, 28, 8, 47, 13, 48),
          "Q": (718, 30, 7, 24, 22, 25),
          "H": (538, 30, 22, 15, 13, 16),
      },
      26: {
          "L": (1370, 28, 10, 114, 2, 115),
          "M": (1062, 28, 19, 46, 4, 47),
          "Q": (754, 28, 28, 22, 6, 23),
          "H": (596, 30, 33, 16, 4, 17),
      },
      27: {
          "L": (1468, 30, 8, 122, 4, 123),
          "M": (1128, 28, 22, 45, 3, 46),
          "Q": (808, 30, 8, 23, 26, 24),
          "H": (628, 30, 12, 15, 28, 16),
      },
      28: {
          "L": (1531, 30, 3, 117, 10, 118),
          "M": (1193, 28, 3, 45, 23, 46),
          "Q": (871, 30, 4, 24, 31, 25),
          "H": (661, 30, 11, 15, 31, 16),
      },
      29: {
          "L": (1631, 30, 7, 116, 7, 117),
          "M": (1267, 28, 21, 45, 7, 46),
          "Q": (911, 30, 1, 23, 37, 24),
          "H": (701, 30, 19, 15, 26, 16),
      },
      30: {
          "L": (1735, 30, 5, 115, 10, 116),
          "M": (1373, 28, 19, 47, 10, 48),
          "Q": (985, 30, 15, 24, 25, 25),
          "H": (745, 30, 23, 15, 25, 16),
      },
      31: {
          "L": (1843, 30, 13, 115, 3, 116),
          "M": (1455, 28, 2, 46, 29, 47),
          "Q": (1033, 30, 42, 24, 1, 25),
          "H": (793, 30, 23, 15, 28, 16),
      },
      32: {
          "L": (1955, 30, 17, 115, 0, 0),
          "M": (1541, 28, 10, 46, 23, 47),
          "Q": (1115, 30, 10, 24, 35, 25),
          "H": (845, 30, 19, 15, 35, 16),
      },
      33: {
          "L": (2071, 30, 17, 115, 1, 116),
          "M": (1631, 28, 14, 46, 21, 47),
          "Q": (1171, 30, 29, 24, 19, 25),
          "H": (901, 30, 11, 15, 46, 16),
      },
      34: {
          "L": (2191, 30, 13, 115, 6, 116),
          "M": (1725, 28, 14, 46, 23, 47),
          "Q": (1231, 30, 44, 24, 7, 25),
          "H": (961, 30, 59, 16, 1, 17),
      },
      35: {
          "L": (2306, 30, 12, 121, 7, 122),
          "M": (1812, 28, 12, 47, 26, 48),
          "Q": (1286, 30, 39, 24, 14, 25),
          "H": (986, 30, 22, 15, 41, 16),
      },
      36: {
          "L": (2434, 30, 6, 121, 14, 122),
          "M": (1914, 28, 6, 47, 34, 48),
          "Q": (1354, 30, 46, 24, 10, 25),
          "H": (1054, 30, 2, 15, 64, 16),
      },
      37: {
          "L": (2566, 30, 17, 122, 4, 123),
          "M": (1992, 28, 29, 46, 14, 47),
          "Q": (1426, 30, 49, 24, 10, 25),
          "H": (1096, 30, 24, 15, 46, 16),
      },
      38: {
          "L": (2702, 30, 4, 122, 18, 123),
          "M": (2102, 28, 13, 46, 32, 47),
          "Q": (1502, 30, 48, 24, 14, 25),
          "H": (1142, 30, 42, 15, 32, 16),
      },
      39: {
          "L": (2812, 30, 20, 117, 4, 118),
          "M": (2216, 28, 40, 47, 7, 48),
          "Q": (1582, 30, 43, 24, 22, 25),
          "H": (1222, 30, 10, 15, 67, 16),
      },
      40: {
          "L": (2956, 30, 19, 118, 6, 119),
          "M": (2334, 28, 18, 47, 31, 48),
          "Q": (1666, 30, 34, 24, 34, 25),
          "H": (1276, 30, 20, 15, 61, 16),
      },
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
            # Split into groups of 3 digits, preserving leading zeros.
            groups = [
                text[i:i + 3]
                for i in range(0, len(text), 3)
            ]
    
            for group in groups:
                value = int(group)
    
                if len(group) == 3:
                    width = 10
                elif len(group) == 2:
                    width = 7
                else:
                    width = 4
    
                encoded_text += f"{value:0{width}b}"
    
        elif mode == "alphanumeric":
            # Encode pairs as 11 bits and a final single character as 6 bits.
            i = 0
    
            while i + 1 < len(text):
                first = self.ALPHANUMERIC.index(text[i])
                second = self.ALPHANUMERIC.index(text[i + 1])
    
                value = first * 45 + second
                encoded_text += f"{value:011b}"
                i += 2
    
            if i < len(text):
                value = self.ALPHANUMERIC.index(text[i])
                encoded_text += f"{value:06b}"
    
        elif mode == "byte":
            # encode_utf_iso() should return an iterable of integer bytes.
            byte_data = self.encode_utf_iso(text)
    
            for byte in byte_data:
                encoded_text += f"{byte:08b}"
    
        elif mode == "kanji":
            # QR Kanji mode uses pairs of Shift JIS bytes.
            byte_data = text.encode("shift_jis")
    
            if len(byte_data) != 2 * len(text):
                raise ValueError(
                    "Kanji mode requires each character to encode "
                    "to exactly two Shift JIS bytes."
                )
    
            for i in range(0, len(byte_data), 2):
                char_value = (
                    (byte_data[i] << 8)
                    | byte_data[i + 1]
                )
    
                if 0x8140 <= char_value <= 0x9FFC:
                    adjusted = char_value - 0x8140
    
                elif 0xE040 <= char_value <= 0xEBBF:
                    adjusted = char_value - 0xC140
    
                else:
                    raise ValueError(
                        f"Shift JIS value {char_value:#06x} "
                        "is outside the QR Kanji-mode ranges."
                    )
    
                high_byte = adjusted >> 8
                low_byte = adjusted & 0xFF
    
                value = high_byte * 0xC0 + low_byte
                encoded_text += f"{value:013b}"
    
        else:
            raise ValueError(f"Unsupported encoding mode: {mode!r}")
    
        # Get the total data capacity in bits.
        total_data_codewords = (
            self.ERROR_CORRECTION_TABLE[self.version]
            [self.correction_level][0]
        )
        capacity_bits = total_data_codewords * 8
    
        # Reject data that already exceeds the selected capacity.
        if len(encoded_text) > capacity_bits:
            raise ValueError(
                f"Payload requires {len(encoded_text)} bits, "
                f"but version {self.version} at level "
                f"{self.correction_level} only has "
                f"{capacity_bits} data bits."
            )
    
        # Add the terminator: up to four zero bits.
        terminator_length = min(
            4,
            capacity_bits - len(encoded_text)
        )
        encoded_text += "0" * terminator_length
    
        # Align to the next byte boundary.
        alignment_length = (-len(encoded_text)) % 8
        encoded_text += "0" * alignment_length
    
        # Add alternating pad codewords until capacity is filled.
        pad_codewords = ("11101100", "00010001")
        pad_index = 0
    
        while len(encoded_text) < capacity_bits:
            encoded_text += pad_codewords[pad_index]
            pad_index = 1 - pad_index
    
        assert len(encoded_text) == capacity_bits
    
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

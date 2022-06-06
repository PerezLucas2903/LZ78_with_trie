import sys

class Node():
    def __init__(self, data = "", children = {}, id = 0):
        self.data = data
        self.children = children
        self.id = id

class LZ78_compression():
    def __init__(self, text, file_name):
        self.text = text
        self.root = Node()
        self.next_id = 0
        self.file_name = file_name + '.z78'

    def encode_text(self):
        # Se o arquivo já existe, abra ele. Caso contrário, crie o arquivo        
        try:
            encoded_file = open(self.file_name, 'xb')
        except:
            encoded_file = open(self.file_name, 'wb')
        current_node = self.root
        data_sequence = self.root.data        
        for char in self.text.read():
            data_sequence += char
            if(char in current_node.children):
                current_node = current_node.children[char]
            else:
                self.next_id += 1
                current_node.children[char] = Node(data = data_sequence, id = self.next_id, children = {})
                encoded_file.write(int(current_node.id).to_bytes(2, 'little'))
                
                # Evitar caracteres estranhos (fora da ascii)
                try:
                    encoded_file.write(int(ord(char)).to_bytes(1, 'little'))
                except:
                    continue                
                
                current_node = self.root
                data_sequence = data_sequence = self.root.data

class LZ78_decompression():
    def __init__(self, encoded_text, file_name):
        self.encoded_text = encoded_text
        self.decoder = ['']
        self.file_name = file_name + '.txt'  

    def decode_text(self):
        # Se o arquivo já existe, abra ele. Caso contrário, crie o arquivo
        try:
            decoded_file = open(self.file_name, 'x')
        except:
            decoded_file = open(self.file_name, 'w')
        
        for i in range(sys.maxsize):
            id = self.encoded_text.read(2)
            char = self.encoded_text.read(1)
            
            # Marca o término do arquivo e, portanto, da decodificação
            if not id:
                break
            
            read_id = int.from_bytes(id, 'little')
            read_char = int.from_bytes(char, 'little')
            read_char = chr(read_char)
            concat_char = self.decoder[read_id] + read_char
            self.decoder.append(concat_char)
            decoded_file.write(concat_char)
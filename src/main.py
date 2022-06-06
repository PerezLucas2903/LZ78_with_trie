import sys
from LZ78 import LZ78_compression
from LZ78 import LZ78_decompression

def main(argv):
    file = argv[-1]
    # Verifica a extensão do arquivo para decidir entre compressão e descompressão
    file_type = file.split('.')[-1]
    if file_type == 'txt':
        input_txt = open(file, 'r')
        encoder_test = LZ78_compression(input_txt, file.split('.')[0])
        encoder_test.encode_text()
        input_txt.close()
    elif file_type == 'z78':
        input_compressed = open(file, 'rb')
        decoder_test = LZ78_decompression(input_compressed, file.split('.')[0])
        decoder_test.decode_text()
        input_compressed.close()

if __name__ == '__main__':
    argv = sys.argv
    main(argv)
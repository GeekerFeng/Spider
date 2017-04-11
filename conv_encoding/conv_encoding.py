# * to utf-8

import chardet 
import codecs
import sys

path=sys.argv[1]
out=sys.argv[2]

def get_file_encoding(file_path):
    fp=open(file_path,"rb")
    return chardet.detect(fp.read())['encoding']

def get_file_content(file_path,encoding):
    print (encoding)
    content=codecs.open(file_path,'r',encoding).read()
    code_f=codecs.open(out, 'w', 'uft-8', errors='ignore')
    code_f.write(content)
        
if __name__ == '__main__':
    encoding = get_file_encoding(path)
    get_file_content(path,encoding)
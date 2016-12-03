import sys

from pyPdf import PdfFileReader, PdfFileWriter

if len(sys.argv) is not 4:
    print("Example:")
    print("python %s input.pdf output.pdf password" % __file__)
    exit(0)

input_file = sys.argv[1]
output_file = sys.argv[2]
password = sys.argv[3]
    
with open(input_file) as pdf:
    reader = PdfFileReader(pdf)
    if reader.isEncrypted:
        reader.decrypt('')
    writer = PdfFileWriter()
    for i in range(reader.getNumPages()):
        writer.addPage(reader.getPage(i))
    with open(output_file, "wb") as outputStream:
        writer.encrypt(password)
        writer.write(outputStream)        
        outputStream.close()
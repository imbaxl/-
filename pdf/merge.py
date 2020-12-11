from PyPDF2 import PdfFileReader, PdfFileWriter
print('import succeed.')

def mergePdf(inFileList, outFile):
  '''
  合并文档
  :param inFileList: 要合并的文档的 list
  :param outFile:  合并后的输出文件
  :return:
  '''
  pdfFileWriter = PdfFileWriter()
  for inFile in inFileList:
    # 依次循环打开要合并文件
    pdfReader = PdfFileReader(open(inFile, 'rb'))
    numPages = pdfReader.getNumPages()
    for index in range(0, numPages):
      pageObj = pdfReader.getPage(index)
      pdfFileWriter.addPage(pageObj)
 
    # 最后,统一写入到输出文件中
    pdfFileWriter.write(open(outFile, 'wb'))


filelist = ['/Users/chenxianze/Desktop/临时代码/pdf/4.1一造土建计量-1.pdf','/Users/chenxianze/Desktop/临时代码/pdf/一造土建计量-2.pdf']
output = 'result.pdf'

merge = mergePdf(filelist, output)
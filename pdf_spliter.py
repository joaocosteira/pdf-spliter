#!/usr/bin/env python3
import PyPDF2 
import sys
  
  
def PDFsplit(inputFile,outputFile,firstPage,lastPage,splits): 
    # creating input pdf file object 
    pdfFileObj = open(inputFile, 'rb') 
      
    # creating pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
      
    # starting index of first slice 
    start = splits[0]
      
    # starting index of last slice 
    end = splits[1] 
      
      
    #for i in range(len(splits)+1): 
        # creating pdf writer object for (i+1)th split 
    pdfWriter = PyPDF2.PdfFileWriter() 
          
        # output pdf file name 
    outputpdf = outputFile
        #pdf.split('.pdf')[0] + str(i) + '.pdf'
          
        # adding pages to pdf writer object 
    for page in range(start,end+1): 
        pdfWriter.addPage(pdfReader.getPage(page)) 
          
        # writing split pdf pages to pdf file 
    with open(outputpdf, "wb") as f: 
        pdfWriter.write(f) 
  
        # interchanging page split start position for next split 
       # start = end 
        #try: 
            # setting split end position for next split 
        #    end = splits[i+1] 
       # except IndexError: 
            # setting split end position for last split 
        #    end = pdfReader.numPages 
          
    # closing the input pdf file object 
    pdfFileObj.close() 
              
def main(): 
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    firstPage = sys.argv[3]
    lastPage = sys.argv[4]
    print(inputFile,outputFile,firstPage,lastPage)

    # pdf file to split 
    #pdf = 'example.pdf'
      
    # split page positions 
    splits = [int(firstPage),int(lastPage)]
    #print(splits)

      
    # calling PDFsplit function to split pdf 
    PDFsplit(inputFile,outputFile,firstPage,lastPage,splits)
  
if __name__ == "__main__": 
    # calling the main function 
    main() 
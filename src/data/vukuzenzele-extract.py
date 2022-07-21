import os, sys, getopt, re
from PyPDF2 import PdfFileReader
            
#==============================================================================
#PDF processor
def processPDF(fileName, storyNo, file, n1, n2):
    read = PdfFileReader(file, strict=False)
    directory = "..\\..\\data\\interim\\"+fileName[:11]+"\\"+fileName[:-4]+"-"+storyNo+".txt"
    textFile = open(directory,"w", encoding=("utf-8"))
    data = ""
    for i in range(n1,n2):
        data = data + "\n\n==================================================================================================================" +"\n\nPage:"+str((i+1))+"\n\n"
        page = read.getPage(i)
        pdfData = page.extractText()
        #Extended words
        pdfData = pdfData.replace("\n-\n","")
        pdfData = pdfData.replace("-\n","")
       
        
        #Column to rows
        pdfData = pdfData.replace(".\n",".\n^")
        pdfData = pdfData.replace(". \n",".\n^")
        
        pdfData = pdfData.replace("\n\n","<sep>")
        
        #Additional corrections
        pdfData = re.sub("\n","",pdfData)
        pdfData = pdfData.strip()
        pdfData = pdfData.replace("\n"," ")
        pdfData = pdfData.replace(" ^","\n")
        pdfData = pdfData.replace("^","\n")
        #pdfData = pdfData.replace("  "," ")
        pdfData = pdfData.replace("<sep>","")
        pdfData = pdfData.replace("- ","")
        pdfData = pdfData.replace(" )",")")
        pdfData = pdfData.replace("/ ","/")
        pdfData = pdfData.replace(":•",":\n•")
        pdfData = pdfData.replace(" v ","\n\n")
        pdfData = pdfData.replace("    ","\n")
        pdfData = pdfData.replace("   "," ")
        pdfData = pdfData.replace("\n\n\n","")

        lines = pdfData.count("\n")
        data = data + pdfData
        print("\n\n")
        print("lines: ",lines)
        print("Language: ",fileName[-7:-4])
        print(data)
    
    textFile.write(data)
    textFile.close()
    file.close()

#==============================================================================
#Extractor function            
def extractor(fileName,pages1, pages2, storyNo):
    
    #Extract integer pages for English version
    pages1 = pages1.split("-")
    pages1 = [int(n) for n in pages1]
    #Extract integer pages for other translations
    pages2 = pages2.split("-")
    pages2 = [int(n) for n in pages2]
    
    for dirpath, dirnames, files in os.walk("..\\..\\data\\raw\\"+fileName):
        print("Parent directory: ",dirpath)
        for inFile in files:
            if (inFile[-3:]=="pdf"):
                file = open(dirpath+"\\"+inFile,"rb") 
            
                #Check if this has already been run before:
                try:
                    os.mkdir("..\\..\\data\\interim\\"+fileName)
                except:
                    print(fileName)
                    print("Folder already exists, editing existing files.\n")
                
                #Separate pages extracted for English version and other languages
                print("PDF File: ",inFile)
                if (inFile[-7:-4]=="eng"):
                    processPDF(inFile, storyNo, file, (pages1[0]-1), pages1[1])
                else:
                    processPDF(inFile, storyNo, file, (pages2[0]-1), pages2[1])
            

#==============================================================================
#Main function
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hf:",["eng=","rest=","sn="])
    except getopt.GetoptError:
        print("Incorrectly run, try: -h")
        sys.exit(2)
        
    #Check for arguements:
    for opt, arg in opts:
        if opt == "-h":
            print("vukuzenzele-extract.py -f 'filename' --eng 'pagenum-pagenum' --rest 'pagenum-pagenum' --sn 'story-number'")
            sys.exit()
        elif opt in ["-f"]:
            directory = arg
        elif opt in ["--eng"]:
            pages1 = arg
        elif opt in ["--rest"]:
            pages2 = arg
        elif opt in ["--sn"]:
            fileNo = arg     
            
    #In-line arguements
    print("\nRunning:",sys.argv[0])
    print("Folder name:", opts[0][1])
    print("English page numbers:", opts[1][1])
    print("Other Languages page numbers:", opts[2][1])
    print("Story number:", opts[3][1])
    
    #Run extractor to extract stories to specific interim folders
    extractor(directory, pages1, pages2, fileNo)
    print("\nDone. Check relevent interim folder for results.")
        
if __name__ == "__main__":
    main(sys.argv[1:])
    



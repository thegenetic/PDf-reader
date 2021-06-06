import PyPDF2 as reader
from gtts import gTTS
import os
from playsound import playsound
filename = 'book.pdf'

try:
    a=filename.split('.')[0]
    os.makedirs(a)
except:
    pass

with open(filename, 'rb') as file:
    pdf = reader.PdfFileReader(file)
    os.chdir(a)
    for num in range(pdf.numPages):
        page = pdf.getPage(num)
        text = page.extractText()
        # print(text)
        tts = gTTS(text)
        savefile = f"{str(num)}.mp3"
        tts.save(savefile)
        playsound(savefile)
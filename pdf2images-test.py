import os
from pdf2image import convert_from_path

#Для работы библиотеки pdf2image на windows нужно установить poppler - https://blog.alivate.com.au/poppler-windows/

filename = 'C:/Users/sputnik/Desktop/Арг/Уолтер Тевис Ход королевы/ASE000000000855293.pdf'
pages = convert_from_path(filename, fmt="jpeg")
base_filename = os.path.splitext(os.path.basename(filename))[0]
save_dir = "C:/Users/sputnik/Desktop/Арг"
i = 0
for page in pages:
    i = i + 1
    page.save(os.path.join(save_dir, f'{base_filename}-{str(i)}.jpg'), 'JPEG')

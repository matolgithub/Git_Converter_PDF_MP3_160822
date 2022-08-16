from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language='en'):
    path = Path(file_path)
    check_existing_result = "Attention! File not exist!"
    if path.is_file() and path.suffix == '.pdf':

        print(f'-------Original file: {path.name}')
        print('-----Processing---------')

        check_existing_result = f"File {file_path.split('/')[-1]} exist!"

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text_from_pdf = ''.join(pages).replace('\n', '')

        my_audio = gTTS(text=text_from_pdf, lang=language, slow=False)
        audio_file_name = Path(file_path).stem
        my_audio.save(f'{audio_file_name}.mp3')

        return f'------File {audio_file_name}.mp3 saved successfully!----------\n'

    return check_existing_result


def main():
    tprint("Program>>PDF>>TO>>MP3.", font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input("Choose, 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()







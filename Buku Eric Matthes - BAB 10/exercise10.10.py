from pathlib import Path

# 1. Menentukan lokasi folder tempat file kode ini berada
folder_skrip = Path(__file__).resolve().parent
jalur_berkas = folder_skrip / 'alice.txt'

# 2. Contoh teks cerita Alice (Program akan otomatis membuat filenya untuk Anda)
teks_cerita = """
Alice was beginning to get very tired of sitting by her sister on the bank, 
and of having nothing to do: once or twice she had peeped into the book her sister 
was reading, but it had no pictures or conversations in it, 'and what is the use 
of a book,' thought Alice 'without pictures or conversations?'
So she was considering in her own mind (as well as she could, for the hot day 
made her feel very sleepy and stupid), whether the pleasure of making a 
daisy-chain would be worth the trouble of getting up and picking the daisies, 
when suddenly a White Rabbit with pink eyes ran close by her.
There was nothing so very remarkable in that; nor did Alice think it so 
very much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear! 
I shall be late!' (when she thought it over afterwards, it occurred to her that 
she ought to have wondered at this, but at the time it all seemed quite natural); 
but when the Rabbit actually took a watch out of its waistcoat-pocket, and 
looked at it, and then hurried on, Alice started to her feet.
"""

# 3. Otomatis membuat dan mengisi file alice.txt jika belum ada
if not jalur_berkas.exists():
    jalur_berkas.write_text(teks_cerita.strip(), encoding='utf-8')

# 4. Fungsi untuk menghitung kata
def count_common_words(jalur, word):
    try:
        contents = jalur.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Berkas tidak ditemukan.")
    else:
        lowercase_text = contents.lower()
        count = lowercase_text.count(word)
        print(f"Kata '{word}' muncul sebanyak: {count} kali.")

# 5. Jalankan penghitungan kata
count_common_words(jalur_berkas, 'the')
count_common_words(jalur_berkas, 'the ')
from pypdf import PdfReader # tämä tuo PdfReader-luokan pypdf-kirjastosta

reader = PdfReader("test.pdf") # tämä lataa pdf-tiedoston

text = "" # tämä silmukka käy läpi kaikki sivut ja hakee niiltä tekstit
for page in reader.pages: # käy läpi kaikki sivut
    text += page.extract_text() + "\n" # hakee tekstin ja lisää rivinvaihdon

print(text[:1000]) # tulostaa ensimmäiset 1000 merkkiä tekstistä


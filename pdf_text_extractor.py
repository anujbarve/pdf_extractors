import re
from pdfminer.high_level import extract_pages,extract_text

text = extract_text("SPOS.pdf")

print(text)
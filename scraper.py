import requests
from bs4 import BeautifulSoup

URL = "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

# Remove unwanted tags
for tag in soup(["script", "style", "nav", "footer", "header", "img", "aside"]):
    tag.decompose()

# Extract text
text = soup.get_text(separator="\n")

# Clean lines
lines = [line.strip() for line in text.splitlines()]
cleaned_text = "\n".join([line for line in lines if line])

# Save text
with open("data/scraped_text.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Website content scraped successfully.")

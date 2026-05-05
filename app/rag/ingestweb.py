import requests
from bs4 import BeautifulSoup
from pathlib import Path


def clean_text(html):
    soup = BeautifulSoup(html, "html.parser")

    # הסרת script ו-style
    for tag in soup(["script", "style"]):
        tag.extract()

    text = soup.get_text(separator="\n")

    # ניקוי שורות ריקות
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    return "\n".join(lines)


def fetch_and_save(url, output_path):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        text = clean_text(response.text)

        # יצירת תיקייה אם לא קיימת
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Saved: {output_path}")

    except Exception as e:
        print(f"Error fetching {url}: {e}")


def ingest_websites(urls, output_folder="data/websites"):
    for i, url in enumerate(urls):
        filename = f"site_{i+1}.txt"
        output_path = f"{output_folder}/{filename}"

        fetch_and_save(url, output_path)


if __name__ == "__main__":
    urls = [
        "https://surmeno.blogspot.com/p/table-of-contents.html",
        # תוסיפי עוד אתרים פה
    ]

    ingest_websites(urls)
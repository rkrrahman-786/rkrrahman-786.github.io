import os
import time
import csv
import argparse
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

URL = "https://josaa.admissions.nic.in/applicant/SeatAllotmentResult/CurrentORCR.aspx"

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def norm_filename(s):
    return "".join(c if c.isalnum() or c in " ._-" else "_" for c in s)[:200]

def scroll_table_until_done(page, table_selector="table"):
    """Scrolls the table until all dynamic rows are loaded."""
    last_count = 0
    stable_rounds = 0
    max_stable = 4
    while stable_rounds < max_stable:
        try:
            table = page.query_selector(table_selector)
            if not table:
                break
            rows = table.query_selector_all("tr")
            count = len(rows)
            if count == last_count:
                stable_rounds += 1
            else:
                stable_rounds = 0
                last_count = count
            page.evaluate("window.scrollBy(0, 1000);")
            time.sleep(0.5)
        except Exception:
            time.sleep(0.5)
    print(f"Loaded {last_count} rows.")

def extract_table_data(page):
    """Extracts table headers and all rows as a list of lists."""
    content = page.content()
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table")
    if not table:
        return [], []

    # headers
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr"):
        cols = [td.get_text(strip=True) for td in tr.find_all("td")]
        if cols:
            rows.append(cols)
    return headers, rows

def main(output_dir):
    ensure_dir(output_dir)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)  # always headed
        page = browser.new_page()
        page.goto(URL, wait_until="networkidle")

        print("=== Manual step ===")
        print("Fill/select any required fields and click 'Search'.")
        input("Press Enter here to start scraping...")

        print("Scrolling table to load all rows...")
        scroll_table_until_done(page)

        headers, rows = extract_table_data(page)
        browser.close()

        if not rows:
            print("No table data found.")
            return

        default_name = "JoSAA_table"
        fname = input(f"Enter CSV filename (without extension) [default: {default_name}]: ").strip() or default_name
        ts = time.strftime("%Y%m%d_%H%M%S")
        out_path = os.path.join(output_dir, f"{fname}_{ts}.csv")

        print(f"Saving CSV to {out_path}...")
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if headers:
                writer.writerow(headers)
            writer.writerows(rows)
        print("Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="downloads", help="Output directory")
    args = parser.parse_args()
    main(args.out)

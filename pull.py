import csv
import requests
from pathlib import Path
from datetime import datetime
from shutil import copyfile


STORE = Path(__file__).parent.absolute() / "data"
STORE.mkdir(parents=True, exist_ok=True)
now = datetime.now()
url = (
    "https://covid.icmr.org.in/testing-facilities?"
    "option=com_hotspots&view=jsonv4&task=gethotspots&hs-language=en-GB&page=1"
    "&per_page=5000&cat=&level=4&ne=43.79634%2C125.305668&sw=-3.741665%2C40.842777"
    "&c=21.975478%2C83.074222&fs=0&offset=0&format=raw"
)

r = requests.get(url)
data = r.json()["items"]
now = now.strftime("%Y-%m-%d")
csv_path = STORE / f"testing-facilities-{now}.csv"
with open(csv_path, "w", newline="") as f:
    keys = data[0].keys()
    writer = csv.DictWriter(f, keys)
    writer.writeheader()
    writer.writerows(data)
copyfile(csv_path, STORE / '../testing-facilities.csv')

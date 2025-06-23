#!/usr/bin/env python3
"""
auto_data_agent.py
~~~~~~~~~~~~~~~~~~

Automated data‑agent voor budget/ startersauto‑advertenties.
Includes a basic Selenium‑based Facebook Marketplace scraper stub.
NOTE: Requires the environment variables FB_EMAIL and FB_PASSWORD to be
set in the GitHub Actions secrets (or locally) and adds Selenium +
webdriver‑manager to requirements.
"""

from __future__ import annotations
import os
import sys
import time
import logging
import datetime as dt
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Callable

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Optional Selenium imports (only used for Facebook Marketplace)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:  # Will be installed in CI
    webdriver = None  # type: ignore

# ──────────────────────────────────────────────────────────────
# CONFIGURATIE
# ──────────────────────────────────────────────────────────────
MODELLEN = [
    "Volkswagen Polo", "Toyota Aygo", "Ford Fiesta", "Kia Picanto",
    "Renault Clio", "Seat Ibiza", "Peugeot 108", "Citroën C1",
    "Opel Corsa", "Hyundai i10", "Peugeot 208", "Ford Focus",
    "Volkswagen Golf", "Kia Rio", "Seat Leon", "Peugeot 207",
    "Peugeot 206", "Fiat 500", "Mini", "Opel Astra",
    "Renault Mégane", "Suzuki Swift", "Volkswagen Up"
]
MAX_BUDGET_EUR: int = 7_500
MIN_BOUWJAAR: int = 2008
MAX_KILOMETERS: int = 160_000
RUN_INTERVAL_HOURS: int = 3

PLATFORMS = [
    "facebook_marketplace"  # Start with FB only; add others later
]

ENABLE_NOTIFICATION: bool = False
WEBHOOK_URL: str | None = None
EMAIL_SETTINGS: Dict[str, str] | None = None

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# ──────────────────────────────────────────────────────────────
# LOGGING
# ──────────────────────────────────────────────────────────────
timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(LOG_DIR, f"run_{timestamp}.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("auto_data_agent")

# ──────────────────────────────────────────────────────────────
# DATACLASS
# ──────────────────────────────────────────────────────────────
@dataclass
class Ad:
    platform: str
    title: str
    model: str
    price: float
    day_value: float
    year: int
    km: int
    url: str
    location: str | None = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

# ──────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ──────────────────────────────────────────────────────────────

def get_day_value(model: str, year: int, km: int) -> float:
    """Dummy day‑value estimate (replace with real source)."""
    basis = 20_000
    leeftijd = max(0, dt.datetime.now().year - year)
    waarde = basis * (0.9 ** leeftijd) - km * 0.02
    return max(waarde, 500)


def price_below_dayvalue(price: float, day_value: float) -> bool:
    return price < day_value


def unique_filename(prefix: str, ext: str = ".xlsx") -> str:
    return f"{prefix}_{dt.datetime.now():%Y%m%d_%H%M%S}{ext}"

# ──────────────────────────────────────────────────────────────
# SCRAPERS
# ──────────────────────────────────────────────────────────────

def scrape_facebook_marketplace() -> List[Ad]:
    """Basic Selenium scraper stub for Facebook Marketplace."""
    logger.info("Scraping Facebook Marketplace…")

    email = os.getenv("FB_EMAIL")
    password = os.getenv("FB_PASSWORD")
    if not email or not password:
        logger.warning("FB_EMAIL / FB_PASSWORD not set; skipping FB scrape")
        return []

    if webdriver is None:
        logger.error("Selenium not available; install selenium & webdriver‑manager")
        return []

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:
        driver.get("https://www.facebook.com/login")
        time.sleep(2)
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "pass").send_keys(password)
        driver.find_element(By.NAME, "login").click()
        time.sleep(5)

        driver.get("https://www.facebook.com/marketplace/category/vehicles")
        time.sleep(5)

        ads: List[Ad] = []
        items = driver.find_elements(By.XPATH, "//a[contains(@href, '/marketplace/item/')]")
        seen = set()
        for item in items[:30]:
            url = item.get_attribute("href")
            if url in seen:
                continue
            seen.add(url)
            title = item.text.split("\n")[0]
            price = 0.0
            try:
                price_text = item.find_element(By.XPATH, ".//span[contains(text(),'€')]").text
                price = float(''.join(ch for ch in price_text if ch.isdigit()))
            except Exception:
                pass
            ads.append(
                Ad(
                    platform="facebook_marketplace",
                    title=title,
                    model=title,
                    price=price,
                    day_value=0,
                    year=0,
                    km=0,
                    url=url,
                )
            )
        logger.info("Found %d FB ads", len(ads))
        return ads
    finally:
        driver.quit()

# Map
SCRAPER_MAP: Dict[str, Callable[[], List[Ad]]] = {
    "facebook_marketplace": scrape_facebook_marketplace,
}

# ──────────────────────────────────────────────────────────────
# MAIN WORKFLOW
# ──────────────────────────────────────────────────────────────

def run_once() -> None:
    logger.info("Start run – platforms: %s", ", ".join(PLATFORMS))
    found: List[Ad] = []
    for p in PLATFORMS:
        scraper = SCRAPER_MAP.get(p)
        if scraper:
            try:
                found.extend(scraper())
            except Exception as exc:
                logger.exception("Scraper %s failed: %s", p, exc)
    logger.info("Total ads scraped: %d", len(found))

    # Enrich & filter
    selected = []
    for ad in found:
        ad.day_value = get_day_value(ad.model, ad.year, ad.km)
        if price_below_dayvalue(ad.price, ad.day_value):
            selected.append(ad.to_dict())

    logger.info("Ads under day‑value: %d", len(selected))
    if selected:
        df = pd.DataFrame(selected)
        out_path = os.path.join(OUTPUT_DIR, unique_filename("fb_deals"))
        df.to_excel(out_path, index=False)
        logger.info("Saved %s", out_path)


def main() -> None:
    if "--loop" in sys.argv:
        import schedule
        import time as _t
        schedule.every(RUN_INTERVAL_HOURS).hours.do(run_once)
        while True:
            schedule.run_pending()
            _t.sleep(60)
    else:
        run_once()

if __name__ == "__main__":
    main()

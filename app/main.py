from sources.handler import *

if __name__ == "__main__":
    new_scraper = Handler()

    new_scraper.get_all_name_price("iphone 13 pro max", 2, "electronics")

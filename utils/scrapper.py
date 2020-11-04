import bs4
import requests
URL_BASE = "https://www.starlist.pro"
URL_BRAWLERS = URL_BASE + "/brawlers/"

SPEED_VALUES = {
    "Very Slow": -1,
    "Slow": 0,
    "Normal": 1,
    "Fast": 2,
    "Very Fast": 3,
}


def get_brawlers():
    response = requests.get(URL_BRAWLERS)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    brawlers = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if "/brawlers/detail/" in href:
            detail_response = requests.get(URL_BASE + href)
            detail_soup = bs4.BeautifulSoup(detail_response.text,
                                            'html.parser')
            brawler_name = detail_soup.find(
                "h1", {
                    "class": "mr-2 mt-1 mb-1 h2 shadow-normal"
                }).text
            if detail_soup.find("h2", {"class": "rarity1 h6 shadow-normal"}):
                rarity, price = detail_soup.find(
                    "h2", {
                        "class": "rarity1 h6 shadow-normal"
                    }).text.split("\xa0· ")
            elif detail_soup.find("h2", {"class": "rarity2 h5 shadow-normal"}):
                rarity = detail_soup.find("h2", {
                    "class": "rarity2 h5 shadow-normal"
                }).text
                price = 0

            image_url = detail_soup.find("img", {
                "class": "brl-big-ico"
            }).get("src")
            description = detail_soup.find(
                "p", {
                    "class": "mb-0 pl-2 pr-2 pb-2 shadow-normal"
                }).text
            health = detail_soup.find("td").text
            speed = "Normal"
            for tr in detail_soup.find_all("tr"):
                if tr.find("th").text == "Speed":
                    speed = tr.find("td").text
            brawlers.append({
                "name": brawler_name,
                "description": description,
                "avatar": image_url,
                "cost": price,
                "rarity": rarity,
                "health": health,
                "speed": SPEED_VALUES[speed]
            })

    return brawlers


if __name__ == "__main__":
    brawlers = get_brawlers()
    print(brawlers)
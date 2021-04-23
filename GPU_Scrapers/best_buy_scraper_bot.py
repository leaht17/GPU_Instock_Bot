from bs4 import BeautifulSoup
import requests
import time
import json

URLS = ["https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",
    "https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434",
    "https://www.bestbuy.com/site/pny-geforce-gt1030-2gb-pci-e-3-0-graphics-card-black/5901353.p?skuId=5901353",
    "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-ti-ftw3-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6444444.p?skuId=6444444",
    "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402",
    "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3070-ventus-3x-oc-bv-8gb-gddr6-pci-express-4-0-graphics-card/6438278.p?skuId=6438278",
    "https://www.bestbuy.com/site/pny-geforce-gt-710-2gb-pci-express-2-0-graphics-card-black/5092306.p?skuId=5092306",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-aorus-master-8gb-gddr6-pci-express-4-0-graphics-card/6439384.p?skuId=6439384",
    "https://www.bestbuy.com/site/asus-nvidia-geforce-tuf-rtx3070-8gb-gddr6-pci-express-4-0-graphics-card-black/6439128.p?skuId=6439128",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-gaming-oc-12gb-gddr6-pci-express-4-0-graphics-card/6454688.p?skuId=6454688",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439299.p?skuId=6439299",
    "https://www.bestbuy.com/site/asus-nvidia-geforce-rog-strix-rtx3070-8gb-gddr6-pci-express-4-0-graphics-card-black/6439127.p?skuId=6439127",
    "https://www.bestbuy.com/site/pny-xlr8-gaming-single-fan-nvidia-geforce-gtx-1660-super-overclocked-edition-6gb-gddr6-pci-express-3-0-graphics-card-black/6407309.p?skuId=6407309",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6-pci-express-4-0-graphics-card/6434198.p?skuId=6434198",
    "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-xc-gaming-12gb-gddr6-pci-express-4-0-graphics-card/6454329.p?skuId=6454329",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-gaming-oc-8gb-gddr6-pci-express-4-0-graphics-card/6437909.p?skuId=6437909",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400",
    "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3090-ventus-3x-24g-oc-bv-24gb-gddr6x-pci-express-4-0-graphics-card-black-silver/6430215.p?skuId=6430215",
    "https://www.bestbuy.com/site/evga-super-sc-ultra-gaming-nvidia-geforce-gtx-1650-super-4gb-gddr6-pci-express-3-0-graphics-card-black-silver/6412939.p?skuId=6412939",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-vision-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6436219.p?skuId=6436219",
    "https://www.bestbuy.com/site/msi-meg-z490-ace-socket-lga1200-usb-c-gen2-intel-motherboard/6412365.p?skuId=6412365",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-gaming-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6430620.p?skuId=6430620",
    "https://www.bestbuy.com/site/asus-nvidia-geforce-gtx-1660-super-oc-edition-6gb-gddr6-pci-express-3-0-graphics-card-black-gray/6405063.p?skuId=6405063",
    "https://www.bestbuy.com/site/msi-nvidia-geforce-gtx-1650-super-4gb-gddr6-pci-express-3-0-graphics-card-black-gray/6397798.p?skuId=6397798",
    "https://www.bestbuy.com/site/msi-geforce-gtx-1660-ti-gaming-x-6gb-gddr6-pci-express-3-0-graphics-card/6330461.p?skuId=6330461",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-black-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439300.p?skuId=6439300",
    "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-xc-gaming-12gb-gddr6-pci-express-4-0-graphics-card/6454328.p?skuId=6454328",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436196.p?skuId=6436196",
    "https://www.bestbuy.com/site/msi-mpg-z490-gaming-carbon-wifi-socket-lga1200-usb-c-gen2-intel-motherboard/6412363.p?skuId=6412363",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3070-ftw3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439301.p?skuId=6439301",
    "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3060-ti-ventus-2x-oc-bv-8gb-gddr6-pci-express-4-0-graphics-card-black/6441172.p?skuId=6441172",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-aorus-master-10gb-gddr6x-pci-express-4-0-graphics-card/6436223.p?skuId=6436223",
    "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3080-ventus-3x-10g-oc-bv-gddr6x-pci-express-4-0-graphic-card-black-silver/6430175.p?skuId=6430175",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3090-ftw3-gaming-24gb-gddr6-pci-express-4-0-graphics-card/6436193.p?skuId=6436193",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-eagle-8gb-gddr6-pci-express-4-0-graphics-card/6437912.p?skuId=6437912",
    "https://www.bestbuy.com/site/nvidia-geforce-rtx-nvlink-bridge-for-3090-cards-space-gray/6441554.p?skuId=6441554",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1650-4gb-gddr5-pci-express-3-0-graphics-card-black-gray/6409179.p?skuId=6409179",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1660-super-oc-edition-6gb-gddr6-pci-express-3-0-graphics-card-black/6409171.p?skuId=6409171",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-black-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432399.p?skuId=6432399",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1660-ti-6gb-gddr6-pci-express-3-0-graphics-card-black-gray/6409180.p?skuId=6409180",
    "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-ti-ftw3-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6444449.p?skuId=6444449",
    "https://www.bestbuy.com/site/evga-sc-ultra-gaming-nvidia-geforce-gtx-1660-ti-6gb-gddr6-pci-express-3-0-graphics-card-black-gray/6373500.p?skuId=6373500",
    "https://www.bestbuy.com/site/asus-dual-geforce-rtx-2060-oc-edition-evo-6gb-gddr6-pci-express-3-0-graphic-card/6439463.p?skuId=6439463",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3090-ftw3-ultra-gaming-24gb-gddr6-pci-express-4-0-graphics-card/6436192.p?skuId=6436192",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-vision-oc-8gb-gddr6-pci-express-4-0-graphics-card/6439385.p?skuId=6439385",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3090-aorus-master-24gb-gddr6x-pci-express-4-0-graphics-card/6437910.p?skuId=6437910",
    "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-ti-xc-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6444445.p?skuId=6444445",
    "https://www.bestbuy.com/site/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432658.p?skuId=6432658",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-eagle-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6430621.p?skuId=6430621",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-ti-gaming-oc-8g-gddr6-pci-express-4-0-graphics-card-black/6442484.p?skuId=6442484",
    "https://www.bestbuy.com/site/gigabyte-geforce-rtx-3090-eagle-oc-24g-gddr6x-pci-express-4-0-graphics-card-black/6430624.p?skuId=6430624",
    "https://www.bestbuy.com/site/pny-nvidia-geforce-rtx-3060-12gb-xlr8-gaming-revel-epic-x-rgb-single-fan-graphics-card/6454318.p?skuId=6454318",
    "https://www.bestbuy.com/site/pny-geforce-rtx-3060ti8gb-uprising-dual-fan-graphics-card/6446660.p?skuId=6446660",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1650-super-oc-edition-4gb-gddr6-pci-express-3-0-graphics-card-black-gray/6409188.p?skuId=6409188",
    "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3060-ventus-3x-12g-oc-12gb-gddr6-pci-express-4-0-graphics-card-black/6452940.p?skuId=6452940",
    "https://www.bestbuy.com/site/pny-geforce-rtx-3090-24gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432657.p?skuId=6432657",
    "https://www.bestbuy.com/site/pny-geforce-rtx-3070-8gb-dual-fan-graphics-card/6432654.p?skuId=6432654",
    "https://www.bestbuy.com/site/pny-geforce-rtx-3070-8gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432653.p?skuId=6432653",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3090-gaming-oc-24gb-gddr6x-pci-express-4-0-graphics-card/6430623.p?skuId=6430623",
    "https://www.bestbuy.com/site/pny-geforce-rtx-3090-24gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432656.p?skuId=6432656",
    "https://www.bestbuy.com/site/pny-nvidia-geforce-rtx-3060-12gb-xlr8-gaming-revel-epic-x-rgb-dual-fan-graphics-card/6454319.p?skuId=6454319",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-ti-eagle-oc-8g-gddr6-pci-express-4-0-graphics-card-black/6442485.p?skuId=6442485",
    "https://www.bestbuy.com/site/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432655.p?skuId=6432655",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1660-oc-edition-6gb-gddr5-pci-express-3-0-graphics-card-black/6409181.p?skuId=6409181",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436194.p?skuId=6436194",
    "https://www.bestbuy.com/site/pny-nvidia-geforce-gtx-1060-6gb-gddr5-pci-express-3-0-graphics-card-black/5507806.p?skuId=5507806",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3090-vision-24g-gddr6-pci-express-4-0-graphics-card/6445108.p?skuId=6445108",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gt-1030-2gb-gddr5-pci-express-3-0-graphics-card-black/6409183.p?skuId=6409183",
    "https://www.bestbuy.com/site/evga-geforce-rtx-2080-xc-gaming-8gb-gddr6-pci-express-3-0-graphics-card-with-dual-hdb-fans-rgb-led/6290681.p?skuId=6290681",
    "https://www.bestbuy.com/site/evga-geforce-gt-710-2gb-single-slot-dual-dvi-graphics-card-black/5597203.p?skuId=5597203"
]

#returns the page request
def get_page(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    return requests.get(url, headers=headers)

# Used to check if the url is valid
# Returns true is status code is 200, false otherwise
def is_valid_url(status_code):
    return str(status_code) == "200"

#returns whether or not the given product is in stock
def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    product_inventory = soup.findAll("div", {"class": "fulfillment-add-to-cart-button"})
    product_status = next(product_inventory[0].find('button').descendants)
    return product_status != "Sold Out" and product_status != "Coming Soon" and product_status != "Check Stores"

# Lets the user know whether the item for the provided newegg url is in stock
# Returns "In stock or out of stock"
def check_inventory(page_html, url):
    if check_item_in_stock(page_html):
        print("In stock: " + url)
    else:
        print("Out of stock: " + url)


#Goes through the list of URL's and prints out whether they're in stock or not or if its an invalid 
# url let the user know
def check_urls():
    go = 1
    while go == 1:
        for site in URLS:
            page = get_page(site)

            if (is_valid_url(page.status_code)):
                check_inventory(page.content, site)
            else:
                print(site + " is not valid")
            print()
        time.sleep(5)

def main():
    check_urls()

if __name__ == "__main__":
    main()


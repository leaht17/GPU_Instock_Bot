import requests
import time
from bs4 import BeautifulSoup

# List of the Nvidia graphics card URLs
URLS = [ 
    "https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060eagle-12gd/p/N82E16814932399?Description=3060&cm_re=3060-_-14-932-399-_-Product",
    "https://www.newegg.com/asus-geforce-rtx-3060-dual-rtx3060-12g/p/N82E16814126493?Item=N82E16814126493",
    "https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-2x-12g/p/N82E16814137638?Item=N82E16814137638",
    "https://www.newegg.com/evga-geforce-rtx-3060-12g-p5-3655-kr/p/N82E16814487538?Item=N82E16814487538&quicklink=true",
    "https://www.newegg.com/gigabyte-geforce-rtx-3060-ti-gv-n306teagle-8gd/p/N82E16814932379?item=N82E16814932379",
    "https://www.newegg.com/evga-geforce-rtx-3060-12g-p5-3657-kr/p/N82E16814487539?Item=N82E16814487539",
    "https://www.newegg.com/zotac-geforce-rtx-3060-ti-zt-a30610e-10m/p/N82E16814500506?item=N82E16814500506",
    "https://www.newegg.com/gigabyte-geforce-rtx-3060-ti-gv-n306tgamingoc-pro-8gd/p/N82E16814932376?item=N82E16814932376",
    "https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060eagle-oc-12gd/p/N82E16814932403?Item=N82E16814932403",
    "https://www.newegg.com/evga-geforce-rtx-3060-ti-08g-p5-3663-kr/p/N82E16814487535?item=N82E16814487535",
    "https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060gaming-oc-12gd/p/N82E16814932402?Item=N82E16814932402",
    "https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-2x-12g-oc/p/N82E16814137632?Item=N82E16814137632",
    "https://www.newegg.com/asus-geforce-rtx-3060-ti-dual-rtx3060ti-8g/p/N82E16814126480?item=N82E16814126480",
    "https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3751-kr/p/N82E16814487528?item=N82E16814487528",
    "https://www.newegg.com/gigabyte-geforce-rtx-3060-ti-gv-n306tgaming-oc-8gd/p/N82E16814932377?item=N82E16814932377",
    "https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060vision-oc-12gd/p/N82E16814932401?Item=N82E16814932401",
    "https://www.newegg.com/asus-geforce-rtx-3060-tuf-rtx3060-o12g-gaming/p/N82E16814126491?Item=N82E16814126491&quicklink=true",
    "https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-3x-12g-oc/p/N82E16814137631?Item=N82E16814137631",
    "https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070eagle-8gd/p/N82E16814932344?item=N82E16814932344",
    "https://www.newegg.com/asus-geforce-rtx-3060-ti-dual-rtx3060ti-o8g/p/N82E16814126468?item=N82E16814126468",
    "https://www.newegg.com/evga-geforce-rtx-3060-ti-08g-p5-3667-kr/p/N82E16814487537?item=N82E16814487537",
    "https://www.newegg.com/asus-geforce-rtx-3060-rog-strix-rtx3060-o12g-gaming/p/N82E16814126492?Item=N82E16814126492&quicklink=true",
    "https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3753-kr/p/N82E16814487529?item=N82E16814487529",
    "https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3765-kr/p/N82E16814487531?item=N82E16814487531",
    "https://www.newegg.com/asus-geforce-rtx-3060-ti-ko-rtx3060ti-o8g-gaming/p/N82E16814126474?item=N82E16814126474",
    "https://www.newegg.com/msi-geforce-rtx-3060-ti-rtx-3060-ti-ventus-2x-oc/p/N82E16814137612?item=N82E16814137612",
    "https://www.newegg.com/asus-geforce-rtx-3060-ti-tuf-rtx3060ti-o8g-gaming/p/N82E16814126471?item=N82E16814126471",
    "https://www.newegg.com/asus-geforce-rtx-3070-dual-rtx3070-8g/p/N82E16814126460?item=N82E16814126460",
    "https://www.newegg.com/zotac-geforce-rtx-3060-ti-zt-a30610h-10m/p/N82E16814500507?item=N82E16814500507",
    "https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3755-kr/p/N82E16814487530?item=N82E16814487530",
    "https://www.newegg.com/gigabyte-geforce-rtx-3060-ti-gv-n306taorus-m-8gd/p/N82E16814932375?item=N82E16814932375",
    "https://www.newegg.com/msi-geforce-rtx-3060-ti-rtx-3060-ti-gaming-x-trio/p/N82E16814137611?item=N82E16814137611",
    "https://www.newegg.com/zotac-geforce-rtx-3070-zt-a30700e-10p/p/N82E16814500501?item=N82E16814500501",
    "https://www.newegg.com/asus-geforce-rtx-3060-ti-rog-strix-rtx3060ti-o8g-gaming/p/N82E16814126470?item=N82E16814126470",
    "https://www.newegg.com/pny-geforce-rtx-3070-vcg30708tfxppb/p/N82E16814133811?item=N82E16814133811",
    "https://www.newegg.com/asus-geforce-rtx-3070-dual-rtx3070-o8g/p/N82E16814126459?item=N82E16814126459",
    "https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3767-kr/p/N82E16814487532?item=N82E16814487532",
    "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g/p/N82E16814137600?item=N82E16814137600",
    "https://www.newegg.com/pny-geforce-rtx-3070-vcg30708dfmpb/p/N82E16814133812?item=N82E16814133812",
    "https://www.newegg.com/msi-geforce-rtx-3070-rtx-3070-ventus-2x-oc/p/N82E16814137602?item=N82E16814137602",
    "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080eagle-oc-10gd/p/N82E16814932330?item=N82E16814932330",
    "https://www.newegg.com/zotac-geforce-rtx-3080-zt-t30800j-10p/p/N82E16814500504?item=N82E16814500504",
    "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3881-kr/p/N82E16814487522?item=N82E16814487522",
    "https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070eagle-oc-8gd/p/N82E16814932343?item=N82E16814932343",
    "https://www.newegg.com/zotac-geforce-rtx-3070-zt-a30700h-10p/p/N82E16814500505?item=N82E16814500505",
    "https://www.newegg.com/msi-geforce-rtx-3070-rtx-3070-ventus-3x-oc/p/N82E16814137601?item=N82E16814137601",
    "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932329?item=N82E16814932329",
    "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3883-kr/p/N82E16814487521?item=N82E16814487521",
    "https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070gaming-oc-8gd/p/N82E16814932342?item=N82E16814932342",
    "https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p/N82E16814126452?item=N82E16814126452",
    "https://www.newegg.com/asus-geforce-rtx-3070-tuf-rtx3070-o8g-gaming/p/N82E16814126461?item=N82E16814126461",
    "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g-oc/p/N82E16814137598?item=N82E16814137598",
    "https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070vision-oc-8gd/p/N82E16814932360?item=N82E16814932360",
    "https://www.newegg.com/msi-geforce-rtx-3070-rtx-3070-gaming-x-trio/p/N82E16814137603?item=N82E16814137603",
    "https://www.newegg.com/asus-geforce-rtx-3070-rog-strix-rtx3070-o8g-gaming/p/N82E16814126458?item=N82E16814126458",
    "https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070aorus-m-8gd/p/N82E16814932359?item=N82E16814932359",
    "https://www.newegg.com/zotac-geforce-rtx-3080-zt-a30800d-10p/p/N82E16814500502?item=N82E16814500502",
    "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-gaming-x-trio-10g/p/N82E16814137597?item=N82E16814137597",
    "https://www.newegg.com/zotac-geforce-rtx-3090-zt-a30900d-10p/p/N82E16814500503?item=N82E16814500503",
    "https://www.newegg.com/msi-geforce-rtx-3090-rtx-3090-ventus-3x-24g/p/N82E16814137599?item=N82E16814137599",
    "https://www.newegg.com/evga-geforce-rtx-3090-24g-p5-3973-kr/p/N82E16814487523?item=N82E16814487523",
    "https://www.newegg.com/gigabyte-geforce-rtx-3090-gv-n3090eagle-oc-24gd/p/N82E16814932328?item=N82E16814932328",
    "https://www.newegg.com/gigabyte-geforce-rtx-3090-gv-n3090gaming-oc-24gd/p/N82E16814932327?item=N82E16814932327",
    "https://www.newegg.com/evga-geforce-rtx-3090-24g-p5-3985-kr/p/N82E16814487525?item=N82E16814487525",
    "https://www.newegg.com/evga-geforce-rtx-3090-24g-p5-3975-kr/p/N82E16814487524?item=N82E16814487524",
    "https://www.newegg.com/evga-geforce-rtx-3090-24g-p5-3987-kr/p/N82E16814487526?item=N82E16814487526",
    "https://www.newegg.com/asus-geforce-rtx-3090-tuf-rtx3090-24g-gaming/p/N82E16814126455?item=N82E16814126455",
    "https://www.newegg.com/msi-geforce-rtx-3090-rtx-3090-ventus-3x-24g-oc/p/N82E16814137596?item=N82E16814137596",
    "https://www.newegg.com/msi-geforce-rtx-3090-rtx-3090-gaming-x-trio-24g/p/N82E16814137595?item=N82E16814137595",
    "https://www.newegg.com/asus-geforce-rtx-3090-rog-strix-rtx3090-o24g-gaming/p/N82E16814126456?item=N82E16814126456",
]


# def get_page_html(url):
#     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
#     page = requests.get(url, headers=headers)
#     print(page.status_code)
#     return page.content

# Returns the page request
def get_page(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    return requests.get(url, headers=headers)

# Used to check if the url is valid
# Returns true is status code is 200, false otherwise
def is_valid_url(status_code):
    print("request status code is " + str(status_code))
    return str(status_code) == "200"

# 
def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    print(soup)
    product_inventory = soup.findAll("div", {"class": "product-inventory"})
    inventory_status = next(product_inventory[0].find('strong').descendants)
    print(inventory_status)
    return str(inventory_status) == "In stock."

# Lets the user know whether the item for the provided newegg url is in stock
# Returns "In stock or out of stock"
def check_inventory(page_html, url):
    if check_item_in_stock(page_html):
        print("In stock: " + url)
    else:
        print("Out of stock: " + url)

# Scans through a list of newegg product urls and checks the product inventory for each of those items
def  check_urls():
    page = get_page(URLS[17])
    # cnt = 0
    # len_of_urls = len(URLS)
    # print(len_of_urls)
    # print("\n---------------------------------")
    # while(True):
        
    #     page = get_page(URLS[cnt])

    #     if (is_valid_url(page.status_code)):
    #         print("url is valid")
    #         check_inventory(page.content, URLS[cnt])
    #     else:
    #         print(URLS[cnt] + " is not a valid URL")
        
    #     print("\n---------------------------------")
        
    #     if cnt != len_of_urls:
    #         cnt += 1
    #     else:
    #         cnt = 0
    #     print(cnt)
    #     time.sleep(1)

    check_inventory(page.content, URLS[17])


if __name__ == '__main__':
    check_urls()

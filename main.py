from requests import get
from re import search

print("Checking Gigabyte Website...")

webdata = get("https://www.gigabyte.com/MicroSite/512/download.html")
RGB_Fusion_Link = search(r"https://download\.gigabyte\.com/FileList/Utility/mb_utility_rgb_fusion.*?\.zip", webdata.text)

if RGB_Fusion_Link:
    with open("links.txt", 'r+') as f:
        readLines = f.readlines()
        if not readLines or readLines[-1].strip() != RGB_Fusion_Link[0]:
            print("Found new link:", RGB_Fusion_Link[0])
            f.write(RGB_Fusion_Link[0] + '\n')
        else:
            print("File already up to date.")
else:
    print("Could not find link")

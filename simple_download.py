import urllib.request
url = "https://www.tees.ac.uk/Images/sections/common/template/TeessideUniversity2b.png"
file_name = "./tees_logo.png"
urllib.request.urlretrieve(url, file_name)

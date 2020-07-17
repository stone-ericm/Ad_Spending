import requests, zipfile, os

url  = "https://storage.googleapis.com/transparencyreport/google-political-ads-transparency-bundle.zip"
r = requests.get(url, allow_redirects=True)

open("google-political-ads-transparency-bundle.zip", 'wb').write(r.content)

with zipfile.ZipFile("google-political-ads-transparency-bundle.zip", 'r') as zip_ref:
	# print(zip_ref.namelist())
	zip_ref.extract("google-political-ads-transparency-bundle/google-political-ads-creative-stats.csv", ".")

os.rename("./google-political-ads-transparency-bundle/google-political-ads-creative-stats.csv", "./google-political-ads-creative-stats.csv")
os.remove("google-political-ads-transparency-bundle.zip")
os.rmdir("./google-political-ads-transparency-bundle")
	# google-political-ads-transparency-bundle\google-political-ads-creative-stats.csv
import webbrowser, os, sys

url = "http://live-icy.gslb01.dr.dk/A/A05H.mp3"

chrome_path = '/usr/lib/chromium-browser/chromium-browser'
webbrowser.get(chrome_path).open(url)

print("Playing: P3")


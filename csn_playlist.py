from bs4 import BeautifulSoup
import requests
import re
import sys
import progress.bar
import time

# Variables
stt = time.time()
pattern = re.compile(
    "https:\/\/chiasenhac.vn\/playlist\/([\w-]{1,255})?([~\w\d=]+).html")
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
try:
    url = str(sys.argv[1])
except:
    url = str(input('Link of playlist? '))

# Sanitize input
while True:
    match = re.match(pattern, url)
    if match:
        print("Now getting download links of playlist: {}".format(
            match.group(1).replace('-', ' ')))

        # Start scrapping first song of the playlist
        r = requests.get(url + '?playlist=1', headers=headers)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        # Get maxPlaylist number
        maxPlaylist = int(
            re.search(r'maxPlaylist = *(\d+)', str(soup)).group(1))

        # Create progress bar
        pbar = progress.bar.Bar('Getting links', max=maxPlaylist)
        pbar.next()
        break
    else:
        url = str(input('Incorrect URL. Try again: '))


def get_download_info(soup):
    content = ''
    # Prepare download info
    download_info = soup.find_all('div', class_="form-group download_status")
    quality_available = download_info[0].find_all('label')
    highest_quality = quality_available[len(quality_available) - 2]
    # Prepare return info
    L = highest_quality.find_all('span')
    content += "{} - {} ({} -{})\n".format(soup.find(
        'p', class_='text-pink mb-2').text, soup.find('h6').text, L[1].text, L[2].text)
    content += str(highest_quality.find('input').get('value')) + '\n'
    return content


scrap = get_download_info(soup)

# Start scrapping the rest of the playlist
for i in range(1, maxPlaylist):
    r = requests.get(url + '?playlist={}'.format(i + 1), headers=headers)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    scrap += get_download_info(soup)
    pbar.next()

with open('download_links_{}.txt'.format(match.group(1)), 'w', encoding='utf-8') as file:
    file.write(scrap)
    file.close()

print('\nCompleted')
hours, rem = divmod((time.time() - stt), 3600)
minutes, sec = divmod(rem, 60)
print("Elapsed Time:\n{:0>2}:{:0>2}:{:05.2f}".format(
    int(hours), int(minutes), sec))

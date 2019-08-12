
# csn-get-download-links      
Simple script to scrap all the download links of chiasenhac.vn playlist in highest possible quality.

## Dependencies 
- [python 3.7.2+](https://python.org)
- [requests](http://docs.python-requests.org/en/master/)
- [bs4 (beautiful soup)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Usage
### Install dependencies
    pip install -r requirements.txt
### Actually using the script
    python csn_playlist.py url
It will then spits out a text file in the same folder with all the links in it.<br/>
Import the text file in your favourite download manager. That's it.

## FAQ
Q: There is already someone made this project.<br/>
A: Ughhhh, want to write my own bad code. Don't judge me.

Q: I need to scrap album's download links!<br/>
A: Yeah I only support playlist scrap for now. May implement album scrap later, idk.

Q: Let me choose the quality!<br/>
A: It's already 2019 (or whatever year you are on right now) dude. HDDs are so cheap now. FLAC lossless or bust.

Q: Why don't the script download the songs?<br/>
A: I can implement that, but my own implementation of a download manager would suck. You should just import the *.txt file into a real download manager instead, it will be much faster.

Q: It doesn't work!<br/>
A: Works for me as of August 2019. Create an issue and maybe I will look into it. Or just go find another script, this script sucks anyway.


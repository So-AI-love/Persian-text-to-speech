# Ganjoor site Persian Audio and text scraper

You can use [docker server][1] with this address:

https://labs.play-with-docker.com/

Then write these commands in docker terminal:

[![enter image description here][2]][2]
```
apk add py-pip libxml2-dev libxslt-dev   py3-lxml zip wget 

#apk add libxml2-dev libxslt1-dev zlib1g-dev py3-pip

pip install gevent --pre
pip install auto-py-to-exe
pip install bs4 scrapy requests tldextract

git clone https://github.com/So-AI-love/Persian-text-to-speech/
cd Persian-text-to-speech/Ganjoor_scraper

mkdir ganjor_Audio_text_files
cp -r ganjoor_link_scraper.py ./ganjor_Audio_text_files/
cd ganjor_Audio_text_files
python3 ganjoor_link_scraper1.py --url  "https://ganjoor.net" --layers_dept1 1000 --layers_dept2 20 --layers_dept3 1


zip -r  ganjor_Audio_text_files.zip ./*
mv  ganjor_Audio_text_files.zip ganjor_Audio_text_files.zip1
#wget --method PUT --body-file=ganjor_Audio_text_files.zip1 https://transfer.sh/ganjor_Audio_text_files.zip1 -O - -nv


curl -H "Max-Downloads: 1" -H "Max-Days: 5" --upload-file ./ganjor_Audio_text_files.zip1 https://transfer.sh/ganjor_Audio_text_files.zip1 


```
It will automatically scrap the '--url' with dept layer of :

```
--url  "https://ganjoor.net"
--layers_dept1 1000 
--layers_dept2 20 
--layers_dept3 1
```
And Upload its data to `https://transfer.sh/!!!/ganjor_Audio_text_files.zip1 `, which `!!!` text would be declared by the output of curl function

Or all will be done, By running these commands in Docker server:

```
git clone https://github.com/So-AI-love/Persian-text-to-speech/
cd Persian-text-to-speech/Ganjoor_scraper
chmod -755 ./Docker_ganjoor_scraper.sh
./Docker_ganjoor_scraper.sh

```
By these defaults:

```
--url "https://ganjoor.net"
--layers_dept1 1000 
--layers_dept2 20 
--layers_dept3 1
```

  [1]: https://labs.play-with-docker.com/
  [2]: https://i.stack.imgur.com/aYqdN.png

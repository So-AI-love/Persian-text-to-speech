## This is reltaed to this question:

[https://stackoverflow.com/questions/63941441/web-scraping-the-audio-and-related-text-form-ganjoor-site-by-colab-as-persian-sp](https://stackoverflow.com/questions/63941441/web-scraping-the-audio-and-related-text-form-ganjoor-site-by-colab-as-persian-sp)

I have tried to gather some audio form [ganjoor site][1] to gather Audio files with its texts like those contents that is reading by ... shown below:

![enter image description here][2]

By using the google colab, so i have tried different method via this coalb :

https://colab.research.google.com/drive/1ntSbqv6iSrNt2F8eyWTvao5ED9Ot0szi?usp=sharing

And I get this kind of errors that you can see at above colab page:

![enter image description here][3]
```
/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:29: DeprecationWarning: use options instead of chrome_options
---------------------------------------------------------------------------
WebDriverException                        Traceback (most recent call last)
<ipython-input-27-c4b1e303b5e7> in <module>()
     28 
     29 wd = webdriver.Chrome('chromedriver', chrome_options=options)
---> 30 wd.get(url)
     31 print(wd.page_source)  # re

2 frames
/usr/local/lib/python3.6/dist-packages/selenium/webdriver/remote/errorhandler.py in check_response(self, response)
    240                 alert_text = value['alert'].get('text')
    241             raise exception_class(message, screen, stacktrace, alert_text)
--> 242         raise exception_class(message, screen, stacktrace)
    243 
    244     def _value_or_default(self, obj, key, default):

WebDriverException: Message: unknown error: net::ERR_CONNECTION_TIMED_OUT
  (Session info: headless chrome=85.0.4183.83)
```
or
![enter image description here][4]
```
onnectionError: HTTPSConnectionPool(host='ganjoor.net', port=443): Max retries exceeded with url: /hafez/ghazal/sh1/ (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f6e23c5c8d0>: Failed to establish a new connection: [Errno 110] Connection timed out',))
```

So my guess is that this kind of web-scraping needs some proper agent header setting or using some proxy in the setting, and I don't know which header is proper and or what proxy sites or free vpn provider is exist and ...

****Update:****

According to answer of **@baduker**, it seams that there is some problem with colab to connect the https://ganjoor.net site and its showing that error again (the **@baduker** codes added to the [related GitHub colab notebooks page][5]:

[![enter image description here][6]][6]

I would be very grateful if you could scrap one audio with its related texts from the ganjoor site, as one example.

Thanks.


  [1]: https://ganjoor.net/hafez/ghazal/sh1/
  [2]: https://i.stack.imgur.com/rV1Eg.png
  [3]: https://i.stack.imgur.com/Yjn3c.png
  [4]: https://i.stack.imgur.com/ja0qW.png
  [5]: https://github.com/So-AI-love/Persian-text-to-speech/blob/master/Webscraping_ganjor_audio.ipynb
  [6]: https://i.stack.imgur.com/FbM8l.png

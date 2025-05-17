
import sqlite3
from PIL import Image
from fake_useragent import UserAgent
import requests
import zlib
import io
import os


class imageCache:

    def __init__(self):
        try:
            os.makedirs("./Databases/")
        except FileExistsError:
        # directory already exists
            pass

        self.imageCache = sqlite3.connect("./Databases/imageCache.sqlite")
        self.imageCache.execute("""CREATE TABLE IF NOT EXISTS "cache" (
	                            "url"	TEXT NOT NULL UNIQUE,
	                            "imageData"	BLOB NOT NULL,
	                            PRIMARY KEY("url")
                                ); """)

    def getImage(self, imageURL):
        imageBlob = self.imageCache.execute("SELECT imageData FROM cache WHERE url = ?", [imageURL]).fetchone()

        if not imageBlob:
            #print("Not found, downloading image")
            #Digikey will happily let you use their api with whatever, 
            #but the moment you want a preview image, they go "NOOO YOU CANT USE A WEV SCARBAPER"
            #I don't care though, fake the user agent.
            ua = UserAgent()
            headers = {'User-Agent':str(ua.chrome)}

            downloadedImage = requests.get(imageURL, headers=headers, stream=True)

            #This is bad, but PIL will complain for no reason if i dont write the file first...
            tempFileName = str(zlib.crc32(bytes(imageURL, "utf-8")))
            with open(tempFileName, "wb") as f:
                f.write(downloadedImage.content)

            imageAsPNG = None
            im = Image.open(tempFileName)
            with io.BytesIO() as fakeThing:
                im.save(fakeThing, "PNG")
                imageAsPNG = fakeThing.getvalue()
            
            os.remove(tempFileName)

            #Insert the converted image into the sql database (finally)
            self.imageCache.execute("INSERT INTO cache (url, imageData) VALUES(?, ?)", [imageURL, sqlite3.Binary(imageAsPNG)]  )
            self.imageCache.commit()

            imageBlob = self.imageCache.execute("SELECT imageData FROM cache WHERE url = ?", [imageURL]).fetchone()

        #Im using fetchone in what scenario would it return more then one item??
        return imageBlob[0]

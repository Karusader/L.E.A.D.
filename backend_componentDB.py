
import sqlite3
import os



class componentDB:
    def __init__(self):
        try:
            os.makedirs("./Databases/")
        except FileExistsError:
        # directory already exists
            pass
        self.componentDB = sqlite3.connect("./Databases/componentDB.sqlite")
        self.componentDB.execute(
            """CREATE TABLE IF NOT EXISTS "partInfo" (
	        "part_number"	TEXT NOT NULL UNIQUE,
	        "manufacturer_number"	TEXT UNIQUE,
	        "price"	INTEGER,
	        "description"	TEXT,
	        "detailed_description"	TEXT,
	        "type"	TEXT,
	        "photo_url"	TEXT,
	        "datasheet_url"	TEXT,
	        "product_url"	TEXT,
	        "part_status"	TEXT,
	        PRIMARY KEY("part_number")
        );""")
        self.componentDB.execute("""
            CREATE TABLE IF NOT EXISTS "partMetadata" (
	        "part_number"	TEXT NOT NULL UNIQUE,
	        "location"	TEXT NOT NULL,
	        "part_count"	INTEGER NOT NULL,
	        "low_part_count"	INTEGER NOT NULL,
	        PRIMARY KEY("part_number")
        );""")

        def add_component(self, partInfo, partMetadata):
            pass
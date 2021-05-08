#Setting up the example db

import sqlite3

conn = sqlite3.connect('image_repo.db')
c = conn.cursor()

c.execute("""CREATE TABLE images (
			metadata text,
			id text UNIQUE,
			image blob
			)""")


c.execute("""CREATE TABLE tags (
			tag text,
			id text
			)""")
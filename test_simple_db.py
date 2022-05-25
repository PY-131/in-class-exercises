import os
import simple_db
import sqlite3
import unittest

class TestMusicDatabase(unittest.TestCase):
    """
    Test the music database
    """
    # this is our fixture
    def setUp(self):
        """
        Setup a temporary database
        """
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()

        # create a table
        cursor.execute("""CREATE TABLE IF NOT EXISTS albums
                          (title text, artist text, release_date text,
                           publisher text, media_type text)
                       """)
        # insert some data
        cursor.execute("INSERT INTO albums VALUES "
                       "('Glow', 'Andy Hunter', '7/24/2012',"
                       "'Xplore Records', 'MP3')")

        # save data to database
        conn.commit()

        # insert multiple records using the more secure "?" method
        albums = [('Exodus', 'Andy Hunter', '7/9/2002',
                   'Sparrow Records', 'CD'),
                  ('Until We Have Faces', 'Red', '2/1/2011',
                   'Essential Records', 'CD'),
                  ('The End is Where We Begin', 'Thousand Foot Krutch',
                   '4/17/2012', 'TFKmusic', 'CD'),
                  ('The Good Life', 'Trip Lee', '4/10/2012',
                   'Reach Records', 'CD')]
        cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)",
                           albums)
        conn.commit()

    def test_select_all_albums(self):
      result = simple_db.select_all_albums('Andy Hunter');
      expected_output = [
        ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3'),
        ('Exodus', 'Andy Hunter', '7/9/2002',
                     'Sparrow Records', 'CD')
      ]
      self.assertEqual(result, expected_output)

    def test_update(self):

      simple_db.update_artist("Trip Lee", "Trap Lee")
      result = simple_db.select_all_albums("Trap Lee")
      expected_output = ('The Good Life', 'Trap Lee', '4/10/2012',
                   'Reach Records', 'CD')
      self.assertEqual(result[0], expected_output)


    def tearDown(self):
        """
        Delete the database
        """
        os.remove("mydatabase.db")

if __name__ == '__main__':
  unittest.main()
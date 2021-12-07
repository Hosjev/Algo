""" A basic example (see _get_serializer) of tuning a class with factory method """
import xml.etree.ElementTree as xetree
import json


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    # Client/interface component
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        return serializer(song)

    # Creator component
    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    # Product component
    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    # Product component
    def _serialize_to_xml(self, song):
        song_element = xetree.Element('song', attrib={'id': song.song_id})
        title = xetree.SubElement(song_element, 'title')
        title.text = song.title
        artist = xetree.SubElement(song_element, 'artist')
        artist.text = song.artist
        return xetree.tostring(song_element, encoding='unicode')

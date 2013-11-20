# -*- coding: utf-8 -*-

from mongoengine import Document, SequenceField, StringField, DictField, \
    DateTimeField, IntField, BooleanField, FloatField, ListField, DecimalField, \
    ImageField, EmailField, GeoPointField, EmbeddedDocument, \
    EmbeddedDocumentField, URLField

from mongoengine import signals
from datetime import datetime


# Some nice to have collections/sets/lists

class PlantData(Document):

    # Might be a significant piece of information
    imei = StringField()
    ph = FloatField()
    n = IntField()
    p = IntField()
    k = IntField()
    temp = FloatField()
    moisture = IntField()
    lat = GeoPointField()
    lon = IntField()
    created_at = DateTimeField()
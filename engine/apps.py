import os
import pickle as pkl
import pyterrier as pt
from django.apps import AppConfig
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    name = 'api'
    FIELDS = ['title', 'abstract', 'subsections', 'authors']
    MODEL_FILE = settings.MODEL_DIR / 'rank_model.pkl'
    with open(MODEL_FILE, 'rb') as f:
        model = pkl.load(f)
    model.indexes = {}
    pt.init()
    for field in FIELDS:
        index_rf = settings.MODEL_DIR / 'index' / field / 'data.properties'
        if not os.path.exists(index_rf):
            raise FileNotFoundError('Index missing! ' + index_rf)
        model.indexes[field] = pt.IndexFactory.of(str(index_rf))


class EngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'engine'

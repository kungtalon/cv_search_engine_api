import os
import pickle as pkl
import pyterrier as pt
from django.apps import AppConfig
from django.apps import AppConfig
from django.conf import settings
import gdown

class ApiConfig(AppConfig):
    name = 'api'
    FIELDS = ['title', 'abstract', 'subsections', 'authors']
    MODEL_FILE = settings.MODEL_DIR / 'rank_model_fix.pkl'
    if not os.path.exists(MODEL_FILE):
        gdown.download('https://drive.google.com/u/0/uc?export=download&confirm=DVOq&id=1ji02FO17Rl3m0DgKD3PKX91_i0Y98n-i', MODEL_FILE, quiet=False)
    with open(MODEL_FILE, 'rb') as f:
        model = pkl.load(f)
    model.indexes = {}
    pt.init(version=5.6, helper_version='0.0.6')
    for field in FIELDS:
        index_rf = settings.MODEL_DIR / 'index' / field / 'data.properties'
        if not os.path.exists(index_rf):
            raise FileNotFoundError('Index missing! ' + index_rf)
        model.indexes[field] = pt.IndexFactory.of(str(index_rf))


class EngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'engine'

from django.db import models
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation,Dropout
from tensorflow.keras.losses import MeanSquaredLogarithmicError
from tensorflow.keras.optimizers import Adam
import joblib

# Create your models here.
class Data(models.Model):
    Home_Team = models.CharField(max_length=100, null=True)
    Away_Team = models.CharField(max_length=100, null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/NFLmodel.h5')
        self.home_score = ml_model.predict([[self.Home_Team ]])
        self.away_score = ml_model.predict([[ self.Away_Team ]])
        self.prediction = ml_model.predict(
            [[ self.Home_Team, self.Away_Team ]])
            

        return super().save(*args, *kwargs)

class meta:
    ordering = ['-date']     

def _str_(self):
    return self.Home_Team

from rest_framework import serializers
from models import Jobdb


class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobdb
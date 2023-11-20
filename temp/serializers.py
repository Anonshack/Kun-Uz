from rest_framework import serializers
from .models import (
    HeadKunUz,
    InternalMenus,
    TodayNews,
    UnderKunUz,
    ThreeInfoUnder
)


class HeadKunUzSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadKunUz
        fields = ['id', 'title', 'image', 'set_data', 'info']


class InternalMenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalMenus
        fields = ['id', 'title', 'set_data', 'link', 'info', 'menu']


class TodayNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayNews
        fields = ['id', 'title', 'set_data', 'info', 'image']


class UnderKunUzSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnderKunUz
        fields = ['id', 'title', 'image', 'set_data', 'info']


class ThreeInfoUnderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeInfoUnder
        fields = ['id', 'title', 'image', 'set_data', 'info']

from django.db import models
from rest_framework import serializers
from shortener.models import ShortenerModel
from shortener.utils import shorten_url, get_page_title

class ShortenerSerializer(serializers.ModelSerializer):
    shortened_url = serializers.SerializerMethodField(method_name='get_shortened_url')

    class Meta:
        model = ShortenerModel
        fields = ('source_url', 'shortened_url', 'views', 'title')
        read_only_fields = ('encoded', 'views', 'shortened_url')

    def create(self, validated_data):
        validated_data['encoded'] = shorten_url(validated_data['source_url'])
        validated_data['title'] = get_page_title(validated_data['source_url'])
        return super().create(validated_data)

    def get_shortened_url(self, obj):
        host = self.context.get('request').get_host()
        scheme = self.context.get('request').scheme
        return f'{scheme}://{host}/{obj.encoded}'

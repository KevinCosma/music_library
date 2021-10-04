from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'genre']

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update (self, instance, validated_data):
        instance.title= validated_data.get('name', instance.title)
        instance.artist = validated_data.get('description', instance.artist)
        instance.album = validated_data.get('album', instance.album)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.gere = validated_data.get('genre', instance.genre)
# models.py 기반으로 작성하는 파일
from .models import Essay,Album,Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk','title','body','author_name')
        # fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    # url로 저장
    image=serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk','author_name','image','desc')

class FilesSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    # url로 저장
    myfile = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = ('pk','author_name','myfile','desc')
from rest_framework import serializers
from .models import Story
from result.models import Result
from django.conf import settings

class GreatsSerializer(serializers.ModelSerializer):
    greatId = serializers.IntegerField(source='id')
    puzzle_cnt = serializers.SerializerMethodField()
    silhouette_url = serializers.SerializerMethodField()
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = Story
        fields = ['greatId', 'name', 'silhouette_url', 'photo_url', 'saying', 'puzzle_cnt', 'nation', 'field']

    def get_puzzle_cnt(self, obj):
        user_id = self.context.get('user_id')
        if user_id is not None:
            result = Result.objects.filter(story=obj, user_id=user_id).first()
            if result:
                return result.puzzle_cnt
        return 0

    def get_silhouette_url(self, obj):
        return self.get_s3_url(obj.silhouette_url)

    def get_photo_url(self, obj):
        return self.get_s3_url(obj.photo_url)

    def get_s3_url(self, file_path):
        if not file_path:
            return None
        return f'https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file_path}'

class GreatDetailSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    life = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = ['video_url', 'gender', 'life']

    def get_gender(self, obj):
        return '남성' if obj.gender == 0 else '여성'

    def get_life(self, obj):
        return obj.life

    def get_video_url(self, obj):
        return self.get_s3_url(obj.video_url)

    def get_s3_url(self, file_path):
        if not file_path:
            return None
        return f'https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file_path}'

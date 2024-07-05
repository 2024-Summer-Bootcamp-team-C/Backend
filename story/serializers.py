from rest_framework import serializers
from .models import Story
from result.models import Result

class GreatsSerializer(serializers.ModelSerializer):
    greatId = serializers.IntegerField(source='id')
    puzzle_cnt = serializers.SerializerMethodField()
    class Meta:
        model = Story
        fields = ['greatId', 'name', 'silhouette_url', 'photo_url', 'saying', 'puzzle_cnt']

    def get_puzzle_cnt(self, obj):
        user_id = self.context.get('user_id')
        if user_id is not None:
            result = Result.objects.filter(story=obj, user_id=user_id).first()
            if result:
                return result.puzzle_cnt

        return 0
class GreatDetailSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    life = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = ['video_url', 'gender', 'life']

    def get_gender(self, obj):
        return '남성' if obj.gender == 0 else '여성'

    def get_life(self, obj):
        return obj.life

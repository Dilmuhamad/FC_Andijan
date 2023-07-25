from rest_framework import serializers
from .models import *


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ArenasInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArenasInformation
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class AcademySerializer(serializers.ModelSerializer):
    class Meta:
        model =Academy
        fields = '__all__'


class ArenaSerializer(serializers.ModelSerializer):
    class Meta:
        model =Arena
        fields = '__all__'
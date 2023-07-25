import datetime as datetime
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import *


@api_view(['GET'])
def get_new_slider(request):
    header = Header.objects.all().order_by('-id')[:3]
    ser = HeaderSerializer(header, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_video(request):
    video = Video.objects.all().order_by('-id')[:4]
    ser = VideoSerializer(video, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_player(request):
    team = Player.objects.all()
    data = {
        'time': datetime.datetime.now().time(),
        'date': datetime.datetime.now().date(),
        'team': TeamSerializer(team, many=True).data,
        'team_count': team.count(),
        'last_player': TeamSerializer(team.last()).data,
    }
    return Response(data)


@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_player_view(request, pk):
    Player.objects.get(id=pk).delete()
    return Response({"message": "Done"})


@api_view(['GET'])
def get_shop(request):
    shop = Shop.objects.all()
    ser = ShopSerializer(shop, many=True).data
    return Response(ser)

@api_view(['GET'])
def get_arenas_information(request):
    info = ArenasInformation.objects.all()
    ser = ArenasInformationSerializer(info, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_partner(request):
    partner = Partnerobjects.all().order_by('-id')[:5]
    ser = PartnerSerializer(partner, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_new(request):
    new = New.objects.all().order_by('-id').last()
    ser = NewSerializer(new).data
    return Response(ser)

@api_view(['GET'])
def club(request):
    content = Club.objects.all()
    ser = ContentSerializer(content, many=True).data
    return Response(ser)



@api_view(['GET'])
def get_club(request):
    content = Club.objects.all()
    ser = ClubSerializer(content, many=True).data
    return Response(ser)


@api_view(['GET'])
def academy(request):
    content = Academy.objects.all()
    ser = AcademySerializer(content, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_academy(request):
    content = Academy.objects.all()
    ser = AcademySerializer(content, many=True).data
    return Response(ser)


@api_view(['GET'])
def arena(request):
    content = Arena.objects.all()
    ser = ArenaSerializer(content, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_arena(request):
    content = Arena.objects.all()
    ser = ArenaSerializer(content, many=True).data
    return Response(ser)




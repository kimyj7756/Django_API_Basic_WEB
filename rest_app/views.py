from rest_framework import viewsets
# models.py
from .models import Essay,Album,Files
# serializers.py
from .serializers import EssaySerializer,AlbumSerializer,FilesSerializer
# 검색 기능
from rest_framework.filters import SearchFilter
# parser_classes 사용하는 import
from rest_framework.parsers import MultiPartParser,FormParser

# class FileViewSet()의 def post()에서 사용
from rest_framework.response import Response
from rest_framework import status

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    # 검색 기능 구현
    filter_backends = [SearchFilter]
    search_fields = ('title','body')

    # author의 이름이 자동적으로 저장되게 하는 함수
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

    # 현재 request를 보낸 유저
    # == self.request.user
    def get_queryset(self):
        qs = super().get_queryset()
        # 현재 staff 계정이면
        if self.request.user.is_staff:
            # 모두 보여줘라
            qs = qs.all()
            return qs
        else:
            # 그냥 회원이라면
            if self.request.user.is_authenticated:
                qs = qs.filter(author = self.request.user)
            else:
                # 보여주지 말아라
                qs = qs.none()
            return qs 

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    # parser_classes 중 MultiPartParser,FormParser 사용
    # 파일 업로드시 parser를 지정하여 사용 가능하게 함
    parser_classes = (MultiPartParser,FormParser)

    # create() 오버라이딩 -> create()는 post방식이므로 post를 오버라이딩
    def post(self,request,*args,**kwargs):
        # data에서 는 받아온 데이터 사용
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 잘 저장했다면(유효성 검사 결과)
            return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            # 잘 저장하지 못 했다면(유효성 검사 결과)
            return Response(serializer.error,status=HTTP_400_BAD_REQUEST)
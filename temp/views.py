from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import DestroyAPIView, get_object_or_404
from rest_framework.response import Response
from .models import (
    HeadKunUz,
    InternalMenus,
    TodayNews,
    UnderKunUz,
    ThreeInfoUnder,
)
from .serializers import (
    HeadKunUzSerializer,
    InternalMenusSerializer,
    TodayNewsSerializer,
    UnderKunUzSerializer,
    ThreeInfoUnderSerializer,
)


class HeadKunUzListView(generics.ListAPIView):
    serializer_class = HeadKunUzSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        if title:
            return HeadKunUz.objects.filter(title__icontains=title)
        else:
            return HeadKunUz.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = HeadKunUzSerializer(queryset, many=True)
        return Response({'HeadKunUz': serializer.data})

    def put(self, request, id):
        try:
            clay = HeadKunUz.objects.get(pk=id)
            serializer = HeadKunUzSerializer(clay, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'res': 'success'})
            return Response({'res': 'error', 'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except HeadKunUz.DoesNotExist:
            return Response({'res': 'error', 'detail': 'Thing not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            sat = HeadKunUz.objects.get(pk=id)
            serializer = HeadKunUzSerializer(sat, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'res': 'success'})
            return Response({'res': 'error', 'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except HeadKunUz.DoesNotExist:
            return Response({'res': 'error', 'detail': 'Thing not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = HeadKunUzSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeadKunUzDeleteView(DestroyAPIView):
    queryset = HeadKunUz.objects.all()
    serializer_class = HeadKunUzSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Object deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class InterMenuListView(generics.ListAPIView):
    queryset = InternalMenus.objects.all()
    serializer_class = InternalMenusSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        if title:
            return InternalMenus.objects.filter(title__icontains=title)
        else:
            return InternalMenus.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = InternalMenusSerializer(queryset, many=True)
        return Response({'InternalMenus': serializer.data})

    def put(self, request, id):
        try:
            clay = InternalMenus.objects.get(pk=id)
            serializer = InternalMenusSerializer(clay, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'result': 'success'})
            return Response({'result': 'error', 'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except InternalMenus.DoesNotExist:
            return Response({'result': 'error', 'detail': 'Thing not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            sat = InternalMenus.objects.get(pk=id)
            serializer = InternalMenusSerializer(sat, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'result': 'success'})
            return Response({'result': 'error', 'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except InternalMenus.DoesNotExist:
            return Response({'result': 'error', 'detail': 'Thing not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = InternalMenusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InternalMenusDelete(DestroyAPIView):
    queryset = InternalMenus.objects.all()
    serializer_class = InternalMenusSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Object deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class TodayNewsView(generics.ListAPIView):
    queryset = TodayNews.objects.all()
    serializer_class = TodayNewsSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        if title:
            return TodayNews.objects.filter(title__icontains=title)
        else:
            return TodayNews.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TodayNewsSerializer(queryset, many=True)
        return Response({'Today\'s new': serializer.data})

    def put(self, request, id):
        try:
            student = TodayNews.objects.get(pk=id)
            serializer = TodayNewsSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'result': 'success'})
            return Response({'result': 'error', 'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except TodayNews.DoesNotExist:
            return Response({'result': 'error', 'detail': 'Thing not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            clay = TodayNews.objects.get(pk=id)
            serializer = TodayNewsSerializer(clay, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'result': 'success'})
            return Response({'result': 'error', 'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except TodayNews.DoesNotExist:
            return Response({'result': 'error', 'detail': 'Thing not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = TodayNewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodayDeleteView(DestroyAPIView):
    queryset = TodayNews.objects.all()
    serializer_class = TodayNewsSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Object deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class UnderKunUzView(generics.ListAPIView):
    queryset = UnderKunUz.objects.all()
    serializer_class = UnderKunUzSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        if title:
            return UnderKunUz.objects.filter(title__icontains=title)
        else:
            return UnderKunUz.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UnderKunUzSerializer(queryset, many=True)
        return Response({'Under new': serializer.data})

    def post(self, request):
        serializer = UnderKunUzSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnderDeleteView(DestroyAPIView):
    queryset = UnderKunUz.objects.all()
    serializer_class = UnderKunUzSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Object deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class UnderInfoUnderUpdateView(generics.UpdateAPIView):
    queryset = UnderKunUz.objects.all()
    serializer_class = UnderKunUzSerializer

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({'result': 'success'})
        except UnderKunUz.DoesNotExist:
            return Response({'result': 'error', 'detail': 'Thing not found'}, status=status.HTTP_404_NOT_FOUND)


class ThreeNewsKunUzView(generics.ListAPIView):
    queryset = ThreeInfoUnder.objects.all()
    serializer_class = ThreeInfoUnderSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        if title:
            return ThreeInfoUnder.objects.filter(title__icontains=title)
        else:
            return ThreeInfoUnder.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ThreeInfoUnderSerializer(queryset, many=True)
        return Response({'Under new': serializer.data})

    def post(self, request):
        serializer = ThreeInfoUnderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThreeNewsDeleteView(DestroyAPIView):
    queryset = ThreeInfoUnder.objects.all()
    serializer_class = ThreeInfoUnderSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Object deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class ThreeInfoUnderUpdateView(generics.UpdateAPIView):
    queryset = ThreeInfoUnder.objects.all()
    serializer_class = ThreeInfoUnderSerializer

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({'result': 'success'})
        except ThreeInfoUnder.DoesNotExist:
            return Response({'result': 'error', 'detail': 'Thing not found'}, status=status.HTTP_404_NOT_FOUND)
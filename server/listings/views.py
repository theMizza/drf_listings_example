from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser, IsAuthenticated

from .serializers import ListingsSerializer, ListingCategoriesSerializer
from .models import Listings, Categories
from .permissions import IsOwner

"""
Used base DRF permissions:
IsAuthenticatedOrReadOnly - returns response to get request, other requests after auth check, 
AllowAny - allow to any users, 
IsAdminUser - allow for admin, 
IsAuthenticated - allow for authenticated

Custom permission class: IsOwner
"""


class CategoriesApiView(ListAPIView):
    """Categories list view"""
    queryset = Categories.objects.all()
    serializer_class = ListingCategoriesSerializer
    permission_classes = (AllowAny,)


class CreateCategoryApiViev(APIView):
    """Category create view"""
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = ListingCategoriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'data': serializer.data})


class CategoryApiView(APIView):
    """Category get/update/delete view"""
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminUser)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'GET not allowed'})
        data = Categories.objects.get(pk=pk)
        return Response({'data': ListingCategoriesSerializer(data).data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'PUT not allowed'})

        try:
            instance = Categories.objects.get(pk=pk)

        except Exception as error:
            return Response({'error': f'PUT method error: {error}'})

        serializer = ListingCategoriesSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'DELETE not allowed'})

        try:
            instance = Categories.objects.get(pk=pk)
            instance.delete()

        except Exception as e:
            return Response({'error': f'DELETE method error: {e}'})

        return Response({'data': f"Category with pk: {pk} was deleted"})


class ListingsApiView(ListAPIView):
    """Listings list view"""
    permission_classes = (AllowAny,)
    queryset = Listings.objects.all()
    serializer_class = ListingsSerializer


class CreateListingApiViev(APIView):
    """Listing create view"""
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ListingsSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'data': serializer.data})


class ListingApiView(APIView):
    """Listing get/update/delete view"""
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwner, )

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'GET not allowed'})
        data = Listings.objects.get(pk=pk)
        return Response({'data': ListingsSerializer(data).data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        print(pk)
        if not pk:
            return Response({'error': 'PUT not allowed'})

        try:
            instance = Listings.objects.get(pk=pk)
            print(instance)
        except Exception as error:
            return Response({'error': f'PUT method error: {error}'})

        if self.check_object_permissions(request, instance):
            serializer = ListingsSerializer(data=request.data, context={'request': request}, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'error': f'No permissions to PUT'})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'DELETE not allowed'})

        try:
            instance = Listings.objects.get(pk=pk)
        except Exception as e:
            return Response({'error': f'DELETE method error: {e}'})

        if self.check_object_permissions(request, instance):
            instance.delete()
            return Response({'data': f"Listing with pk: {pk} was deleted"})
        else:
            return Response({'error': f'No permissions to DELETE'})


class UsersListingsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        listings = Listings.objects.filter(user=request.user)
        return Response({'data': ListingsSerializer(listings, many=True).data})

"""
There are also a lot generics api classes:
CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView etc

example:

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

more info here - https://www.django-rest-framework.org/api-guide/generic-views/
"""
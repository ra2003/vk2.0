from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from account.models import Account
from edit.forms import PhotoForm
from photo.models import Photo
from like.models import Like


class AlbumsView(View):
    def get(self, request, pk):
        main_user = Account.objects.get(pk=request.user.pk)
        photo_form = PhotoForm(instance=main_user)
        user = Account.objects.select_related().get(pk=pk)
        all_photo = user.images.all()
        count_photo = all_photo.count()
        context = dict()
        context['user'] = user
        context['main_user'] = main_user
        context['all_photo'] = all_photo
        context['count_photo'] = count_photo
        context['photo_form'] = photo_form
        return render(request, 'photo/albums.html', context=context)

    def post(self, request, pk):
        main_user = Account.objects.get(pk=request.user.pk)
        new_photo = Photo.objects.create(photo=request.FILES['photo'], account=main_user)
        main_user.images.add(new_photo)
        return redirect('albums', pk=main_user.pk)


class DeletePhotoView(View):
    def get(self, request):
        main_user = Account.objects.select_related().get(pk=request.user.pk)
        photo = main_user.images.select_related().get(pk=request.GET['pk'])
        photo.delete()
        return JsonResponse({})


class MakeMainPhoto(View):
    def get(self, request):
        main_user = Account.objects.get(pk=request.user.pk)
        main_photo = Photo.objects.get(pk=request.GET['pk'])
        main_user.main_photo = main_photo.photo
        main_user.save()
        return JsonResponse({})


class PutLikePhoto(View):
    def get(self, request):
        main_user = Account.objects.get(pk=request.user.pk)
        photo = Photo.objects.get(pk=request.GET['pk'])
        like, created = Like.objects.get_or_create(user=main_user, photo=photo, defaults={'user': main_user})
        if not created:
            like.delete()
            count_likes = photo.likes.count()
            photo.like_put = False
            photo.save()
            return JsonResponse({'likes_put': photo.like_put, 'count_likes': count_likes})
        main_user.likes.add(like)
        photo.likes.add(like)
        count_likes = photo.likes.count()
        photo.like_put = True
        photo.save()
        return JsonResponse({'likes_put': photo.like_put, 'count_likes': count_likes})

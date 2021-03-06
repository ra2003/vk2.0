from django.http import JsonResponse
from django.views import View
from account.models import Account
from photo.models import Photo
from post.models import Post
from group.models import Group
from like.models import Like


class PostView(View):
    def post(self, request):
        if request.POST['url'] == '/id{}/'.format(request.user.pk):
            main_user = Account.objects.get(pk=request.user.pk)
            content = request.POST['content']
            Post.objects.create(author=main_user, content=content)
            return JsonResponse({})
        group = Group.objects.get(pk=request.POST['public_pk'])
        content = request.POST['content']
        Post.objects.create(group=group, content=content)
        return JsonResponse({})


class DeletePostView(View):
    def get(self, request):
        post = Post.objects.get(pk=request.GET['pk'])
        post.delete()
        return JsonResponse({})


class PutLikePost(View):
    def get(self, request):
        main_user = Account.objects.get(pk=request.user.pk)
        post = Post.objects.select_related().get(pk=request.GET['pk'])
        try:
            like = post.likes.get(user=main_user)
            like.delete()
            post.who_liked.remove(main_user)
            count_likes = post.likes.count()
            likes_put = False
            post.save()
        except:
            like = Like.objects.create(user=main_user, post=post)
            main_user.likes.add(like)
            post.likes.add(like)
            count_likes = post.likes.count()
            likes_put = True
            post.who_liked.add(main_user)
            post.save()
        return JsonResponse({'likes_put': likes_put,
                             'count_likes': count_likes})


class PinPostView(View):
    def get(self, request):
        post = Post.objects.select_related().get(pk=request.GET['pk'])
        group = Group.objects.select_related().get(pk=request.GET['public_pk'])
        group.fixed_post = post
        group.save()
        return JsonResponse({})

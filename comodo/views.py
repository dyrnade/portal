from __future__ import absolute_import
from django.shortcuts import render
from django.views import generic
from .models import Post, Material, MyUser, Comment
from .forms import RegistrationsForm, EditPostForm, CreatePostForm, CreateMaterialForm, CommentForm
from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from comodo.serializers import PostSerializer
from rest_framework import generics
from django.contrib import messages


# Permissons

class VolunteerTestMixin(UserPassesTestMixin):
    # If user_status volunteer, show the page. ====> UserPassesTestMixin <=====
    def test_func(self):
        if self.request.user.user_status == 1:
            raise Http404
        else:
            return True

class RecipantTestMixin(UserPassesTestMixin):
    # If user_status volunteer, show the page. ====> UserPassesTestMixin <=====
    def test_func(self):
        if self.request.user.user_status == 2:
            raise Http404
        else:
            return True

class IndexView(SuccessMessageMixin,LoginRequiredMixin, RecipantTestMixin, generic.ListView):
    template_name = 'index.html'
    context_object_name = 'postList'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.all()

class DetailView(LoginRequiredMixin,generic.DetailView):
    model = Post
    template_name = 'detail.html'

class MaterialView(LoginRequiredMixin,SuccessMessageMixin, VolunteerTestMixin,generic.ListView):
    template_name = 'main_yardim_alan.html'
    context_object_name = 'materialList'
    paginate_by = 10

    # If user_status recipant, show the page. ====> UserPassesTestMixin <=====
    def test_func(self):
        if self.request.user.user_status == 1:
            raise Http404
        else:
            return True

    def get_queryset(self):
        return Material.objects.all()

class UserMaterialView(LoginRequiredMixin,generic.ListView):
    template_name = 'malzeme_listesi.html'
    context_object_name = 'user_materialList'
    def get_queryset(self):
        return Material.objects.all()


class MaterialDetailView(LoginRequiredMixin,generic.DetailView):
    model = Material
    template_name = 'malzeme.html'

    def get_queryset(self):
        return super(MaterialDetailView, self).get_queryset().prefetch_related('comments')

class MaterialStatusUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Material
    template_name = 'malzeme.html'
    fields = []

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.status = 1
        instance.reserved_by = self.request.user
        instance.save()
        return HttpResponseRedirect('/comodo/yardim/')


class MaterialDeleteView(LoginRequiredMixin,generic.UpdateView):
    model = Material
    template_name = 'reversed_by.html'
    fields = []

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.status = 2
        instance.reserved_by = self.request.user
        instance.save()
        return HttpResponseRedirect('/comodo/yardim/')



def register(request):
    url = reverse('comodo:registration_complete')
    if request.method == "POST":
        form = RegistrationsForm(request.POST)  # filled form/i'm skipping validation for this example
        if form.is_valid():
            form.save(commit=True)
            print("Form is valid")
        else:
            messages.add_message(request, 25, 'A serious error occurred.')
            return HttpResponse(str((form.errors)))
        return HttpResponseRedirect('/comodo/register/')  # go to some other page if successfully saved
    else:
        form = RegistrationsForm  # if the user accessed the register url directly, just display the empty form
    return render(request, 'kayit.html', {'form': form})


# class LoginView(LoginRequiredMixin,generic.FormView):
#     form_class = LoginForm
#     success_url = reverse_lazy('index')
#     template_name = 'kayit.html'
#
#     def form_valid(self, form):
#         form.cleaned_data
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(username=username, password=password)
#
#         if user is not None and user.is_active:
#             login(self.request, user)
#             return super(LoginView, self).form_valid(form)
#         else:
#             return self.form_invalid(form)

class CreatePostView(LoginRequiredMixin,generic.CreateView):
    form_class = CreatePostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return HttpResponseRedirect('/comodo/yardim/')

# class CreateMaterialView(generic.CreateView):
#     form_class = CreateMaterialForm
#     model = Material
#     template_name = 'material_create.html'
#
#     def form_valid(self, form):
#         instance = form.save(commit=False)
#         instance.user = self.request.user
#         instance.status = 0
#         instance.save()
#         return HttpResponseRedirect('/comodo/')

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = CreateMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Material(material_name=request.POST['material_name'],material_message=request.POST['material_message'],material_image=request.FILES['material_image'])
            instance.user = request.user
            instance.status = 0
            instance.save()
            return HttpResponseRedirect('/comodo/')
    else:
        form = CreateMaterialForm()
    return render(request, 'material_create.html', {'form': form})

class EditPostView(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):
    form_class = EditPostForm
    model = Post
    template_name = 'post_edit.html'

class ReservedItemsView(LoginRequiredMixin,generic.ListView):
    template_name = 'reserved_by.html'
    context_object_name = 'materialList'
    model = Material
    def get_queryset(self):
        return Material.objects.all()

class GivenItemsView(LoginRequiredMixin,generic.ListView):
    template_name = 'given_material.html'
    context_object_name = 'given_materials'
    model = Material
    def get_queryset(self):
        return Material.objects.all()

class ProfileListView(LoginRequiredMixin, generic.ListView):
    template_name = 'profilim.html'
    model = MyUser
    fields = []

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return instance

    # def get_queryset(self):
    #     return MyUser.objects.all().prefetch_related('user')

# class ProfileDetailView(LoginRequiredMixin,generic.DetailView):
#     template_name = 'profilim.html'
#     # context_object_name = 'profil_bilgisi'
#     model = MyUser
#     # def get_queryset(self):
#     #     return MyUser.objects.all()

@login_required
def redirecting(request):
    if request.user.user_status == 1:
        return HttpResponseRedirect('/comodo/')
    else:
        return HttpResponseRedirect('/comodo/yardim/')


class ApiPostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ApiPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class CommentSendView(generic.CreateView):
#     template_name = 'yorum_yap.html'
#     model = Comment
#     form_class = CommentForm
#
#     def form_valid(self, form):
#         instance = form.save(commit=False)
#         instance.author = self.request.user
#         instance.save()
#         return HttpResponseRedirect('comodo:yardim_sayfasi')
#
# class CommentShowView(generic.DetailView):
#     template_name = 'yorumlar.html'
#     model = Comment




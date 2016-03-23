from __future__ import absolute_import
from django.shortcuts import render
from django.views import generic
from .models import Post, Material
from .forms import RegistrationsForm, EditPostForm, CreatePostForm, LoginForm, MyUserProfileForm, CreateMaterialForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy

# Create your viewsi here.


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'postList'
    paginate_by = 2
    def get_queryset(self):
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'

class MaterialView(generic.ListView):
    template_name = 'main_yardim_alan.html'
    context_object_name = 'materialList'
    paginate_by = 10
    def get_queryset(self):
        return Material.objects.all()

class UserMaterialView(generic.ListView):
    template_name = 'malzeme_listesi.html'
    context_object_name = 'user_materialList'
    def get_queryset(self):
        return Material.objects.all().prefetch_related('user')


class MaterialDetailView(generic.DetailView):
    model = Material
    template_name = 'malzeme.html'

class MaterialStatusUpdateView(generic.UpdateView):
    model = Material
    template_name = 'malzeme.html'
    fields = []

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.status = 1
        instance.save()
        return HttpResponseRedirect('/comodo/yardim/')


def register(request):
    if request.method == "POST":
        form = RegistrationsForm(request.POST)  # filled form/i'm skipping validation for this example
        if form.is_valid():
            form.save(commit=True)
            print("Form is valid")
        else:
            return HttpResponse(str((form.errors)))
        return HttpResponseRedirect('/comodo/')  # go to some other page if successfully saved
    else:
        form = RegistrationsForm  # if the user accessed the register url directly, just display the empty form
    return render(request, 'kayit.html', {'form': form})


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('index')
    template_name = 'kayit.html'

    def form_valid(self, form):
        form.cleaned_data
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


# def post_create(request):
#     form = CreatePostForm(request.POST)
#     form.Meta.model.user = "g@g.com"
#     form.Meta.model.is_accomplished = True
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#     else:
#         print str(form.errors)
#
#     context = {
#         "form" : form,
#     }
#     return render(request, 'main_yardim_alan.html', context)
class CreatePostView(generic.CreateView):
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

class EditPostView(generic.UpdateView):
    form_class = EditPostForm
    model = Post
    template_name = 'post_edit.html'

class ReservedItemsView(generic.ListView):
    template_name = 'reserved_by.html'
    context_object_name = 'reserved_materials'
    model = Material
    def get_queryset(self):
        return Material.objects.all()

class GivenItemsView(generic.ListView):
    template_name = 'given_material.html'
    context_object_name = 'given_materials'
    model = Material
    def get_queryset(self):
        return Material.objects.all()

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, CreateView, ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# rest_framework
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from .forms import ContactForm, AppointmentForm, CommentForm
from .forms import UserRegisterForm
from .models import *
from .serializers import HomeSectionSerializer, HealthCenterSerializer, FooterBannerSerializer, DoctorsSerializer, \
    BlogSerializer, AppointmentSerializer, ContactSerializer, CommentSerializer


def index(request):
    return render(request, 'user/index.html', {'title': 'index'})


# def signup(request):
#     form = UserRegisterForm()
#     data = {
#         "form": form,
#     }
#     print(data)
#     exit
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#
#         if(password1 !=password2):
#             pass
#             # messages.add_message(request, Message.info,'password mismatch')
#         # else:
#         #     user = create_user(username=username,password1=password1,email=email,name=name)
#         #     if(user.is_active):
#         #         print('register')
#         #     else:
#         #         print('err')
#
#     return render(request, 'user/register.html', context=data)

class SignUpView(CreateView):
    template_name = 'user/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


def validate_username(request):
    """Check username availability"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)


########### register here #####################################
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             messages.success(request, f'Your account has been created ! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'user/register.html', {'form': form, 'title': 'reqister here'})


################ login forms###################################################
def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'log in'})


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero'] = HomeSection.objects.all()
        context['health_center'] = HealthCenter.objects.all()
        context['doctors'] = Doctors.objects.all()
        context['blogs'] = Blog.objects.all().order_by("-pk")[:3]
        context['footer_banner'] = FooterBanner.objects.all()
        return context


class DoctorView(TemplateView):
    template_name = 'doctors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctors.objects.all()
        context['footer_banner'] = FooterBanner.objects.all()
        return context


class AboutUsView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['health_center'] = HealthCenter.objects.all()
        context['footer_banner'] = FooterBanner.objects.all()
        context['doctors'] = Doctors.objects.all()[:3]
        return context


# class BlogView(TemplateView):
#     template_name = 'blog.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['blogs'] = Blog.objects.all()
#         context['health_center'] = HealthCenter.objects.all()
#         context['blog'] = Blog.objects.all().order_by("-pk")[:3]
#         return context


class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        context = super(BlogView, self).get_context_data(**kwargs)
        p = Blog.objects.all()
        paginator = Paginator(p, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            pagination = paginator.page(page)
        except PageNotAnInteger:
            pagination = paginator.page(1)
        except EmptyPage:
            pagination = paginator.page(paginator.num_pages)

        context['blogs'] = pagination
        context['health_center'] = HealthCenter.objects.all()
        context['blog'] = Blog.objects.all().order_by("-pk")[:3]
        context['footer_banner'] = FooterBanner.objects.all()
        # context['blogs'] = Blog.objects.all()
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_banner'] = FooterBanner.objects.all()
        return context


class ContactusView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        self.object = form.save()
        return redirect(reverse('contact_us'))


class AppointmentView(CreateView):
    template_name = 'index.html'
    form_class = AppointmentForm

    def form_valid(self, form):
        self.object = form.save()
        return redirect(reverse('index'))

    def form_invalid(self, form):
        pass


class CommentView(CreateView):
    template_name = 'blog-details.html'
    form_class = CommentForm

    def form_valid(self, form):
        self.object = form.save()
        return redirect(reverse('leave_comment'))


# class DetailView(TemplateView):
#     template_name = 'blog-details.html'


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_id = self.kwargs['pk']
        context['blog'] = Blog.objects.filter(id=blog_id)
        context['recent_blog'] = Blog.objects.all().order_by("-pk")[:3]
        context['health_center'] = HealthCenter.objects.all()
        context['footer_banner'] = FooterBanner.objects.all()
        return context


# class BlogDetailView(generic.DetailView):
#     model = Blog
#     template_name = 'blog-details.html'
#
#     # def get(self, request, *args, **kwargs):
#     #     pass
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         blog_id = self.kwargs['pk']
#         context['blog'] = Blog.objects.filter(id=blog_id)
#         # context['blogs'] = Blog.objects.all().order_by("-pk")[:3]
#         # context['category'] = Category.objects.all()
#         return context

# class FileExamListView(ListView):
#     model = Blog
#     template_name = "blog.html"
#     paginate_by = 3
#
#     def get_context_data(self, **kwargs):
#         context = super(FileExamListView, self).get_context_data(**kwargs)
#         list_exam = Blog.objects.all()
#         paginator = Paginator(list_exam, self.paginate_by)
#
#         page = self.request.GET.get('page')
#
#         try:
#             file_exams = paginator.page(page)
#         except PageNotAnInteger:
#             file_exams = paginator.page(1)
#         except EmptyPage:
#             file_exams = paginator.page(paginator.num_pages)
#
#         context['blogs'] = file_exams
#         return context

def contact_form(request):
    form = ContactForm()
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['full_name']
            form.save()
            return JsonResponse({"full_name": name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "contact.html", {"form": form})


# search bar
# def search(request):
#     qur = request.GET.get('search')
#     # doctor = Admin_Addinfo.objects.filter(doctor_name__contains = qur)
#     doctor = [item for item in Doctors.objects.all() if
#               qur in item.name or qur in item.department]
#     return render(request, 'navbar.html', {"doctor": doctor})


class SearchView(ListView):
    model = Doctors
    template_name = 'doctors.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            # postresult = Doctors.objects.filter(department__contains=query)
            doctor = [item for item in Doctors.objects.all() if query in item.name or query in item.department]
            result = doctor
        else:
            result = None
        return result


class BlogSearchView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        result = super(BlogSearchView, self).get_queryset()
        query = self.request.GET.get('blog_search')
        if query:
            # postresult = Doctors.objects.filter(department__contains=query)
            doctor = [item for item in Blog.objects.all() if
                      query in item.disease or query in item.title or query in item.author_name]
            result = doctor
        else:
            result = None
        return result


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")


# RestFramework api

class HomeSectionViewSet(viewsets.ModelViewSet):
    serializer_class = HomeSectionSerializer
    queryset = HomeSection.objects.all().order_by('-pk')


class HealthCenterViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = HealthCenterSerializer
    queryset = HealthCenter.objects.all().order_by('-pk')


class FooterBannerViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = FooterBannerSerializer
    queryset = FooterBanner.objects.all().order_by('-pk')


class DoctorsViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorsSerializer
    queryset = Doctors.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'department']


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all().order_by('-pk')
    filter_backends = [filters.SearchFilter]
    search_fields = ['disease', 'title', 'author_name']


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    filter_backends = [filters.OrderingFilter]


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all().order_by('-pk')


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by('-pk')

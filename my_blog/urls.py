from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', MyBlogHome.as_view(), name = 'home'),
    path('post/<slug:post_slug>/', Show_post.as_view(), name = 'post'),
    path('category/<slug:cat_slug>/', Show_posts_by_category.as_view(), name = 'category'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('add_post/', Create_post.as_view(), name = 'add_post'),
    path('instructions/', show_instructions, name = 'instructions'),
    path('polls/', show_polls, name = 'polls'),
    path('personal_space/', show_polls, name = 'personal_space')
    

]
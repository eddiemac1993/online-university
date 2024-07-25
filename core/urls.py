from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/lessons/create/', views.create_lesson, name='create_lesson'),
    path('courses/<int:course_id>/assignments/create/', views.create_assignment, name='create_assignment'),
    path('assignments/<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),
    path('courses/<int:course_id>/discussions/create/', views.create_discussion, name='create_discussion'),
]
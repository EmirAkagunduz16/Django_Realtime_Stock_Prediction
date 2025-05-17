from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet, basename='employee')
router.register(r'employees', views.EmployeeDetailViewSet, basename='employeedetail')

urlpatterns = router.urls

urlpatterns = [
    path('students/', views.studentsView, name='students_list'),
    path('students/<int:pk>/', views.studentDetailView, name='student_detail'),
    path('', include(router.urls)),
    path('blogs/', views.BlogView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('comments/', views.CommentView.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment_detail'),
]

from .import views
from django.urls import path
app_name='bookapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('book/<int:book_id>/',views.detail, name='detail'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('add/', views.add_book, name='add_book'),
    path('cbvhome/',views.Booklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Bookdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Bookupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Bookdeleteview.as_view(),name='cbvdelete'),
]

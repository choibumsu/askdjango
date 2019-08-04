from django.urls import path, re_path
from . import views, views_cbv

app_name = 'dojo'

urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    path("<int:pk>/", views.post_detail),
    path('list1/', views.post_list1),
    path('list2/', views.post_list2),
    path('list3/', views.post_list3),
    path('excel/', views.excel_download),

    path('cbv/list1/', views_cbv.post_list1),
    path('cbv/list2/', views_cbv.post_list2),
    path('cbv/list3/', views_cbv.post_list3),
    path('cbv/list4/<int:pk>', views_cbv.post_list4),
    path('cbv/excel/', views_cbv.excel_download),

    path('example/', views.form_prac),
    path('account/', views.account_list, name="account_list"),
    path('account/<int:pk>', views.account_detail, name="account_detail"),
    path('account/create/', views.account_create, name="account_create"),
    path('post/', views.post_list, name="post_list"),
    path('post/<int:pk>', views.post_detail, name="post_detail"),
    path('post/create/', views.post_create, name="post_create"),
]

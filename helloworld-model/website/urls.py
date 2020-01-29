from  .  import views

app_name = 'website'

urlpatterns[

   url(r'^$', views.index, name='index'),
]
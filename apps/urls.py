from django.contrib import admin
from django.urls import path, include
from apps.views import Landing, Maps, Mail, InboxMail, MailHtmlInvoice, ToS, Supervisor, Account
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'apps.views.entry_not_found'

urlpatterns = [
    path('', Landing.as_view(context=''), name='landing'),
    path('tos/', ToS.as_view(context=''), name='terms-of-service'),
    path('maps/', Maps.as_view()),
    path('login/', Account.as_view(context='login'), name='login'),
    path('logout/', Account.as_view(context='logout'), name='logout'),
    path('spv/', Supervisor.as_view(context='dashboard'), name='dashboard'),
    path('spv/project/tehtarikjodi/', Supervisor.as_view(context='project-tehtarikjodi'), name='project-tehtarikjodi'),
    path('spv/project/bsl/', Supervisor.as_view(context='project-bsl'), name='project-bsl'),
    path('spv/support/', Supervisor.as_view(context='dashboard-support'), name='dashboard-support'),
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

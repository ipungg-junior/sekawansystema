from django.contrib import admin
from django.urls import path, include
from apps.views import Landing, Maps, Mail, InboxMail, MailHtmlInvoice, ToS
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'apps.views.entry_not_found'

urlpatterns = [
    path('', Landing.as_view(context='')),
    path('tos/', ToS.as_view(context='')),
    path('maps/', Maps.as_view()),
    #path('mail-to/<str:idEmail>/', Mail.as_view()),
    #path('mail-html/', MailHtmlInvoice.as_view()),
    #path('inbox-mail/', InboxMail.as_view())
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse
from apps.services import SupportForms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from service import utils, _database



def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)

# Create your views here.
class Landing(View):
    
    context = ''

    def post(self, request):
        response = SupportForms.check(request)
        return JsonResponse(response)

    def get(self, request):
        return render(request, 'index.html')
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class Supervisor(View):
    
    context = ''

    def post(self, request):
        pass

    def get(self, request):
        if (self.context == 'dashboard'):
            usage = utils.analyze_system_storage()
            return render(request, 'dashboard.html', context={'usage': usage})
        if (self.context == 'dashboard-support'):
            _t = _database.SupportTicket().get_all()
            return render(request, 'dashboard-support.html', context={'list_ticket': _t})
        


class Account(View):

    context = ''

    def get(self, request):
        if (self.context == 'logout'):
            logout(request)
            return redirect('/login/')
        return render(request, 'sign-in.html')

    def post(self, request):
        if (self.context == 'login'):
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if(user is not None):
                try:
                    login(request, user)
                    return redirect('dashboard')
                except:
                    return JsonResponse({'status': 500, 'url_dest': '/login/', 'info': 'Internal Server Error'})
            else:
                return JsonResponse({'status': 400, 'url_dest': '/login/', 'info': 'Username atau Password salah'})


    
class ToS(View):
    
    context = ''

    def get(self, request):
        return render(request, 'TOS.html')


class Maps(View):
    
    context = ''

    def get(self, request):
        return render(request, 'maps.html')
    

class Mail(View):

    context = ''

    def get(self, request, idEmail):
        subject = 'Systema.id Proposal Penawaran (POS GROSIR ECER)'
        message = f'''
Yang terhormat Bpk/Ibu {idEmail},
    
Kami harap email ini menemui Anda dalam keadaan baik. Kami dari Systema ingin memberikan penawaran khusus 
untuk membantu meningkatkan kehadiran online bisnis Anda.
    
Dalam era digital ini, sebuah website yang responsif dan menarik menjadi kunci untuk menjangkau lebih banyak pelanggan, meningkatkan kepercayaan,
dan meningkatkan penjualan. Inilah mengapa kami siap membantu Anda membangun web presence yang efektif dan sesuai dengan kebutuhan bisnis Anda.
    
Ayo, bangun bersama kami dan tingkatkan eksistensi digital bisnis Anda! Untuk mendiskusikan lebih lanjut atau meminta penawaran kustom, 
Jika Anda tertarik maka klik tautan untuk memberikan informasi kepada kami https://systema.id/quotation-confirmation/2dcsib8-3iusnf/
Atau, hubungi tim kami di (WA: 083837358230) pada waktu yang nyaman bagi Anda.
    
Terima kasih atas perhatian Anda, dan kami berharap dapat bekerja sama untuk mencapai kesuksesan bersama.


Hormat kami,
Marketing Systema.id
        '''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['ipungg.id@gmail.com', ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/')
    

class InboxMail(View):

    context = ''

    def get(self, request):
        # Example usage
        username = "cs@systema.id"
        password = "Ipung443833!"
        server = "imap.hostinger.com"
        import imaplib, email
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(server)

        # Login to the server
        mail.login(username, password)

        # Select the mailbox (e.g., INBOX)
        mail.select("INBOX")

        # Search for email messages
        result, data = mail.search(None, "ALL")

        # Get the list of email message IDs
        email_ids = data[0].split()
        stack = []
        # Iterate over the email IDs and fetch the messages
        for email_id in email_ids:
            result, data = mail.fetch(email_id, "(RFC822)")
            raw_email = data[0][1]
            # Parse the raw email data
            email_message = email.message_from_bytes(raw_email)
            
            # Extract the message content
            if email_message.is_multipart():
                for part in email_message.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/html":
                        message = part.get_payload(decode=True).decode()
                        stack.append(message)
                        # Close the connection
                        
            else:
                message = email_message.get_payload(decode=True).decode()
                stack.append(message)
                # Close the connection
        mail.logout()
        return render(request, 'inboxmail.html', context={'mail': stack})

            # Process the raw email data as needed
            # For example, you can use the email library to parse the email

        
class MailHtmlInvoice(View):
    
    context = ''

    def get(self, request):
        html_template = 'invoice-mail.html'
        context = {
            'promo': 0,
            'total': 145000,
            'items': [
                {'item':'Yellow', 'qty': 12, 'price': 10000},
                {'item':'Red Carpet', 'qty': 1, 'price': 20000},
                {'item':'Minior', 'qty': 100, 'price': 30000}
            ]
        }
        # Render template HTML ke dalam string
        html_content = render_to_string(html_template, context)

        # Ambil isi teks dari HTML untuk versi teks email
        text_content = strip_tags(html_content)

        # Kirim email menggunakan EmailMessage
        email = EmailMessage(
            subject="Invoice Systema",
            body=text_content,
            from_email=settings.EMAIL_HOST_USER,  # Ganti dengan alamat email Anda
            to=['ipungg.id@gmail.com',],
        )
        email.content_subtype = 'html'  # Mengatur tipe konten ke HTML
        email.send()
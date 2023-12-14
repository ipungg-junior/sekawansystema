from django.core.validators import validate_email

class SupportForms:

    @staticmethod
    def check(request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        topic = request.POST.get('topic')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if (len(name) < 4):
            return {'status': 'error', 'message': 'Nama tidak valid.'}

        try:
            validate_email(email)
        except:
            return {'status': 'error', 'message': 'Email tidak valid.'}
        
        if (len(phone) < 10):
            return {'status': 'error', 'message': 'Nomor tidak valid.'}
            
        if (len(topic) < 10):
            return {'status': 'error', 'message': 'Topic tidak valid.'}
        
        if (len(message) < 30):
            return {'status': 'error', 'message': 'Pesan minimal 30 karakter.'}
        
        return {'status': 'success', 'message': 'Terimakasih, kami segera membalas pesan Anda'}
        


from apps import models


class SupportTicket:
    
    @staticmethod
    def get_all():
        _tckt = models.SupportForm.objects.all()
        return _tckt


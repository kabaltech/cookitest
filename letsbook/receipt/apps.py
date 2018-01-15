from django.apps import AppConfig


class ReceiptConfig(AppConfig):
    name = 'letsbook.receipt'
    verbose_name = "Receipts"

    def ready(self):
        """Override this to put in:
            Receipts system checks
            Receipts signal registration
        """
        pass
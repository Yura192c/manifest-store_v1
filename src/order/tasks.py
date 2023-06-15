from celery import shared_task
from django.core.mail import send_mail
from .models import Order
# from config.settings.development import EMAIL_HOST_USER


@shared_task
def order_created(order_id):
    """
    Задание по отправке уведомления по электронной почте
    при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ номер {order.id}'
    message = f'Здравствуйте, {order.first_name},\n\n' \
              f'Вы успешно отправили заказ.' \
              f'Ваш номер заказа: {order.id}. Сохраните это сообщение на случай возникновения проблем.'
    mail_sent = send_mail(subject, message,
                          'yra.mironchik2003@gmail.com',
                          [order.email])
    return mail_sent

from payreminder.celery import app
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import *
from datetime import datetime
from .utils import SendEmail




@app.task(name='task_send_notification')
def send_notification():
    try:
        curr_time = datetime.now()
        sales_ps = SaleOrder.objects.filter(paid=False,due_date__year=curr_time.year, due_date__month=curr_time.month, due_date__day=curr_time.day).select_related('user')        
        for sales_obj in sales_ps:
            # print(sales_obj.user.email)
            SendEmail().send_notification_email(sales_obj.user.email)
        return True
    except Exception as error:
        print(error)
        return False
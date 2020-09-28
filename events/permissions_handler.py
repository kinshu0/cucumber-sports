from django.contrib.auth.models import Group

event_manager, created = Group.objects.get_or_create(name='event_manager')
payment_manager, created = Group.objects.get_or_create(name='payment_manager')

event_manager.permissions.set([
    'events.add_Event',
    'events.change_Event',
    'events.view_Event'
])


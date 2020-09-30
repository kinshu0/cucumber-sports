from decimal import Decimal, getcontext
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import get_object_or_404
from accounts.models import Registration

from django.core.serializers.json import DjangoJSONEncoder
# from django.core.serializers import serialize

import json
from datetime import timedelta

from django.db.models.expressions import RawSQL

'''
Function to save results of any timed event competition (running, swimming, etc.)
'''
def timed_event(form_data, event, profile):
    try:
        converted_form_data = json.loads(form_data)
        # time_duration = timedelta(hours=converted_form_data['time']['hours'], minutes=converted_form_data['time']['minutes'], seconds=converted_form_data['time']['seconds'])
        if not converted_form_data['disqualified']:
            time_duration = f"{converted_form_data['time']['hours'] * 60 + converted_form_data['time']['minutes']:02d}:{converted_form_data['time']['seconds']:02d}"
        else:
            time_duration = f"DQ {converted_form_data['time']['hours'] * 60 + converted_form_data['time']['minutes']:02d}:{converted_form_data['time']['seconds']:02d   }"
        converted_form_data['time'] = time_duration
        converted_form_data.pop('disqualified')
        # final = json.dumps(converted_form_data, cls=DjangoJSONEncoder)
        # all_registrations = Registration.objects.filter(event=event).order_by(RawSQL("result->>%s", ("time",)))
        registration = get_object_or_404(
            Registration, event=event, profile=profile)
        # registration.result = final
        registration.result = converted_form_data
        registration.save()
        all_registrations = Registration.objects.filter(
            event=event).order_by(RawSQL("result->>%s", ("time",)))
        x = 1
        for i in all_registrations:
            if not i.result:
                i.result = {'#': 0}
            i.result['#'] = x
            i.result_place = x
            x += 1
            i.save()
    except:
        raise Exception("Error Saving or getting Registration object lol")


def points_event():
    pass


def unknown():
    pass


result_functions = {
    'T': timed_event,
    'P': points_event,
    '0': unknown
}


def display_format(registrations, display_schema):
    pass


getcontext().prec = 2

place_prize_settings = {
    'is_flat_fee': False,
    'percent_fee': Decimal('0.1'),
    'flat_fee': Decimal('10'),
    'first_share': Decimal('0.5'),
    'second_share':  Decimal('0.3'),
    'third_share':  Decimal('0.2'),
    'sponsored_prize_rake': Decimal('0.0'),
}


def place_prize_display(event):
    number_of_registrations = Registration.objects.filter(event=event).count()
    registration_fee = event.registration_fee


    total_prize = number_of_registrations * registration_fee

    if place_prize_settings['is_flat_fee']:
        awardable_prize = total_prize - place_prize_settings['flat_fee']

    else:
        awardable_prize = total_prize * (Decimal('1.00')-place_prize_settings['percent_fee'])

    first_prize = place_prize_settings['first_share'] * awardable_prize
    second_prize = place_prize_settings['second_share'] * awardable_prize
    third_prize = place_prize_settings['third_share'] * awardable_prize

    my_fee = total_prize - first_prize - second_prize - third_prize

    
    if event.sponsored_prize > Decimal('0.0'):
        awardable_sponsored_prize = event.sponsored_prize * (Decimal('1.00') - place_prize_settings['percent_fee'])
        my_fee += event.sponsored_prize * place_prize_settings['percent_fee']

        first_prize += place_prize_settings['first_share'] * awardable_sponsored_prize
        second_prize += place_prize_settings['second_share'] * awardable_sponsored_prize
        third_prize += place_prize_settings['third_share'] * awardable_sponsored_prize      

    prize_template = get_template('events/subtemplates/place_prize.html')
    prize_template_context = {
        'total_prize': f'{awardable_prize:.2f}',
        'first_prize': f'{first_prize:.2f}',
        'second_prize': f'{second_prize:.2f}',
        'third_prize': f'{third_prize:.2f}',
    }

    return prize_template.render(prize_template_context), prize_template_context


def win_loss_prize():
    pass


def unknown():
    pass


prize_display_functions = {
    'T': place_prize_display,
    'P': win_loss_prize,
    '0': unknown
}


def place_prize_calc(event, commit=False):
    prize_page, prize_context = place_prize_display(event=event)
    first_place = Registration.objects.get(result_place=1)
    second_place = Registration.objects.get(result_place=2)
    third_place = Registration.objects.get(result_place=3)
    
    first_place.amount_won = Decimal(prize_context['first_prize'])
    second_place.amount_won = Decimal(prize_context['second_prize'])
    third_place.amount_won = Decimal(prize_context['third_prize'])

    if commit:
        first_place.save()
        second_place.save()
        third_place.save()

    return first_place, second_place, third_place

def win_prize_calc():
    pass


def unknown_calc():
    pass


prize_calc_functions = {
    'T': place_prize_calc,
    'P': win_prize_calc,
    '0': unknown_calc
}

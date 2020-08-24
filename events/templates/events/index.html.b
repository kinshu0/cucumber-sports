{% extends 'accounts/base.html' %}
{% load static %}

{% block content %}
    <script>
        
    </script>

    {% for event in upcoming_events %}
        <li>{{ event.name }} | {{ event.when | date:'M' }}</li>
    {% endfor %}

{% endblock %}
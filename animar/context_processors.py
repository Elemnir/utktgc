from django.core.urlresolvers import reverse

def nav_menu(request):
    return { 'nav_menu': [
        (
            { 'name': 'Home', 'url': reverse('home')},
            {}
        ),
        (
            { 'name': 'About', 'url': reverse('about')},
            {}
        ),
        (
            { 'name': 'Forum', 'url': reverse('forum')},
            {}
        ),
        (
            { 'name': 'Calendar', 'url': reverse('calendar')},
            {}
        ),
        (
            { 'name': 'Post Archive', 'url': reverse('archive')},
            {}
        ),
    ]}

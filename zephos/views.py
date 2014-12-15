import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger('zephos')

def robots(request):
    logger.info("robots.txt requested by: {0}".format(
        request.META.get('HTTP_USER_AGENT', 'NOT PROVIDED')
    ))
    return HttpResponse(
        "# robots.txt for www.utktgc.com" +
        "\nUser-agent: *" +
        "\nDisallow: /static/" +
        "\nDisallow: /accounts/", 
        content_type="text/plain")

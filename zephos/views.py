import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger('zephos')

def robots(request):
    logger.info("robots.txt requested by: {0}".format(request.META['HTTP_USER_AGENT']))
    return HttpResponse(
        "# robots.txt for www.utktgc.com" +
        "\nUser-agent: *" +
        "\nDisallow: /static/" +
        "\nDisallow: /accounts/", 
        content_type="text/plain")

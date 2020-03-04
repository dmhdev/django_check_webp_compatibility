from django.shortcuts import render
from django.http import HttpResponse
import httpagentparser

def getMajorBrowserVersionAsInt(user_browser):
  return int(user_browser['version'][:user_browser['version'].find('.')])

def getWebpCompatibleBrowser(request):
    webp_compatible_browsers = {'Firefox':65, 'Chrome':25, 'Edge':18, 'Opera':11}
    user_browser = httpagentparser.detect(request.META['HTTP_USER_AGENT'])['browser']
    
    for compatible_browser_key in webp_compatible_browsers:
        if (compatible_browser_key in user_browser['name']) and \
            (getMajorBrowserVersionAsInt(user_browser) >= webp_compatible_browsers[compatible_browser_key]):
            return True
    return False

def index(request):
    context_dict = {'webp_compatible_browser':getWebpCompatibleBrowser(request)}
    return render(request, 'index.html', context_dict)

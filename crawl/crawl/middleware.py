# Middleware.

from crawl import settings
import random


class RandomUserAgentDownloaderMiddleware(object):
    """Random user agent downloader middleware."""

    def __init__(self):
        self._user_agent_list = getattr(settings, 'USER_AGENT_LIST', None)

    def process_request(self, request, spider):
        if self._user_agent_list:
            ua = random.choice(self._user_agent_list)
            if ua:
                request.headers.setdefault('User-Agent', ua)


class ProxyMiddleware(object):
    """Send traffic through proxy."""

    def __init__(self):
        self._proxy = getattr(settings, 'HTTP_PROXY', None)

    def process_request(self, request, spider):
        if self._proxy:
            request.meta['proxy'] = self._proxy

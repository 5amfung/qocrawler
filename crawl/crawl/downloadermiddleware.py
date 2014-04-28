# Download middleware to randamize user agents.
#

from crawl.settings import USER_AGENT_LIST
import random


class RandomUserAgentDownloaderMiddleware(object):
    """Random user agent downloader middleware."""

    def __init__(self, user_agent_list=USER_AGENT_LIST):
        self._user_agent_list = user_agent_list

    def process_request(self, request, spider):
        ua = random.choice(self._user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)

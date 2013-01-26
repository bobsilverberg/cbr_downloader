#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.popstache import PopstacheListPage, PopstacheArticlePage
from test_base import TestBase


class TestPopstachePage(TestBase):

    @pytest.mark.nondestructive
    def test_download_mp3s(self, mozwebqa):
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:17.0) Gecko/20100101 Firefox/17.0'
        popstache_page = PopstacheListPage(mozwebqa)
        popstache_page.go_to_page()
        if popstache_page.url_current_page.endswith('free-mp3-download/'):
            all_links = popstache_page.article_links

            for link in all_links:
                article_page = PopstacheArticlePage(mozwebqa)
                article_page.go_to_page(link)
                if not self.grab_mp3(article_page, link, headers):
                    break
        else:
            next_link = popstache_page.first_article_in_sidebar_link
            while len(next_link) > 0:
                article_page = PopstacheArticlePage(mozwebqa)
                article_page.go_to_page(next_link)
                mp3_link = article_page.mp3_link
                if self.grab_mp3([mp3_link], popstache_page.base_url, headers):
                    # get next link
                    next_link = popstache_page.previous_article_link
                else:
                    next_link = ''

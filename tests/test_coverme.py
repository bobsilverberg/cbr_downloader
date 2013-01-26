#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.coverme import CoverMeLandingPage, CoverMeArticlePage
from test_base import TestBase


class TestCoverMePage(TestBase):

    @pytest.mark.nondestructive
    def test_download_mp3s(self, mozwebqa):
        coverme_page = CoverMeLandingPage(mozwebqa)
        coverme_page.go_to_page()
        all_links = coverme_page.article_links
        page_count = 1
        while page_count < 2:
            coverme_page.go_to_next_page()
            all_links += coverme_page.article_links
            page_count += 1

        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:17.0) Gecko/20100101 Firefox/17.0'

        for link in all_links:
            article_page = CoverMeArticlePage(mozwebqa)
            article_page.go_to_page(link)
            if not self.grab_mp3(article_page.mp3_links, link, headers):
                break

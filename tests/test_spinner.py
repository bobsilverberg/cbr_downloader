#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.spinner import SpinnerLandingPage, SpinnerArticlePage
from test_base import TestBase


class TestSpinnerPage(TestBase):

    @pytest.mark.nondestructive
    def test_download_mp3s(self, mozwebqa):
        spinner_page = SpinnerLandingPage(mozwebqa)
        spinner_page.go_to_page()
        all_links = spinner_page.article_links
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:17.0) Gecko/20100101 Firefox/17.0'

        for link in all_links:
            article_page = SpinnerArticlePage(mozwebqa)
            article_page.go_to_page(link)
            mp3_link = article_page.mp3_link
            if not self.grab_mp3([mp3_link], link, headers):
                break

#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from pages.coverme import CoverMeLandingPage, CoverMeArticlePage


class TestCoverMePage:

    @pytest.mark.nondestructive
    def test_download_mp3s(self, mozwebqa):
        coverme_page = CoverMeLandingPage(mozwebqa)
        coverme_page.go_to_page()
        all_links = coverme_page.article_links
        page_count = 1
        while page_count < 20:
            coverme_page.go_to_next_page()
            all_links += coverme_page.article_links
            page_count += 1

        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:17.0) Gecko/20100101 Firefox/17.0'

        for link in all_links:
            article_page = CoverMeArticlePage(mozwebqa)
            article_page.go_to_page(link)
            for mp3_link in article_page.mp3_links:
                mp3_name = mp3_link.split('/')[-1]
                headers['Referer'] = link
                mp3 = requests.get(mp3_link, headers=headers)
                with open(article_page.download_folder + mp3_name, "wb") as code:
                    code.write(mp3.content)

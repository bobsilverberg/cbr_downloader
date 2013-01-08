#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from page import Page


class PopstacheListPage(Page):

    _article_link_locator = (By.CSS_SELECTOR, 'a.read-more')

    def go_to_page(self):
        self.open('http://popstache.com/free-mp3-download/')

    @property
    def article_links(self):
        all_links = self.selenium.find_elements(*self._article_link_locator)
        hrefs = []
        for link in all_links:
            hrefs.append(link.get_attribute('href'))
        return hrefs


class PopstacheArticlePage(Page):

    _mp3_link_locator = (By.CSS_SELECTOR, 'a[onclick*="javascript:_gaq.push"]')

    def go_to_page(self, url):
        self.open(url)

    @property
    def mp3_link(self):
        return self.selenium.find_element(*self._mp3_link_locator).get_attribute('href')

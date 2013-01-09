#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from page import Page


class CoverMeLandingPage(Page):

    _article_link_locator = (By.CSS_SELECTOR, 'span.more-link a.more-link')
    _prev_page_link_locator = (By.CSS_SELECTOR, 'div.page-nav span.previous-entries a')

    def go_to_page(self):
        self.open('http://www.covermesongs.com/category/download')

    def go_to_next_page(self):
        self.selenium.find_element(*self._prev_page_link_locator).click()

    @property
    def article_links(self):
        all_links = self.selenium.find_elements(*self._article_link_locator)
        hrefs = []
        for link in all_links:
            hrefs.append(link.get_attribute('href'))
        return hrefs


class CoverMeArticlePage(Page):

    _mp3_link_locator = (By.CSS_SELECTOR, 'a[href$=mp3]')

    def go_to_page(self, url):
        self.open(url)

    @property
    def mp3_links(self):
        all_links = self.selenium.find_elements(*self._mp3_link_locator)
        hrefs = []
        for link in all_links:
            hrefs.append(link.get_attribute('href'))
        return hrefs

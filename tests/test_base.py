#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os.path
import requests


class TestBase:

    _download_folder = '/Volumes/Data/MP3Downloads/'

    def grab_mp3(self, mp3_links, referer_link, headers):
        for mp3_link in mp3_links:
            mp3_name = mp3_link.split('/')[-1]
            file_path = self._download_folder + mp3_name
            if not os.path.isfile(file_path):
                headers['Referer'] = referer_link
                mp3 = requests.get(mp3_link, headers=headers)
                with open(file_path, "wb") as code:
                    code.write(mp3.content)
            else:
                return False
        return True

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time


class Waiter(object):

    def __init__(self, polling=0.05):
        self._polling = polling

    def exe(self, timeout, func, *args, **kwgs):
        if not timeout:
            return func(*args, **kwgs) or False
        limit = int(time.time()) + timeout
        while int(time.time()) <= limit:
            result = func(*args, **kwgs)
            if result:
                return result
            time.sleep(self._polling)
        return False
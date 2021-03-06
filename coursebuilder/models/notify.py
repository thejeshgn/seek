# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utility for Sending notifications."""

__author__ = 'Abhinav Khandelwal (abhinavk@google.com)'

from modules.notifications import notifications

from google.appengine.api import mail
from google.appengine.api import users


class EmailManager(object):
    """Notification Manager. Sends emails out."""

    def __init__(self, course):
        self._course = course
        self._user = users.get_current_user()

    def send_mail(self, subject, body, reciever, sender=None, intent='default'):
        """send email."""
        if sender is None:
            sender = self._user.email()

        notifications.Manager.send_async(
            reciever, sender, intent, body, subject,
            )
        return True

    def send_mail_sync(self, subject, body, reciever, sender=None):
        """send email synchronously"""
        if sender is None:
            sender = self._user.email()

        notifications.Manager.send_sync(reciever, sender, body, subject)

    def send_announcement(self, subject, body, intent):
        """Send an announcement to course announcement list."""
        announce_email = self._course.get_course_announcement_list_email()
        if announce_email:
            self.send_mail(subject, body, announce_email, self._user.email(), intent)
        return False

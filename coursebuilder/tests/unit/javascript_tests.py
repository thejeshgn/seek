# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests for the javascript code."""

__author__ = 'John Orr (jorr@google.com)'

import os

import subprocess
import unittest

import appengine_config


class AllJavaScriptTests(unittest.TestCase):

    def karma_test(self, test_folder):
        karma_conf = os.path.join(
            appengine_config.BUNDLE_ROOT, 'tests', 'unit',
            'javascript_tests', test_folder, 'karma.conf.js')
        self.assertEqual(0, subprocess.call(['karma', 'start', karma_conf]))

    def test_activity_generic(self):
        self.karma_test('assets_lib_activity_generic')

    def test_assessment_tags(self):
        self.karma_test('modules_assessment_tags')

    def test_butterbar(self):
        self.karma_test('assets_lib_butterbar')

    def test_certificate(self):
        self.karma_test('modules_certificate')

    def test_core_tags(self):
        self.karma_test('modules_core_tags')

    def test_dashboard(self):
        self.karma_test('modules_dashboard')

    def test_oeditor(self):
        self.karma_test('modules_oeditor')

    def test_questionnaire(self):
        self.karma_test('modules_questionnaire')

    def test_skill_map(self):
        self.karma_test(os.path.join('modules_skill_map', 'lesson_editor'))
        self.karma_test(
            os.path.join('modules_skill_map', 'student_skill_widget'))

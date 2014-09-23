#!/usr/bin/env python
# encoding: utf-8
#
# Copyright © 2014 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2014-09-23
#

"""
"""

from __future__ import print_function, unicode_literals


import os
import sys

from workflow import Workflow, ICON_INFO


GITHUB_SLUG = 'deanishe/alfred-workflow-dummy'
VERSION = open(os.path.join(os.path.dirname(__file__),
                            'version')).read().strip()

log = None


def main(wf):
    query = None
    if len(wf.args):
        query = wf.args[0]

    wf.add_item('Current version : {}'.format(VERSION),
                'Version currently installed', icon=ICON_INFO)

    wf.send_feedback()


if __name__ == '__main__':
    update_settings = {'github_slug': GITHUB_SLUG, 'version': VERSION}
    wf = Workflow(update_settings=update_settings)
    log = wf.logger
    sys.exit(wf.run(main))

# -*- coding: utf-8 -*-
"""pavement.py -- paver tasks for doesitrockyet.com
"""
from paver.easy import *


@task
def sync():
    sh(
        ('s3cmd sync ./ s3://cache.doesitrockyet.com '
         '--recursive --exclude=".git*" '
         '--acl-public --guess-mime-type '
         '--add-header="Cache-Control:public"'
         )
        )

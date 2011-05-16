# -*- coding: utf-8 -*-
"""pavement.py -- paver tasks for doesitrockyet.com
"""
from paver.easy import *


@task
def s3sync():
    """Sync the files to S3/Cloudfront.
    """
    sh(
        ('s3cmd sync ./ s3://cache.doesitrockyet.com '
         '--recursive --exclude=".git*" '
         '--acl-public --guess-mime-type '
         '--add-header="Cache-Control:public"'
         )
        )


@task
def sync():
    """Sync the files to the webhost.
    """
    sh('rsync -ravz ./ --exclude=".git*" eykd@doesitrockyet.com:webapps/com_doesitrockyet__static/')


@task
@needs('s3sync', 'sync')
def deploy():
    """Deploy the site.
    """
    pass

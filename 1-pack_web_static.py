#!/usr/bin/python3
""" In this Function we conpress a folder to be sent to the web server """

from datetime import datetime
from fabric.api import local
import io


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except Exception:
        return None

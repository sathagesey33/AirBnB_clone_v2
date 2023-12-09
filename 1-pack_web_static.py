#!/usr/bin/python3
"""
A script to generate .tgz file from the contents of webstatic
usage: fab -f 1-pack_web_static.py do_pack
"""
from fabric.api import local
from datetime import datetime
from fabric.api import task
import os


@task
def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Archive path if generated successfully, None otherwise.
    """
    try:
        # Create the 'versions' folder if it doesn't exist
        local("mkdir -p versions")

        # Get the current date and time
        now = datetime.now()
        date_time = now.strftime("%Y%m%d%H%M%S")

        # Set the archive path and name
        archive_path = "versions/web_static_{}.tgz".format(date_time)

        # Create the .tgz archive
        print("Packing web_static to {}".format(archive_path))
        local("tar -cvzf {} web_static".format(archive_path))

        # Check if the archive was created successfully
        if os.path.exists(archive_path):
            return archive_path
        else:
            return None

    except Exception as e:
        print("Error: {}".format(str(e)))
        return None

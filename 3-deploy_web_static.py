#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["54.87.157.124", "54.146.73.232"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Distribute archive.
    """
    if os.path.exists(archive_path):
        # Extracting necessary information from the archive_path
        archived_file = archive_path.split("/")[-1]
        filename_no_ext = os.path.splitext(archived_file)[0]

        # Remote paths on the server
        newest_version = "/data/web_static/releases/" + filename_no_ext
        archived_file_remote = "/tmp/" + archived_file

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file_remote,
                                             newest_version))

        # Delete the archive from the web server
        run("sudo rm {}".format(archived_file_remote))

        # Move content to the correct location
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))

        # Remove unnecessary directory
        run("sudo rm -rf {}/web_static".format(newest_version))

        # Delete the symbolic link /data/web_static/current from the web server
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current on the web server
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False


@task
def deploy():
    # deploys static file to then servers
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


@task
def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Archive path if generated successfully, None otherwise.
    """
    try:
        # Create the 'versions' folder if it doesn't exist
        if local("mkdir -p versions").failed is True:
            return None

        # Get the current date and time
        now = datetime.now()
        date_time = now.strftime("%Y%m%d%H%M%S")

        # Set the archive path and name
        archive_path = "versions/web_static_{}.tgz".format(date_time)

        # Create the .tgz archive
        print("Packing web_static to {}".format(archive_path))
        if local("tar -cvzf {} web_static".format(
                archive_path)).failed is True:
            print("anything")
            return None

        # Check if the archive was created successfully
        if os.path.exists(archive_path):
            return archive_path
        else:
            return print("no path")
    except Exception as e:
        print("Error: {}".format(str(e)))
        return None

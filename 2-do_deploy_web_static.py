#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import env, put, run
import os

env.hosts = ['<54.227.128.48>', '<100.25.119.208>']
env.user = os.environ['ubuntu']
env.key_filename = os.environ['~/.ssh/id_rsa']


def do_deploy(archive_path):
    """Deploys the archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress archive to folder /data/web_static/releases/<archive filename without extension>
        filename = os.path.basename(archive_path)
        folder_name = "/data/web_static/releases/" + os.path.splitext(filename)[0]
        run("sudo mkdir -p {}".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C {} --strip-components=1".format(filename, folder_name))

        # Delete the archive from the web server
        run("sudo rm /tmp/{}".format(filename))

        # Delete the symbolic link /data/web_static/current from the web server
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current on the web server
        run("sudo ln -s {} /data/web_static/current".format(folder_name))

        return True

    except:
        return False

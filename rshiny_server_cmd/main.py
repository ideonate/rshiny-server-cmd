# With thanks to https://github.com/ryanlovett/jupyter-shiny-proxy/

import os
import logging
from tempfile import NamedTemporaryFile
import getpass
import subprocess

import click

class RShinyServerException(Exception):
    pass

def get_server_conf(command, dirname, port):
    return """

        run_as {user};
        
        server {{
            listen {port};
            location / {{
                site_dir {site_dir};
                log_dir {site_dir}/logs;
                bookmark_state_dir {site_dir}/bookmarks;
                directory_index on;
            }}
        }}

    """.format(
        user=getpass.getuser(),
        port=str(port),
        site_dir=dirname
    )

@click.command()
@click.option('--port', default=8888, type=click.INT, help='port for the proxy server to listen on')
@click.option('--ip', default=None, help='Address to listen on')
@click.option('--debug/--no-debug', default=False, help='To display debug level logs')
@click.argument('command', nargs=1, required=True)
def run(port, ip, debug, command):

    if debug:
        print('Setting debug')


    # Command can be absolute, or could be relative to cwd
    app_r_path = os.path.join(os.getcwd(), command)

    print("Fetching R script or folder {}".format(app_r_path))

    dirname = os.path.dirname(app_r_path)

    print("CWD to {}".format(dirname))

    os.chdir(dirname)

    with NamedTemporaryFile(mode='w', delete=False) as conf_file:

        conf_str = get_server_conf(command, dirname, port)

        conf_file.write(conf_str)

        conf_file.close()

        subprocess.run(['shiny-server', conf_file.name])

        os.unlink(conf_file.name)
     
    
if __name__ == '__main__':

    try:

        run()

    except SystemExit as se:
        print('Caught SystemExit {}'.format(se))

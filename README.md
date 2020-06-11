# rshiny-server-cmd

Command line wrapper to run a named R Shiny Server script/folder.

This project is used in [ContainDS Dashboards](https://github.com/ideonate/cdsdashboards), which is a user-friendly 
way to launch Jupyter notebooks as shareable dashboards inside JupyterHub. Also works with Streamlit and other 
visualization frameworks.

## Install and Run

Install using pip.

```
pip install rshiny-server-cmd
```

The file to start is specified on the command line, for example:

```
rshiny-server-cmd ~/Dev/myrfile.R
```

By default the server will listen on port 8888

To specify a different port, use the --port flag.

```
rshiny-server-cmd --port=8888 ~/Dev/myrfile.R
```

To run directly in python: `python -m rshiny_server_cmd.main <rest of command line>`

## Other command line args

--debug

--ip

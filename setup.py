import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

# read requirements.txt
with open('requirements.txt', 'r') as f:
    content = f.read()
li_req = content.split('\n')
install_requires = [e.strip() for e in li_req if len(e)]

setuptools.setup(
    name="rshiny-server-cmd",
    version="0.0.1",
    author="Dan Lester",
    author_email="dan@ideonate.com",
    description="Command line wrapper to run an R Shiny Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ideonate/rshiny-server-cmd",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["rshiny-server-cmd = rshiny_server_cmd.main:run"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)



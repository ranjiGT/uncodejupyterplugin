import setuptools

setuptools.setup(
    name="uncodejupyterplugin",
    version='0.1.0',
    url="https://github.com/ranjiGT/uncode-jupyterplugin",
    author="Ranji Raj",
    description="JupyterHub Plugin for submitting files to UNCode",
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook',
        'jupyterhub',
        'bs4',
        'gitpython',
        'requests'
    ],
    package_data={'uncodejupyterplugin': ['static/*']},
)

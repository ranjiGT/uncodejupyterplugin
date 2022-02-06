####################### Changes in jupyterhub_config.py ###########################
if [ ! -f ~/.jupyter/jupyterhub_config.py ]; then
   jupyterhub --generate-config
fi

echo 'c.NotebookApp.disable_check_xsrf = True' >> ~/.jupyter/jupyterhub_config.py

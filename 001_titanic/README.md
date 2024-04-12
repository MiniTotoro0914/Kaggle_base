# pipのtimeout対策　どっちか
export PIP_DEFAULT_TIMEOUT=1000
sudo pip --default-timeout=1000 install [MODULE_NAME]
例）
pip --default-timeout=1000 --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org install torch

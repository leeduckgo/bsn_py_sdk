virtualenv --no-site-packages venv
pip3 install ipython
touch .startup.py
echo "export PYTHONSTARTUP=.startup.py" > .envrc
direnv allow
source venv/bin/activate

virtualenv --no-site-packages venv
source venv/bin/activate
pip3 install ipython
touch .startup.py
echo "export PYTHONSTARTUP=.startup.py" > .envrc
direnv allow

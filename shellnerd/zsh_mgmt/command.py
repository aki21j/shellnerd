import os
import subprocess
import sys

from shellnerd import cli
from PyInquirer import prompt
from shellnerd.utils.logger import logger
from shellnerd.utils.utils import style, get_script_path, default_menu_or_exit
from shellnerd.questions import retrieve_questions

dir_path = os.path.dirname(os.path.realpath(__file__))

def init():
    selected = prompt(retrieve_questions('zsh', 'init'), style=style)
    if selected['zsh'] == "install":
        script_path = get_script_path(dir_path,"install-zsh.sh")
        subprocess.run(['bash', script_path])
    elif selected['zsh'] == "ls-themes":
        script_path = get_script_path(dir_path,"ls-themes.sh")
        subprocess.run(['bash', script_path])
    elif selected['zsh'] == "set-theme":
        script_path = get_script_path(dir_path,"set-theme.sh")
        inp = prompt(retrieve_questions('zsh','set_theme_ques'), style=style)
        subprocess.run(['bash', script_path, inp['set_theme_name']])
    else:
        default_menu_or_exit(selected['zsh'])
    init()

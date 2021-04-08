import os
import subprocess
import sys

from plonk import cli
from PyInquirer import prompt
from plonk.utils.logger import logger
from plonk.utils.utils import style, get_script_path

dir_path = os.path.dirname(os.path.realpath(__file__))

questions = [
    {
        'type': 'list',
        'name': 'zsh',
        'message': 'What do you want?',
        'choices': [
            {
                'key': 0,
                'name': 'Install ZSH',
                'value': 'install'
            },
            {
                'key': 1,
                'name': 'List available themes',
                'value': 'ls-themes'
            },
            {
                'key': 2,
                'name': 'Set theme',
                'value': 'set-theme'
            },
            {
                'key': 3,
                'name': 'Go to Main Menu',
                'value': 'main-menu'
            },
            {
                'key': 4,
                'name': 'Exit',
                'value': 'exit'
            }
        ]
    }
]

set_theme_ques = {
    'type': 'input',
    'name': 'set_theme_name',
    'message': 'Enter name of the theme to be set:'
}

def init():
    selected = prompt(questions, style=style)
    if selected['zsh'] == "install":
        script_path = get_script_path(dir_path,"install-zsh.sh")
        print(script_path)
        subprocess.run(['bash', script_path])
    elif selected['zsh'] == "ls-themes":
        script_path = get_script_path(dir_path,"ls-themes.sh")
        print(script_path)
        subprocess.run(['bash', script_path])
    elif selected['zsh'] == "set-theme":
        script_path = get_script_path(dir_path,"set-theme.sh")
        print(script_path)
        inp = prompt(set_theme_ques, style=style)
        subprocess.run(['bash', script_path, inp['set_theme_name']])
    elif selected['zsh'] == 'main-menu':
        cli.main()
    elif selected['zsh'] == 'exit':
        logger.info("Exiting...")
        sys.exit(0)

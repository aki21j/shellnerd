import subprocess
import os
from PyInquirer import style_from_dict, Token, prompt, Separator
from utils import style, check_package_existence, install_package
from logger import logger


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
            }
        ]
    }
]

set_theme_ques =  {
        'type': 'input',
        'name': 'set_theme_name',
        'message': 'Enter name of the theme to be set:'
}

def init_zsh():
  selected = prompt(questions, style=style)
  if selected['zsh'] == "install":
    subprocess.run(['bash', 'zshMgmt/commands/install-zsh.sh'])
  elif selected['zsh'] == "ls-themes":
    subprocess.run(['bash', 'zshMgmt/commands/ls-themes.sh'])
  elif selected['zsh'] == "set-theme":
    inp = prompt(set_theme_ques, style=style)
    subprocess.run(['bash', 'zshMgmt/commands/set-theme.sh', inp['set_theme_name']])

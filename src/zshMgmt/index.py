import subprocess
import os,sys
from PyInquirer import style_from_dict, Token, prompt, Separator
from utils import style, check_package_existence, install_package
from logger import logger
import main as Main

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
  elif selected['zsh'] == 'main-menu':
    Main.main()
  elif selected['zsh'] == 'exit':
    logger.info("Exiting...")
    sys.exit(0)
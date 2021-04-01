from PyInquirer import style_from_dict, Token, prompt, Separator
import sys

from utils import style
from logger import logger

from zshMgmt import index as Zsh
from gitMgmt import index as Git

questions = [
    {
        'type': 'list',
        'name': 'init_choice',
        'message': 'What do you want to do?',
        'choices': [
            {
                'key': 0,
                'name': 'ZSH Management',
                'value': 'zsh-mgmt'
            },
            {
                'key': 1,
                'name': 'GIT Config Management',
                'value': 'git-mgmt'
            },
            {
                'key': 2,
                'name': 'Exit',
                'value': 'exit'
            }
        ]
    }
]

def main():
  selected = prompt(questions, style=style)
  if selected['init_choice'] == "zsh-mgmt":
    # show zsh options
    Zsh.init_zsh()
  elif selected['init_choice'] == "git-mgmt":
    #show git options
    Git.init_git()
  elif selected['init_choice'] == 'exit':
    logger.info("Exiting...")
    sys.exit(0)



if __name__ == "__main__":
  main()
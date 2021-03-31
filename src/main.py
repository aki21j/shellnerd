from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

from utils import style
from zshMgmt import index as Zsh

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
            }
        ]
    }
]

def main(selected):
  print(selected['init_choice'])
  if selected['init_choice'] == "zsh-mgmt":
    # show zsh options
    Zsh.init_zsh()

  elif selected['init_choice'] == "git-mgmt":
    #show git options
    print("GIT")


if __name__ == "__main__":
  selected = prompt(questions, style=style)
  main(selected)
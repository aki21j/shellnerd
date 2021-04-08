#!/usr/bin/env bash

default_shell=${SHELL##*/}

if [[ "${default_shell}" =~ "zsh" ]]; then
    echo "> zsh is already set as your default shell."
fi
if [[ ! "${default_shell}" =~ "zsh" ]]; then
    echo '> Run the following commands to install zsh:
        sudo apt install zsh
        sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
        chsh -s $(which zsh)
    '
    echo "> Once done, log out and login again for the changes to take place."
fi
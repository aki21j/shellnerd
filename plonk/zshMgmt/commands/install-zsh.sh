#!/usr/plonk/env bash

default_shell=${SHELL##*/}

if [[ "${default_shell}" =~ "zsh" ]]; then
    echo "> zsh is already set as your default shell."
fi
if [[ ! "${default_shell}" =~ "zsh" ]]; then
    echo "> Installing zsh..."
    # install zsh
    sudo apt install zsh
    # download and install oh-my-zsh for themes and fonts
    sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
    # make zsh the default
    chsh -s $(which zsh)
    echo "> Log out and login again for the changes to take place."
fi
#!/usr/bin/env bash

themes_list=()

get_themes(){
  zsh_themes_dir=$ZSH/themes
  echo "> oh-my-zsh directory: $ZSH"

  files=($zsh_themes_dir/*)
  pos=$(( ${#files[*]} - 1 ))
  last=${files[$pos]}

  for entry in "$zsh_themes_dir"/*
  do
    theme_with_ext=${entry##*/}
    theme=$(echo "$theme_with_ext" | cut -f 1 -d '.')
    
    if [[ $entry == $last ]]
    then
      themes_list+=("$theme")
      break
    else
      themes_list+=("$theme,")
    fi
  done
}

set_theme(){
  get_themes

  if [[ ! "${themes_list[@]}" =~ "${1}" ]]; then
      # throw error if user choice is not available
      echo "> ERROR: $1 is not a valid theme"
  fi

  if [[ "${themes_list[@]}" =~ "${1}" ]]; then
      zshrc_path=$HOME/.zshrc
      update_command=s/^ZSH_THEME=.*/ZSH_THEME="${1}"/
      echo "> Updating zsh theme to: $1"
      sed -i "$update_command" $zshrc_path
      echo "> Run: source \$HOME/.zshrc or reload your terminal for the changes to take effect."
  fi

}

set_theme "$1"
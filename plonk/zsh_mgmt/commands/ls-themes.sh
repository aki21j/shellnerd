#!/usr/bin/env bash

# function to list all available oh-my-zsh themes
zsh_themes_dir=$ZSH/themes
echo "> oh-my-zsh directory: $ZSH"

themes_list=()

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
echo "> available oh-my-zsh themes: "
echo "${themes_list[@]}"
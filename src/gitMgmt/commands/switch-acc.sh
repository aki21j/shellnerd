#!/usr/bin/env bash

available_configs=()

get_configs(){
  config_file_path="$HOME/.ssh/ssh-config.json"
  available_configs+=$(jq "keys" $config_file_path)
}

use_config(){
  get_configs
  config_file_path="$HOME/.ssh/ssh-config.json"
  selected_config="${1}"

  if [[ ! "${available_configs[@]}" =~ "$selected_config" ]]; then
      # throw error if user choice is not available
      log_error "$1 is not a option"
  fi
  if [[ "${available_configs[@]}" =~ "$selected_config" ]]; then
      username=$(jq ".$selected_config.name" $config_file_path )
      email=$(jq ".$selected_config.email" $config_file_path )
      git config user.name $username
      git config user.email $email
      echo "> set username to $username and email to $email"
  fi
}

use_config "$1"
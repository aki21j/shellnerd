#!/usr/bin/env bash

use_config(){
  username="${1}"
  email="${2}"

  git config user.name $username
  git config user.email $email
  echo "> set username to $username and email to $email"
}

use_config "$1" "$2"
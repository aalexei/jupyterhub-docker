#!/bin/bash

input_file="users_list.txt"

# Ensure the file exists and is not empty
if [ ! -s $input_file ]; then
  echo "Input file is missing or empty."
  exit 1
fi

# Read each line from the file
while IFS=: read -r username password
do
  # Check if the user already exists
  if id "$username" &>/dev/null; then
    echo "User $username already exists!"
  else
    # Create a new user with the specified password
    useradd -m "$username"
    echo "$username:$password" | chpasswd
    echo "User $username created with the specified password."
  fi
done < "$input_file"

echo "All users have been created."


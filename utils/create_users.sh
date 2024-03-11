#!/bin/bash

# Specify the number of users
num_users=10

# File to store user and password
output_file="users_list.txt"

# Clear file content before appending
> $output_file

# Generate users with random passwords
for i in $(seq 1 $num_users)
do
  username="user$i"
  password=$(openssl rand -base64 12) # Generating a 12 character base64 password
  echo "$username:$password" >> $output_file
done

echo "Generated list of users with passwords in $output_file"


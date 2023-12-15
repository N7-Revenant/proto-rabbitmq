#!/usr/bin/env bash
set -o errexit
set -o nounset

wget -qO - http://tc-build.telecontact.ru/linux/debian/repository/repo-keys.asc | tee /etc/apt/trusted.gpg.d/telecc-repo-keys.asc

sh -c "echo 'deb http://tc-build.telecontact.ru/linux/debian/repository/tcdev/build/ lunar main
'>> /etc/apt/sources.list.d/telecc.list"

apt-get update -y --fix-missing
apt-get upgrade -y

sudo apt-get install rabbitmq-server -y

sudo rabbitmq-plugins enable rabbitmq_management

sudo rabbitmqctl add_user admin admin
sudo rabbitmqctl set_user_tags admin administrator
sudo rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

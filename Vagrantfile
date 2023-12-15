# -*- mode: ruby -*-
# vi: set ft=ruby :

PROJECT_NAME = "RabbitMQ 20.04 ENV"
BOX_REPO_URI = 'https://tc-build.telecontact.ru/artifact/repository/Vagrant.telecc/base-boxes'

Vagrant.configure("2") do |config|
  config.vm.box_url = "#{BOX_REPO_URI}/ubuntu-2004-amd64/index.json"
  config.vm.box = "ubuntu-2004-amd64"

  config.vm.provider 'virtualbox' do |machine|
    machine.name = "ub2004"
    machine.memory = 1024
    machine.cpus = 1
  end

  config.vm.define "ub2004" do |host|
    host.vm.hostname = "ub2004"
    host.vm.network "private_network", ip: "192.168.56.81"
  end

  config.vm.provision "shell", path: "bootstrap.sh"
end

# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/disco64"
  config.ssh.forward_agent = false
  config.vm.box_check_update = false

  config.vm.network "private_network", ip: "192.168.33.59"
  config.vm.synced_folder ".", "/vagrant_data"

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--name", "reports", "--memory", "3072", "--cpus", "2"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    # docker
    apt update
    apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    apt update
    apt-get install -y docker-ce=5:19.03.1~3-0~ubuntu-disco docker-ce-cli=5:19.03.1~3-0~ubuntu-disco containerd.io
    usermod -aG docker vagrant

    # docker-compose
    curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
  SHELL
end

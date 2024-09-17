Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  # Control Node
  config.vm.define "controlnode" do |control|
    control.vm.hostname = "controlnode"
    control.vm.network "private_network", ip: "192.168.56.100"
    control.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y ansible git openssh-client

      sudo -u vagrant mkdir -p /home/vagrant/.ssh
      sudo chmod 700 /home/vagrant/.ssh

      if [ ! -f /home/vagrant/.ssh/id_rsa ]; then
        sudo -u vagrant ssh-keygen -t rsa -b 2048 -f /home/vagrant/.ssh/id_rsa -N ""
      fi

      sudo chown vagrant:vagrant /home/vagrant/.ssh/id_rsa /home/vagrant/.ssh/id_rsa.pub
      sudo chmod 600 /home/vagrant/.ssh/id_rsa
      sudo chmod 644 /home/vagrant/.ssh/id_rsa.pub

      sudo -u vagrant bash -c 'cat /home/vagrant/.ssh/id_rsa.pub >> /home/vagrant/.ssh/authorized_keys'
      sudo chmod 600 /home/vagrant/.ssh/authorized_keys
      sudo chown vagrant:vagrant /home/vagrant/.ssh/authorized_keys

      sudo -u vagrant git clone https://github.com/samgabrail/env0-ansible-playbooks-tutorial.git /home/vagrant/ansible/env0-ansible-playbooks-tutorial

      cp /home/vagrant/.ssh/id_rsa.pub /vagrant/control_node_key.pub
    SHELL
  end

  # For other VMs (webserver1, webserver2, dbserver)
  ["webserver1", "webserver2", "dbserver"].each do |server|
    config.vm.define server do |node|
      node.vm.hostname = server
      ips = {"webserver1" => "101", "webserver2" => "102", "dbserver" => "103"}
      node.vm.network "private_network", ip: "192.168.56.#{ips[server]}"
      node.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y openssh-server

        sudo -u vagrant mkdir -p /home/vagrant/.ssh
        sudo chmod 700 /home/vagrant/.ssh

        cat /vagrant/control_node_key.pub >> /home/vagrant/.ssh/authorized_keys
        sudo chmod 600 /home/vagrant/.ssh/authorized_keys
        sudo chown -R vagrant:vagrant /home/vagrant/.ssh
      SHELL
    end
  end
end

Vagrant.configure("2") do |config|
    # Define the base box for all machines
    config.vm.box = "ubuntu/focal64"
  
    # Control Node
    config.vm.define "controlnode" do |control|
      control.vm.hostname = "controlnode"
      control.vm.network "private_network", ip: "192.168.56.100"
      control.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y ansible git openssh-client

        # Create .ssh directory if it doesn't exist
        sudo -u vagrant mkdir -p /home/vagrant/.ssh
        sudo chmod 700 /home/vagrant/.ssh

        # Generate SSH keys if they don't exist
        if [ ! -f /home/vagrant/.ssh/rsa_id ]; then
          sudo -u vagrant ssh-keygen -t rsa -b 2048 -f /home/vagrant/.ssh/rsa_id -N ""
        fi

        # Set ownership and permissions
        sudo chown vagrant:vagrant /home/vagrant/.ssh/rsa_id /home/vagrant/.ssh/rsa_id.pub
        sudo chmod 600 /home/vagrant/.ssh/rsa_id
        sudo chmod 644 /home/vagrant/.ssh/rsa_id.pub

        # Add public key to authorized_keys for SSH access
        sudo -u vagrant bash -c 'cat /home/vagrant/.ssh/rsa_id.pub >> /home/vagrant/.ssh/authorized_keys'
        sudo chmod 600 /home/vagrant/.ssh/authorized_keys
        sudo chown vagrant:vagrant /home/vagrant/.ssh/authorized_keys

        # Clone the Ansible playbooks repository
        sudo -u vagrant git clone https://github.com/samgabrail/env0-ansible-playbooks-tutorial.git /home/vagrant/ansible/env0-ansible-playbooks-tutorial
      SHELL
      
      # Optional synced folder to share files between host and control node
      control.vm.synced_folder ".", "/home/vagrant/ansible", type: "virtualbox"
    end
  
    # Web Server 1
    config.vm.define "webserver1" do |web1|
      web1.vm.hostname = "webserver1"
      web1.vm.network "private_network", ip: "192.168.56.101"
      web1.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y openssh-server

        # Create .ssh directory
        sudo -u vagrant mkdir -p /home/vagrant/.ssh
        sudo chmod 700 /home/vagrant/.ssh

        # Add control node's public key to authorized_keys
        sudo -u vagrant bash -c 'cat /home/vagrant/ansible/env0-ansible-playbooks-tutorial/rsa_id.pub >> /home/vagrant/.ssh/authorized_keys'
        sudo chmod 600 /home/vagrant/.ssh/authorized_keys
        sudo chown -R vagrant:vagrant /home/vagrant/.ssh
      SHELL
    end
  
    # Web Server 2
    config.vm.define "webserver2" do |web2|
      web2.vm.hostname = "webserver2"
      web2.vm.network "private_network", ip: "192.168.56.102"
      web2.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y openssh-server

        # Create .ssh directory
        sudo -u vagrant mkdir -p /home/vagrant/.ssh
        sudo chmod 700 /home/vagrant/.ssh

        # Add control node's public key to authorized_keys
        sudo -u vagrant bash -c 'cat /home/vagrant/ansible/env0-ansible-playbooks-tutorial/rsa_id.pub >> /home/vagrant/.ssh/authorized_keys'
        sudo chmod 600 /home/vagrant/.ssh/authorized_keys
        sudo chown -R vagrant:vagrant /home/vagrant/.ssh
      SHELL
    end
  
    # Database Server
    config.vm.define "dbserver" do |db|
      db.vm.hostname = "dbserver"
      db.vm.network "private_network", ip: "192.168.56.103"
      db.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y openssh-server

        # Create .ssh directory
        sudo -u vagrant mkdir -p /home/vagrant/.ssh
        sudo chmod 700 /home/vagrant/.ssh

        # Add control node's public key to authorized_keys
        sudo -u vagrant bash -c 'cat /home/vagrant/ansible/env0-ansible-playbooks-tutorial/rsa_id.pub >> /home/vagrant/.ssh/authorized_keys'
        sudo chmod 600 /home/vagrant/.ssh/authorized_keys
        sudo chown -R vagrant:vagrant /home/vagrant/.ssh
      SHELL
    end
  end
  
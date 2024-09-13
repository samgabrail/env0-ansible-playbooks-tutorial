Vagrant.configure("2") do |config|
    # Define the base box for all machines
    config.vm.box = "ubuntu/focal64"
  
    # Control Node
    config.vm.define "controlnode" do |control|
      control.vm.hostname = "controlnode"
      control.vm.network "private_network", ip: "192.168.56.100"
      control.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y ansible
      SHELL
      # Optional synced folder to share files between host and control node
      control.vm.synced_folder ".", "/home/vagrant/ansible", type: "virtualbox"
    end
  
    # Web Server 1
    config.vm.define "webserver1" do |web1|
      web1.vm.hostname = "webserver1"
      web1.vm.network "private_network", ip: "192.168.56.101"
    end
  
    # Web Server 2
    config.vm.define "webserver2" do |web2|
      web2.vm.hostname = "webserver2"
      web2.vm.network "private_network", ip: "192.168.56.102"
    end
  
    # Database Server
    config.vm.define "dbserver" do |db|
      db.vm.hostname = "dbserver"
      db.vm.network "private_network", ip: "192.168.56.103"
    end
  end
  
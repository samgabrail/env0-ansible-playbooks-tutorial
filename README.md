# Overview
This is a Tutorial for Ansible Playbooks


## Get started

Run `vagrant up`

This will create 4 VMs:

- A Linux control node to run Ansible from
- 2 webservers
- 1 database server

To access the VMs, use `vagrant ssh controlnode`, `vagrant ssh webserver1`, `vagrant ssh webserver2`, and `vagrant ssh dbserver`

## Run the playbook

Run the playbook with `ansible-playbook -i inventory techcorp_playbook.yaml`


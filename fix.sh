cd ..
rm -rf env0-ansible-playbooks-tutorial/
git clone https://github.com/samgabrail/env0-ansible-playbooks-tutorial.git
cd env0-ansible-playbooks-tutorial
ansible-playbook -i inventory techcorp_playbook_advanced.yaml
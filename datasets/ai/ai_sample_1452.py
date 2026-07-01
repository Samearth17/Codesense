---
 - name: Deploy web application
 hosts: server
 tasks:
 - name: Transfer application files
 copy:
 src: '{{ application }}'
 dest: /var/www/app

- name: Create web environment
 command: python create_env.py
 args:
 chdir: /var/www/app

- name: Configure web server
 command: ansible-playbook web.yml

- name: Restart web server
 service: name=nginx state=restarted
---
- name: A simple playbook to demonstrate Ansible capabilities
  hosts: all
  become: yes

  vars:
    web_package: nginx
    web_service: nginx
    html_path: /var/www/html/index.html

  tasks:
    - name: Update apt cache (for Debian/Ubuntu)
      ansible.builtin.apt:
        update_cache: yes
        cache_valid_time: 3600
      when: ansible_os_family == "Debian"

    - name: Install the web server package
      ansible.builtin.package:
        name: "{{ web_package }}"
        state: present

    - name: Create a custom index.html with hostname information
      ansible.builtin.copy:
        content: |
          <h1>Welcome from {{ ansible_hostname }}</h1>
          <p>Served by Ansible</p>
        dest: "{{ html_path }}"
        owner: www-data
        group: www-data
        mode: '0644'
      notify: restart web service

    - name: Start and enable the web service
      ansible.builtin.service:
        name: "{{ web_service }}"
        state: started
        enabled: yes

    - name: Install several helpful packages using a loop
      ansible.builtin.package:
        name: "{{ item }}"
        state: present
      loop:
        - curl
        - git
        - htop

    - name: Check disk usage on the root filesystem
      ansible.builtin.command: df -h /
      register: disk_usage
      changed_when: false

    - name: Display disk usage information
      ansible.builtin.debug:
        msg: "Disk usage on /: {{ disk_usage.stdout_lines }}"

  handlers:
    - name: restart web service
      ansible.builtin.service:
        name: "{{ web_service }}"
        state: restarted

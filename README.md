# **Manage repositories**

This role enables you to manage repositories on **debian-based** distributions. It can be used on its own , or be called by other roles the configure repositories on demand.

## **Requirements**

None.

## **Role Variables**

### Default repositories

```yaml
manage_repositories_enable_default_repo: true
```

This variable enables or disables the configuration of the main distribution repositories. Setting this to `false` will not configure the default apt repositories for the host.

```yaml
manage_repositories_main_repo_uri:
  ubuntu: "http://fr.archive.ubuntu.com/ubuntu"
  debian: "http://deb.debian.org/debian"
```

This variable sets the mirror URLs for the main repositories.

### Custom repositories

```yaml
manage_repositories_enable_custom_repo: false
```

This variable enables the configuration of custom repositories.

```yaml
manage_repositories_custom_repo:
  - name: docker
    uri: "https://download.docker.com/linux/{{ ansible_distribution|lower }}"
    comments: "{{ ansible_distribution|lower }} docker repository"
    types:
      - deb
    suites:
      - "{{ ansible_distribution_release }}"
    components:
      - stable
    signed_by: "https://download.docker.com/linux/{{ ansible_distribution|lower }}/gpg"
  - name: ...
```

This variable contains a list (1 to N) of custom repositories to install. IT HAS TO BE SET if `manage_repositories_enable_custom_repo == true`, or else the role might fail. The above example highlights the different options you can set per repository. See the [deb822 module documentation](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/deb822_repository_module.html) for more details. Note that not all options in the module are currently supported.

## **Dependencies**

None.

## **Example Playbook**

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednz_cloud.manage_repositories
```

```yaml
# calling the role inside a playbook and injecting variables (in another role for example)
- hosts: servers
  tasks:
    - name: "Configure hashicorp repository"
      ansible.builtin.include_role:
        name: ednz_cloud.manage_repositories
      vars:
        manage_repositories_enable_default_repo: false
        manage_repositories_enable_custom_repo: true
        manage_repositories_custom_repo:
          - name: docker
            uri: "https://download.docker.com/linux/{{ ansible_distribution|lower }}"
            comments: "{{ ansible_distribution|lower }} docker repository"
            types:
              - deb
            suites:
              - "{{ ansible_distribution_release }}"
            components:
              - stable
            signed_by: "https://download.docker.com/linux/{{ ansible_distribution|lower }}/gpg"
```

## **License**

MIT / BSD

## **Author Information**

This role was created by Bertrand Lanson in 2023.

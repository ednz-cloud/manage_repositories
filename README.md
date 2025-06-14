<!-- DOCSIBLE START -->

# 📃 Role overview

## manage_repositories



Description: Repository management for debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 14/06/2025 |








### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [manage_repositories_enable_default_repo](defaults/main.yml#L9)   | bool   | `True` |    false  |  Enable or disable the default repository management. |
| [manage_repositories_main_repo_uri](defaults/main.yml#L16)   | dict   | `{'ubuntu': 'http://fr.archive.ubuntu.com/ubuntu', 'debian': 'http://deb.debian.org/debian'}` |    true  |  The main repository URI for the distribution. |
| [manage_repositories_enable_custom_repo](defaults/main.yml#L24)   | bool   | `False` |    false  |  Enable or disable the custom repository management. |
| [manage_repositories_custom_repo](defaults/main.yml#L50)   | list   | `[]` |    false  |  Custom repositories to be managed. |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<b>manage_repositories_enable_default_repo:</b> Enable or disable the default repository management.<br>
If set to true, the default repositories for the distribution will be managed.<br>
<br>
<b>manage_repositories_main_repo_uri:</b> The main repository URI for the distribution.<br>
This is used to set the main repository for the distribution.<br>
<br>
<b>manage_repositories_enable_custom_repo:</b> Enable or disable the custom repository management.<br>
<br>
<b>manage_repositories_custom_repo:</b> A list of custom repositories to be managed.<br>
Each repository should be a dictionary with the following keys:<br>
- name: The name of the repository.<br>
- uri: The URI of the repository.<br>
- comments: A comment for the repository.<br>
- types: The types of the repository (e.g., deb, rpm).<br>
- suites: The suites of the repository (e.g., stable, testing).<br>
- components: The components of the repository (e.g., main, universe).<br>
- signed_by: The URI of the GPG key for the repository. (optional).<br>
See the deb822 module documentation for more details.<br>
Example:<br>
- name: docker<br>
uri: "https://download.docker.com/linux/{{ ansible_distribution|lower }}"<br>
comments: "{{ ansible_distribution|lower }} docker repository"<br>
types:<br>
- deb<br>
suites:<br>
- "{{ ansible_distribution_release }}"<br>
components:<br>
- stable<br>
signed_by: "https://download.docker.com/linux/{{ ansible_distribution|lower }}/gpg"<br>
<br>
<br>
</details>


### Vars

**These are variables with higher priority**
#### File: vars/debian.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [manage_repositories_default_repo](vars/debian.yml#L7)   | list   | `[{'name': 'debian', 'uri': '{{ manage_repositories_main_repo_uri[ansible_distribution¦lower] }}', 'comments': 'debian main repository', 'types': ['deb'], 'suites': ['{{ ansible_distribution_release }}', '{{ ansible_distribution_release }}-updates', '{{ ansible_distribution_release }}-backports'], 'components': ['main']}, {'name': 'debian-security', 'uri': '{{ manage_repositories_main_repo_uri[ansible_distribution¦lower] }}-security', 'comments': 'debian main repository', 'types': ['deb'], 'suites': ['{{ ansible_distribution_release }}-security'], 'components': ['main']}]` |    true  |  Default repository configuration for Debian distributions. |
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [manage_repositories_sources_list_location](vars/main.yml#L7)   | str   | `/etc/apt/sources.list` |    true  |  Location of the sources list file. |
| [manage_repositories_repo_location](vars/main.yml#L12)   | str   | `/etc/apt/sources.list.d` |    true  |  Location of the repository files. |
| [manage_repositories_signing_keys_location](vars/main.yml#L17)   | str   | `/usr/share/keyrings` |    true  |  Location of the signing keys. |
| [manage_repositories_sources_list_message](vars/main.yml#L22)   | str   | `# See /etc/apt/sources.list.d/{{ ansible_distribution¦lower }}.sources\n` |    true  |  Comment for the sources list file. |
| [manage_repositories_required_packages](vars/main.yml#L27)   | list   | `['python3-debian']` |    true  |  Required packages for managing repositories. |
#### File: vars/ubuntu.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [manage_repositories_default_repo](vars/ubuntu.yml#L7)   | list   | `[{'name': 'ubuntu', 'uri': '{{ manage_repositories_main_repo_uri[ansible_distribution¦lower] }}', 'comments': 'ubuntu main repository', 'types': ['deb'], 'suites': ['{{ ansible_distribution_release }}', '{{ ansible_distribution_release }}-security', '{{ ansible_distribution_release }}-updates', '{{ ansible_distribution_release }}-backports'], 'components': ['main', 'restricted', 'universe', 'multiverse']}]` |    true  |  Default repository configuration for Ubuntu distributions. |
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/debian.yml</b></summary>
<br>
<b>manage_repositories_default_repo:</b> This variable defines the default repositories for Debian distributions.
<br>
<br>
</details>
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/main.yml</b></summary>
<br>
<b>manage_repositories_sources_list_location:</b> This variable defines the location of the sources list file for the package manager.
<br>
<b>manage_repositories_repo_location:</b> This variable defines the location of the repository files for the package manager.
<br>
<b>manage_repositories_signing_keys_location:</b> This variable defines the location of the signing keys for the package manager.
<br>
<b>manage_repositories_sources_list_message:</b> This variable defines the comment for the sources list file (because it is not used).
<br>
<b>manage_repositories_required_packages:</b> This variable defines the packages required for managing repositories.
<br>
<br>
</details>
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/ubuntu.yml</b></summary>
<br>
<b>manage_repositories_default_repo:</b> This variable defines the default repositories for Ubuntu distributions.
<br>
<br>
</details>


### Tasks


#### File: tasks/custom_repositories.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| APT Repo ¦ Configure custom repositories | ansible.builtin.deb822_repository | False |
| APT Repo ¦ Set cache-update variable | ansible.builtin.set_fact | True |

#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| APT Repo ¦ Set cache-update variable | ansible.builtin.set_fact | False |
| APT Repo ¦ Load variables | ansible.builtin.include_vars | False |
| APT Repo ¦ Import prerequisites.yml | ansible.builtin.include_tasks | False |
| APT Repo ¦ Import main repositories for {{ ansible_distribution¦lower }} | ansible.builtin.include_tasks | True |
| APT Repo ¦ Import custom_repositories.yml | ansible.builtin.include_tasks | True |
| APT Repo ¦ Update apt caches | ansible.builtin.apt | True |

#### File: tasks/main_repositories.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| APT Repo ¦ Emtpy /etc/apt/sources.list | block | False |
| APT Repo ¦ Read the current content of source.list | ansible.builtin.slurp | False |
| APT Repo ¦ Convert sources.list current content to string | ansible.builtin.set_fact | False |
| APT Repo ¦ Define sources.list new content | ansible.builtin.set_fact | False |
| APT Repo ¦ Create file /etc/apt/sources.list | ansible.builtin.file | True |
| APT Repo ¦ Replace content of /etc/apt/sources.list | ansible.builtin.replace | True |
| APT Repo ¦ Configure main repositories into sources.list.d for {{ ansible_distribution¦lower }}  | ansible.builtin.deb822_repository | False |
| APT Repo ¦ Set cache-update variable | ansible.builtin.set_fact | True |

#### File: tasks/prerequisites.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| APT Repo ¦ Update repositories cache | ansible.builtin.apt | False |
| APT Repo ¦ Install required packages | ansible.builtin.apt | False |







## Author Information
Bertrand Lanson

#### License

license (BSD, MIT)

#### Minimum Ansible Version

2.10

#### Platforms

- **Ubuntu**: ['focal', 'jammy', 'noble']
- **Debian**: ['bullseye', 'bookworm']


#### Dependencies

No dependencies specified.
<!-- DOCSIBLE END -->

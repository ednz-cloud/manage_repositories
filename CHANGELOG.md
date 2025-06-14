## v0.2.0 (2025-06-14)

### Feat

- remove validity timeout for cache update

## v0.1.0 (2024-12-20)

### Feat

- add support for ubuntu noble
- use deb822 module for custom repositories
- **core**: change namespace
- remove become from role, fix #6
- change default sample file to provide a better example of custom variables
- add vagrant test, remove cache_time=0 when installing python3-debian
- add vagrant molecule scenarios (for later pipelines)
- use become for handler
- add become statements to avoid relying on ansible.cfg

### Fix

- update required package list variable after removal of manage_apt_packages dependency
- fixed a comment

"""Role testing files using testinfra."""

def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_source_list_default(host):
    """Validate /etc/apt/sources.list file."""
    etc_apt_sources_list_default = host.file("/etc/apt/sources.list")
    dist_os = host.system_info.distribution
    dist_codename = host.system_info.codename
    assert etc_apt_sources_list_default.exists
    assert etc_apt_sources_list_default.user == "root"
    assert etc_apt_sources_list_default.group == "root"
    assert etc_apt_sources_list_default.mode == 0o644
    if dist_os == "debian":
        assert etc_apt_sources_list_default.contains("deb http://deb.debian.org/debian " + dist_codename + " main contrib")
        assert etc_apt_sources_list_default.contains("deb http://deb.debian.org/debian " + dist_codename + "-updates main contrib")
        assert etc_apt_sources_list_default.contains("deb http://deb.debian.org/debian-security " + dist_codename + "-security main contrib")
        assert etc_apt_sources_list_default.contains("deb http://deb.debian.org/debian " + dist_codename + "-backports main")
    elif dist_os == "ubuntu":
        assert etc_apt_sources_list_default.contains("deb http://fr.archive.ubuntu.com/ubuntu " + dist_codename + " main restricted universe multiverse")
        assert etc_apt_sources_list_default.contains("deb http://fr.archive.ubuntu.com/ubuntu " + dist_codename + "-updates main restricted universe multiverse")
        assert etc_apt_sources_list_default.contains("deb http://fr.archive.ubuntu.com/ubuntu " + dist_codename + "-security main restricted universe multiverse")
        assert etc_apt_sources_list_default.contains("deb http://fr.archive.ubuntu.com/ubuntu " + dist_codename + "-backports main restricted universe multiverse")

def test_source_list_custom(host):
    """Validate /etc/apt/sources.list.d/custom.list file does not exist."""
    etc_apt_sources_list_custom = host.file("/etc/apt/sources.list.d/custom.list")
    assert not etc_apt_sources_list_custom.exists

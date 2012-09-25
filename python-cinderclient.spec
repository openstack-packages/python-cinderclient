%global snaptag 20120925git
Name:             python-cinderclient
Version:          0.2.26
Release:          0.1.%{snaptag}%{?dist}
Summary:          Python API and CLI for OpenStack cinder

Group:            Development/Languages
License:          ASL 2.0
URL:              http://github.com/openstack/python-cinderclient
Source0:          https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}~%{snaptag}.tar.gz

#
# patches_base=0.2
#

BuildArch:        noarch
BuildRequires:    python-setuptools

Requires:         python-httplib2
Requires:         python-prettytable
Requires:         python-setuptools

%description
This is a client for the OpenStack cinder API. There's a Python API (the
cinderclient module), and a command-line script (cinder). Each implements
100% of the OpenStack cinder API.

%prep
%setup -q

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove bundled egg-info
rm -rf python_cinderclient.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/tests

%files
%doc README.rst
%doc LICENSE
%{_bindir}/cinder
%{python_sitelib}/cinderclient
%{python_sitelib}/*.egg-info

%changelog
* Mon Sep 25 2012 Pádraig Brady <P@draigBrady.com> 0.2.26-0.1.20120925git
- Build from git to support latest cinder

* Mon Sep  3 2012 Pádraig Brady <P@draigBrady.com> 0.2-2
- Initial release

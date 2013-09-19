Name:             python-cinderclient
Version:          1.0.5
Release:          2%{?dist}
Summary:          Python API and CLI for OpenStack cinder

Group:            Development/Languages
License:          ASL 2.0
URL:              http://github.com/openstack/python-cinderclient
Source0:          http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

#
# patches_base=1.0.5
#
Patch0001: 0001-Remove-runtime-dependency-on-python-pbr.patch
Patch0002: 0002-Stop-pbr-from-installing-requirements-during-build.patch
Patch0003: 0003-Add-update_snapshot_metadata-action.patch

BuildArch:        noarch

BuildRequires:    python2-devel
BuildRequires:    python-setuptools
BuildRequires:    python-pbr
BuildRequires:    python-d2to1

Requires:         python-prettytable
Requires:         python-requests
Requires:         python-setuptools
Requires:         python-simplejson
Requires:         python-six

%description
This is a client for the OpenStack cinder API. There's a Python API (the
cinderclient module), and a command-line script (cinder). Each implements
100% of the OpenStack cinder API.

%prep
%setup -q

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATCINDERCLIENTVERSION/%{version}/ cinderclient/__init__.py

# Remove bundled egg-info
rm -rf python_cinderclient.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

install -p -D -m 644 tools/cinder.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/cinder.bash_completion

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/cinderclient/tests

%files
%doc LICENSE README.rst
%{_bindir}/cinder
%{python_sitelib}/cinderclient
%{python_sitelib}/*.egg-info
%{_sysconfdir}/bash_completion.d/cinder.bash_completion

%changelog
* Thu Sep 19 2013 Jakub Ruzicka <jruzicka@redhat.com> 1.0.5-2
- Add update_snapshot_metadata action

* Thu Sep 12 2013 Jakub Ruzicka <jruzicka@redhat.com> 1.0.5-1
- Update to upstream version 1.0.5.
- Update dependencies.
- Remove runtime dependency on python-pbr.
- Change Source0 to PyPI.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Jakub Ruzicka <jruzicka@redhat.com> 1.0.4-1
- Update to upstream version 1.0.4.

* Tue Apr 02 2013 Jakub Ruzicka <jruzicka@redhat.com> 1.0.3-1
- Update to upstream version 1.0.3.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Eric Harney <eharney@redhat.com> 1.0.2-1
- Add bash completion support
- Update to latest client

* Mon Sep 25 2012 Pádraig Brady <P@draigBrady.com> 0.2.26-1
- Update to latest client to support latest cinder

* Mon Sep  3 2012 Pádraig Brady <P@draigBrady.com> 0.2-2
- Initial release

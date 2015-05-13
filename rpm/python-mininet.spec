%global realname mininet

Name:           python-mininet
Version:        2.2.1
%define dist    none
Release:        1%{?dist}
Summary:        Emulator for rapid prototyping of Software Defined Networks

Packager:       arcolife
License:        BSD
URL:            http://mininet.org/
Source0:        https://github.com/mininet/mininet/archive/%{version}.tar.gz

Buildarch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

%description
Mininet is a network emulator which uses lightweight virtualization to create
virtual networks for rapid prototyping of Software-Defined Network (SDN)
designs using OpenFlow.

%prep
%setup -qn %{realname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{_bindir}/mn
%{python2_sitelib}/mininet/*
%{python2_sitelib}/mininet/examples/*

%doc README.md
%license LICENSE
%{python2_sitelib}/*.egg-info

%changelog
* Wed May 13 2015 Archit Sharma <archit.py@gmail.com> - 2.1.1
- Packaging 2.1.1 version

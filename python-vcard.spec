%define 	module	vcard
Summary:	vCard validator, class and utility functions
Name:		python-%{module}
Version:	0.7.4
Release:	1
License:	GPL v3
Group:		Development/Languages
URL:		http://sourceforge.net/projects/vcard-module/
Source0:	http://downloads.sourceforge.net/vcard-module/vCard-module-%{version}.tar.gz
# Source0-md5:	e34a32e41799d4a7065bb786d98b0a04
BuildRequires:	python-isodate
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-isodate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vCard validator, class and utility functions.

%prep
%setup -q -n vCard-module-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vcard
%dir %{py_sitescriptdir}/vcard
%{py_sitescriptdir}/vcard/*.py*
%{py_sitescriptdir}/vCard_module-%{version}*.egg-info

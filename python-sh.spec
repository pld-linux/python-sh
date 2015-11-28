#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	sh
Summary:	SH module for python
Summary(pl.UTF-8):	Moduł sh dla pythona
# Name must match the python module/package name (as in 'import' statement)
Name:		python-%{module}
Version:	1.08
Release:	1
License:	Free for use
Group:		Libraries/Python
Source0:	https://github.com/amoffat/sh/archive/%{version}.tar.gz
# Source0-md5:	a89e4600d9500210b78dbcefad63b443
URL:		https://amoffat.github.io/sh/
# remove BR: python-devel for 'noarch' packages.
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
# when using /usr/bin/env or other in-place substitutions
#BuildRequires:	sed >= 4.0
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
#Requires:		python-libs
Requires:		python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package -n python3-%{module}
Summary:	SH module for python 3
Summary(pl.UTF-8):	Moduł sh dla pythona 3
Group:		Libraries/Python

%description -n python3-%{module}

%description -n python3-%{module} -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.md CHANGELOG.md README.md
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/sh-*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS.md CHANGELOG.md README.md
%{py3_sitescriptdir}/*.py
%{py3_sitescriptdir}/__pycache__
%{py3_sitescriptdir}/%{module}-*.egg-info
%endif


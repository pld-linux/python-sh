#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module		sh
%define 	egg_name	sh
%define		pypi_name	sh
Summary:	Python subprocess interface
Name:		python-%{module}
Version:	1.11
Release:	7
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	7af8df6c92d29ff927b6db0146bddec3
URL:		https://amoffat.github.io/sh/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sh (previously pbs) is a full-fledged subprocess replacement for
Python 2.6 - 3.4 that allows you to call any program as if it were a
function

%package -n python3-%{module}
Summary:	SH module for python 3
Summary(pl.UTF-8):	Moduł sh dla pythona 3
Group:		Libraries/Python

%description -n python3-%{module}
sh (previously pbs) is a full-fledged subprocess replacement for
Python 2.6 - 3.4 that allows you to call any program as if it were a
function

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
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/%{egg_name}-*-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS.md CHANGELOG.md README.md
%{py3_sitescriptdir}/__pycache__/%{module}.*.pyc
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/%{egg_name}-*-py*.egg-info
%endif

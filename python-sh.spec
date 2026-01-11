#
# Conditional build:
%bcond_without	tests	# functional tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-sh.spec)

%define 	module		sh
Summary:	Python 2 subprocess replacement
Summary(pl.UTF-8):	Zamiennik modułu subprocess dla Pythona 2
Name:		python-%{module}
# keep 1.x here for python2 support
Version:	1.14.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/sh/%{module}-%{version}.tar.gz
# Source0-md5:	d60498172876f35aef6303a9cbb8eb11
URL:		https://pypi.org/project/sh/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sh is a full-fledged subprocess replacement for Python 2, Python 3,
PyPy and PyPy3 that allows you to call any program as if it were a
function.

%description -l pl.UTF-8
sh to w pełni rozwinięty zamiennik modułu subprocess dla Pythona 2,
Pythona 3, PyPy i PyPy3, pozwalający na wywołanie dowolnego programu
tak, jakby był funkcją.

%package -n python3-%{module}
Summary:	Python 3 subprocess replacement
Summary(pl.UTF-8):	Zamiennik modułu subprocess dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
sh is a full-fledged subprocess replacement for Python 2, Python 3,
PyPy and PyPy3 that allows you to call any program as if it were a
function.

%description -n python3-%{module} -l pl.UTF-8
sh to w pełni rozwinięty zamiennik modułu subprocess dla Pythona 2,
Pythona 3, PyPy i PyPy3, pozwalający na wywołanie dowolnego programu
tak, jakby był funkcją.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} test.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} test.py
%endif
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
%doc CHANGELOG.md LICENSE.txt README.rst
%{py_sitescriptdir}/sh.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.txt README.rst
%{py3_sitescriptdir}/sh.py
%{py3_sitescriptdir}/__pycache__/sh.cpython-*.pyc
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

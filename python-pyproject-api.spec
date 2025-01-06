Name:		python-pyproject-api
Version:	1.8.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pyproject-api/pyproject_api-%{version}.tar.gz
Summary:	API to interact with the python pyproject.toml based projects
URL:		https://pypi.org/project/pyproject-api/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
API to interact with the python pyproject.toml based projects

%prep
%autosetup -p1 -n pyproject_api-%{version}

%files
%{py_sitedir}/pyproject_api
%{py_sitedir}/pyproject_api-*.*-info

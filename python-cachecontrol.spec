%global debug_package %{nil}

Name: python-cachecontrol
Epoch: 100
Version: 0.12.8
Release: 1%{?dist}
BuildArch: noarch
Summary: Caching library for Python requests
License: Apache-2.0
URL: https://github.com/ionrock/cachecontrol/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
CacheControl is a port of the caching algorithms in httplib2 for use
with requests session object.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-cachecontrol
Summary: Caching library for Python requests
Requires: python3
Requires: python3-lockfile >= 0.9
Requires: python3-msgpack >= 0.5.2
Requires: python3-requests
Provides: python3-cachecontrol = %{epoch}:%{version}-%{release}
Provides: python3dist(cachecontrol) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cachecontrol = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cachecontrol) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cachecontrol = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cachecontrol) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-cachecontrol
CacheControl is a port of the caching algorithms in httplib2 for use
with requests session object.

%files -n python%{python3_version_nodots}-cachecontrol
%license LICENSES/Apache-2.0.txt
%{_bindir}/doesitcache
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-cachecontrol
Summary: Caching library for Python requests
Requires: python3
Requires: python3-lockfile >= 0.9
Requires: python3-msgpack >= 0.5.2
Requires: python3-requests
Provides: python3-cachecontrol = %{epoch}:%{version}-%{release}
Provides: python3dist(cachecontrol) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cachecontrol = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cachecontrol) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cachecontrol = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cachecontrol) = %{epoch}:%{version}-%{release}

%description -n python3-cachecontrol
CacheControl is a port of the caching algorithms in httplib2 for use
with requests session object.

%files -n python3-cachecontrol
%license LICENSES/Apache-2.0.txt
%{_bindir}/doesitcache
%{python3_sitelib}/*
%endif

%changelog

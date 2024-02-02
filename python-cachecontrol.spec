# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-cachecontrol
Epoch: 100
Version: 0.14.2
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
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-cachecontrol
Summary: Caching library for Python requests
Requires: python3
Requires: python3-filelock >= 3.8.0
Requires: python3-msgpack >= 0.5.2
Requires: python3-requests >= 2.16.0
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
%license LICENSE.txt
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-cachecontrol
Summary: Caching library for Python requests
Requires: python3
Requires: python3-filelock >= 3.8.0
Requires: python3-msgpack >= 0.5.2
Requires: python3-requests >= 2.16.0
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
%license LICENSE.txt
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog

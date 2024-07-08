%global debug_package %{nil}

Name:           impala
Version:        0.2.1
Release:        1%{?dist}
Summary:        TUI for managing wifi on Linux
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/pythops/%{name}
BuildRequires:  cmake
BuildRequires:  cargo, rust
Requires:       iwd
Source:         https://github.com/pythops/%{name}/archive/refs/tags/v%{version}.tar.gz

%description
Prerequisites: A Linux based OS with iwd installed.

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/%{name} %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc *.md
/usr/bin/%{name}

%changelog
* Tue Jul 9 2024 Jamie Curnow <jc@jc21.com> - 0.2.1-1
- Initial spec

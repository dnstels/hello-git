%define namePackager Not Shure
%define addressPackager notshure@localhost
%define dateFormated Wed Oct 10 2012

Name: hello
Version: 1.3
Release: alt1

Summary: The hello programm
License: GPLv3
Group: Development/Other

Url: http://mit.edu
Source: %{name}-%{version}.tar.gz
Packager: %{namePackager} <%{addressPackager}>

# Fake dependency. Used as example of syntax, etc.
BuildPreReq: /proc

BuildRequires: gcc
BuildArch: i586

%description
Hello, I love you,
Won't you tell me your name?
Hello, I love you,
Let me jump in your game.

%prep
%setup

%build

%define dirBuild %{_topdir}/BUILD/%{name}-%{version}
%define dirBin %{dirBuild}/%{name}-%{version}
mkdir -p %{dirBin}
gcc "%{dirBuild}/hello.c" -o "%{dirBin}/hello.out"

%install
install -D -m755 "%{dirBin}/hello.out" %{buildroot}%{_bindir}/hello.out
rm -rf %{dirBin}

%files
%{_bindir}/*

%doc hello.c

%changelog
* %{dateFormated} %{namePackager} <%{addressPackager}> %{version}-%{release}
- Initial build for ALT Linux Sisyphus
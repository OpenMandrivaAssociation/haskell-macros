%define name haskell-macros
%define version 6.2
%define release %mkrel 1

Summary: Rpms macros to easilly build haskell modules
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Source0: %name-%version.tar.gz
Group: System/Configuration/Packaging
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: cabalrpmdeps
Requires: haddock

%description
Rpms macros to easilly build haskell modules.

%prep
%setup -q

%install
%makeinstall_std rpmmacrosdir=%_sys_macros_dir prefix=%_prefix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sys_macros_dir}/%name.macros
%_bindir/*



Summary:	Rpms macros to easilly build haskell modules
Name:		haskell-macros
Version:	6.4
Release:	10
License:	GPLv3+
Source0:	%{name}-%{version}.tar.gz
Patch0:		haskell-macros-for7.patch
Group:		System/Configuration/Packaging
Requires:	haskell(cabalrpmdeps)
BuildArch:	noarch

%description
Rpms macros to easilly build haskell modules.

%files
%{_sys_macros_dir}/%{name}.macros
%{_bindir}/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .for7

%install
%makeinstall_std rpmmacrosdir=%{_sys_macros_dir} prefix=%{_prefix}



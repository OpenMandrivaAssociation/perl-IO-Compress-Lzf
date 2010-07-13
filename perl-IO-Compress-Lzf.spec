%define	upstream_name	 IO-Compress-Lzf
%define upstream_version 2.027

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	IO::Compress::Lzf - Write lzf files/buffers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Compress::LZF)
BuildRequires: perl(IO::Compress::Base) >= %{version}

BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a Perl interface that allows writing lzf compressed data
to files or buffer.

Note that although this module uses Compress::LZF for compression, it uses a
different file format. The lzf file format used here is the same as the lzf
command-line utility that ships with the lzf library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/*

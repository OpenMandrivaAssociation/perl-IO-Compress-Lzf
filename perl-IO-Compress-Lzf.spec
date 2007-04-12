%define	module	IO-Compress-Lzf
%define	name	perl-%{module}
%define	version	2.004
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	IO::Compress::Lzf - Write lzf files/buffers
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/modules/by-module/Compress/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires: perl(IO::Compress::Base) >= %version
BuildRequires: perl(Compress::LZF)
BuildArch: noarch

%description
This module provides a Perl interface that allows writing lzf compressed data
to files or buffer.

Note that although this module uses Compress::LZF for compression, it uses a
different file format. The lzf file format used here is the same as the lzf
command-line utility that ships with the lzf library.

%prep
%setup -q -n %{module}-%{version}

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



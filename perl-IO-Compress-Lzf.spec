%define	upstream_name	 IO-Compress-Lzf
%define upstream_version 2.037

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	IO::Compress::Lzf - Write lzf files/buffers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Compress::LZF)
BuildRequires:	perl(IO::Compress::Base) >= %{version}

BuildArch:	noarch

%description
This module provides a Perl interface that allows writing lzf compressed data
to files or buffer.

Note that although this module uses Compress::LZF for compression, it uses a
different file format. The lzf file format used here is the same as the lzf
command-line utility that ships with the lzf library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/*


%changelog
* Sun Jun 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.37.0-1mdv2011.0
+ Revision: 687341
- update to new version 2.037

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.35.0-1
+ Revision: 674663
- update to new version 2.035

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.33.0-2
+ Revision: 657781
- rebuild for updated spec-helper

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.33.0-1
+ Revision: 635188
- update to new version 2.033

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-1mdv2011.0
+ Revision: 561931
- update to 2.030

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.27.0-1mdv2011.0
+ Revision: 552322
- update to 2.027

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 2.26.0-1mdv2010.1
+ Revision: 536186
- update to 2.026

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 2.25.0-1mdv2010.1
+ Revision: 530263
- update to 2.025

* Mon Jan 11 2010 Jérôme Quelin <jquelin@mandriva.org> 2.24.0-1mdv2010.1
+ Revision: 489503
- update to 2.024

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 2.23.0-1mdv2010.1
+ Revision: 464136
- update to 2.023

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 2.21.0-1mdv2010.0
+ Revision: 437230
- update to 2.021

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.020-1mdv2010.0
+ Revision: 383971
- update to new version 2.020

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.019-1mdv2010.0
+ Revision: 371953
- new version

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.015-1mdv2009.0
+ Revision: 281713
- new version

* Thu Jul 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.012-1mdv2009.0
+ Revision: 236717
- update to new version 2.012

* Wed May 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.011-1mdv2009.0
+ Revision: 209683
- update to new version 2.011

* Wed May 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.010-1mdv2009.0
+ Revision: 202772
- new version

* Wed Apr 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.009-1mdv2009.0
+ Revision: 196825
- update to new version 2.009

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.008-1mdv2008.1
+ Revision: 108302
- update to new version 2.008

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.006-1mdv2008.0
+ Revision: 78418
- new version

* Thu Jul 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.005-1mdv2008.0
+ Revision: 48384
- 2.005


* Mon Mar 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.004-1mdv2007.0
+ Revision: 132964
- 2.004

* Sun Jan 07 2007 Olivier Thauvin <nanardon@mandriva.org> 2.003-1mdv2007.1
+ Revision: 105019
- first mandriva package
- Create perl-IO-Compress-Lzf


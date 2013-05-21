%define	modname	Devel-Cover
%define	modver	1.00

%define __noautoreq 'perl\\(Devel::Cover::Dumper\\)'

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	2

Summary:	Code coverage metrics for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{modname}-%{modver}.tar.gz

BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Pod::Coverage)
BuildRequires:	perl(Template)
BuildRequires:	perl(JSON)
BuildRequires:	perl(Perl::Tidy)
BuildRequires:	perl-devel

%description
This module provides code coverage metrics for Perl. Code coverage metrics
describe how thoroughly tests exercise code. By using Devel::Cover you can find
areas of code not exercised by your tests and find out which tests to create to
increase coverage. Code coverage can be considered as an indirect measure of
quality.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# fixme
make test || /bin/true

%install
%makeinstall_std

%files
%doc META.yml README
%{perl_vendorarch}/Devel
%{perl_vendorarch}/auto/Devel
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.780.0-3mdv2012.0
+ Revision: 765167
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.780.0-2
+ Revision: 763696
- rebuilt for perl-5.14.x

* Thu May 19 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.780.0-1
+ Revision: 676151
- update to new version 0.78

* Mon May 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.770.0-1
+ Revision: 675015
- update to new version 0.77

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.760.0-1
+ Revision: 659930
- update to new version 0.76

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.730.0-1mdv2011.0
+ Revision: 587629
- new version

* Sun Oct 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.700.0-2mdv2011.0
+ Revision: 582778
- rebuild

* Fri Sep 03 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.700.0-1mdv2011.0
+ Revision: 575595
- update to 0.70

* Tue Aug 31 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.690.0-1mdv2011.0
+ Revision: 574790
- update to 0.69

* Fri Aug 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.680.0-1mdv2011.0
+ Revision: 569461
- new version

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.670.0-4mdv2011.0
+ Revision: 564428
- rebuild for perl 5.12.1

  + JÃ©rÃ´me Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12
    - rebuild

* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.670.0-1mdv2011.0
+ Revision: 553124
- update to 0.67

* Sun Apr 18 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.660.0-1mdv2010.1
+ Revision: 536136
- update to 0.66

* Fri Dec 11 2009 Shlomi Fish <shlomif@mandriva.org> 0.650.0-2mdv2010.1
+ Revision: 476446
- Rebuilding a new release for the new perl package

* Thu Aug 20 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.650.0-1mdv2010.0
+ Revision: 418411
- update to 0.65

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.640.0-1mdv2010.0
+ Revision: 403099
- rebuild using %%perl_convert_version

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.64-2mdv2009.0
+ Revision: 265356
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.64-1mdv2009.0
+ Revision: 193800
- update to new version 0.64

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.63-3mdv2008.1
+ Revision: 152060
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-2mdv2008.1
+ Revision: 110482
- better description

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-1mdv2008.1
+ Revision: 110283
- update to new version 0.63

* Wed Nov 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.62-1mdv2008.1
+ Revision: 106646
- update to new version 0.62
- update to new version 0.62


* Wed Feb 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.61-1mdv2007.0
+ Revision: 120847
- new version
- Import perl-Devel-Cover

* Sat Aug 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.59-1mdv2007.0
- New version 0.59

* Sat Aug 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.57-1mdv2007.0
- New version 0.57

* Wed Feb 22 2006 Oden Eriksson <oeriksson@mandriva.com> 0.55-3mdk
- rebuilt against new perl

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.55-2mdk
- Buildrequires fix

* Sat Sep 24 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdk
- New release 0.55

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.54-1mdk
- New release 0.54

* Tue Apr 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.53-1mdk
- new release
- spec cleanup
- better url

* Fri Mar 04 2005 Guillaume Rousse <guillomovitch@mandrake.org> 0.52-1mdk 
- first mdk release


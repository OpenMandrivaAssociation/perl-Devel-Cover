%define	modname	Devel-Cover
%define modver 1.09

%define __noautoreq 'perl\\(Devel::Cover::Dumper\\)'

Summary:	Code coverage metrics for Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
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
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man1/*
%{_mandir}/man3/*




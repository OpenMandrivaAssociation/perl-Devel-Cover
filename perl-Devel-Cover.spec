%define module  Devel-Cover
%define name    perl-%{module}
%define version 0.64
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Code coverage metrics for Perl
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Devel/%{module}-%{version}.tar.bz2
BuildRequires:  perl-devel
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Template)
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module provides code coverage metrics for Perl. Code coverage metrics
describe how thoroughly tests exercise code. By using Devel::Cover you can find
areas of code not exercised by your tests and find out which tests to create to
increase coverage. Code coverage can be considered as an indirect measure of
quality.

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
%doc CHANGES README
%{perl_vendorarch}/Devel
%{perl_vendorarch}/auto/Devel
%{_bindir}/*
%{_mandir}/*/*



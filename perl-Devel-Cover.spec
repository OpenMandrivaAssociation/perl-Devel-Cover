%define upstream_name    Devel-Cover
%define upstream_version 0.67

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Code coverage metrics for Perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Template)
BuildRequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides code coverage metrics for Perl. Code coverage metrics
describe how thoroughly tests exercise code. By using Devel::Cover you can find
areas of code not exercised by your tests and find out which tests to create to
increase coverage. Code coverage can be considered as an indirect measure of
quality.

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
%doc CHANGES README
%{perl_vendorarch}/Devel
%{perl_vendorarch}/auto/Devel
%{_bindir}/*
%{_mandir}/*/*

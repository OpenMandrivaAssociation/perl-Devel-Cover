%define module  Devel-Cover
%define name    perl-%{module}
%define version 0.63
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
This module provides code coverage metrics for Perl.

If you can't guess by the version number this is an alpha release.

Code coverage data are collected using a pluggable runops function which counts
how many times each op is executed. These data are then mapped back to reality
using the B compiler modules. There is also a statement profiling facility
which needs a better backend to be really useful.

The cover program can be used to generate coverage reports.

Statement, branch, condition, subroutine, pod and time coverage information is
reported. Statement coverage data should be reasonable, although there may be
some statements which are not reported. Branch and condition coverage data
should be mostly accurate too, although not always what one might initially
expect. Subroutine coverage should be as accurate as statement coverage. Pod
coverage comes from Pod::Coverage. Coverage data for path coverage are not yet
collected.

The gcov2perl program can be used to convert gcov files to Devel::Cover
databases.

You may find that the results don't match your expectations. I would imagine
that at least one of them is wrong.

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



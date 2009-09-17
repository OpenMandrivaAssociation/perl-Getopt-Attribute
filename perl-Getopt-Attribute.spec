%define upstream_name    Getopt-Attribute
%define upstream_version 1.44

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Attribute wrapper for Getopt::Long
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Getopt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Note: This version of the module works works with perl 5.8.0. If you need
it to work with perl 5.6.x, please use an earlier version from CPAN.

This module provides an attribute wrapper around 'Getopt::Long'. Instead of
declaring the options in a hash with references to the variables and
subroutines affected by the options, you can use the 'Getopt' attribute on
the variables and subroutines directly.

As you can see from the Synopsis, the attribute takes an argument of the
same format as you would give as the hash key for 'Getopt::Long'. See the
'Getopt::Long' manpage for details.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



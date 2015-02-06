%define upstream_name    Getopt-Attribute
%define upstream_version 2.101700

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Attribute wrapper for Getopt::Long
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Getopt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More) >= 0.940.0
BuildRequires:	perl(UNIVERSAL::require)

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 2.101.700-2mdv2011.0
+ Revision: 658533
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.101.700-1mdv2011.0
+ Revision: 552369
- bump test::more minimum version in buildrequires:
- update to 2.101700

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 1.460.0-1mdv2010.1
+ Revision: 474655
- update to 1.46

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.440.0-1mdv2010.0
+ Revision: 444059
- import perl-Getopt-Attribute


* Thu Sep 17 2009 cpan2dist 1.44-1mdv
- initial mdv release, generated with cpan2dist

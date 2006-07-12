%define dist	MDV-Packdrakeng
%define version	1.01
%define release	%mkrel 2

Summary:	Simple Archive Extractor/Builder
Name:		perl-%{dist}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Source0:	%{dist}-%{version}.tar.bz2
Url:		http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/perl-%{dist}/
BuildRoot:	%{_tmppath}/%{name}-buildroot/
BuildArch:	noarch
BuildRequires:	perl-Compress-Zlib
# perl-Compress-Zlib is only "suggested"
%define _requires_exceptions perl(Compress::Zlib)

%description
MDV::Packdrakeng is a simple indexed archive builder and extractor using
standard compression methods.

%prep
%setup -q -n %{dist}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/*/*
%{perl_vendorlib}/MDV/Packdrakeng
%{perl_vendorlib}/MDV/Packdrakeng.pm

%changelog
* Wed Feb 15 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.01-2mdk
- Rebuild; use mkrel (misc)

* Fri Nov 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.01-1mdk
- 1.01

* Fri Oct 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.00-1mdk
- Initial MDV release

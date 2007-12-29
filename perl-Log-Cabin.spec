#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Cabin
Summary:	Log::Cabin - Partial implementation of Log::Log4perl with reduced disk IO.
#Summary(pl):	
Name:		perl-Log-Cabin
Version:	0.05
Release:	0.2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	245dc55397b6bee8e72138daffd53fe9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Cabin provides a selection of the features of Log::Log4perl but with 
a focus on reduced disk IO.  Just calling 'use Log::Log4perl' results in
hundreds of stat calls to the file system.  If you have a shared file system
with many nodes running perl scripts at once, this could result in a significant
decrease in performance.

After implementing this module we were able to cut up to 70,000 stat/open
calls per second on our NFS.  Of course, this module doesn't currently support
all the features of Log::Log4perl, but many of the most comment ones are
implemented.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/*.pm
%{perl_vendorlib}/Log/Cabin
%{_mandir}/man3/*

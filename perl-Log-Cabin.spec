#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Cabin
Summary:	Log::Cabin - Partial implementation of Log::Log4perl with reduced disk IO
Summary(pl.UTF-8):	Log::Cabin - częściowa implementacja Log::Log4perl z ograniczonym dyskowym I/O
Name:		perl-Log-Cabin
Version:	0.05
Release:	0.3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Log/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	245dc55397b6bee8e72138daffd53fe9
URL:		http://search.cpan.org/dist/Log-Cabin/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Cabin provides a selection of the features of Log::Log4perl but
with a focus on reduced disk IO. Just calling 'use Log::Log4perl'
results in hundreds of stat calls to the file system. If you have a
shared file system with many nodes running perl scripts at once, this
could result in a significant decrease in performance.

After implementing this module its authors were able to cut up to
70,000 stat/open calls per second on our NFS. Of course, this module
doesn't currently support all the features of Log::Log4perl, but many
of the most comment ones are implemented.

%description -l pl.UTF-8
Moduł Perla Log::Cabin udostępnia wybrane możliwości modułu
Log::Log4perl, ale z naciskiem na ograniczone dyskowe operacje
wejścia/wyjścia. Samo wywołanie "use Log::Log4perl" powoduje setki
wywołań stat na systemie plików. Jeśli system plików jest
współdzielony z wieloma innymi węzłami, na których jednocześnie
działają skrypty Perla, efektem może być znaczny spadek wydajności.

Po zaimplementowaniu tego modułu autorom udało się zmniejszyc liczbę
stat/open nawet o 70000 wywołań na sekundę na swoim NFS-ie. Oczywiście
ten moduł nie obsługuje wszystkich możliwości Log::Log4perl, ale
najistotniejsze są zaimplementowane.

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
%{perl_vendorlib}/auto/Log/Cabin/autosplit.ix
%{perl_vendorlib}/auto/Log/Cabin/Foundation/autosplit.ix
%{_mandir}/man3/*

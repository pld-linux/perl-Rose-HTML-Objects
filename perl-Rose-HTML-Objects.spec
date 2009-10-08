#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Rose
%define	pnam	HTML-Objects
Summary:	Rose::HTML::Objects - Object-oriented interfaces for HTML.
#Summary(pl.UTF-8):	
Name:		perl-Rose-HTML-Objects
Version:	0.604
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Rose/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ccf516df97e399806daf9854d3e2e724
URL:		http://search.cpan.org/dist/Rose-HTML-Objects/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Clone::PP)
BuildRequires:	perl(Rose::DateTime) >= 0.532
BuildRequires:	perl(Rose::Object) >= 0.854
BuildRequires:	perl(Rose::URI) >= 0.021
BuildRequires:	perl-DateTime >= 0.20
BuildRequires:	perl-Email-Valid
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-Image-Size
BuildRequires:	perl-IO-String >= 1.08
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rose::HTML::Objects is a framework for creating a reusable set of
HTML widgets as mutable Perl objects that can be serialized to HTML
or XHTML for display purposes.

# %description -l pl.UTF-8
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
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Rose/HTMLx/Form

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Rose/HTML
%{perl_vendorlib}/Rose/HTMLx
%{_mandir}/man3/*

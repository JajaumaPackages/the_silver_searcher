%global commit cfcaede7c5fe5ee16b7cfad59cbb0648c80d4cb2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global bashcompdir %(pkg-config --variable=completionsdir bash-completion)

Name:           the_silver_searcher
Version:        0.22.0
Release:        1%{?dist}
Summary:        Super-fast text searching tool
Group:          Applications/Text
License:        ASL 2.0 and BSD
URL:            https://github.com/ggreer/the_silver_searcher
Source:         https://github.com/ggreer/the_silver_searcher/archive/%{commit}/%{version}-%{shortcommit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

%description
The Silver Searcher is a code searching tool similar to ack,
with a focus on speed.

%prep
%setup -q -n %{name}-%{commit}

%build
aclocal
autoconf
autoheader
automake --add-missing
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{bashcompdir}
install -pm 0644 ag.bashcomp.sh $RPM_BUILD_ROOT%{bashcompdir}/ag
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%{_bindir}/ag
%{_mandir}/man1/ag.1*
%(dirname %{bashcompdir})
%doc README.md LICENSE

%changelog
* Tue Apr 22 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.21.0-1
- update to 0.21.0

* Thu Sep 12 2013 Henrik Hodne <henrik@hodne.io> - 0.16-2
- Initial RPM release

Name:           ocaml-newt
Version:        0.9
Release:        3
Summary:        OCaml library for using newt text mode window system
License:        LGPLv2+ with exceptions
Group:          Development/Other
URL:            https://et.redhat.com/~rjones/ocaml-newt/
Source0:        http://et.redhat.com/~rjones/ocaml-newt/ocaml-newt-%{version}.tar.gz
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  newt-devel

%description
This is a set of OCaml bindings to newt.

The newt windowing system is a terminal-based window and widget
library designed for writing applications with a simple, but
user-friendly, interface.  While newt is not intended to provide the
rich feature set advanced applications may require, it has proven to
be flexible enough for a wide range of applications (most notably, Red
Hat's installation process).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure --libdir=%{_libdir}
# Dependencies are broken in the upstream package.
make newt_int.mli
rm -f .depend
make depend
make all
make opt
make doc

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/newt
make install

%files
%defattr(-,root,root)
%doc COPYING.LIB INSTALL README
%dir %{_libdir}/ocaml/newt
%{_libdir}/ocaml/newt/META
%{_libdir}/ocaml/newt/*.cma
%{_libdir}/ocaml/newt/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc html
%{_libdir}/ocaml/newt/*.a
%{_libdir}/ocaml/newt/*.cmxa
%{_libdir}/ocaml/newt/*.cmx
%{_libdir}/ocaml/newt/*.mli



%changelog
* Mon Sep 07 2009 Florent Monnier <blue_prawn@mandriva.org> 0.9-1mdv2010.0
+ Revision: 432962
- take the devel one in BR
- BuildRequires: ocaml-camlidl
- spec file mostly imported from the fedora's one by Richard Jones


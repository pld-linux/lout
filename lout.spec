Summary:	The Lout document formatting language.
Name:		lout
Version:	3.08
Release:	7
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
Source0:	ftp://ftp.cs.su.oz.au/jeff/%{name}.%{version}.tar.gz
Patch0:		%{name}-3.08-make.patch
Patch1:		%{name}-3.08-nobr.patch
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lout is a high-level language for document formatting. Lout reads a
high-level description of a document (similar in style to LaTeX) and
can produce a PostScript(TM) file for printing or produce plain text.
Lout supports the typesetting of documents which contain floating
figures, table, diagrams, rotated and scaled text or graphics,
footnotes, running headers, footers, an index, a table of contents and
bibliography, cross-references, mathematical equations and statistical
graphs. Lout can be extended with definitions that should be easier to
write than other languages, since Lout is a high-level language. Lout
supports (with hyphenation) a variety of languages: Czech, Danish,
Dutch, English, Finnish, French, German, Norwegian, Russian,
Slovenian, Spanish and Swedish.

Install the lout package if you'd like to try the Lout document
formatting system. Unless you're already a Lout expert, you'll
probably want to also install the lout-doc package, which contains the
documentation for Lout.

%package doc
Summary:	The documentation for the Lout document formatting language.
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie

%description doc
The lout-doc package includes all of the documentation for the Lout
document formatting language. The documentation includes manuals for
regular users and for experts, written in Lout and available as
PostScript(TM) files. The documentation provides good examples for how
to write large documents with Lout.

If you're installing the lout package, you should install the lout-doc
package.

%prep
%setup -q -n lout.3.08
%patch0 -p1
%patch1 -p1 -b .nobr

%build
%ifarch sparc
%{__make} RPM_OPT_FLAGS="" lout c2lout
%else
%{__make} RPM_OPT_FLAGS="%{rpmcflags}" lout c2lout
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1}

%{__make} DESTDIR=$RPM_BUILD_ROOT install installman installdoc

for i in user slides expert design; do
	chmod 755 $RPM_BUILD_ROOT%{_docdir}/lout/$i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc blurb README maillist whatsnew notes.dsc
%attr(755,root,root) %{_bindir}/lout
%attr(755,root,root) %{_bindir}/c2lout
%{_mandir}/man1/lout.1*
%{_mandir}/man1/c2lout.1*
%{_libdir}/lout

%files doc
%defattr(644,root,root,755)
%attr(-,root,root %{_docdir}/lout

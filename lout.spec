Summary:	The Lout document formatting language
Summary(pl):	Lout - j�zyk formatowania dokument�w
Name:		lout
Version:	3.24
Release:	1
License:	GPL
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(es):	Aplicaciones/Editoraci�n
Group(pl):	Aplikacje/Publikowanie
Group(pt_BR):	Aplica��es/Editora��o
Source0:	ftp://ftp.cs.usyd.edu.au/jeff/lout/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://www.ptc.spbu.ru/~uwe/lout/
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

%description -l pl
Lout to j�zyk wysokiego poziomu do formatowania dokument�w. Lout czyta
opis dokumentu (w stylu przypominaj�cym LaTeX) i mo�e wyprodukowa�
plik PostScript(TM) do wydruku lub czysty tekst. Obs�uguje sk�adanie
dokument�w zawieraj�cych rysunki, diagramy, obracany lub skalowany
tekst lub grafik�, przypisy, nag��wki, stopki, indeks, spis tre�ci
oraz bibliografi�, odno�niki, r�wnania matematyczne i wykresy
statystyczne. Lout mo�e by� rozszerzany przez definicje, co u�atwia
pisane w stosunku do innych j�zyk�w, poniewa� Lout jest j�zykiem
wysokiego poziomu. Lout wspiera (z dzieleniem wyraz�w) wiele j�zyk�w:
angielski, czeski, du�ski, fi�ski, francuski, hiszpa�ski, holenderski,
niemiecki, norweski, rosyjski, s�owe�ski i szwedzki.

%package doc
Summary:	The documentation for the Lout document formatting language
Summary(pl):	Dokumentacja do j�zyka formatowania dokument�w Lout
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(es):	Aplicaciones/Editoraci�n
Group(pl):	Aplikacje/Publikowanie
Group(pt_BR):	Aplica��es/Editora��o

%description doc
The lout-doc package includes all of the documentation for the Lout
document formatting language. The documentation includes manuals for
regular users and for experts, written in Lout and available as
PostScript(TM) files. The documentation provides good examples for how
to write large documents with Lout.

If you're installing the lout package, you should install the lout-doc
package.

%description doc -l pl
Ten pakiet zawiera ca�� dokumentacj� do j�zyka formatowania dokument�w
Lout. Sk�ada si� z podr�cznik�w dla zwyk�ych u�ytkownik�w i ekspert�w,
naapisanych w Loucie i dost�pnych w plikach PostScript. Dokumentacja
to tak�e dobre przyk�ady jak tworzy� du�e dokumenty w Loucie.

%prep
%setup -q 
%patch0 -p1

%build
%ifarch sparc
%{__make} RPM_OPT_FLAGS=""
%else
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1}

%{__make} DESTDIR=$RPM_BUILD_ROOT install installman installdoc

for i in user slides expert design; do
	chmod 755 $RPM_BUILD_ROOT%{_docdir}/lout/$i
done

gzip -9nf blurb README maillist whatsnew notes.dsc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%dir %{_libdir}/lout
%{_libdir}/lout/*

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/lout

Summary:	The Lout document formatting language
Summary(es):	Sistema de formateado de texto
Summary(pl):	Lout - jêzyk formatowania dokumentów
Summary(pt_BR):	Sistema de formatação de texto
Name:		lout
Version:	3.25
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.cs.usyd.edu.au/jeff/lout/%{name}-%{version}.tar.gz
# Source0-md5:	c5aa6ba32b3bb1cb6cc434ff3954f117
Patch0:		%{name}-makefile.patch
URL:		http://www.ptc.spbu.ru/~uwe/lout/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	lout-doc

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

%description -l es
El sistema lout lee una descripción de altonivel de un documento
similar en estilo al LaTeX y produce un archivo PostScript, que puede
ser impreso en muchas impresoras laser y dispositivos gráficos de
display. También se encuentra disponible la salida en formato texto.
Lout ofrece muchas características avanzadas, incluyendo optimización
de saltos de párrafos y páginas, separación automática, inclusión y
creación de archivos PsotScript EPS, formatos de ecuaciones, tablas,
gráficos, rotación y escalonamiento, índices ordenados, banco de datos
bibliográficos, documentos de múltiples idiomas que incluye separación
(soporta la mayoría de los idiomas europeos, incluso el ruso),
formatos de programas C/C++, y mucho más. Todo listo para usar.

%description -l pl
Lout to jêzyk wysokiego poziomu do formatowania dokumentów. Lout czyta
opis dokumentu (w stylu przypominaj±cym LaTeX) i mo¿e wyprodukowaæ
plik PostScript(TM) do wydruku lub czysty tekst. Obs³uguje sk³adanie
dokumentów zawieraj±cych rysunki, diagramy, obracany lub skalowany
tekst lub grafikê, przypisy, nag³ówki, stopki, indeks, spis tre¶ci
oraz bibliografiê, odno¶niki, równania matematyczne i wykresy
statystyczne. Lout mo¿e byæ rozszerzany przez definicje, co u³atwia
pisane w stosunku do innych jêzyków, poniewa¿ Lout jest jêzykiem
wysokiego poziomu. Lout wspiera (z dzieleniem wyrazów) wiele jêzyków:
angielski, czeski, duñski, fiñski, francuski, hiszpañski, holenderski,
niemiecki, norweski, rosyjski, s³oweñski i szwedzki.

%description -l pt_BR
O sistema lout lê uma descrição de alto nível de um documento similar
em estilo ao LaTeX e produz um arquivo PostScript, que pode ser
impresso em muitas impressoras laser e dispositivos gráficos de
display. Saída em formato texto também esta disponível. Lout oferece
muitas características avançadas, incluindo otimização de quebras de
parágrafos e páginas, hifenização automática, inclusão e geração de
arquivos PostScript EPS, formatação de equações, tabelas, diagramas,
rotação e escalamento, índices ordenados, bancos de dados
bibliográficos, headers e paginação par-ímpar, referência cruzada
automática, documentos de múltiplos idiomas incluindo hifenização (a
maioria dos idiomas europeus são suportados, inclusive russo),
formatação de programas C/C++, e muito mais, tudo pronto para usar.

%prep
%setup -q
%patch0 -p1

%build
%{__make} lout prg2lout \
	COPTS="-ansi -pedantic -Wall %{rpmcflags}" \
	CC=%{__cc}

(cd doc/design; ../../lout -EPS -I ../../include -D../../data all -o ../../design.ps)
(cd doc/expert; ../../lout -EPS -I ../../include -D../../data all -o ../../expert.ps)
(cd doc/slides; ../../lout -EPS -I ../../include -D../../data all -o ../../slides.ps)
(cd doc/user; ../../lout -EPS -I ../../include -D../../data all -o ../../user.ps)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1}

%{__make} install installman \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc blurb README maillist whatsnew notes.dsc *.ps
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%dir %{_libdir}/lout

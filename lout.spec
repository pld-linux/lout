Summary:	The Lout document formatting language
Summary(es):	Sistema de formateado de texto
Summary(pl):	Lout - j�zyk formatowania dokument�w
Summary(pt_BR):	Sistema de formata��o de texto
Name:		lout
Version:	3.29
Release:	5
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.cs.usyd.edu.au/jeff/lout/%{name}-%{version}.tar.gz
# Source0-md5:	cff3a2c009b928e794a9a57b208df788
Patch0:		%{name}-makefile.patch
URL:		http://www.ptc.spbu.ru/~uwe/lout/
Obsoletes:	lout-doc
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

%description -l es
El sistema lout lee una descripci�n de altonivel de un documento
similar en estilo al LaTeX y produce un archivo PostScript, que puede
ser impreso en muchas impresoras laser y dispositivos gr�ficos de
display. Tambi�n se encuentra disponible la salida en formato texto.
Lout ofrece muchas caracter�sticas avanzadas, incluyendo optimizaci�n
de saltos de p�rrafos y p�ginas, separaci�n autom�tica, inclusi�n y
creaci�n de archivos PsotScript EPS, formatos de ecuaciones, tablas,
gr�ficos, rotaci�n y escalonamiento, �ndices ordenados, banco de datos
bibliogr�ficos, documentos de m�ltiples idiomas que incluye separaci�n
(soporta la mayor�a de los idiomas europeos, incluso el ruso),
formatos de programas C/C++, y mucho m�s. Todo listo para usar.

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

%description -l pt_BR
O sistema lout l� uma descri��o de alto n�vel de um documento similar
em estilo ao LaTeX e produz um arquivo PostScript, que pode ser
impresso em muitas impressoras laser e dispositivos gr�ficos de
display. Sa�da em formato texto tamb�m esta dispon�vel. Lout oferece
muitas caracter�sticas avan�adas, incluindo otimiza��o de quebras de
par�grafos e p�ginas, hifeniza��o autom�tica, inclus�o e gera��o de
arquivos PostScript EPS, formata��o de equa��es, tabelas, diagramas,
rota��o e escalamento, �ndices ordenados, bancos de dados
bibliogr�ficos, headers e pagina��o par-�mpar, refer�ncia cruzada
autom�tica, documentos de m�ltiplos idiomas incluindo hifeniza��o (a
maioria dos idiomas europeus s�o suportados, inclusive russo),
formata��o de programas C/C++, e muito mais, tudo pronto para usar.

%prep
%setup -q
%patch0 -p1

%build
%{__make} lout prg2lout \
	COPTS="-ansi -pedantic -Wall %{rpmcflags}" \
	CC="%{__cc}"

cd doc/design
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../design.ps
cd ../expert
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../expert.ps
cd ../slides
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../slides.ps
cd ../user
PATH="../..:$PATH" \
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../user.ps

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_prefix}/lib,%{_mandir}/man1}

%{__make} install installman \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc blurb README maillist whatsnew *.ps
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/lout
%{_mandir}/man1/*.1*

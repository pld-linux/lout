Summary:	The Lout document formatting language
Summary(es.UTF-8):   Sistema de formateado de texto
Summary(pl.UTF-8):   Lout - język formatowania dokumentów
Summary(pt_BR.UTF-8):   Sistema de formatação de texto
Name:		lout
Version:	3.31
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.cs.usyd.edu.au/jeff/lout/%{name}-%{version}.tar.gz
# Source0-md5:	8cc03412d5c26c208811877b89ad3174
Patch0:		%{name}-makefile.patch
URL:		http://snark.ptc.spbu.ru/~uwe/lout/lout.html
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

%description -l es.UTF-8
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

%description -l pl.UTF-8
Lout to język wysokiego poziomu do formatowania dokumentów. Lout czyta
opis dokumentu (w stylu przypominającym LaTeX) i może wyprodukować
plik PostScript(TM) do wydruku lub czysty tekst. Obsługuje składanie
dokumentów zawierających rysunki, diagramy, obracany lub skalowany
tekst lub grafikę, przypisy, nagłówki, stopki, indeks, spis treści
oraz bibliografię, odnośniki, równania matematyczne i wykresy
statystyczne. Lout może być rozszerzany przez definicje, co ułatwia
pisane w stosunku do innych języków, ponieważ Lout jest językiem
wysokiego poziomu. Lout wspiera (z dzieleniem wyrazów) wiele języków:
angielski, czeski, duński, fiński, francuski, hiszpański, holenderski,
niemiecki, norweski, rosyjski, słoweński i szwedzki.

%description -l pt_BR.UTF-8
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
	CC="%{__cc}"

# process each document three times, to get proper crossreferences
cd doc/design
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../design.ps
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../design.ps
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../design.ps
cd ../expert
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../expert.ps
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../expert.ps
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../expert.ps
cd ../slides
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../slides.ps
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../slides.ps
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../slides.ps
cd ../user
# PATH needed for prg2lout filter
PATH="../..:$PATH" \
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../user.ps
PATH="../..:$PATH" \
../../lout -I../../include -D../../data -C../../maps -F../../font -H../../hyph all -o ../../user.ps
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

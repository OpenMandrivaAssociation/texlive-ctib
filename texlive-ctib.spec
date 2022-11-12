Name:		texlive-ctib
Version:	15878
Release:	1
Summary:	Tibetan for TeX and LATeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/tibetan/ctib
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctib.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package using a modified version of Sirlin's Tibetan font. An
advantage of this Tibetan implementation is that all consonant
clusters are formed by TeX and Metafont. No external
preprocessor is needed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/ctib/bzrsetup.mf
%{_texmfdistdir}/fonts/source/public/ctib/ctib.mf
%{_texmfdistdir}/fonts/source/public/ctib/ctibcode.mf
%{_texmfdistdir}/fonts/source/public/ctib/ctiblett.mf
%{_texmfdistdir}/fonts/source/public/ctib/ctibligs.mf
%{_texmfdistdir}/fonts/source/public/ctib/ctibnum.mf
%{_texmfdistdir}/fonts/source/public/ctib/ctibpunc.mf
%{_texmfdistdir}/fonts/source/public/ctib/ctibsplt.mf
%{_texmfdistdir}/fonts/source/public/ctib/ctibvow.mf
%{_texmfdistdir}/fonts/tfm/public/ctib/ctib.tfm
%{_texmfdistdir}/tex/latex/ctib/ctib.sty
%{_texmfdistdir}/tex/latex/ctib/ctib.tex
%{_texmfdistdir}/tex/latex/ctib/lctctib.fd
%{_texmfdistdir}/tex/latex/ctib/lctenc.def
%doc %{_texmfdistdir}/doc/latex/ctib/README
%doc %{_texmfdistdir}/doc/latex/ctib/ctib4tex.pdf
%doc %{_texmfdistdir}/doc/latex/ctib/ctib4tex.tex
#- source
%doc %{_texmfdistdir}/source/latex/ctib/COPYING
%doc %{_texmfdistdir}/source/latex/ctib/EMTEX
%doc %{_texmfdistdir}/source/latex/ctib/HISTORY
%doc %{_texmfdistdir}/source/latex/ctib/INSTALL
%doc %{_texmfdistdir}/source/latex/ctib/MIKTEX

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}

# revision 15878
# category Package
# catalog-ctan /language/tibetan/ctib
# catalog-date 2007-02-04 13:34:13 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-ctib
Version:	20070204
Release:	6
Summary:	Tibetan for TeX and LATeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/tibetan/ctib
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctib.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070204-2
+ Revision: 750667
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070204-1
+ Revision: 718182
- texlive-ctib
- texlive-ctib
- texlive-ctib
- texlive-ctib


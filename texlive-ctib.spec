%global tl_name ctib
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Tibetan for TeX and LaTeX2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/tibetan/ctib
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package using a modified version of Sirlin's Tibetan font. An
advantage of this Tibetan implementation is that all consonant clusters
are formed by TeX and Metafont. No external preprocessor is needed.


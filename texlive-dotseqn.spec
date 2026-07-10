%global tl_name dotseqn
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Flush left equations with dotted leaders to the numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dotseqn
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a different format for typesetting equations, one
reportedly used in 'old style Britsh books': equations aligned on the
left, with dots on the right leading to the equation number. In default
of an equation number, the package operates much like the fleqn class
option (no leaders).


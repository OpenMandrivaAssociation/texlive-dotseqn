Name:		texlive-dotseqn
Version:	17195
Release:	2
Summary:	Flush left equations with dotted leaders to the numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dotseqn
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a different format for typesetting
equations, one reportedly used in 'old style Britsh books':
equations aligned on the left, with dots on the right leading
to the equation number. In default of an equation number, the
package operates much like the fleqn class option (no leaders).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dotseqn/dotseqn.sty
%doc %{_texmfdistdir}/doc/latex/dotseqn/dotseqn.pdf
%doc %{_texmfdistdir}/doc/latex/dotseqn/readme
#- source
%doc %{_texmfdistdir}/source/latex/dotseqn/dotseqn.dtx
%doc %{_texmfdistdir}/source/latex/dotseqn/dotseqn.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

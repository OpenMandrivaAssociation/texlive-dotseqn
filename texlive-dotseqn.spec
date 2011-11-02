Name:		texlive-dotseqn
Version:	1.1
Release:	1
Summary:	Flush left equations with dotted leaders to the numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dotseqn
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a different format for typesetting
equations, one reportedly used in 'old style Britsh books':
equations aligned on the left, with dots on the right leading
to the equation number. In default of an equation number, the
package operates much like the fleqn class option (no leaders).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

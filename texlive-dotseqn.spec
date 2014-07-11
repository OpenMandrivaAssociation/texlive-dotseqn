# revision 17195
# category Package
# catalog-ctan /macros/latex/contrib/dotseqn
# catalog-date 2010-02-24 21:28:09 +0100
# catalog-license other-free
# catalog-version 1.1
Name:		texlive-dotseqn
Version:	1.1
Release:	8
Summary:	Flush left equations with dotted leaders to the numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dotseqn
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotseqn.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 751063
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718250
- texlive-dotseqn
- texlive-dotseqn
- texlive-dotseqn
- texlive-dotseqn


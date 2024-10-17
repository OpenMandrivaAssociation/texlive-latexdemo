Name:		texlive-latexdemo
Version:	67201
Release:	1
Summary:	Demonstrate LaTeX code with its resulting output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latexdemo
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexdemo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexdemo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexdemo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides configurable tools to print out LaTeX code
and the resulting output in the same document. It also supports
printing the result inside a conditional sequence; thus one may
suppress printing if the code would not compile.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/latexdemo
%{_texmfdistdir}/tex/latex/latexdemo
%doc %{_texmfdistdir}/doc/latex/latexdemo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

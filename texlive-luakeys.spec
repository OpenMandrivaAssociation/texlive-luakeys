Name:		texlive-luakeys
Version:	65346
Release:	2
Summary:	A Lua module for parsing key-value options
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luakeys
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luakeys.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luakeys.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a Lua module that can parse key-value
options like the TeX packages keyval, kvsetkeys, kvoptions,
xkeyval, pgfkeys etc. luakeys, however, accomplishes this task
entirely by using the Lua language and does not rely on TeX.
Therefore this package can only be used with the TeX engine
LuaTeX. Since luakeys uses LPeg, the parsing mechanism should
be pretty robust.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/luakeys
%doc %{_texmfdistdir}/doc/luatex/luakeys

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

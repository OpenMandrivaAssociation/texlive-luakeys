%global tl_name luakeys
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.17.0
Release:	%{tl_revision}.1
Summary:	A Lua module for parsing key-value options
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/luakeys
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luakeys.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luakeys.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a Lua module that can parse key-value options like
the TeX packages keyval, kvsetkeys, kvoptions, xkeyval, pgfkeys etc.
luakeys, however, accomplishes this task entirely by using the Lua
language and does not rely on TeX. Therefore this package can only be
used with the TeX engine LuaTeX. Since luakeys uses LPeg, the parsing
mechanism should be pretty robust.


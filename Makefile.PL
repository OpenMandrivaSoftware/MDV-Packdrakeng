# $Id$

use 5.008;
use strict;
use ExtUtils::MakeMaker;

sub MY::postamble {
    <<MAKE;
.PHONY: ChangeLog 

ChangeLog:
	LC_ALL=C svn2cl -o ChangeLog
	rm -f *.bak

MAKE
}

WriteMakefile(
    NAME	 => 'MDV::Packdrakeng',
    VERSION_FROM => 'lib/MDV/Packdrakeng.pm',
    dist	=> { COMPRESS => "xz -f", SUFFIX => ".xz" },
);

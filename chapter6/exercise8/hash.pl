#!/usr/bin/perl -w

use strict;
use warnings;

use Time::HiRes qw( time );

my $start = time();

# BEGIN CODE

srand( time() ^ ($$ + ($$ << 15)) );
my @abc = qw ( a b c d e f g h i j k l m n o p q r s t u v w x y z );
my %name_age;
my $tmp;

for (1..10000) {
  # GENERATING RANDOM STRING AND NUMBER
  my ($num, $str) = (0, '');
  $str .= $abc[int(rand(26))] for 1 .. 3;
  $num = int(rand(90));
  # CHECKING IF NAME EXISTS
  if( exists($name_age{$str}) ){
    $tmp = $name_age{$str};
  }
  else{
    $name_age{$str} = $num;
  }
}


# END CODE

my $end = time();
printf("It took: %.2f seconds\n", $end - $start);


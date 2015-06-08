#!/usr/bin/perl -w

use strict;
use warnings;

use Time::HiRes qw( time );
use List::Util qw(first);

my $start = time();

# BEGIN CODE

srand( time() ^ ($$ + ($$ << 15)) );
my @abc = qw ( a b c d e f g h i j k l m n o p q r s t u v w x y z );
my @names;
my $idx = 0;
my $tmp;

for (1..10000) {
  # GENERATING RANDOM STRING AND NUMBER
  my ($num, $str) = (0, '');
  $str .= $abc[int(rand(26))] for 1 .. 3;
  $num = int(rand(90));
  # CHECKING IF NAME EXISTS
  if( $str ~~ @names ) {
    $tmp = $num;
  }
  else{
    $names[$idx] = $str;
    $idx = $idx + 1;
  }
}


# END CODE

my $end = time();
printf("It took: %.2f seconds\n", $end - $start);


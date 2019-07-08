#!/usr/bin/env ruby
print ARGV[0].scan(/(?<=\[from:)[+\w]*/).join + ','
print ARGV[0].scan(/(?<=\[to:)[+\w]*/).join + ','
puts ARGV[0].scan(/(?<=\[flags:)[-:\w]*/).join

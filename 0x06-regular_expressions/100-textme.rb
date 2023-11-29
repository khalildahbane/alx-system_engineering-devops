#!/usr/bin/env ruby
# This script parses a log file and prints the sender, receiver and flags

puts ARGV[0].scan(/(?<=from:|to:|flags:)[^\]]*/).join(',')

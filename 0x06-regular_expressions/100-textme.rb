#!/usr/bin/env ruby
puts ARGV[0].scan(/from:([\WA-Za-z0-9]{1,13})\]/).join + "," +
ARGV[0].scan(/to:([\WA-Za-z0-9]{1,13})\]/).join + "," +
ARGV[0].scan(/flags:([\WA-Za-z0-9]{1,13})\]/).join

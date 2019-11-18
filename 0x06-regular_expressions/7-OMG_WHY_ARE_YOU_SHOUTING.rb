#!/usr/bin/env ruby
puts ARGV[0].scan(/[^a-z\s]{2}+/).join

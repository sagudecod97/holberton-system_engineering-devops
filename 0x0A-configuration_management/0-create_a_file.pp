file { '/tmp/holberton':
path    => '/tmp/holberton',
content => 'I Love Puppet',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
}

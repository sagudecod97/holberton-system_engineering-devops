# Change the OS Config
exec { "sudo sed -i 's/5/3000/g; s/4/3000/g' /etc/security/limits.conf":
  path => '/bin:/usr/bin:/usr/sbin:/sbin',
}

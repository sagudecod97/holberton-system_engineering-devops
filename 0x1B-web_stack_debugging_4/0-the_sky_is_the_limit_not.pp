# Limit the number of files
exec { "sudo sed -i 's/15/5000/g' /etc/default/nginx; service nginx restart":
  path => '/bin:/usr/bin:/usr/sbin:/sbin',
}

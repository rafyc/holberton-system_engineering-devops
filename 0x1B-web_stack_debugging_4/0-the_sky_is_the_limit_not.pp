#Increase traffic

exec { 'update_nginx':
  command => 'sed -i s/15/2000/ /etc/default/nginx',
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/', 'usr/local/bin',],
}
exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/', 'usr/local/bin',],
}

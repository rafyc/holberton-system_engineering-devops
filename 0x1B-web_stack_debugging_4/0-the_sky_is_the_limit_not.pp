#Increase traffic

exec { 'update_nginx':
  command => 'sed -i s/15/2000/ /etc/default/nginx',
}
exec { 'restart_nginx':
  command => 'sudo service nginx restart',
}

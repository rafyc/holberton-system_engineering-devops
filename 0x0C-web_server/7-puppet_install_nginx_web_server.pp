# Install Nginx web server with Puppet
package { 'nginx':
ensure   => 'installed',
}

file { 'Hello World':
ensure => 'present',
path => '/var/www/html/index.nginx-debian.html',
content => 'Hello World\n',
}

file_line { 'Add the redirect_me page':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
after  => 'server_name _;',
line   => 'location /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent; }',
}

service { 'nginx':
ensure  => 'running',
require => Package['nginx'],
}

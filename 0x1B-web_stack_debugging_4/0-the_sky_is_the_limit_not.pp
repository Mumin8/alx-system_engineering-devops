ncrease the ULIMIT of the default file
exec { 'fix--for-nginx':
command => 'sed -i "s/15/4096/" /etc/default/nginx',
path    => '/usr/local/bin/:/bin/',
notify  => Exec['nginx-restart'], # Notify the restart exec if this one changes
}

# Restart Nginx
exec { 'nginx-restart':
command => '/etc/init.d/nginx restart', # Use the correct restart command
path    => '/sbin:/usr/sbin:/bin:/usr/bin',
refreshonly => true, # Only run when notified by other resources
}


# create file with puppet in /tmp
file{ 'ALX':
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
  path    => '/tmp/school',
}

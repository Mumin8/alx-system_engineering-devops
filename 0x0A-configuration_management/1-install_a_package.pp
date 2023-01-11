# install flask with puppet
package { 'puppet-lint':
    ensure     => 'installed',
    source     => 'pip3',
    name       => 'gem',
}

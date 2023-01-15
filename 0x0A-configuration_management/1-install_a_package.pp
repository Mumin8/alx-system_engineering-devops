# install flask with puppet
package {'Flask':
	ensure   => installed,
	provider => 'pip3',
}

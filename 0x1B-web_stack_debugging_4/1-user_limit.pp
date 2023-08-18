# Changes the Os configuration so that user holberton logs in without error.
exec {'fix-holberton':
  command => 'sed -iE "s/^holberton soft nofile .*/holberton soft nofile 65536/" /etc/security/limits.conf;\
sed -iE "s/^holberton hard nofile .*/holberton hard nofile 131072/" /etc/security/limits.conf;',
  path    => '/usr/bin:/usr/sbin:/bin'
}

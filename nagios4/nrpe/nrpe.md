# NRPE

## INSTALACIÓN

### COMPILACIÓN
<!--TODO: explicar como compila la instalacion de nrpe -->
### PAQUETES PRE-COMPILADOS

#### UBUNTU/DEBIAN

En Ubuntu y Debian el nombre de los paquetes es: ``nagios-nrpe-server`` y ``nagios-nrpe-plugin``
``sudo apt install nagios-nrpe-server nagios-nrpe-plugin``

#### CENTOS/RHEL

En CentOS y Red Hat Enterprise Linux el nombre de los paquetes es: ``nagios-nrpe`` y ``nagios-plugins-nrpe``
``sudo yum install nagios-nrpe nagios-plugins-nrpe``

#### WINDOWS

En Windows el nombre del paquete es: ``NRPE_NT``
[Descargar NRPE_NT](http://sourceforge.net/projects/nrpent/)
Ofrece las mismas funcionalidades que las versiones para UNIX y se configura de la misma forma.
**IMPORTANTE**  
Los plugins de Nagios no proveen version para Windows, asi que es probable que necesites compilarlos con [cygwin](http://www.cygwin.com/)
<!--TODO: explicar como se compilan los plugins para windows -->
## CONFIGURANDO EL NRPE DAEMON

Ahora ya está listo para ser desplegado en los equipos remotos. Sólo necesitamos configurarlo para que acepte conexiones de otros equipos.
NRPE puede trabajar de distitnas formas:  

- Proceso independiente que gestiona las conexiones entrantes
- Parte de [inetd](http://en.wikipedia.org/wiki/inetd) o [xinetd](http://www.xinetd.org)
<!--TODO: explicar que es inetd y xinetd -->
En cualquier caso, es necesario un fichero de configuración: ``nrpe.conf``

### CONFIGURACIÓN NRPE.CONF

Este fichero contiene comandos que pueden ser usados y opciones adicionales para ejecutar el NRPE daemon de forma autónoma.

De igual forma que el fichero de configuración de Nagios, los parámetros tienen la misma sintaxis: ``name=value``

Si has compilado el código de NRPE la ruta de este fichero es ``sample-config/nrpe.conf``
En Ubuntu/Debian es ``/etc/nagios/nrpe.conf``
En CentOS/RHEL es <!--TODO: mirar que path tienen en rhel o centos--> ``POR DETERMINAR``

#### CONFIGURACIÓN NRPE.CONF PARA INITD O PROCESO INDEPENDIENTE

~~~cfg
log_facility=daemon
log_file=/var/log/nrpe.log
debug=0
pid_file=/var/run/nagios/nrpe.pid
server_port=5666
server_address=127.0.0.1
listen_queue_size=5
nrpe_user=nagios
nrpe_group=nagios
allowed_hosts=127.0.0.1,::1
dont_blame_nrpe=0
allow_bash_command_substitution=0
command_prefix=/usr/bin/sudo
max_commands=0
command_timeout=60
connection_timeout=300
allow_weak_random_seed=1
ssl_version=SSLv2+
ssl_use_adh=1
#ssl_cipher_list=ALL:!MD5:@STRENGTH
#ssl_cipher_list=ALL:!MD5:@STRENGTH:@SECLEVEL=0
#ssl_cipher_list=ALL:!aNULL:!eNULL:!SSLv2:!LOW:!EXP:!RC4:!MD5:@STRENGTH
#ssl_cacert_file=/etc/ssl/servercerts/ca-cert.pem
#ssl_cert_file=/etc/ssl/servercerts/nagios-cert.pem
#ssl_privatekey_file=/etc/ssl/servercerts/nagios-key.pem
#ssl_client_certs=0
#ssl_logging=0x00
# nasty_metachars="|`&><'\\[]{};\r\n"
command[check_users]=/usr/lib/nagios/plugins/check_users -w 5 -c 10
command[check_load]=/usr/lib/nagios/plugins/check_load -r -w .15,.10,.05 -c .30,.25,.20
command[check_hda1]=/usr/lib/nagios/plugins/check_disk -w 20% -c 10% -p /dev/hda1
command[check_zombie_procs]=/usr/lib/nagios/plugins/check_procs -w 5 -c 10 -s Z
command[check_total_procs]=/usr/lib/nagios/plugins/check_procs -w 150 -c 200
#command[check_users]=/usr/lib/nagios/plugins/check_users $ARG1$
#command[check_load]=/usr/lib/nagios/plugins/check_load $ARG1$
#command[check_disk]=/usr/lib/nagios/plugins/check_disk $ARG1$
#command[check_swap]=/usr/lib/nagios/plugins/check_swap $ARG1$
#command[check_cpu_stats]=/usr/lib/nagios/plugins/check_cpu_stats.sh $ARG1$
#command[check_mem]=/usr/lib/nagios/plugins/custom_check_mem -n $ARG1$
#command[check_init_service]=sudo /usr/lib/nagios/plugins/check_init_service $ARG1$
#command[check_services]=/usr/lib/nagios/plugins/check_services -p $ARG1$
#command[check_yum]=/usr/lib/nagios/plugins/check_yum
#command[check_apt]=/usr/lib/nagios/plugins/check_apt
### PROCESSES ###
#command[check_all_procs]=/usr/lib/nagios/plugins/custom_check_procs
#command[check_procs]=/usr/lib/nagios/plugins/check_procs $ARG1$

### OPEN FILES ###
#command[check_open_files]=/usr/lib/nagios/plugins/check_open_files.pl $ARG1$

### NETWORK CONNECTIONS ###
#command[check_netstat]=/usr/lib/nagios/plugins/check_netstat.pl -p $ARG1$ $ARG2$

### ASTERISK ###
#command[check_asterisk]=/usr/lib/nagios/plugins/check_asterisk.pl $ARG1$
#command[check_sip]=/usr/lib/nagios/plugins/check_sip $ARG1$
#command[check_asterisk_sip_peers]=sudo /usr/lib/nagios/plugins/check_asterisk_sip_peers.sh $ARG1$
#command[check_asterisk_version]=/usr/lib/nagios/plugins/nagisk.pl -c version
#command[check_asterisk_peers]=/usr/lib/nagios/plugins/nagisk.pl -c peers
#command[check_asterisk_channels]=/usr/lib/nagios/plugins/nagisk.pl -c channels 
#command[check_asterisk_zaptel]=/usr/lib/nagios/plugins/nagisk.pl -c zaptel 
#command[check_asterisk_span]=/usr/lib/nagios/plugins/nagisk.pl -c span -s 1
#include=<somefile.cfg>
#include_dir=<somedirectory>
#include_dir=<someotherdirectory>
include=/etc/nagios/nrpe_local.cfg
include_dir=/etc/nagios/nrpe.d/
~~~

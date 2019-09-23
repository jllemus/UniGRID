<?php
//Functions file;
include 'functions.php';
// info that will be sent to reset.py;
$sw = $_GET['sw'];
shell_exec("python /var/www/html/reset.py '".$sw."' ");
//Database connection;
database_connection(0,0);
?>

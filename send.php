<?php
//Import functions.php file;
include 'functions.php';
//Data that will be sent to send.py file;
$position = $_GET['position'];
$phase = $_GET['phase'];

//information returned. Sent as a variable named data in file ini.js
//this will be working with the success function in ajax
if($phase == "empty" and $position == "empty"){
	echo "Fields are empty";
}elseif($phase == "empty"){
	echo "Phase's field is empty";
}elseif($position == "empty"){
	echo "Position's field is empty";
}else{
	shell_exec("python /var/www/html/send.py '".$position."' '".$phase."'");
}
//Send the information to the database;
database_connection($phase,$position);
?>

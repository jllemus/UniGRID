<?php 
//DATABASE CONNECTION;

//database information;
$user = "jose5";
$pass = "12345";
$server = "localhost";
$database = "database";


//database connection;
$conec = mysqli_connect($server,$user,$pass) or die ("Couldn't connect to the database server");

//Database selection;
$db = mysqli_select_db($conec,$database) or die ("Upps! couldn't connect to the database");

//mysql consult to get te table information;
$consult = "SELECT * FROM info2";

//Making the connection and retrieving table information;
$res = mysqli_query($conec,$consult) or die ("Something went wrong");

$data = array();
	if($res){
		//Saving retrieved data;
		$data = mysqli_fetch_assoc($res);
	}
	echo json_encode($data);
	

?>
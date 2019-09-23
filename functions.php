<?php
//FUNCTIONS.PHP
function database_connection($phase,$position){
	//Database information;
	$user = "jose5";
	$pass = "12345";
	$server = "localhost";
	$database = "database";
	//Database connection;
	$conec = mysqli_connect($server,$user,$pass);
	//Database selection;
	$db = mysqli_select_db($conec,$database) or die("Ups! didn't connect to the database");
	//Discrimate phases and positions and last, send info to db
	if($phase == 1){
        	if($position == 0){
                	$consult = "UPDATE info2 SET phase1 = '$position', res1 = '∞'";
        	}elseif($position == 1){
                	$consult = "UPDATE info2 SET phase1 = '$position', res1 = '240'";
        	}elseif($position == 2){
                	$consult = "UPDATE info2 SET phase1 = '$position', res1 = '120'";
        	}elseif($position == 3){
                	$consult = "UPDATE info2 SET phase1 = '$position', res1 = '80'";
        	}elseif($position == 4){
                	$consult = "UPDATE info2 SET phase1 = '$position', res1 = '60'";
        	}elseif($position == 5){
                	$consult = "UPDATE info2 SET phase1 = '$position', res1 = '48'";
        	}elseif($position == 6){
                	$consult = "UPDATE info2 SET phase1 = '$position', res1 = '40'";
        	}
	}elseif($phase == 2){
        	if($position == 0){
                	$consult = "UPDATE info2 SET phase2 = '$position', res2 = '∞'";
        	}elseif($position == 1){
                	$consult = "UPDATE info2 SET phase2 = '$position', res2 = '240'";
        	}elseif($position == 2){
                	$consult = "UPDATE info2 SET phase2 = '$position', res2 = '120'";
        	}elseif($position == 3){
                	$consult = "UPDATE info2 SET phase2 = '$position', res2 = '80'";
        	}elseif($position == 4){
                	$consult = "UPDATE info2 SET phase2 = '$position', res2 = '60'";
        	}elseif($position == 5){
                	$consult = "UPDATE info2 SET phase2 = '$position', res2 = '48'";
        	}elseif($position == 6){
                	$consult = "UPDATE info2 SET phase2 = '$position', res2 = '40'";
        	}
	}elseif($phase == 3){
        	if($position == 0){
                	$consult = "UPDATE info2 SET phase3 = '$position', res3 = '∞'";
        	}elseif($position == 1){
                	$consult = "UPDATE info2 SET phase3 = '$position', res3 = '240'";
        	}elseif($position == 2){
                	$consult = "UPDATE info2 SET phase3 = '$position', res3 = '120'";
        	}elseif($position == 3){
                	$consult = "UPDATE info2 SET phase3 = '$position', res3 = '80'";
        	}elseif($position == 4){
                	$consult = "UPDATE info2 SET phase3 = '$position', res3 = '60'";
        	}elseif($position == 5){
                	$consult = "UPDATE info2 SET phase3 = '$position', res3 = '48'";
        	}elseif($position == 6){
                	$consult = "UPDATE info2 SET phase3 = '$position', res3 = '40'";
        	}
	}else{
		$consult = "UPDATE info2 SET phase1 = '0', phase2 = '0', phase3 = '0', res1 = '∞',res2 = '∞', res3 ='∞'";
	}
	$res = mysqli_query($conec,$consult) or die ("Something went wrong");
}

?>

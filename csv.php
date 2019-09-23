<?php
include 'functions.php';
$phase1 = $_GET['phase1'];
$phase2 = $_GET['phase2'];
$phase3 = $_GET['phase3'];
$time = $_GET['time'];
$array = $_GET['array'];


for($i = 0; $i< sizeof($array);$i++){
	$jsonarray[] = array( "phase1" => $array[$i][0],"phase2"=>$array[$i][1],"phase3"=>$array[$i][2], "time"=>$array[$i][3]);
}
$res = json_encode($jsonarray);
shell_exec("python3 /var/www/html/csv.py '".$res."' ");
echo $res;
?>

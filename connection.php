<?php  
$server = "localhost";
$userName = "root";
$password = "";
$dbname = "hostel1";

$conn = mysqli_connect($server,$userName,$password,$dbname);

if($conn){

	echo "Connection OK".'<br/>';

}
else{
	die("Your connection is interrupted because ".mysqli_connect_error());
}



?>
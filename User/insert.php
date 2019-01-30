<?php
include("../connection.php");
error_reporting(0);
?>

<!DOCTYPE html>
<html>
<head>
	
</head>
<body>

	

	<form action="" method="GET">
		roomno : <input type="text" name="roomno" value=""><br/><br/>
		capacity : <input type="text" name="capacity" value=""><br/><br/>
		available : <input type="text" name="available" value=""><br/><br/>
		outdate : <input type="text" name="outdate" value="12-01-1700"><br/><br/>
		Submit : <input type="submit" name="submit" value="Submit">

	</form>

</body>
</html>

<?php  

if($_GET['submit']){
	$rn = $_GET['roomno'];
	$cp = $_GET['capacity'];
	$al = $_GET['available'];
	$od = $_GET['outdate'];

	echo $rn;

	if($rn!="" && $cp!="" && $al!=""){
		// $query = "INSERT INTO boys value ('$rn','$cp','$al')";
		$query="INSERT INTO `Boys`(`roomno`, `capacity`, `available`,`outdate`) VALUES ('".$rn."','".$cp."','".$al."','".$od."')";
		$data = mysqli_query($conn,$query);



		if($data){

			echo "Data inserted into Data Base"."<br/>";	
		}
	}

	else{
		echo "All fields are required";
	}
}



?>	


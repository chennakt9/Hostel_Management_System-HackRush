
<?php

include("../connection.php");

?>

<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<h1 align="center" style="color: green">APPROVAL PENDIND BY ADMIN</h1>

</body>
</html>


<?php
if(isset($_POST['bro_submit'])){
	$name = $_POST["name"];
	$males = $_POST["males"];
	$females = $_POST["females"];
	$purpose = $_POST["purpose"];
	$in = $_POST["in"];
	$out = $_POST["out"];
	$mess = $_POST["mess"];
	$reference = $_POST["reference"];
	$email = $_POST["email"];
	$number = $_POST["number"];



	// echo $name."<br>";
	// echo $males."<br>";
	// echo $females."<br>";
	// echo $purpose."<br>";
	// echo $in."<br>";
	// echo $out."<br>";
	// echo $mess."<br>";
	// echo $reference."<br>";
	// echo $email."<br>";
	// echo $number."<br>";

	$query="INSERT INTO `users`(`no_of_male`, `no_of_female`, `purpose_of_visit`, `mess_facility`, `indate`, `outdate`, `reference`, `name`, `contactno`, `email`) VALUES ('".$males."','".$females."','".$purpose."','".$mess."','".$in."','".$out."','".$reference."','".$name."','".$number."','".$email."')";
	$data = mysqli_query($conn,$query);

	if($data){

		echo "Data inserted into Data Base"."<br/>";


		//For getting the id of the respected person

		$sql="SELECT * FROM `users` WHERE `purpose_of_visit`='".$purpose."' AND `contactno`='".$number."' AND `email`='".$email."' AND `indate`='".$in."' AND `no_of_male`='".$males."' AND `name`='".$name."'";


		// $sql="SELECT * FROM `users` WHERE `purpose_of_visit`='".$purpose."'";
		$res=mysqli_query($conn,$sql);

		// echo mysqli_num_rows($res);
		

		$row=mysqli_fetch_assoc($res);
		$id=$row['id'];
		// echo $row['id'];

		//Getting id block is done

	//For sending the mail to the admin


	require "../phpmailer/PHPMailerAutoload.php";
	$mail = new PHPMailer(); // create a new object
    $mail->IsSMTP(); // enable SMTP
    $mail->SMTPDebug = 1; // debugging: 1 = errors and messages, 2 = messages only
    $mail->SMTPAuth = true; // authentication enabled
    $mail->SMTPSecure = 'tls'; // secure transfer enabled REQUIRED for Gmail
	$mail->Host = "smtp.gmail.com";
	$mail->SMTPOptions = array(
    'ssl' => array(
        'verify_peer' => false,
        'verify_peer_name' => false,
        'allow_self_signed' => true
    )
);
	$mail->Port = 587; // or 587
	$mail->IsHTML(true);
	$mail->Username = "chennakesava301@gmail.com";
	$mail->Password = "8374741305";
	// $mail->SetFrom("rahulchalla143@gmail.com");
	$mail->SetFrom("chennakesava301@gmail.com");
	$mail->Subject = "Re: Hostel Room Booing";

	$body="<a href='http://localhost/HostelManagement/Approval/echo.py?id=".$id."'>view</a>";
	$mail->Body = "You have been requested by ".$name." for hostel accomdation click here to ".$body;
	$mail->AddAddress("kesavatirunagari306@gmail.com");
	if(!$mail->Send()) {
		echo "{'suc':false}";
		
	} 
	else {
		echo "{'suc':true}";
	}

	//http://localhost/PythonTest/echo.py?id=18
	//http://localhost/HostelManagement/Approval/echo.py?id=5
	//Finished mailing block





		
	}

	




	else{
		echo "THERE IS AN ERROR WHILE SUBMITTING THE FORM";
	}


}



?>


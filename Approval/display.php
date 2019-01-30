<?php
include("../connection.php");
error_reporting(0);

$query = "SELECT * FROM student";
$data = mysqli_query($conn,$query);

$totalrows = mysqli_num_rows($data);







if($totalrows){
	?>

	<table border="1">
		<tr>
			<th>Roll No</th>
			<th>Name</th>
			<th>Class</th>
		</tr>
			
	

	<?php

	while ($result = mysqli_fetch_assoc($data)) {
		echo "<tr>
				<td>".$result['rollno']."</td>
				<td>".$result['name']."</td>
				<td>".$result['class']."</td>
			</tr>";
	}
	
}
else{
	echo "Table has no records";
}


?>


</table>
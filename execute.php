<!DOCTYPE HTML>
<html>

<body>

Command is <?php echo $_POST["name"]; ?><br>

<?php

$command=$_POST["name"];

$a = 'python /var/pscript/client.py ';


$b= $a.$command;


$last_line = system($b);

header('Location:signal.php');

?>



</body>

</html>

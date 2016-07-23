<?php
	if(isset($_POST["ON"]))
	{
		exec("sudo -s python /home/pi/relay/relay_on_all.py");
	}
	if(isset($_POST["OFF"]))
	{
		exec("sudo -s python /home/pi/relay/relay_off_all.py");
	}
	if(isset($_POST["LUZ1"]))
	{
		exec("sudo -s python /home/pi/relay/relay_in1.py");
	}
	if(isset($_POST["LUZ2"]))
	{
		exec("sudo -s python /home/pi/relay/relay_in2.py");
	}
?>

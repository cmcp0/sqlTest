<?php

		return "success"; die(); // Remove this line in live site, it is only for testing
		
		if($_REQUEST['name'] == '' || $_REQUEST['phone'] == '' || $_REQUEST['contact_email'] == '' || $_REQUEST['message'] == ''):
			return "error";
		endif;
		
		if (filter_var($_REQUEST['contact_email'], FILTER_VALIDATE_EMAIL)):
			// receiver email address
			$to = 'receiver_email@domain.com';
			
			// prepare header
			$header = 'From: '. $_REQUEST['name'] . ' <'. $_REQUEST['contact_email'] .'>'. "\r\n";
			$header .= 'Reply-To:  '. $_REQUEST['name'] . ' <'. $_REQUEST['contact_email'] .'>'. "\r\n";
			// $header .= 'Cc:  ' . 'example@domain.com' . "\r\n";
			// $header .= 'Bcc:  ' . 'example@domain.com' . "\r\n";
			$header .= 'X-Mailer: PHP/' . phpversion();
			
			// Contact Subject
			$subject = "Feedback From GEO";
			
			// Contact Message
			$message = $_REQUEST['message'];
			
			// Send contact information
			$mail = mail( $to, $subject , $message, $header );
			
			return $mail ? "success" : "error";
		else:
			return "error";
		endif;
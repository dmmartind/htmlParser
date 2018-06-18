<?php
$this->openHtml(FALSE);
$this->openHead( [], FALSE );
$this->Meta( ['charset'=>'utf-8'], FALSE );
$this->Title( ['text' =>'Untitled Page'], FALSE );
$this->Meta( ['name'=>'generator', 'content'=>'WYSIWYG Web Builder 14 Trial Version - http://www.wysiwygwebbuilder.com'], FALSE );
$this->Link( ['href'=>'wb.validation.css', 'rel'=>'stylesheet'], FALSE );
$this->Link( ['href'=>'contact_us.css', 'rel'=>'stylesheet'], FALSE );
$this->Link( ['href'=>'index.css', 'rel'=>'stylesheet'], FALSE );
$this->Script( ['src'=>'jquery-1.12.4.min.js'], FALSE );
$this->Script( ['src'=>'wb.validation.min.js'], FALSE );
$this->Script( ['src'=>'index.js'], FALSE );
$this->openBody( [], FALSE );
$this->ATag( ['href'=>'http://www.wysiwygwebbuilder.com', 'target'=>'_blank'], FALSE );
$this->Image( ['src'=>'images/builtwithwwb14.png', 'alt'=>'WYSIWYG Web Builder', 'id'=>'wb_uid0'], FALSE );
$this->openDiv( ['id'=>'wb_Form1'], FALSE );
$this->openForm( ['name'=>'contact_us', 'method'=>'post', 'action'=>'', 'enctype'=>'text/plain', 'id'=>'Form1'], FALSE );
$this->Label( ['for'=>'firstLastName', 'id'=>'Label1'], FALSE );
$this->Input( ['type'=>'text', 'id'=>'firstLastName', 'name'=>'Editbox1', 'value'=>'', 'spellcheck'=>'false'], FALSE );
$this->Label( ['for'=>'emailAddr', 'id'=>'Label2'], FALSE );
$this->Input( ['type'=>'email', 'id'=>'emailAddr', 'name'=>'Editbox2', 'value'=>'', 'spellcheck'=>'false'], FALSE );
$this->Label( ['for'=>'phoneNumber', 'id'=>'Label3'], FALSE );
$this->Input( ['type'=>'tel', 'id'=>'phoneNumber', 'name'=>'Editbox3', 'value'=>'', 'spellcheck'=>'false'], FALSE );
$this->Label( ['for'=>'orderNumber', 'id'=>'Label4'], FALSE );
$this->Input( ['type'=>'text', 'id'=>'orderNumber', 'name'=>'Editbox4', 'value'=>'', 'spellcheck'=>'false'], FALSE );
$this->Label( ['for'=>'subject', 'id'=>'Label5'], FALSE );
echo 'Error: no matching code for tag: select'
$this->Label( ['for'=>'questions', 'id'=>'Label6'], FALSE );
echo 'Error: no matching code for tag: textarea'
$this->Input( ['type'=>'submit', 'id'=>'submit', 'name'=>'', 'value'=>'Submit'], FALSE );
$this->closeForm( [], FALSE );
$this->closeBody( [], FALSE );
$this->closeHtml(FALSE);
?>
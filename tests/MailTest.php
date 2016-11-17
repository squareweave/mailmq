<?php
use PHPUnit\Framework\TestCase;

class MailTest extends TestCase
{
    public function testSendMail()
    {
        mail("badger@example.com",
             "Snake",
             "Mushroom");
    }
}

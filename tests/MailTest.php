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

    public function testSendMailAdditionalOption()
    {
        mail("badger@example.com",
             "Snake",
             "Mushroom",
             null,
             "-fbigbadger@example.com");
    }
}

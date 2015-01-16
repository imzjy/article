Notes on RubyGems
===========

1, How to install Gem behind the proxy ?

- update the RubyGem version more than 1.3.0
- exec the command: gem install win32-service -r -p http://username:password@proxy_url:port (But I found that it's hard to work with Microsoft ISA server, because ISA server using ntlm authentication:)

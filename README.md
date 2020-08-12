# cloudflare-automatic-dns-update

This script does three things:

1. Checks your external IP
2. Checks your domain's A-record
3. If these match, no action is taken, if they do not match, the A-record is updated.

Perfect for servers deployed to dynamic IP:s!

# How to use

1. Download or clone the repository
2. Edit settings.py to configure the script for your specific domain
3. Set up a cronjob to run the script as often as you like

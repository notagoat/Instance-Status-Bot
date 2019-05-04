# Instance-Status-Bot
A simple python bot to post the status of the mastodon instance's usage using cron

# Requirements

* Mastodon.py
* Python3
* Mastodon access tokens

# Monitoring

The bot currently monitors:

* Disk Usage
* Memory Usage
* Network Connections
* Processes Running

And then prints out statuses relating to them.

These are all based in functions so they can be easily turned off

# Running

1. Make an account for the bot

2. In main.py fill in the instance name, the access token and your mastodon handle

3. Add your path to your cron.

4. Set a cronjob for however often you want the bot to post


# Upcoming Features

* Easier Setup
* Better control on post visibility
* More stats!

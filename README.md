Telegram Message Relay
======================

Forwards messages from one chat (User, Group or Channel) to other chats.

Configuration
-------------

1.  Register a Telegram App at
    [my.telegram.org](https://my.telegram.org/).
2.  Set `API_ID` and `API_HASH` to `.env` file
    or your environment.
3.  And the most important part: Setup RELAY_MAP with the list
    of source and destination channels.
4.  Optionally you can setup the file for the Session storage. Full
    paths are also accepted.

Why do I have to register an App?
---------------------------------

This relay is **not** a Telegram bot. It acts like a normal Telegram
user who forwards messages. To make this work, the relay needs to be
registered as an Telegram client, like for example the Telegram Desktop
App.

Registering an App is very easy and instantaneous. Go through [Telegram
Docs](https://core.telegram.org/api/obtaining_api_id) to get your API ID
and Hash.

Setting up RELAY_MAP
------------------------------

RELAY_MAP follows a CSV like encoding to defining multiple relays to multiple
channels. The format starts with the source channel which is followed a colon
and then a comma separated list of destination channels. Multiple pairs of
source and destination channels can be separated with semicolons. Both source
and destination channels must be defined using their numeric IDs. The [List
Channels](#listchannels) command can help you build the map.

Example:
`RELAY_MAP=SOURCE_CHANNEL1:DST_CHANNEL1,DST_CHANNEL2;SOURCE_CHANNEL2:DST_CHANNEL3`

List Channels <a name="listchannels"></a>
-------------

You can list your channels and groups by running the `listchannels.py`
app. You can use the output to setup RELAY_MAP.

`$ ./listchannels.py`

Don't forward, re-send
----------------------

If you don't want to use Telegram's forwarding functionality, e.g. so
you don't expose the original poster or channel to appear, set
`FORWARD` environment variable to `False`.

This app is Docker ready
------------------------

```sh
$ docker build -t tg-relay .
$ docker run -e API_ID=XXXX -e API_HASH=XXXX -e SESSION_NAME="/data/session" -v `pwd`/<data:/data> tg-relay
```

This app is [Dokku](http://dokku.viewdocs.io/dokku/) ready
----------------------------------------------------------

1.  Setup storages for persistent storing of sessions.
2.  Configure environment variables
3.  Git push to Dokku
4.  Make sure to scale web to 0 and cmd to 1 to avoid nginx troubles.
    `dokku ps:scale tg-relay web=0 cmd=1`

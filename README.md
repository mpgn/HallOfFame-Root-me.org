# HallOfFame Root-me

Hall Of Fame dashboard for Root-me.org. Users information are in the `users.json`.

![screenshot](https://i.gyazo.com/56b4c6fcc5c5306e3d904735c0716835.png)

## Informations

Since root-me doesn't have any API, this is dirty parsing ! But it's working ;)

/!\ The statistics in the demo are not updated every night !

### Add a user

Add the user in the `users.json` like this :
```
python3 update.py add username realname
```
You can get the username form the url of a Root-me profile : https://www.root-me.org/username 
**/!\ CAUTION: take the username from the URL !**

### Update users informations

Update the `json` like this : 
```
python3 update.py update
```

Use a cron job to update the script every night ;)

### Delete a user

```
python3 update.py delete username
```

## History

* 0.0.1
	* First release
* 0.0.2
	* Fix issues
* 0.0.2
	* Add delete function

## Troubleshoot

### Error loading the `users.json` file

If you run this in a browser, you might get the following CORS error because the file is not on a server:

```Access to XMLHttpRequest at 'file:///[...]/site/users.json' from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, isolated-app, brave, https, chrome-untrusted, data, chrome-extension, chrome.```

To fix this, make sure the JSON file is on a local or remote server. You can use a Live server on your IDE: [this is how to run a localhost server with VSCode.](https://www.geeksforgeeks.org/how-to-enable-live-server-on-visual-studio-code/).

## Credits

* [@mpgn_x64](https://twitter.com/mpgn_x64)

## License

MIT License
